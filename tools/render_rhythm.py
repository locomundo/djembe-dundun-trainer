#!/usr/bin/env python3
"""Render a West-African drum score (16th-note grid) to WAV.

Patterns are written as strings on a 16th-note grid, one character per slot:
    .  rest      B  bass        T  tone       S  slap
    O  open dundun tone         M  muted/closed dundun tone
    x  bell (separate 'bell' line for the dundun parts)
Spaces and '|' are ignored, so beats can be grouped for readability.

Usage:  python3 render_rhythm.py [--bpm 100] [--cycles 8] [--outdir ../audio]
"""
import argparse, math, os, random, struct, wave

SR = 44100

# ---------------------------------------------------------------- synthesis
# Modal synthesis: each stroke is a bank of damped sinusoids at the inharmonic
# modes of a circular membrane (1 : 1.593 : 2.135 : 2.295 : ...), excited by a
# filtered noise transient - the hand or stick landing on the skin. That
# transient is most of what makes a stroke recognisable as a drum.

# name -> f0, pitch bend + its time constant, duration, gain,
#         [(mode ratio, amplitude, decay)], (noise amp, highpass, lowpass, decay)
SRC = {
    'T':            (218, 1.22, .045, .60, .62,
                     [(1,1,.40),(1.593,.52,.24),(2.135,.34,.17),(2.295,.26,.15),
                      (2.653,.20,.11),(2.917,.14,.09),(3.155,.10,.07),(3.50,.07,.055)],
                     (.42, 1100, 7000, .016)),
    'B':            (84, 1.55, .050, .75, 1.00,
                     [(1,1,.38),(1.593,.26,.14),(2.135,.12,.09),(2.295,.08,.07)],
                     (.30, 180, 1400, .022)),
    'S':            (218, 1.06, .020, .32, .80,
                     [(1.593,.30,.075),(2.135,.42,.065),(2.653,.50,.055),(2.917,.45,.048),
                      (3.50,.38,.040),(4.06,.30,.034),(4.60,.22,.028)],
                     (1.0, 1700, 9000, .045)),
    'sangban_O':    (112, 1.35, .040, 1.00, .90,
                     [(1,1,.55),(1.593,.18,.13),(2.135,.09,.08)], (.55, 2600, 11000, .005)),
    'sangban_M':    (112, 1.35, .040, .28, .72,
                     [(1,1,.09),(1.593,.14,.05),(2.135,.08,.04)], (.55, 2600, 11000, .005)),
    'kenkeni_T':    (176, 1.30, .035, .65, .66,
                     [(1,1,.34),(1.593,.20,.11),(2.135,.10,.07)], (.60, 3000, 12000, .005)),
    'doundounba_T': (70, 1.42, .055, 1.25, 1.05,
                     [(1,1,.70),(1.593,.14,.13),(2.135,.07,.08)], (.45, 2200, 9000, .006)),
    # kenken: forged iron, so the partials are wide and genuinely inharmonic
    'bell':         (900, 1.0, .010, .50, .40,
                     [(1,1,.16),(1.62,.85,.13),(2.31,.70,.10),(3.04,.55,.075),
                      (3.89,.42,.055),(5.12,.30,.040),(6.40,.20,.030)],
                     (.80, 3500, 14000, .006)),
    'click':        (1600, 1.0, .010, .09, .30,
                     [(1,1,.030),(2.02,.5,.020)], (.25, 4000, 12000, .003)),
}

def render_voice(spec, variant=0):
    f0, bend, bt, dur, gain, modes, (namp, nhp, nlp, ndec) = spec
    n = int(SR * dur)
    out = [0.0] * n
    det = 1.0 + (0.0 if variant == 0 else (0.012 if variant % 2 else -0.009))
    ph = [0.0] * len(modes)
    two_pi_sr = 2 * math.pi / SR
    for i in range(n):
        t = i / SR
        benv = 1.0 + (bend - 1.0) * math.exp(-t / bt)
        v = 0.0
        for m, (r, amp, dec) in enumerate(modes):
            ph[m] += two_pi_sr * f0 * det * r * benv
            v += math.sin(ph[m]) * amp * math.exp(-t / dec)
        out[i] = v
    # attack transient: white noise -> 1-pole highpass -> 1-pole lowpass
    rnd = random.Random(1234 + variant)
    ah = math.exp(-2 * math.pi * nhp / SR)
    al = 1 - math.exp(-2 * math.pi * nlp / SR)
    yh = xp = yl = 0.0
    for i in range(n):
        e = math.exp(-(i / SR) / ndec)
        if e < 1e-4:
            break
        w = rnd.random() * 2 - 1
        yh = ah * (yh + w - xp); xp = w
        yl += al * (yh - yl)
        out[i] += yl * namp * e
    peak = max(abs(v) for v in out) or 1.0
    k = gain / peak
    fade = min(600, n // 12)
    for i in range(n):
        v = math.tanh(out[i] * k * 1.25) / 1.25      # gentle saturation = skin and body
        if i < 48:
            v *= i / 48                              # no click on the attack
        if i > n - fade:
            v *= (n - i) / fade
        out[i] = v
    return out

def reverb(mono, wet=0.17, room=0.80):
    """Schroeder reverb - 4 parallel combs into 2 allpasses. O(n), no FFT needed,
    and a little room is most of what separates 'a drum' from 'a sine wave'."""
    n = len(mono)
    out = [0.0] * n
    for delay, fb in ((1557, room), (1617, room - .01), (1491, room - .02), (1422, room - .03)):
        buf = [0.0] * delay
        i = 0
        for j in range(n):
            v = buf[i]
            out[j] += v * 0.25
            buf[i] = mono[j] + v * fb
            i += 1
            if i == delay:
                i = 0
    for delay, fb in ((225, .5), (556, .5)):
        buf = [0.0] * delay
        i = 0
        for j in range(n):
            v = buf[i]
            y = -out[j] + v
            buf[i] = out[j] + v * fb
            out[j] = y
            i += 1
            if i == delay:
                i = 0
    return [v * wet for v in out]

# ---------------------------------------------------------------------------
# Voice bank. Real samples from ../samples if they are there, synthesis if not.
DIV = [4]          # set per render; accent falls on each beat
SAMPLE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'samples')

def load_wav(path):
    with wave.open(path, 'rb') as w:
        if w.getframerate() != SR or w.getsampwidth() != 2:
            raise ValueError(f'{path}: need 16-bit {SR} Hz')
        n, ch = w.getnframes(), w.getnchannels()
        raw = struct.unpack('<%dh' % (n * ch), w.readframes(n))
    if ch == 1:
        return [v / 32768.0 for v in raw]
    return [(raw[i] + raw[i + 1]) / 65536.0 for i in range(0, len(raw), 2)]

# voice -> the sample files that play it (several = round robin)
SAMPLES = {
    'B': ['bass'], 'T': ['tone_1', 'tone_2', 'tone_3', 'tone_4'], 'S': ['slap'],
    'sangban_O': ['sangban_O'], 'sangban_M': ['sangban_M'],
    'kenkeni_T': ['kenkeni_T'], 'doundounba_T': ['doundounba_T'], 'bell': ['bell'],
}

def build_voices():
    voices, sampled = {}, 0
    for name, spec in SRC.items():
        files = SAMPLES.get(name, [])
        bank = []
        for f in files:
            path = os.path.join(SAMPLE_DIR, f + '.wav')
            if os.path.exists(path):
                try:
                    bank.append(load_wav(path))
                except Exception as e:
                    print(f'  ! {f}.wav unusable ({e}) - synthesising instead')
        if bank:
            voices[name] = bank; sampled += 1
        else:
            voices[name] = [render_voice(spec, i) for i in range(3)]
    print(f'  voices: {sampled} sampled, {len(SRC) - sampled} synthesised')
    return voices

VOICES = build_voices()

def damp(sig, tau=0.085):
    """A closed / choked version of an open dundun stroke."""
    out = []
    for i, v in enumerate(sig):
        out.append(v * math.exp(-(i / SR) / tau))
    n = len(out); fade = min(400, n // 8)
    for i in range(fade):
        out[n - fade + i] *= (fade - i) / fade
    return out

# black noteheads on the kenkeni are closed strokes; green ones ring
VOICES['kenkeni_M'] = [damp(v) for v in VOICES['kenkeni_T']]
# ---------------------------------------------------------------- the score
def strip(p):
    return p.replace('|', '').replace(' ', '')

# One cycle = 2 bars of 4/4 = 32 sixteenths.
RHYTHMS = {}
RHYTHMS['djole'] = {
    'div': 4,          # sixteenths per beat
    'name': 'Djole',
    'slots': 32,
    'signal': {
        # call: pickup into the bar, then the phrase; played twice
        'drum': strip('T.TT|.T.T|T.SS|S...') * 2,
        'pickup': 'T',          # one grace tone on the 16th before each bar
        'pan': 0.0,
    },
    'parts': [
        {'key': 'djembe1', 'label': 'Djembé 1', 'pan': -0.35,
         'drum': strip('B.TT|B.SS|B.TT|B.SS') + strip('B.TT|B.SS|B.TT|B.SS')},
        {'key': 'djembe2', 'label': 'Djembé 2', 'pan': 0.35,
         'drum': strip('B..T|T...|B...|TTTT') + strip('T..T|T...|B...|T...')},
        {'key': 'sangban', 'label': 'Sangban', 'pan': -0.15,
         'drum': strip('O...|M...') * 4,
         'bell': strip('x.x.|x.x.') * 4},
        {'key': 'kenkeni', 'label': 'Kenkeni', 'pan': 0.15,
         'drum': strip('..TT') * 8,
         'bell': strip('..xx') * 8},
        {'key': 'doundounba', 'label': 'Doundounba', 'pan': 0.0,
         'drum': strip('O...|....') * 4,
         'bell': strip('x.xx|.xx.') * 4},
    ],
}


RHYTHMS['fankani'] = {
    'div': 4,          # sixteenths per beat
    'name': 'Fankani',
    'slots': 32,
    'signal': {   # the same call the Djole sheet uses
        'drum': strip('T.TT|.T.T|T.SS|S...') * 2,
        'pickup': 'T',
        'pan': 0.0,
    },
    'parts': [
        {'key': 'djembe1', 'label': 'Djembé 1', 'pan': -0.35,
         'drum': strip('S..S|S.B.|S.TT|S.B.') * 2},
        {'key': 'djembe2', 'label': 'Djembé 2', 'pan': 0.35,
         'drum': strip('S..S|S.TT') * 4},
        {'key': 'sangban', 'label': 'Sangban', 'pan': -0.15,
         'drum': strip('....|..T.|T.TT|..O.') + strip('....|..O.|..TT|..O.'),
         'bell': strip('x.xx|.xx.') * 4,
         'begin': 26},
        {'key': 'kenkeni', 'label': 'Kenkeni', 'pan': 0.15,
         'drum': strip('TT..|O...') * 4,
         'bell': strip('xx.x|x.x.') * 4},
        {'key': 'doundounba', 'label': 'Doundounba', 'pan': 0.0,
         'drum': strip('....|....|....|..T.') + strip('....|..T.|....|..T.'),
         'bell': strip('x.xx|.xx.') * 4,
         'begin': 30},
    ],
}


RHYTHMS['djole-guinee'] = {
    'div': 4,          # sixteenths per beat
    'name': 'Djole (Guinee)',
    'slots': 32,
    'signal': {
        'drum': strip('T.TT|.T.T|T.SS|S...') * 2,
        'pickup': 'T',
        'pan': 0.0,
        'einde': 28,
    },
    'parts': [
        {'key': 'djembe1', 'label': 'Djembe 1', 'pan': -0.40,
         'drum': strip('S.SS|.STT') * 4, 'einde': 27},
        {'key': 'djembe2', 'label': 'Djembe 2', 'pan': 0.0,
         'drum': strip('B.TT|B.SS') * 4, 'einde': 28},
        {'key': 'djembe3', 'label': 'Djembe 3', 'pan': 0.40,
         # the red crosses carry an underline: an open, ringing slap
         'drum': strip('S...|S...|S..T|T...') + strip('S...|TTTT|TT.T|T...'),
         'einde': 28},
        {'key': 'sangban', 'label': 'Sangban', 'pan': -0.15,
         'drum': strip('....|T...|....|T.T.') * 2,
         'bell': strip('x.x.') * 8, 'einde': 28},
        {'key': 'kenkeni', 'label': 'Kenkeni', 'pan': 0.15,
         'drum': strip('..TT') * 8,
         'bell': strip('..xx') * 8, 'einde': 27},
        {'key': 'doundounba', 'label': 'Doundounba', 'pan': 0.0,
         'drum': strip('T...|....|T.T.|....') * 2,
         'bell': strip('x.x.') * 8, 'einde': 28},
    ],
}


# GIDAMBA is ternary - 12/8, three subdivisions to the beat. The doundounba runs
# a four-bar phrase where every other part is one or two bars, so the cycle is 48.
RHYTHMS['gidamba'] = {
    'div': 3,          # eighth-note triplets per beat
    'name': 'Gidamba',
    'slots': 48,
    'signal': {
        'drum': strip('TTT|TT.|TT.|T..') * 4,
        'pickup': 'T',
        'pan': 0.0,
        'einde': 21,
    },
    'parts': [
        {'key': 'djembe1', 'label': 'Djembe 1', 'pan': -0.35,
         'drum': strip('S.T|S..') * 8, 'einde': 21},
        {'key': 'djembe2', 'label': 'Djembe 2', 'pan': 0.35,
         'drum': strip('S.S|STT') * 8, 'einde': 21},
        {'key': 'sangban', 'label': 'Sangban', 'pan': -0.15,
         'drum': strip('O..|T..') * 8,
         'bell': strip('xx.') * 16, 'einde': 21},
        {'key': 'kenkeni', 'label': 'Kenkeni', 'pan': 0.15,
         'drum': strip('T.T|.T.|.T.|T..') * 4,
         'bell': strip('x.x|.x.|xx.|x.x') * 4,
         'begin': 23, 'einde': 21},
        {'key': 'doundounba', 'label': 'Doundounba', 'pan': 0.0,
         # a genuine four-bar phrase; the bell follows the drum in bar 3
         'drum': strip('T.T|...|...|..T') * 2
               + strip('T.T|.TT|.T.|T.T') + strip('T.T|...|...|T.T'),
         'bell': strip('x.x|.x.|xx.|x.x') * 2
               + strip('x.x|.xx|.x.|x.x') + strip('x.x|.x.|xx.|x.x'),
         'begin': 47, 'einde': 45},
    ],
}


RHYTHMS['gumbe'] = {
    'div': 4,
    'name': 'Gumbe',
    'slots': 32,
    'signal': {   # a different call from the Djole family - all tones, no slaps
        'drum': strip('T.TT|.T.T|T.T.|T...') * 2,
        'pickup': 'T',
        'pan': 0.0,
        'einde': 28,
    },
    'parts': [
        {'key': 'djembe1', 'label': 'Djembe 1', 'pan': -0.38,
         'drum': strip('TT.S|TTS.') * 4, 'einde': 28},
        {'key': 'djembe2', 'label': 'Djembe 2', 'pan': 0.38,
         'drum': strip('B.TT|..S.') * 4, 'einde': 30},
        {'key': 'sangban', 'label': 'Sangban 1', 'pan': -0.22,
         'drum': strip('O...|T.T.') * 4,
         'bell': strip('x.') * 16, 'einde': 28},
        {'key': 'sangban2', 'label': 'Sangban 2', 'pan': 0.10,
         'drum': strip('TT..|O...') * 4,
         'bell': strip('xx.x|x.x.') * 4, 'einde': 28},
        {'key': 'kenkeni', 'label': 'Kenkeni', 'pan': 0.22,
         'drum': strip('T...') * 8,
         'bell': strip('x.') * 16, 'einde': 28},
        {'key': 'doundounba', 'label': 'Doundounba', 'pan': 0.0,
         'drum': strip('O..O|..T.|T.T.|....') * 2,
         'bell': strip('x.xx|.xx.|x.x.|x.x.') * 2, 'einde': 28},
    ],
}


RHYTHMS['soli-lent'] = {
    'div': 4,
    'name': 'Soli Lent',
    'slots': 32,
    'signal': {'drum': strip('T.TT|.T.T|T.SS|S...') * 2, 'pickup': 'T', 'pan': 0.0},
    'parts': [
        {'key': 'djembe1', 'label': 'Djembe 1', 'pan': -0.38,
         'drum': strip('B.TT|..ST|T.BS|..S.') * 2},
        {'key': 'djembe2', 'label': 'Djembe 2', 'pan': 0.38,
         'drum': strip('S..S|S.TT|S.BS|S.TT') * 2},
        {'key': 'sangban', 'label': 'Sangban', 'pan': -0.15,
         'drum': strip('T...|T...|T.O.|T...') * 2,
         'bell': strip('x.') * 16},
        {'key': 'kenkeni', 'label': 'Kenkeni', 'pan': 0.15,
         'drum': strip('T...|..T.') * 4,
         'bell': strip('x.xx|.xx.') * 4, 'begin': 30},
        {'key': 'doundounba', 'label': 'Doundounba', 'pan': 0.0,
         'drum': strip('....|....|..T.|....') + strip('....|....|..T.|T...'),
         'bell': strip('x.xx|.xx.|x.x.|x.x.') * 2},
    ],
}

RHYTHMS['sunun'] = {
    'div': 4,
    'name': 'Sunun',
    'slots': 32,
    'signal': {'drum': strip('T.TT|.T.T|T.SS|S...') * 2, 'pickup': 'T', 'pan': 0.0},
    'parts': [
        {'key': 'djembe1', 'label': 'Djembe 1', 'pan': -0.38,
         'drum': strip('T.SS|..ST|T.SS|B.ST') * 2, 'begin': 31},
        {'key': 'djembe2', 'label': 'Djembe 2', 'pan': 0.38,
         'drum': strip('S..S|S.TT') * 4},
        {'key': 'sangban', 'label': 'Sangban', 'pan': -0.15,
         'drum': strip('T...|..T.') * 4,
         'bell': strip('x.xx|.xx.') * 4, 'begin': 30},
        {'key': 'kenkeni', 'label': 'Kenkeni', 'pan': 0.15,
         'drum': strip('T...') * 8,
         'bell': strip('x.') * 16},
        {'key': 'doundounba', 'label': 'Doundounba', 'pan': 0.0,
         'drum': strip('T.TT|..O.|..O.|O..T') * 2,
         'bell': strip('x.xx|.xx.|x.x.|x.xx') * 2, 'begin': 31},
    ],
}

RHYTHMS['toro'] = {
    'div': 4,
    'name': 'Toro',
    'slots': 32,
    'signal': {'drum': strip('T.TT|.T.T|T.SS|S...') * 2, 'pickup': 'T', 'pan': 0.0},
    'parts': [
        # played once to bring the ensemble in, then it drops out
        {'key': 'entrance', 'label': 'Entrance', 'pan': 0.0, 'once': True,
         'drum': strip('S...|S.S.|S...|S.S.') + '.' * 16},
        {'key': 'djembe1', 'label': 'Djembe 1', 'pan': -0.38,
         'drum': strip('TT.B|S.S.|S..B|S.S.') * 2},
        {'key': 'djembe2', 'label': 'Djembe 2', 'pan': 0.38,
         'drum': strip('S..S|S.TT') * 4, 'einde': 26},
        {'key': 'sangban', 'label': 'Sangban', 'pan': -0.15,
         # bar 1 closes on muted tones, bar 2 on open ones
         'drum': strip('TT..|O.O.|O...|T.T.') + strip('TT..|O.O.|O...|O.O.'),
         'bell': strip('xx.x|x.x.|x.x.|x.x.') * 2, 'begin': 26},
        {'key': 'kenkeni', 'label': 'Kenkeni', 'pan': 0.15,
         'drum': strip('..TT|..O.') * 4,
         'bell': strip('x.xx|.xx.') * 4},
        {'key': 'doundounba', 'label': 'Doundounba', 'pan': 0.0,
         'drum': strip('TT..|....|..TT|.TT.') + strip('TT..|....|....|....'),
         'bell': strip('xx.x|x.x.|x.xx|.xx.') + strip('xx.x|x.x.|x.x.|x.x.')},
    ],
}

# which voice a drum character maps to, per part
def voice_for(part_key, ch):
    if part_key in ('signal', 'djembe1', 'djembe2', 'djembe3', 'entrance'):
        return {'B': 'B', 'T': 'T', 'S': 'S'}.get(ch)
    if part_key in ('sangban', 'sangban2'):
        return {'O': 'sangban_O', 'M': 'sangban_M', 'T': 'sangban_M'}.get(ch)
    if part_key == 'kenkeni':
        return {'O': 'kenkeni_T', 'M': 'kenkeni_M', 'T': 'kenkeni_M'}.get(ch)
    if part_key == 'doundounba':
        return {'O': 'doundounba_T', 'M': 'doundounba_T', 'T': 'doundounba_T'}.get(ch)
    return None

# ---------------------------------------------------------------- rendering
class Track:
    def __init__(self, nsamples):
        self.L = [0.0] * nsamples
        self.R = [0.0] * nsamples
        self.rr = 0
        self.rnd = random.Random(99)

    def add(self, voice, at, gain=1.0, pan=0.0, vel=1.0):
        bank = VOICES[voice]
        s = bank[self.rr % len(bank)]
        self.rr += 1
        a = gain * vel * (0.92 + self.rnd.random() * 0.16)   # human dynamics
        gl = a * math.sqrt((1 - pan) / 2) * math.sqrt(2)
        gr = a * math.sqrt((1 + pan) / 2) * math.sqrt(2)
        end = min(at + len(s), len(self.L))
        if at < 0 or at >= len(self.L):
            return
        for i in range(end - at):
            v = s[i]
            self.L[at + i] += v * gl
            self.R[at + i] += v * gr

def write_wav(path, track, peak_target=0.89):
    send = reverb([(l + r) * 0.5 for l, r in zip(track.L, track.R)])
    for i, w in enumerate(send):
        track.L[i] += w
        track.R[i] += w
    peak = max(max(abs(v) for v in track.L), max(abs(v) for v in track.R), 1e-9)
    k = peak_target / peak if peak > peak_target else 1.0
    frames = bytearray()
    for l, r in zip(track.L, track.R):
        frames += struct.pack('<hh', int(max(-1, min(1, l * k)) * 32767),
                                     int(max(-1, min(1, r * k)) * 32767))
    with wave.open(path, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(bytes(frames))
    return len(track.L) / SR

def lay(track, pattern, part_key, step, off, cycles, pan, vel=1.0):
    n = len(pattern)
    for c in range(cycles):
        for i, ch in enumerate(pattern):
            if ch == '.':
                continue
            v = 'bell' if ch == 'x' else voice_for(part_key, ch)
            if not v:
                continue
            # a touch of accent on the downbeat of each beat
            acc = vel * (1.06 if i % DIV[0] == 0 else 0.92)
            track.add(v, off + int((c * n + i) * step), pan=pan, vel=acc)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bpm', type=float, default=100.0)
    ap.add_argument('--cycles', type=int, default=8)
    ap.add_argument('--outdir', default=os.path.join(os.path.dirname(__file__), '..', 'audio'))
    ap.add_argument('--suffix', default='')
    ap.add_argument('--rhythm', default='djole', choices=sorted(RHYTHMS))
    a = ap.parse_args()

    sc = RHYTHMS[a.rhythm]
    R = a.rhythm
    div = sc.get('div', 4); DIV[0] = div                   # subdivisions per beat
    step = SR * 60.0 / a.bpm / div            # samples per subdivision
    slots = sc['slots']
    cycle = step * slots
    os.makedirs(a.outdir, exist_ok=True)
    tail = int(SR * 1.6)
    made = []

    def total(cycles, lead_cycles=0):
        return int(cycle * (cycles + lead_cycles)) + tail

    # ---- full ensemble: signal (call) once, then the groove
    nlead = 1
    t = Track(total(a.cycles, nlead))
    sig = sc['signal']
    sig_off = int(step)                     # room for the pick-up before bar 1
    lay(t, sig['drum'], 'signal', step, sig_off, 1, sig['pan'])
    for bar in (0, 16):                     # pick-up tone before each bar of the call
        t.add(voice_for('signal', sig['pickup']), sig_off + int((bar - 1) * step),
              pan=sig['pan'], vel=0.55)
    off = int(cycle * nlead)
    for p in sc['parts']:
        lay(t, p['drum'], p['key'], step, off, a.cycles, p['pan'])
        if 'bell' in p:
            lay(t, p['bell'], p['key'], step, off, a.cycles, p['pan'], vel=0.85)
    made.append((f'{R}-full{a.suffix}', write_wav(os.path.join(a.outdir, f"{R}-full{a.suffix}.wav"), t)))

    # ---- one file per instrument, with a 1-bar count-in click
    def countin(track):
        for i in range(4):
            track.add('click', int(i * div * step), vel=1.0 if i == 0 else 0.6)

    for p in sc['parts']:
        t = Track(total(a.cycles, 1))
        countin(t)
        off = int(cycle * 0.5)              # count-in is 1 bar = half a cycle
        lay(t, p['drum'], p['key'], step, off, a.cycles, 0.0)
        if 'bell' in p:
            lay(t, p['bell'], p['key'], step, off, a.cycles, 0.0, vel=0.85)
        # quiet quarter-note pulse so you can hear where the beat is
        beats = slots // div
        for q in range(int(a.cycles * beats)):
            t.add('click', off + int(q * step * div), vel=0.16)
        name = f"{R}-{p['key']}{a.suffix}"
        made.append((name, write_wav(os.path.join(a.outdir, name + '.wav'), t)))

        # dundun parts also get one hand at a time, for building the part up
        if 'bell' in p:
            for lane in ('drum', 'bell'):
                t = Track(total(a.cycles, 1))
                countin(t)
                lay(t, p[lane], p['key'], step, off, a.cycles, 0.0,
                    vel=1.0 if lane == 'drum' else 0.85)
                for q in range(int(a.cycles * beats)):
                    t.add('click', off + int(q * step * div), vel=0.16)
                nm = f"{R}-{p['key']}-{lane}{a.suffix}"
                made.append((nm, write_wav(os.path.join(a.outdir, nm + '.wav'), t)))

    # ---- the signal (call) on its own
    t = Track(int(cycle) + tail)
    countin(t)
    sig_off = int(cycle * 0.5)
    lay(t, sig['drum'], 'signal', step, sig_off, 1, 0.0)
    for bar in (0, 16):
        t.add(voice_for('signal', sig['pickup']), sig_off + int((bar - 1) * step), vel=0.55)
    made.append((f'{R}-signal{a.suffix}', write_wav(
        os.path.join(a.outdir, f"{R}-signal{a.suffix}.wav"), t)))

    for n, d in made:
        print(f"  {n}.wav  {d:5.1f}s")

if __name__ == '__main__':
    main()
