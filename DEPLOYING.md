# Putting the trainer on a website

The trainer is a static page: one HTML file plus the `samples/` folder it
fetches WAVs from at runtime. Anywhere that serves static files will host it.

**It is already live at**

> https://locomundo.github.io/djembe-dundun-trainer/dundun-trainer.html

served by GitHub Pages from this repo's `main` branch. Relative paths work
unchanged, so nothing needed modifying.

---

## Embedding it in WordPress

Tested assumption: you have a `wp-admin` login but **no FTP or file-manager
access**. That rules out uploading the files to the site itself, for three
reasons:

1. WordPress **refuses `.html` uploads** by default — a blocked MIME type.
2. The block editor **strips `<script>` and `<style>`** from Custom HTML blocks
   unless your user has the `unfiltered_html` capability. Administrators on a
   single-site install have it; Editors do not. The trainer is ~67 KB of inline
   CSS and JS, so losing either kills it.
3. The 11 WAVs would each need uploading to the Media Library and every path
   rewritten to an absolute URL.

So: host it here, embed it there.

### The iframe

New page → add a **Custom HTML** block → paste:

```html
<iframe src="https://locomundo.github.io/djembe-dundun-trainer/dundun-trainer.html"
        style="width:100%;height:90vh;border:0" loading="lazy"
        title="Dundun Trainer"></iframe>
```

GitHub Pages sends no `X-Frame-Options` and no `frame-ancestors` policy
(verified), so framing is permitted.

### If the iframe vanishes when you save

That is WordPress stripping it, which means your user lacks `unfiltered_html`.
Either get an Administrator account, or use a plain link instead — nothing
strips a link:

```
https://locomundo.github.io/djembe-dundun-trainer/dundun-trainer.html
```

A link is a perfectly good answer. The trainer wants the full screen anyway, and
a link avoids an iframe fighting the theme for height on a phone.

---

## Troubleshooting

**The page loads but there is no sound.**
Browsers block audio until the visitor interacts with the page, and inside an
iframe the click has to land *in the iframe*. Pressing **Play** counts. If it
still fails, open the page directly — if sound works there but not framed, it is
the gesture policy, not the files.

**The transport says "synthesised" instead of "real instruments".**
The WAVs failed to load; the page falls back to synthesis so it still works.
Check `https://locomundo.github.io/djembe-dundun-trainer/samples/bass.wav`
returns 200.

**The iframe is too short, or scrolls awkwardly on mobile.**
Raise `height`, or switch to `height:100vh`. Some themes constrain content
width; a full-width or blank page template usually helps. Or use the link.

**Nothing appears at all.**
Check the browser console for a mixed-content error — the site must be served
over HTTPS for an HTTPS iframe to load.

---

## Updating it

Push to `main`. The live page rebuilds in about a minute; no re-uploading, and
the embed URL does not change.

## Serving it from agbodo.nl instead

GitHub Pages supports a custom domain — e.g. `trainer.agbodo.nl` — set in
Settings → Pages, with a DNS `CNAME` record pointing at
`locomundo.github.io`. That needs DNS access, not WordPress. It would make the
URL read as Michael's rather than a github.io address.

## Turning it off

```sh
gh api -X DELETE repos/locomundo/djembe-dundun-trainer/pages
```

or Settings → Pages in the repo.

## Note on the root URL

`https://locomundo.github.io/djembe-dundun-trainer/` currently renders the
README, not the trainer — the repo root reads as a project page and the trainer
sits at its own path. To make the root *be* the trainer instead, add an
`index.html` that redirects, or rename the file.
