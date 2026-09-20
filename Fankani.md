# Fankani — transcription

Read off `Fankani.pdf`. Audio for every line is in `audio/`.

**Metre** 4/4, counted in sixteenths. **Cycle** 2 bars = 32 sixteenths.
Same engraver and layout as `Djole.pdf`, so the same legend applies — see
[Djole.md](Djole.md) for the symbol table.

Where Djole is built on a bass every quarter, **Fankani is built on slaps**.
Both djembe parts open on a slap and keep coming back to it; the tones and
basses are what fall between.

---

## Signal (call)

**Identical to the Djole signal** — same pick-up, same phrase. The teacher
appears to use one call for both.

```
        1 e & a   2 e & a   3 e & a   4 e & a
  (T)   T . T T   . T . T   T . S S   S . . .
   ^pick-up
```

## Djembé 1 — one bar, repeated

```
        1 e & a   2 e & a   3 e & a   4 e & a
        S . . S   S . B .   S . T T   S . B .
```

A slap on every quarter. After that the bar splits in half: beats 1–2 answer
with a **bass on the "&"**, beats 3–4 answer with **two tones** then another
bass. The slap on the "a" of beat 1 is the one that trips people up — it comes
straight after the downbeat slap.

## Djembé 2 — half bar, repeated 4×

```
        1 e & a   2 e & a
        S . . S   S . T T
```

The same opening as Djembé 1 — slap, slap on the "a", slap on 2 — but it
resolves into two tones every half bar instead of alternating. Shortest part on
the sheet and the best one to start on.

## Sangban — full two bars, **begins at bar 2 beat 3**

```
  bar 1  1 e & a   2 e & a   3 e & a   4 e & a
  drum   . . . .   . . T .   T . T T   . . O .
  bell   ✕ . ✕ ✕   . ✕ ✕ .   ✕ . ✕ ✕   . ✕ ✕ .

  bar 2  1 e & a   2 e & a   3 e & a   4 e & a
  drum   . . . .   . . O .   . . T T   . . O .
  bell   ✕ . ✕ ✕   . ✕ ✕ .   ✕ . ✕ ✕   . ✕ ✕ .
                             ↑ Begin
```

The sheet marks **Begin** on the "&" of bar 2 beat 3 — that is where the
sangban's own cycle starts, not at bar 1. The two bars are nearly the same; bar
1 has one extra closed tone on beat 3.

## Kenkeni — half bar, repeated 4×

```
        1 e & a   2 e & a
  drum  T T . .   O . . .
  bell  ✕ ✕ . ✕   ✕ . ✕ .
```

Two closed tones on 1 and the "e", then the **open** tone on 2. Every drum
stroke has a bell stroke underneath it.

## Doundounba — three strokes in the whole cycle, **begins at bar 2 beat 4**

```
  bar 1  drum  . . . .   . . . .   . . . .   . . T .
  bar 2  drum  . . . .   . . T .   . . . .   . . T .
                                             ↑ Begin
  bell (both bars)  ✕ . ✕ ✕   . ✕ ✕ .   ✕ . ✕ ✕   . ✕ ✕ .
```

Only **three** drum strokes per 32-sixteenth cycle, all on the "&". Note the
gap: there is no stroke on the "&" of bar 1 beat 2, even though the pattern
elsewhere repeats every half bar. That is how the sheet is written and I have
kept it literal rather than "correcting" it — worth checking with your teacher.

---

## Practising the dunduns

Same principle as Djole: what makes a part hard is **how much the bell plays
alone** while the drum hand waits.

| | Bell strokes per cycle | Drum strokes | Bell-only |
|---|---|---|---|
| **Kenkeni** | 20 | 12 | 8 |
| **Sangban** | 20 | 9 | 11 |
| **Doundounba** | 20 | 3 | **17** |

In Fankani **every single drum stroke lands on a bell stroke** — in all three
parts. There is no moment where the drum hand moves alone, which makes this
easier than Djole's doundounba. The whole difficulty is in holding the bell
while the drum hand rests.

So again: **kenkeni first, then sangban, then doundounba**, and get the bell
automatic before you add the drum hand.

The two bells are not the same, which is easy to miss:

- Sangban and Doundounba share `✕ . ✕ ✕ . ✕ ✕ .`
- Kenkeni plays `✕ ✕ . ✕ ✕ . ✕ .`

## Audio

```sh
python3 tools/render_rhythm.py --rhythm fankani --bpm 100 --cycles 8
python3 tools/render_rhythm.py --rhythm fankani --bpm 76 --cycles 6 --suffix=-slow
```

Files land in `audio/fankani-*.wav`: the full ensemble, the call, one file per
part, and for each dundun a **drum-only** and **bell-only** file.
