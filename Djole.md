# Djole — transcription

Read off `Djole.pdf`. Audio for every line is in `audio/` (see below).

**Metre** 4/4, counted in sixteenths. **Cycle** 2 bars = 32 sixteenths.
Only Djembé 2 actually uses the full two bars; everything else is a shorter
pattern that repeats inside it.

## Legend

| Symbol | On the sheet | Stroke |
|---|---|---|
| `B` | letter **B** | bass |
| `T` | black notehead | tone |
| `S` | red ✗ | slap |
| `O` | green notehead, underlined | dundun **open** tone (let it ring) |
| `M` | black notehead | dundun **muted** / closed tone |
| `x` | ✗ on the beam | bell (kenken), played by the dundun player |
| `.` | — | rest |

Hands follow the `R L R L` printed above the staff: every **even** sixteenth
(`1 &  2 &  …`) is right, every **odd** one (`e  a`) is left.

---

## Signal (call)

One bar, played twice, each time led into by a pick-up tone on the sixteenth
before the bar.

```
        1 e & a   2 e & a   3 e & a   4 e & a
  (T)   T . T T   . T . T   T . S S   S . . .
   ^pick-up
        R L R L   R L R L   R L R L   R L R L
```

Tones through the first half, then the three slaps that announce the break.

---

## Djembé 1 — one bar, repeated

```
        1 e & a   2 e & a   3 e & a   4 e & a
        B . T T   B . S S   B . T T   B . S S
        R   R L   R   R L   R   R L   R   R L
```

Bass on every quarter, then a pair on the `&`–`a`: **tones** on beats 1 and 3,
**slaps** on beats 2 and 4. That tone/slap alternation is the whole part.

## Djembé 2 — full two bars

```
  bar 1  1 e & a   2 e & a   3 e & a   4 e & a
         B . . T   T . . .   B . . .   T T T T
         R     L   R         R         R L R L

  bar 2  1 e & a   2 e & a   3 e & a   4 e & a
         T . . T   T . . .   B . . .   T . . .
         R     L   R         R         R
```

The two bars are identical except at the start: bar 1 opens on a **bass**,
bar 2 opens on a **tone**, and bar 1 ends with four straight tones where bar 2
has just one. Beat 4 of bar 1 is the hook — count it out loud.

## Sangban — half-bar pattern (repeats 4× per cycle)

```
        1 e & a   2 e & a
  drum  O . . .   M . . .
  bell  x . x .   x . x .
```

Open tone on 1, muted tone on 2. Bell straight through on the eighths.

## Kenkeni — one beat, repeated (16× per cycle)

```
        1 e & a
  drum  . . T T
  bell  . . x x
```

Nothing on the beat itself — the pair sits on `&` and `a`, drum and bell
together. It is the part that makes Djole lean forward.

## Doundounba — half-bar pattern (repeats 4× per cycle)

```
        1 e & a   2 e & a
  drum  O . . .   . . . .
  bell  x . x x   . x x .
```

One deep open tone per half bar; the bell carries the rest.

---

## Audio

Rendered by `tools/render_rhythm.py` (pure Python, no dependencies) using the
recorded samples in `samples/` — see `samples/CREDITS.md` for sources and
licences. If a sample is missing the renderer falls back to modal synthesis for
that voice, so it always produces output.

| File | What |
|---|---|
| `audio/djole-full.wav` | the call, then 8 cycles of the whole ensemble |
| `audio/djole-signal.wav` | the call alone |
| `audio/djole-djembe1.wav`, `-djembe2.wav` | one part each, count-in + quiet quarter-note pulse |
| `audio/djole-sangban.wav`, `-kenkeni.wav`, `-doundounba.wav` | dundun part, drum and bell together |
| `audio/djole-<part>-drum.wav` | dundun **drum hand only** |
| `audio/djole-<part>-bell.wav` | dundun **bell hand only** |

Default set is 96 bpm; a `-slow` set at 60 bpm sits alongside it for coordination
work. Other tempos:

```sh
python3 tools/render_rhythm.py --bpm 120 --cycles 12 --suffix=-fast
```

## Practising the dundun parts

The three dundun parts differ mainly in **how often the two hands coincide**, and
that — not the tempo — is what makes them hard. Learn them in this order:

1. **Kenkeni** — drum and bell are in unison, every stroke. No independence at all;
   the only difficulty is that nothing lands on the beat.
2. **Sangban** — bell on straight eighths, drum on every other one. Every drum
   stroke has a bell stroke under it, so the hands never truly separate. Say it as
   *both – bell – both – bell*.
3. **Doundounba** — the bell plays a syncopated five-stroke figure and the drum
   plays once per half bar, on the first of them. Four of the five bell strokes are
   bell-only, which is what makes this the hard one.

The method that works: get the **bell alone** to the point of boredom first, then
sing the drum part over it, then add only the strokes where both hands move
together, then fill in. Drop the tempo to 40–60 — much slower than feels necessary
— and practise it on your knees away from the drums.
