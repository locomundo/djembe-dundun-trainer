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

New page → add a **Custom HTML** block (or, in Enfold's Avia builder, a **Code
Block**) → paste:

```html
<iframe id="dundun-trainer"
        src="https://locomundo.github.io/djembe-dundun-trainer/dundun-trainer.html?lang=nl"
        style="width:100%;height:900px;border:0" loading="lazy"
        title="Dundun Trainer"></iframe>
<script>
window.addEventListener("message", function (e) {
  if (e.origin !== "https://locomundo.github.io") return;
  if (e.data && e.data.type === "dundun-trainer:height") {
    document.getElementById("dundun-trainer").style.height = e.data.height + "px";
  }
});
</script>
```

`?lang=nl` opens the trainer in Dutch for agbodo.nl's visitors; they can still
switch to English with the EN button. Leave it off and the page follows the
visitor's browser language instead.

The trainer posts its height to the host page, and that listener resizes the
iframe to match — so the page grows to fit instead of scrolling inside the
frame, which looks wrong on a themed site. The `e.origin` check means only the
trainer can drive the resize. The `900px` is just a starting height before the
first message arrives.

GitHub Pages sends no `X-Frame-Options` and no `frame-ancestors` policy
(verified by GET, not just HEAD), so framing is permitted. agbodo.nl sets no
`Content-Security-Policy`, so it will not block the frame either.

### Make the page full width

The trainer is a wide grid and looks cramped in a theme's content column, with
gutters either side. In Enfold, on the page edit screen:

- **Layout → Sidebar**: choose **No Sidebar**
- If the theme still constrains width, use a **Color Section** element set to
  full width and put the Code Block inside it

### The page's address

The site uses pretty permalinks (`agbodo.nl/contact/`), so a page with the slug
`dundun-trainer` lives at `agbodo.nl/dundun-trainer/`. The slug is editable
under the title in the editor. A `?page_id=1234&preview=true` URL is only the
preview link for an unpublished draft.

### Adding it to the menu

**Weergave → Menu's** → select the main menu → tick the page under **Pagina's**
→ **Aan menu toevoegen** → drag it to sit next to Contact → **Menu opslaan**.

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

## As deployed (verified 2026-10-03)

Live at **https://agbodo.nl/ritmes/**, in the main menu as **Ritmes**, next to
Contact. Verified from outside the browser: page returns 200, the listener
script survived WordPress, the iframe carries its `id`, and the trainer reports
"real instruments" (so all 11 samples load from Pages).

The site runs **Enfold 8** with the **Classic Editor**.

### The one thing that decides whether this works

**Paste into the `Tekst` tab, never `Visueel`.** The Classic Editor's visual
mode strips `<script>` tags, and switching tabs re-runs TinyMCE and strips them
again — so do not switch back to Visueel before saving. Everything else about
this deployment was straightforward; this was the only real obstacle.

TinyMCE will also reformat the markup harmlessly (`height:900px` becomes
`height: 900px;`, `loading="lazy"` is dropped) and sometimes saves invisible
`<span data-mce-type="bookmark" class="mce_SELRES_start">` cursor artifacts into
the content. They do nothing, but delete them if you see them.

To check the script survived: save, then reopen the **Tekst** tab. If the
`<script>` block is gone, it was stripped.

### Page width

The page uses Enfold's **Indeling → Zijbalken** setting (the Dutch label for the
layout panel). Removing the sidebar widens it, but Enfold still holds the
content inside the theme's max-width container — it is not edge to edge. True
full-bleed would need the Avia Layout Builder with a Color Section, which is a
larger change to the page. The boxed look reads fine as an embedded tool.

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

## SEO of the embed page (Yoast)

The site runs Yoast, and the Ritmes page scored red. The score is accurate,
not a misconfiguration: the page body is a single `<iframe>`, so there is no
text for Yoast to analyse. More importantly there is none for Google either —
**iframe content is never attributed to the parent page.** The trainer's own
text is indexed under `locomundo.github.io`; `agbodo.nl/ritmes/` reads as an
empty page.

Verified live on 2026-10-03:

    <title>Ritmes - Agbodo Workshops</title>
    og:description content="&#xFEFF;"   <- the TinyMCE bookmark artifact, not a description
    headings: none
    body: one <iframe>, nothing else

So the fix is content, not settings. Three things, in order of payoff.

### 1. Text around the iframe

Roughly 300 words of Dutch, with subheadings, placed **above** the iframe
(intro) and **below** it (the rest). Draft copy is in `seo-copy-ritmes.md` —
paste it in the `Tekst` tab, same rule as the embed snippet: never switch to
`Visueel` before saving, or the `<script>` is stripped.

This alone clears most of Yoast's red bullets: word count, subheading
distribution, keyphrase in intro, and the "no content" readability flags.

### 2. Yoast fields on the page

- **Focus keyphrase:** `djembé ritmes oefenen`
- **SEO title:** `Djembé ritmes oefenen | Agbodo Workshops` — this is separate
  from the page title, so the menu item stays `Ritmes`.
- **Meta description:** write one. It is currently the stray `&#xFEFF;`
  character above, which is what leaks into `og:description` when the page is
  shared on social media.
- The slug `ritmes` already contains the keyphrase; leave it alone, since
  changing it breaks the published URL.

### 3. Internal links

Yoast checks for them and they are genuinely useful here: link from the copy
to the lessons and contact pages, and add a link *to* `/ritmes/` from the
lessons page. An orphan page ranks poorly however good its content is.

### What not to chase

Green is not the goal — it measures whether a page is written like an article,
and this one is a tool. Once the copy is in, the remaining red bullets will be
things like outbound links and keyphrase density, which are not worth
distorting the text for.

One open question for Michael: the trainer is also reachable at its
GitHub Pages URL, which can compete with `agbodo.nl` for his own material.
A `rel="canonical"` or a `noindex` on the GitHub copy would point search
engines at his site instead. Not done — it is his call.
