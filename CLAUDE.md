# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Not a software project — a personal practice folder for West-African drumming:
one-page notation PDFs, phone videos of lessons, and audio rendered from the
notation. There is no build, no test suite, and no git repository.

See `README.md` for the rhythm-by-rhythm index and the file-naming conventions.

**The score PDFs are not tracked by git** — they are the teacher's work, and the
repo is public. They live in this folder but are gitignored, along with `audio/`
(regenerable, 1.6 GB) and the lesson videos. Do not add them.

## Reading the notation PDFs

The PDFs are vector scores on a **sixteenth-note grid**, one row per instrument
(Signal, Djembé 1–2, Sangban, Kenkeni, Doundounba). They are not machine
readable as text — decode them visually, and prefer measuring pixels over
eyeballing:

```sh
pdftoppm -r 200 -png Djole.pdf out    # 200 dpi gives ~60 px per sixteenth
```

At 200 dpi the layout is regular: eight beamed groups of four sixteenths,
groups 181 px wide at a pitch of 241 px, so slot *j* of group *g* sits at
`x = start[g] + 60.33*j`. Detecting the beams (the longest horizontal black
runs) gives the grid; everything else hangs off it. Note that the dundun rows
are engraved ~15 px left of the djembe rows, so derive the grid per row or
allow a tolerance when snapping.

Symbols, and how to pick them out programmatically:

| Symbol | Meaning | Detection |
|---|---|---|
| black notehead | tone | filled disc, r ≈ 14 px — a disc test survives the stem it hangs from |
| red ✗ | slap | colour alone is enough |
| **B** | bass | merges with the beam, so template-match it rather than using connected components |
| `R L R L` | sticking | printed above the **djembe** staves only; positional, so no need to read it |
| green notehead + underline | dundun open tone | colour; ignore the short underline blob |
| ✗ on the beam | bell | sits astride the beam, arms poking above it |

**`tools/read_score.py` does this.** It renders the PDF, finds the staves and
each one's grid, and prints one line per part:

```sh
python3 tools/read_score.py ../Toro.pdf --rows 253,464,610,832,1034,1250,1466 \
  --staves signal,entrance,djembe1,djembe2,sangban,kenkeni,doundounba
```

Pass `--rows` rather than trusting auto-detection: a beam is drawn as a *double*
line, so the detector reports each stave twice on some sheets. Get the true rows
by eye from the rendered PNG.

It prints a **period** for each line. Almost every part is a short loop, so a
line reported as `period 32` is nearly always a missed notehead, not a real
irregularity — go and crop that slot. Two real exceptions found so far: Toro's
sangban (bar 1 ends closed, bar 2 open) and Toro's doundounba (bar 2 nearly
empty).

Three failure modes worth knowing:

- **The repeat barlines merge into the outer beams**, stretching those groups
  and skewing their slot positions by ~18 px, which silently drops the last
  stroke of the cycle. `beams()` clamps any span wider than the nominal beam.
- **Bells need paired-arm detection.** The cross arms rise only ~8 px above the
  beam and the beam is a double line, so thresholding a band does not work.
  Find the arm runs on several scan lines and keep slots that two lines agree on.
- **The `R L R L` labels sit above the djembe beams**, so only look for bells on
  dundun staves.

`Djole.md` and `Fankani.md` are worked examples of the finished output. Both
sheets come from the same engraver, so the geometry above is reusable as-is —
Fankani needed no new measurements.

Two things the Djole sheet does not show up:

- **`Begin` arrows.** A downward triangle over a stem marks where that part's
  own cycle starts, which need not be bar 1. Sangban and Doundounba carry them
  on the Fankani sheet. Record it; do not rotate the pattern to match it.
- **`Einde` arrows** (upward, Dutch for "end") mark the stroke a part finishes
  on — a performance instruction, not a cycle marker, and not the same thing as
  `Begin`. The Djolé (Guinée) sheet uses them on all seven staves.
- **An underline means "let it ring"** regardless of the notehead it sits under
  — green dundun noteheads and the red ✗ of that sheet's Djembé 3 alike. Those
  are open slaps.
- **Staves vary.** Djolé (Guinée) has seven, not six. Detect the stave rows
  rather than hardcoding bands: scan for y values with a high black-pixel count
  across the page and cluster them.
- **Green vs black noteheads on kenkeni.** Green + underline is an open
  (ringing) stroke, black is closed. Djole's kenkeni is all black, Fankani's has
  both, which is why `kenkeni_M` exists as a damped copy of the sample.

Transcribe literally. Fankani's doundounba has a gap where a period-8 reading
would predict a stroke; that is what the sheet says, so that is what the
renderer plays, with the discrepancy flagged in `Fankani.md`.

## Rendering audio

`tools/render_rhythm.py` — pure Python (`wave`, `math`, `random`), no
third-party packages. numpy is **not** available and cannot be pip-installed
here; PIL is.

Voices come from `samples/` when the files are present and fall back to the
modal synthesis in `SRC` otherwise — keep both paths working. Samples must be
16-bit mono 44.1 kHz or `load_wav` rejects them. `tools/build_pack.py` is the
conditioning step: trim to 3 ms before the attack, cap the length, level-match.
Skipping the trim is what makes a sampled part drag behind the beat.

Reverb is a Schroeder network, not convolution — FFT convolution is impractical
without numpy, and an O(n) comb/allpass chain does the job.

Scores are dicts of grid strings (`.` rest, `B`/`T`/`S` djembe, `O`/`M` dundun,
`x` bell); `|` and spaces are ignored, so write them grouped in beats. Each
part carries its own pattern length and is tiled to fill the cycle. Voices are
synthesised once into buffers at import and mixed by sample offset.

```sh
python3 tools/render_rhythm.py --bpm 100 --cycles 8
python3 tools/render_rhythm.py --bpm 76 --cycles 6 --suffix=-slow   # note the '='
```

`--suffix=-slow` needs the `=`; argparse reads a bare `-slow` as a flag.

Verify a render by detecting onsets and snapping them to the sixteenth grid —
they should land on integers. Note that a loud drum stroke masks a bell hit
immediately after it, so a naive envelope detector under-reports the bell
lines; missing positions are fine, unexpected ones are not.

**Sticking never needs extracting.** It is purely positional — even slot index
is the right hand, odd is the left. That holds for the binary sheets (`R L R L`
per group of four) and for ternary ones, where groups of three flip the printed
alternation to `R L R / L R L` by themselves. The dundun staves carry no
sticking at all: one hand is on the bell.

## Ternary sheets

Gidamba is **12/8** — three subdivisions to the beat. Scores carry a `div` field
(4 or 3); the renderer and the trainer page both derive step duration, beat
accents, bar lines and tick labels from it, so never reintroduce a hardcoded
`/4` or `% 16`.

The geometry differs too: groups hold **three** stems over a 125 px beam (≈60.6
px apart) at a pitch of ~250 px, and — unlike the binary sheets — **each stave
is engraved at its own horizontal offset**, up to ~30 px apart. Fit the grid per
row; a shared grid with a tolerance wide enough to absorb that offset is wider
than half a slot and will mis-snap. Deriving offsets from detected stems is
unreliable where stems are short, so anchor on noteheads and beam spans, and
check any group that looks odd by cropping it.

Cycle length is the longest part, not a constant: Gidamba's doundounba is a
four-bar phrase where everything else loops in one or two bars, so the cycle is
48 and the short parts tile into it. Both the renderer and the page tile with
`pattern[i % pattern.length]`.

## Adding a rhythm

1. `tools/read_score.py` the PDF; crop and check anything it flags as aperiodic.
2. Transcribe to `<Rhythm>.md` using the layout in `Djole.md`.
3. Add a score dict to `render_rhythm.py` (`div`, `slots`, `signal`, `parts`)
   and render both tempos.
4. Verify by detecting onsets in the rendered WAV and snapping them to the grid
   — they must land on integers. Extra positions mean a false detection (a loud
   stroke masks the next); *missing* positions mean a real bug.
5. Add the rhythm to `RHYTHMS` in the trainer page and a button to the switcher.
6. Add the row to the table in `README.md`.

Part keys drive voice selection in both the renderer and the page: `signal`,
`entrance` and `djembe*` use djembe voices, `sangban`/`sangban2` the sangban
ones. A new key needs adding in both places.
