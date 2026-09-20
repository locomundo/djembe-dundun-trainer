# djembe-dundun-trainer

Tools for reading one-page West-African drum scores off a PDF, rendering
play-along audio from them, and drilling the parts — particularly the **dundun**
parts, where one hand plays the bell and the other the drum.

Pure Python, no third-party packages. The trainer is a single HTML file.

## Why

Learning a dundun part is mostly a coordination problem: the bell hand has to
become automatic before the drum hand can do anything independent. What helps is
being able to **switch one hand off** and play the other against the rest of the
ensemble — which is what this does.

## The trainer

`dundun-trainer.html` — one page, no build step, no dependencies. For each
rhythm it shows every part on a grid, with the dundun parts split into separate
**drum** and **bell** lanes you can mute independently. Tempo down to 40 bpm,
sticking, a count, and the call.

Browsers block `fetch()` on `file://`, so serve it rather than double-clicking:

```sh
python3 -m http.server 8000     # then open http://localhost:8000/dundun-trainer.html
```

## The tools

| | |
|---|---|
| `tools/read_score.py` | Reads a score PDF: finds the staves, works out each one's grid, prints the parts. Reports a **period** per line — since almost every part is a short loop, a line that is not periodic is usually a missed notehead, which is what makes the output checkable. |
| `tools/render_rhythm.py` | Renders WAVs per rhythm: the full ensemble, one file per part, and **drum-only / bell-only** for each dundun part. |
| `tools/build_pack.py` | Conditions raw sample downloads — trims to 3 ms before the attack, caps length, level-matches. |

```sh
python3 tools/read_score.py Rhythm.pdf --rows 261,461,658 --staves signal,djembe1,djembe2
python3 tools/render_rhythm.py --rhythm djole --bpm 100 --cycles 8
```

Rendered WAVs land in `audio/`, which is gitignored — the full set runs to over
a gigabyte and regenerates from the tools.

Scores live in the `RHYTHMS` dict in `render_rhythm.py` and in `RHYTHMS` in the
trainer, written on a subdivision grid:

```
.  rest    B  bass    T  tone    S  slap
O  open dundun tone   M  muted   x  bell
```

`div` is subdivisions per beat — 4 for a binary rhythm, 3 for a ternary one like
Gidamba in 12/8. Bar lines, accents and tick labels all derive from it.

## Sound

Modal synthesis was the starting point — damped sinusoids at the inharmonic
modes of a drum head, struck by a filtered noise transient — but recorded
samples turned out far more recognisable, so `samples/` holds conditioned
one-shots and synthesis is only the fallback when a sample fails to load.

## Hosting the trainer

`dundun-trainer.html` needs the `samples/` folder beside it — it fetches the
WAVs at runtime by relative path. Copy both and it works anywhere static files
are served; there is nothing to build and no server-side code.

## What is not here

**The source notation.** These transcriptions were read from one-page scores
written by [Michael Agbodo](https://agbodo.nl), who teaches these rhythms. The
rhythms themselves are traditional, but the scores are his work and he is
preparing a book of them, so they are not included here. The tools are written
against that layout, so to use `read_score.py` you will need your own scores in
a similar format.

## Credits

Taught and notated by **[Michael Agbodo](https://agbodo.nl)**. The rhythms are
traditional West-African repertoire; the scores they were transcribed from are
his.

Drum samples come from [Freesound](https://freesound.org); ten are CC0 and one
is CC BY 3.0. Per-file sources and licences are in `samples/CREDITS.md`.

## Licence

MIT for the code — see `LICENSE`. The samples keep their own terms.
