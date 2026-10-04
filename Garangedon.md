# Garangedon — transcription

Read off `notenblad-Garangedon.pdf`. Audio in `audio/garangedon-*.wav`. Legend
as in [Djole.md](Djole.md).

**Metre 12/8 — ternary.** Counted **1 la li**, four beats to the bar = 12 slots.

**Cycle 2 bars = 24 slots.**

The sheet marks **Begin** (down arrow) on djembé 1, sangban, kenkeni and
doundounba at the last slot of bar 2 — slot 23. There are no **Einde** marks.

> The arrows sit *between* staves and point **down** into the row they belong
> to. `read_score.py` attributes each one to both neighbouring staves, so it
> reports a spurious `einde` on the row above every `begin`. Garangedon has no
> ends at all; ignore them.

---

## Signal

```
        1 la li   2 la li   3 la li   4 la li
 (T)    T  .  T   T  .  T   T  .  T   T  .  .     bar 1
 (T)    T  .  T   T  .  T   .  .  T   T  .  .     bar 2
```

The two bars are **not** identical: bar 2 drops the stroke on beat 3 and
answers on the **li** instead. Each bar is led in by a **galop** — grace note
and beat as two very fast strokes, left then right.

## Djembé 1 — two bars

```
 bar 1  B  .  S   .  .  S   .  .  S   .  .  S
 bar 2  B  .  S   T  T  S   T  T  S   .  .  S
```

A **slap on the li of every beat**, without exception — that is the spine of
the part. Bar 2 fills beats 2 and 3 with two tones ahead of the slap.

## Djembé 2 — two beats, repeated

```
 S  .  T   S  .  .
```

## Djembé 3 — two beats, repeated

```
 S  .  .   S  T  T
```

## Sangban — one bar, repeated

```
 drum   T  .  O   .  .  T   .  .  O   .  .  T
 bell   ✕  .  ✕   ✕  .  ✕   ✕  .  ✕   ✕  .  ✕
```

The only part that uses both dundun tones: closed on beat 1, **open** on the
**li**, and open again on the li of beat 3.

## Kenkeni — two beats, repeated

```
 drum   .  .  T   T  .  .
 bell   ✕  .  ✕   ✕  .  ✕
```

Two drum strokes **back to back across the beat** — the li of one beat and the
beat that follows — then a beat off. Both are bell strokes.

## Doundounba — two bars

```
 bar 1  T  .  T   T  .  .   .  .  T   T  .  T
 bar 2  T  .  T   .  .  .   .  .  .   .  .  T
 bell   ✕  .  ✕   ✕  .  ✕   ✕  .  ✕   ✕  .  ✕     (both bars)
```

Busy through bar 1, then **two whole beats of bell alone** in bar 2 before a
single stroke closes the cycle.

---

## All three bells are identical

```
 ✕  .  ✕     every beat, every part, both bars
```

This is unusual on these sheets and it is the most useful thing about
Garangedon: learn the bell hand once and it carries the sangban, the kenkeni
and the doundounba alike, so you can swap drum parts without relearning the
bell.

## Coincidence count

| part | drum | bell | drum on a bell stroke | bell only |
|---|---|---|---|---|
| sangban | 10 | 16 | 10 (all) | 6 |
| kenkeni | 8 | 16 | 8 (all) | 8 |
| doundounba | 9 | 16 | 9 (all) | 7 |

No hand ever moves alone. The sangban has the most drum strokes and the fewest
bell-only strokes, which makes it easier to hold than its density suggests.
