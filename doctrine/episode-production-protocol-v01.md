# BOSS Episode Production Protocol — v0.1 (review candidate)

**Status:** SPECIFIED / NOT QUALIFIED. Applies to new BOSS episodes and instructional publishing. Inherits `design-system/boss-design-contract.json`, `design-system/library-policy.md`, `doctrine/visual-evidence-gate.md`, and `doctrine/production-contract.md`. This document does **not** approve artwork, override a print profile, certify ANSI/ISO conformity, or authorize publication.

## Publishing intent

**One canonical teaching script; multiple independently designed reading and viewing outputs.** BOSS may generate new episode-specific artwork without NotebookLM. NotebookLM is an optional source-exploration input, not a required generator, authority, or approval gate.

The **11 × 17 inch illustrated technical magazine** is the commercial print priority; the **1920 × 1080 slide sequence** is a word-for-word course/video *companion*; responsive web, video, and landscape/portrait/square infographic adapters are separate profiles. Never scale a slide and call it a print design.

### Core editorial design: rich, not cramped

- Preserve the large magazine headline, readable multi-column body copy, original Bioscillate logo, fine visible CAD/ISO-inspired drafting grid, zone indices, drawing/title block, illustration callouts, and reflection or evidence rail as story-relevant elements.
- **Art first:** draft the teaching story, design one or more scene-specific technical illustrations, obtain concept selection, then compose **separate** art, prose, and callout layers. No SVG-based slide construction and no flattening editorial text into the illustration.
- Prefer deliberate density and real paragraphs over generic bullets or empty slide space. Density is **not** permission to shrink type below tested readability.
- Distinguish conceptual drawings from certified technical drawings. Title plate on conceptual artwork includes sheet ID, title, revision, brand, date, status, and `NTS` (not to scale), rather than invented measurements.
- Maintain human editorial/visual/release approval. New art, layout, and copy are candidates until selected.

## Word-for-word companion contract (new requirement)

For each episode, identify a versioned **canonical narration/reading manuscript** with stable paragraph IDs and a SHA-256 checksum. The manuscript is authoritative for wording; reference notes, artwork labels, speaker cues, timing, localization, and editorial improvements must not be silently substituted into its quoted words.

For every segment in the **verbatim companion track**:
1. Record `episode_id`, `script_version`, paragraph/segment IDs, exact source text, ordered words, media time ranges if synchronized, and proposed page/slide placements.
2. Render each source segment as **native, selectable HTML text** in the slide sequence and as actual extractable text in the print PDF. Do not bake narration into artwork or SVG text.
3. Preserve word order, spelling, punctuation, and meaningful paragraph boundaries. If the source itself is corrected, make that change in a new manuscript revision; do not "fix" it only in the page.
4. **Across the entire companion sequence**, each required source segment appears exactly once in order (except explicitly labeled repeats), with no silent omissions, paraphrases, duplicate paragraphs, or invented narration. A single page need not contain the whole script.
5. Keep explanatory callouts, source citations, captions, analogies, reflection questions, and diagram labels in separately identified **supplemental** text fields. Supplemental copy must not be passed off as verbatim narration.
6. Record sentence/paragraph-to-page maps, text extraction results, any exceptions, and the human editorial sign-off. Automated sequence tests may flag missing/duplicated/mutated text but do not verify legibility or approve content.
7. If a video transcript includes unconfirmed speech recognition, mark `TRANSCRIPT_UNVERIFIED`; narration matching is not proven by a slide text match alone. Record audio/timestamp review separately.
8. English is the source track until an approved language edition exists. Spanish is a separately reviewed translation, not "word for word" identical to the English track.

**Reader promise:** a viewer should be able to follow the instructor's approved words in order, while enjoying a more fully illustrated and annotated print experience.

## Per-episode repeatable execution gates

| Gate | Required output | Blocking check |
|---|---|---|
| 00 — Source intake | Evidence bundle, citations, script origin, rights, hashes, uncertainties | Unsupported claims remain flagged; no invented source |
| 01 — Editorial manuscript | Stable paragraph IDs, episode thesis, complete canonical script, copy revision | Human editorial decision on manuscript |
| 02 — Story bridge | Sequence of teaching scenes and one visual concept per scene | Source claims and creative analogies clearly distinguished |
| 03 — Art concept | New scene-specific art candidates, provenance, title plate/CAD plan | Human selects concept before component reconstruction |
| 04 — Layout adapters | Distinct `slide` and `print` compositions from one content manifest | No generic SVG/wireframe stand-in; copy in native text layers |
| 05 — Structural evidence | Text coverage/in-order report, assets, versions, exact dimensions, collision tests | Missing/changed manuscript words or unknown assets = HOLD |
| 06 — Visual evidence | Full-size browser PNGs, approved-reference comparison, grid/title-block inspection, readable text | Human visual review; structural success cannot self-approve |
| 07 — Destination QA | Print PDF trim/MediaBox/text, print sample, optional editor import/edit/reopen, video narration alignment | Target-specific test separately recorded; printer proof before commercial release |
| 08 — Human release | Decision record with candidate ID, version/hash, scope, date, explicit authorization | No inferred approval or automatic publishing |

Version the package per episode as `EP##_source_manifest`, `EP##_script_vN`, `EP##_storyboard`, `EP##_art_manifest`, `EP##_slide_render`, `EP##_print_render`, `EP##_text_coverage`, `EP##_visual_evidence`, and `EP##_release_decision`. A new episode reuses the gates, **not** yesterday's artwork or example copy.

## Density experiment — proposed test bands, not approved production minima

The target is **more words per page without loss of editorial quality**. Use the revised two-column connector article as a reference for the magazine voice, not as a claim that a particular text size passed screen testing.

- **1920 × 1080 reading slide:** pilot **120–220 narration words per slide** for text-led spreads, then measure on actual laptop/mobile-sized viewer and at classroom projection distance. Fewer words for art-led scenes. Never claim projector readability from a high-resolution PNG alone.
- **11 × 17 inch print article page:** pilot **250–500 narration words plus separate illustrations/callouts**, conditioned on layout and physical proof. Print copy may be denser, but it must be independently typeset for paper.
- Treat these as starting hypotheses. Record measured body font size, line length, leading, usable text area, contrast, clipping, number of words, average reading time, and reviewer notes. **Don't hit a quota by reducing legibility.**
- If a word-for-word manuscript will not fit legibly, **add pages or slides**; never delete, summarize, compress or rasterize source words to force a count.
- For live video/projection, permit a **presenter scene** with less visible copy **only if** the separately provided `verbatim reading track` includes all manuscript text, clearly labeled and synchronizable; do not claim that presenter scene alone is the word-for-word companion.

## First implementation test

For Episode 01, begin with **“AI is art imitating life”** and the thesis **“The right procedure, the wrong environment”**; the manifesto comes **after** this opening. This is editorial direction, not an approved complete manuscript. Create new relevant artwork of **the same procedure situated in two visibly different execution environments**; do not reuse retired aviation/parcel metaphors or generically redraw old connector art. Compare one dense 1920 × 1080 reading spread and one 11 × 17 inch portrait or landscape article page using approved story/manuscript segments. Choose orientation and actual print bleed/binding with printer input. Validate the exact-script coverage, independent art and text, CAD title plate and grid, and both renders before requesting human qualification.

**Unimplemented in this PR:** renderer, automated text coverage test, video timing integration, artwork generation, print preflight, and actual human concept/visual approvals.
