# Gidamba — transcription

Read off `Gidamba.pdf`. Audio in `audio/gidamba-*.wav`. Legend as in
[Djole.md](Djole.md).

**Metre 12/8 — this one is ternary.** Three subdivisions to the beat, not four,
so count **1 la li** rather than *1 e & a*. Four beats to the bar = 12 slots.

**Cycle 4 bars = 48 slots.** Only the doundounba actually needs that length;
everything else is a two-beat or one-bar loop repeating inside it.

The sheet marks **Einde** (Dutch, "end") on every part at beat 4 of the written
second bar, and **Begin** on the kenkeni and doundounba a slot later.

---

## Signal

```
        1 la li   2 la li   3 la li   4 la li
 (TT)   T  T  T   T  T  .   T  T  .   T  .  .
  ^two grace notes
```

Led in by two grace notes, then a run of tones thinning out across the bar —
three, two, two, one.

## Djembé 1 — two beats, repeated

```
        1 la li   2 la li
        S  .  T   S  .  .
```

The simplest part on the sheet. Slap, tone, slap, rest.

## Djembé 2 — two beats, repeated

```
        1 la li   2 la li
        S  .  S   S  T  T
```

Three slaps into two tones. The slap on the **li** of beat 1 running straight
into the slap on beat 2 is the bit to get clean.

## Sangban — two beats, repeated

```
        1 la li   2 la li
  drum  O  .  .   T  .  .
  bell  ✕  ✕  .   ✕  ✕  .
```

One stroke per beat, alternating **open** and **closed**. The bell is the
simplest on any of these sheets: two strokes then a gap, every beat.

## Kenkeni — one bar, repeated

```
        1 la li   2 la li   3 la li   4 la li
  drum  T  .  T   .  T  .   .  T  .   T  .  .
  bell  ✕  .  ✕   .  ✕  .   ✕  ✕  .   ✕  .  ✕
```

Every drum stroke sits on a bell stroke; the bell adds two more.

## Doundounba — a real four-bar phrase

```
  bars 1–2  drum  T  .  T   .  .  .   .  .  .   .  .  T
            bell  ✕  .  ✕   .  ✕  .   ✕  ✕  .   ✕  .  ✕

  bar 3     drum  T  .  T   .  T  T   .  T  .   T  .  T
            bell  ✕  .  ✕   .  ✕  ✕   .  ✕  .   ✕  .  ✕

  bar 4     drum  T  .  T   .  .  .   .  .  .   T  .  T
            bell  ✕  .  ✕   .  ✕  .   ✕  ✕  .   ✕  .  ✕
```

The only part on the sheet that is a phrase rather than a loop, which is why it
gets two staves. Bars 1 and 2 are sparse — three strokes each. **Bar 3 fills up
and the bell doubles the drum exactly**, then bar 4 thins out again. Note the
bell itself changes in bar 3 (a stroke on the **li** of beat 2 instead of beat
3's **1**) to follow the drum.

---

## Practising the dunduns

Every drum stroke in all three parts lands on a bell stroke, so no hand ever
moves alone. The work is holding the bell through the gaps — and, for the
doundounba, remembering a four-bar phrase.

| | Bell per cycle | Drum | Bell-only |
|---|---|---|---|
| **Kenkeni** | 28 | 20 | 8 |
| **Doundounba** | 28 | 17 | 11 |
| **Sangban** | 32 | 16 | 16 |

The counts say sangban is hardest, but they mislead here: its bell is the most
regular thing on the page and its drum is one stroke per beat. Take them
**kenkeni → sangban → doundounba**, and leave the doundounba last because it is
a memory problem rather than a hands problem.

Useful shortcut on the doundounba: **learn bar 3 first.** Drum and bell are in
unison for that whole bar, so it needs no independence at all — and it is the
bar that gives the phrase its shape.

## Audio

```sh
python3 tools/render_rhythm.py --rhythm gidamba --bpm 100 --cycles 6
python3 tools/render_rhythm.py --rhythm gidamba --bpm 72 --cycles 4 --suffix=-slow
```
