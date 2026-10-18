# Episode 01 — Design skill guidance, controlled Phase 2 comparison

**Status:** PRIVATE EXPERIMENT EXECUTED / BOTH PATTERNS CONDITIONALLY ENDORSED / PAGE-LEVEL VISUAL APPROVAL PENDING.
Date: 2026-10-18. No unpublished manuscript, source art, private manifest or PDFs belong in this public repository.

## Scope and provenance

Two independently composed 17 x 11 inch landscape two-page candidates (A and B) used the same eight complete paragraphs from the *unapproved* Episode 01 new narration candidate: section 01 paragraphs 1–5, section 02 paragraphs 1–3. Headers, captions and footers were explicitly nonscripted editorial apparatus.

Guidance actually inspected:
- Taste Skill: asymmetric composition, authentic subject image inventory, proof-before-layout thinking, browser look/fix loop. Its website-specific no-grid rule conflicts with the governing BOSS CAD accent requirement, so was not adopted.
- Impeccable: Read mode, grouping by meaning instead of boxes/cards, typesetting rhythm and browser inspection. Its context-loading binary and deterministic detectors were **not** executed.
- Awesome DESIGN.md: Tesla and WIRED design analyses read as inspiration only. No external brand colors, proprietary fonts or images imported.
- Playwright: the **preinstalled Python Playwright with local Chromium actually executed**. Upstream Playwright CLI was not installed or run.

The environment blocked local HTTP navigation. Browser rendering instead used in-memory page content with locally embedded, owner-supplied art. No outside network resources were required for rendering.

## Verified private outputs

| Check | A | B |
|---|---|---|
| Real Chromium screenshots | 2 pages | 2 pages |
| PDF page size | Both 1224 x 792 pt | Both 1224 x 792 pt |
| Exact private-manifest paragraph equality in browser DOM | PASS, 5+3 paragraphs | PASS, 5+3 paragraphs |
| Whitespace-normalized paragraph matches in PDF selectable text | PASS | PASS |
| Native selectable type in PDF | PASS | PASS |
| Embedded images in PDF | One per page | One per page |
| Automated text/footer/figure overlap checks | No flags | No flags |
| Human visual approval | PENDING | PENDING |
| Physical print test | NOT_TESTED | NOT_TESTED |

### Distinctions to review

Candidate A keeps the whole engineering two-environment concept together on the second page, and uses a mechanical-detail image on page one. Candidate B creates a broad gear-art band and changes the narration to a magazine-like horizontal reading rhythm. B crops part of the engineering scene, which may reduce teaching context. The data do **not** justify declaring a universal visual winner. The owner later confirmed that both A and B are useful, **depending on the teaching story**. Page-level approval remains separate.

### Human composition feedback — 2026-10-18

The owner reviewed the A/B comparison and confirmed: **both A and B work, depending on the story described on each page**. Consequently **neither is a universal winner**. This is human validation of their usefulness as **conditional composition patterns**, **not** unconditional page/master approval or print publication authorization.

**Narrative-led pattern (A):** Favor fuller diagrams, explanatory relationships and native narrative text when multiple constraints must be read together. Preserve essential engineering relationships in view.

**Art-led pattern (B):** Favor larger storytelling images and text flowing around/below them when the image carries the principal teaching point. Cropping is acceptable only if it does not remove relationships needed for comprehension.

**Hybrid / other:** The art/story relationship may require a third arrangement; do not enforce a binary template family. The same overall issue should vary paragraph density and image prominence *per source beat* rather than alternate layouts mechanically.

**Selection procedure for each page:** (1) identify the exact candidate/approved script passage and its teaching assertion; (2) identify the visual evidence or engineering relationship necessary to understand it; (3) assign narrative-led, art-led or hybrid based on which content must dominate; (4) compose without imprisoning narration in boxes; (5) verify no omitted, reordered or manufactured spoken copy; (6) render and inspect actual readability, art integrity and print geometry; (7) obtain separate human page/issue approval. A beautiful page that truncates a critical mechanism is a failed teaching page.

## Reproducibility without releasing private work

The new generic tool at tools/visual-poc/render_local_proof.py renders vetted local 17 x 11 HTML and locally supplied art with actual Chromium into screenshots, a PDF and an independent structural report. It disables JavaScript and network requests in the browser. Sample invocation:

    python tools/visual-poc/render_local_proof.py /PRIVATE/candidate_B.html --image-dir /PRIVATE --output-dir /PRIVATE/render_B --pages 2

This script verifies the canvas size and basic overflow; it is **not** a complete visual-collision checker, source-copy comparator, or printer acceptance tool. For separate PDF dimensions and copy checks, use tools/visual-poc/check_print_pdf.py with a local private manifest. Do not commit private inputs or upload private render artifacts to public Actions logs.

## Explicit limits and next gate

- A skill's design advice applied manually is not the same as running Taste's draw.mjs or Impeccable's CLI detectors. Those native executables, licenses of bundled assets, hooks, permissions and transitive dependencies still require isolated admission.
- These files do not change BOSS's 1920 x 1080 slide profile or automatically approve any 17 x 11 print master.
- The Episode 01 script remains a *NEW_SCRIPT_CANDIDATE*, not a verified transcript of a recording.
- No 48-page issue was built, and no Canva import, individual rendered-page approval, prepress/physical proof, or release was established. The owner's acceptance of both composition *patterns* is recorded above.
- **HOLD** on public publication, external provider installers and visual master claims until documented human review.

This report records reproducible local methods, but does not include unreleased script or art bytes.
