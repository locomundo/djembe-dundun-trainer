#!/usr/bin/env python3
"""Read one of these one-page drum scores off its PDF.

The sheets are vector engravings on a fixed grid: eight beamed groups per
system, four stems per group for a binary rhythm (beam ~181 px at 200 dpi) or
three for a ternary one (~125 px). This finds the staves, works out each one's
grid, and reads the noteheads off it.

    python3 read_score.py ../Gumbé.pdf --staves signal,djembe1,djembe2,...

Symbols: black disc = tone, red cross = slap, green disc + underline = open
dundun tone, B = bass, cross on the beam = bell. An underline means "let it
ring" whatever it sits under.
"""
import argparse, os, subprocess, sys, tempfile
from collections import deque
from PIL import Image

def render(pdf, dpi=200):
    d = tempfile.mkdtemp()
    subprocess.run(['pdftoppm', '-r', str(dpi), '-png', pdf, os.path.join(d, 'p')], check=True)
    return Image.open(os.path.join(d, 'p-1.png')).convert('RGB')

class Score:
    def __init__(self, im, div=4):
        self.im = im; self.W, self.H = im.size; self.px = im.load()
        self.div = div
        self.span = 181 if div == 4 else 125      # beam width at 200 dpi
        self.step = self.span / (div - 1)

    def blk(self, x, y):
        p = self.px[x, y]; return p[0] < 110 and p[1] < 110 and p[2] < 110
    def kind(self, x, y):
        r, g, b = self.px[x, y]
        if r > 150 and g < 110 and b < 110: return 'red'
        if g > 110 and r < 120 and b < 140: return 'green'
        if r < 110 and g < 110 and b < 110: return 'black'

    def staves(self, min_ink=150, min_gap=60):
        ink = [sum(1 for x in range(150, self.W - 20, 2) if self.blk(x, y)) for y in range(self.H)]
        out = []
        for y in range(1, self.H - 1):
            if ink[y] > min_ink and ink[y] >= ink[y - 1] and ink[y] > ink[y + 1]:
                if not out or y - out[-1] > min_gap: out.append(y)
        return out

    def beams(self, by):
        """(start, end) of each beamed group on this stave."""
        ink = [x for x in range(150, self.W - 20)
               if any(self.blk(x, y) for y in (by - 1, by, by + 1))]
        if not ink: return []
        cl = [[ink[0]]]
        for x in ink[1:]:
            (cl[-1].append(x) if x - cl[-1][-1] <= 55 else cl.append([x]))
        out = []
        for c in cl:
            a, b = c[0], c[-1]
            if b - a <= self.span * 0.6: continue
            # the repeat barlines sit close enough to merge into the outer
            # groups; a beam is always exactly self.span wide, so clamp it
            if b - a > self.span * 1.12:
                if out: b = a + self.span          # trailing barline swallowed
                else:   a = b - self.span          # leading one
            out.append((a, b))
        return out

    def grid(self, by, ref=None):
        """The slot x-positions for this stave."""
        b = self.beams(by)
        if len(b) == 8:
            return [s + (e - s) / (self.div - 1) * j for s, e in b for j in range(self.div)]
        if ref is None: return None
        return None            # caller re-fits against the reference

    def fit(self, glyphs, ref):
        best = (-1, 0)
        for d in range(-45, 46):
            hits = sum(1 for g in glyphs if min(abs(g - (s + d)) for s in ref) <= 11)
            if hits > best[0]: best = (hits, d)
        return [s + best[1] for s in ref]

    def discs(self, y0, y1, R=9):
        cand = []
        for y in range(y0 + R, y1 - R, 2):
            for x in range(200, self.W - 40, 2):
                if self.kind(x, y) != 'black': continue
                tot = hit = 0
                for dy in range(-R, R + 1, 2):
                    for dx in range(-R, R + 1, 2):
                        if dx * dx + dy * dy <= R * R:
                            tot += 1
                            if self.kind(x + dx, y + dy) == 'black': hit += 1
                if hit / tot > 0.97: cand.append((x, y))
        out = []
        for x, y in cand:
            for c in out:
                if abs(c['x'] - x) < 18 and abs(c['y'] - y) < 18:
                    c['p'].append((x, y)); c['x'] = sum(q[0] for q in c['p']) / len(c['p']); break
            else: out.append({'x': x, 'y': y, 'p': [(x, y)]})
        return out

    def blobs(self, y0, y1, kind, minn=90):
        seen = set(); out = []
        for y in range(y0, y1):
            for x in range(200, self.W - 40):
                if (x, y) in seen or self.kind(x, y) != kind: continue
                q = deque([(x, y)]); seen.add((x, y)); pts = []
                while q:
                    a, b = q.popleft(); pts.append((a, b))
                    for dx in (-1, 0, 1):
                        for dy in (-1, 0, 1):
                            n1, n2 = a + dx, b + dy
                            if (y0 <= n2 < y1 and 200 <= n1 < self.W - 40
                                    and (n1, n2) not in seen and self.kind(n1, n2) == kind):
                                seen.add((n1, n2)); q.append((n1, n2))
                if len(pts) > minn:
                    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
                    out.append({'x': sum(xs) / len(xs), 'h': max(ys) - min(ys)})
        return out

    def bells(self, by, slots):
        """A cross shows as two separate arms just above the beam; pair them.

        Thresholding a band does not work - the arms rise only a few pixels and
        the beam is a double line - so find arm runs on several scan lines and
        keep the slots that at least two lines agree on."""
        votes = {}
        for dy in range(-12, -2):
            y = by + dy
            runs, cur = [], []
            for x in range(200, self.W - 30):
                if self.blk(x, y): cur.append(x)
                elif cur:
                    if 1 <= len(cur) <= 14: runs.append((cur[0] + cur[-1]) / 2)
                    cur = []
            if 1 <= len(cur) <= 14: runs.append((cur[0] + cur[-1]) / 2)
            for i in range(len(runs) - 1):
                gap = runs[i + 1] - runs[i]
                if not (8 < gap < 34): continue
                c = (runs[i] + runs[i + 1]) / 2
                d = sorted((abs(c - s), k) for k, s in enumerate(slots))
                if d[0][0] < self.step * 0.4:
                    votes[d[0][1]] = votes.get(d[0][1], 0) + 1
        return sorted(k for k, v in votes.items() if v >= 2)

    def bees(self, y0, y1, slots, tpl):
        """The letter B merges with the beam, so match it as a template."""
        th, tw = len(tpl), len(tpl[0]); tot = th * tw
        hits = []
        for y in range(y0, y1 - th):
            for x in range(200, self.W - tw - 30):
                m = 0
                for j in range(th):
                    row = tpl[j]
                    for i in range(tw):
                        if row[i] == self.blk(x + i, y + j): m += 1
                if m / tot > 0.86: hits.append((x, y))
        keep = []
        for x, y in hits:
            if any(abs(a - x) < 15 and abs(b - y) < 15 for a, b in keep): continue
            keep.append((x, y))
        out = []
        for x, y in keep:
            d = sorted((abs(x + tw / 2 - s), i) for i, s in enumerate(slots))
            if d[0][0] < 26: out.append(d[0][1])
        return sorted(set(out))

    def arrows(self, by, slots, above):
        y0, y1 = (by - 72, by - 20) if above else (by + 100, by + 178)
        y0, y1 = max(0, y0), min(self.H, y1)
        seen = set(); out = []
        for y in range(y0, y1):
            for x in range(1300, self.W - 30):
                if (x, y) in seen or not self.blk(x, y): continue
                q = deque([(x, y)]); seen.add((x, y)); pts = []
                while q:
                    a, b = q.popleft(); pts.append((a, b))
                    for dx in (-1, 0, 1):
                        for dy in (-1, 0, 1):
                            n1, n2 = a + dx, b + dy
                            if (y0 <= n2 < y1 and 1300 <= n1 < self.W - 30
                                    and (n1, n2) not in seen and self.blk(n1, n2)):
                                seen.add((n1, n2)); q.append((n1, n2))
                xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
                if 12 < max(xs) - min(xs) < 30 and 20 < max(ys) - min(ys) < 50 and len(pts) > 200:
                    cx = sum(xs) / len(xs)
                    d = sorted((abs(cx - s), i) for i, s in enumerate(slots))
                    if d[0][0] < 28: out.append(d[0][1])
        return sorted(set(out))

def load_b_template(path='b_template.png'):
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    if not os.path.exists(here): return None
    im = Image.open(here).convert('RGB'); px = im.load()
    return [[px[i, j][0] < 110 and px[i, j][1] < 110 and px[i, j][2] < 110
             for i in range(im.size[0])] for j in range(im.size[1])]

def periodicity(pat):
    """Smallest period that fits, or the best near-fit and where it breaks.

    Most of these parts are short loops, so a result that is not periodic is
    usually a missed notehead rather than a real irregularity - this points at
    the slot to go and look at."""
    n = len(pat)
    for p in (d for d in range(1, n + 1) if n % d == 0):
        if all(pat[i] == pat[i % p] for i in range(n)):
            return p, []
    best, bad = None, None
    for p in (d for d in range(1, n) if n % d == 0):
        miss = [i for i in range(n) if pat[i] != pat[i % p]]
        if bad is None or len(miss) < len(bad): best, bad = p, miss
    return best, bad

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf')
    ap.add_argument('--staves', required=True, help='comma-separated names, top to bottom')
    ap.add_argument('--div', type=int, default=4)
    ap.add_argument('--rows', default='', help='override detected stave y positions')
    a = ap.parse_args()

    sc = Score(render(a.pdf), a.div)
    names = a.staves.split(',')
    ys = [int(v) for v in a.rows.split(',')] if a.rows else sc.staves()
    if len(ys) != len(names):
        print(f'! detected {len(ys)} staves {ys} but was given {len(names)} names', file=sys.stderr)
        print('  pass --rows to pin them down', file=sys.stderr)
        sys.exit(1)

    tpl = load_b_template()
    ref = None
    for by in ys:                      # the first clean 8-group stave sets the reference
        g = sc.grid(by)
        if g: ref = g; break
    n = 8 * a.div
    for nm, by in zip(names, ys):
        dun = not (nm.startswith('djembe') or nm.startswith('signal'))
        slots = sc.grid(by)
        y0, y1 = by + 16, by + (130 if a.div == 3 else 170)
        D = sc.discs(y0, y1); R = sc.blobs(y0, y1, 'red'); G = sc.blobs(y0, y1, 'green')
        X = [s for s in (slots or ref)]
        if slots is None:
            glyphs = [c['x'] for c in D + R + G]
            slots = sc.fit(glyphs, ref) if glyphs else ref
        def snap(x, tol=None):
            tol = tol or sc.step * 0.42
            d = sorted((abs(x - s), i) for i, s in enumerate(slots))
            return d[0][1] if d[0][0] < tol else None
        ev = {}
        for c in D:
            i = snap(c['x'])
            if i is not None: ev[i] = 'T'
        for c in R:
            i = snap(c['x'])
            if i is None: continue
            ev[i] = 'S' if c['h'] >= 20 else ev.get(i, 'S')      # thin = the underline
        for c in G:
            if c['h'] < 9: continue
            i = snap(c['x'])
            if i is not None: ev[i] = 'O'
        if tpl and not dun:
            for i in sc.bees(y0, y1, slots, tpl):
                ev.setdefault(i, 'B')
        drum = ''.join(ev.get(i, '.') for i in range(n))
        bl = sc.bells(by, slots) if dun else []
        bell = ''.join('x' if i in bl else '.' for i in range(n))
        up = sc.arrows(by, slots, above=False); dn = sc.arrows(by, slots, above=True)
        mark = (f'  einde={up}' if up else '') + (f'  begin={dn}' if dn else '')
        pd, bad = periodicity(drum)
        note = f'  period {pd}' if not bad else f'  ! period {pd}, breaks at {bad}'
        print(f'{nm:14s} drum {drum}{mark}{note}')
        if any(ch == 'x' for ch in bell):
            pb, badb = periodicity(bell)
            nb = f'  period {pb}' if not badb else f'  ! period {pb}, breaks at {badb}'
            print(f'{"":14s} bell {bell}{nb}')

if __name__ == '__main__':
    main()
