# Djolé (Guinée) — transcription

Read off `djole-guinee-3partijen.pdf` (*3 partijen* = three parts). Audio in
`audio/djole-guinee-*.wav`. Same engraver and legend as [Djole.md](Djole.md).

**Metre** 4/4 in sixteenths. **Cycle** 2 bars = 32 sixteenths. **Seven staves** —
this setting has **three** djembe parts.

Two markings that the plain Djolé sheet doesn't use:

- **Einde** (Dutch, "end") — an upward arrow marking the stroke each part
  finishes on. They cluster on beat 4 of bar 2; Djembé 1 and Kenkeni stop one
  sixteenth earlier, on the "a" of beat 3.
- **Underlined red ✗** on Djembé 3 — the underline means the same thing it does
  under a green dundun notehead: *let it ring*. So these are **open slaps**.

---

## Signal

The same call as Djole and Fankani. Ends at bar 2 beat 4.

## Djembé 1 — half bar, repeated 4×

```
        1 e & a   2 e & a
        S . S S   . S T T
```

Five strokes in eight. The slaps on **&** and **a** of beat 1 running straight
into the slap on the "e" of beat 2 is the awkward bit.

## Djembé 2 — half bar, repeated 4×

```
        1 e & a   2 e & a
        B . T T   B . S S
```

**This is note-for-note the Djembé 1 part from `Djole.pdf`.** If you know that,
you already have this part.

## Djembé 3 — full two bars

```
  bar 1  1 e & a   2 e & a   3 e & a   4 e & a
         S . . .   S . . .   S . . T   T . . .

  bar 2  1 e & a   2 e & a   3 e & a   4 e & a
         S . . .   T T T T   T T . T   T . . .
```

The exposed part. Four bare **open slaps** (let them ring), a pair of tones at
the end of bar 1, then bar 2 opens into a run of six straight tones. Sparse,
then suddenly not — the run is the whole character of the part.

## Sangban — one bar, repeated

```
        1 e & a   2 e & a   3 e & a   4 e & a
  drum  . . . .   T . . .   . . . .   T . T .
  bell  ✕ . ✕ .   ✕ . ✕ .   ✕ . ✕ .   ✕ . ✕ .
```

## Doundounba — one bar, repeated

```
        1 e & a   2 e & a   3 e & a   4 e & a
  drum  T . . .   . . . .   T . T .   . . . .
  bell  ✕ . ✕ .   ✕ . ✕ .   ✕ . ✕ .   ✕ . ✕ .
```

**The doundounba is the sangban a beat earlier** — identical figure, shifted
back four sixteenths. Once you see it, the two parts are one idea.

## Kenkeni — one beat, repeated

```
        1 e & a
  drum  . . T T
  bell  . . ✕ ✕
```

**Identical to the other Djolé's kenkeni.** Drum and bell in unison; nothing on
the beat.

---

## Practising the dunduns

Both the sangban and the doundounba run against a **straight-eighths bell**, and
every drum stroke lands on one — no hand ever moves alone in any of the three
parts.

| | Bell per cycle | Drum | Bell-only |
|---|---|---|---|
| **Kenkeni** | 16 | 16 | 0 — unison |
| **Doundounba** | 16 | 6 | 10 |
| **Sangban** | 16 | 6 | 10 |

Order: **kenkeni** (unison), then **doundounba**, then **sangban** — and take
sangban last precisely *because* it is the same figure as doundounba. The
similarity is the trap: it is easy to play and hard to hear, and if you learn
them the other way round you will keep sliding into the doundounba's placement.

## Audio

```sh
python3 tools/render_rhythm.py --rhythm djole-guinee --bpm 100 --cycles 8
python3 tools/render_rhythm.py --rhythm djole-guinee --bpm 76 --cycles 6 --suffix=-slow
```
