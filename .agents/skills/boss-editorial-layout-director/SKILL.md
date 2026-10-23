---
name: boss-editorial-layout-director
description: Choose and validate 1–4 column BOSS manuscript layouts from exact source-locked spoken paragraphs, including text-only, art-led and hybrid Episode 01 pages. Use before artwork composition and before browser/PDF export.
---

# BOSS Editorial Layout Director — manuscript-first slides

## Authority and approved scope
Read `AGENTS.md`, `skills/draftdeck/SKILL.md`, `design-system/boss-design-contract.json`, the approved owner-provided spoken source and current slide-to-paragraph manifest. The owner approved Episode 01 V4 narration; an older V1/V3 approval or unrelated pitch-slide headline is not a substitute for the mapped V4 paragraph IDs and hashes. Keep unpublished manuscript bytes out of the public repository.

The eight consulting-style communication principles are **editorial disciplines**, not McKinsey branding or a new visual palette: story before styling, conclusion-led **nonspoken** title, one primary teaching job per page, correct relationship layout, sourced evidence, stable spacing, functional page families and three independent review passes.

## Decision before rendering
1. Preserve exact spoken text and paragraph sequence. Record `slide_id`, ordered `paragraph_ids`, source paragraph hashes, slide-level SHA-256 of paragraphs joined with `\n\n`, and source word count. Do not rewrite or drop narration to fit.
2. Define the one principal instructional takeaway. Add a candidate nonspoken action title; it must not impersonate narrator copy or introduce an unverified factual assertion.
3. Select the column count from meaning **and** measured rendering, not an aesthetic quota:
   - **One manuscript column:** continuous exposition, typically with separate technical illustration.
   - **Two:** compare physical/digital systems or two connected stages.
   - **Three:** claim/evidence/implication or ordered analytical parts.
   - **Four:** dense book-style manuscript/synthesis; legibility on a presentation display is a distinct human gate.
4. Preserve the BOSS wordmark candidate as a separately identified asset, clean white drafting ground, cyan/magenta/black brand and CAD/ISO geometry. Art may be omitted on deliberately text-only pages; never include a filler photo or flatten manuscript words into art.
5. If columns would be uneven, split long paragraphs **only at sentence boundaries**, retain every original whitespace character in concatenated fragments, preserve contiguous per-paragraph fragments and DOM reading order, and use `data-para-id` plus contiguous `data-run` indexes. The output must reconstruct the exact approved bytes and hashes.
6. No auto-summarization, unauthorized extra pages, invisible text, font shrinking below the chosen readability threshold, or clipped overflow to achieve an apparent PASS. A failure invokes HOLD and human-authorized layout/pagination review.

## Required mechanical gates
- Run `python tools/editorial-layout/check_editorial_manuscript.py rendered_single_slide.html slide_manifest.json` against the actual single-slide HTML, not JSX or a combined page. It checks source/paragraph hashes, exact word count, column count, order and fragment indexes.
- Render in Chromium at 1920×1080, inspect each `.copy-col` scroll size and actual glyph bounds, title/reflection/crop regions, font sizes and reading order. No browser renders or measured geometry → **NOT_TESTED**.
- PDF export must preserve selectable spoken text. Compare PDF raster against actual browser output, inspect at real viewing scale, and verify downstream edit/save/reopen in the intended editor separately.
- Mark `source_integrity`, `text_fit`, `human_legibility`, `illustration_provenance`, `pdf_native_text`, `browser_pdf_difference`, `target_editability`, `human_selection` independently. Structural text PASS never grants visual or publication approval.

## Local-private baseline, October 22, 2026
Four tests used the owner-approved 250-paragraph V4 local source with **no private script bytes committed**:
- Slide 02: 133 words, one column + reference-only artwork, 25.5px body.
- Slide 18: 312 words, two columns, 24.7px body.
- Slide 36: 359 words, three columns, 23.1px body.
- Slide 59: 385 words, four columns, 22.2px body.

All four **exact source hashes and browser overflow** tests passed after correcting initial overflow in every layout; four PDF exports had native text. This validates feasibility, not comfort of dense 22.2px projection, clean illustration source status, human visual approval, or adoption across all 60 slides. Art on Slide 02 was a cropped historical concept and is **not** production-approved. Keep those results in a private review package, not in public CI.

## Release boundary
**Author-approved narration ≠ accepted layout ≠ accepted artwork ≠ accepted target editor ≠ authorized release.** A slide may be text-only if intentional and complete; an art-led slide must additionally pass the governed art/story gate. Unresolved state → HOLD.
