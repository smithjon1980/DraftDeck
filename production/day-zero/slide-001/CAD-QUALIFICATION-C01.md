# Day Zero — Slide 001 CAD Qualification Package

**Status:** CAD_CANDIDATE_SPECIFIED — NOT_RENDERED — HUMAN_APPROVAL_PENDING  
**Scope:** DraftDeck Slide 001, Stage I / Scene 01, manuscript paragraph 001  
**Source:** `manuscripts/day-zero/CANDIDATE-006-100-paragraphs.txt` (100 paragraphs, editorial baseline approved under `governance/approvals/APPROVED-EDITORIAL-006.md`)  
**Source custody commit:** `7b9e5c951d35b24dfacd445d118a3b278a7a6f13`  
**Source Git blob:** `d154ee72c6194f10ee7ed37d5f92db7bbfea1cb5`  
**Design authorities:** `design-system/boss-design-contract.json`, `design-system/tokens/tokens.css`, `design-system/components.md`, `doctrine/visual-evidence-gate.md`.

## Source paragraph

> 001. Imagine arriving at the end of a demanding workweek with the uncomfortable realization that you have been busy almost every hour, yet the most important project remains exactly where it started. You answered messages, corrected documents, investigated software, attended meetings, and resolved problems that appeared urgent. Each activity had a reasonable explanation. Nevertheless, when you examine what actually advanced the organization, the evidence is surprisingly thin. How can a week filled with completed tasks produce so little meaningful progress?

**Instructional question:** How can abundant activity coexist with negligible meaningful progress?  
**Editorial rule:** Source wording is locked. Any proposed on-slide condensation must be labeled an excerpt; full paragraph remains linked as selectable source/narration copy. No rewriting.

## CAD-only layout candidate (NTS)

- Logical canvas: **1920 × 1080**, 16:9, pure white `#FFFFFF`, fixed coordinates, CSS scaling for viewport.
- Use the actual DraftDeck React/Tailwind rendering path, `SlideCanvas`, `BrandMasthead`, `TechnicalPanel`, `PauseAndConsider`, and `ReleaseStatus` where implemented and verified; the registry is a candidate specification, not evidence of code availability.
- Hairline visible CAD drafting grid, measured inner border, visible zone markers, technical callout anchors, registration marks and title block. All framing must remain unobtrusive to later approved art/story and live text.
- Header: Bioscillate Operating System by Seven / DAY ZERO / STAGE I / SCENE 01.
- Primary story field: reserve dominant editorial artwork area; **no placeholder stick figures, synthetic diagram, or substitute art**.
- Copy field: reserve native selectable HTML text, including paragraph ID and guided-reasoning question. Keep full manuscript text available without clipping.
- Reflection rail: question anchored to paragraph 001, no invented answer.
- Title block: sheet `DZ-S001`, title `The Work That Never Moves Forward`, revision `CAD-C01`, status `CONCEPT — REFERENCE NOT APPROVED`, date, `NTS`, and source ID.
- CMYK brand treatment: use repository tokens for cyan/magenta/black; **yellow is a pending token/design-contract reconciliation**, not an invented replacement palette.
- Avoid SVG-based *slide construction* and SVG text. CAD framing can be native CSS/HTML; any independently approved SVG art remains a separate layer.

## Inspector gates — required evidence

| Gate | Current state | Required proof |
| --- | --- | --- |
| Manuscript 001 exists and is sequential | PASS (repository read) | Git blob and 001–100 count |
| Original upload byte parity | NOT_TESTED | Compare original bytes and repository bytes |
| CAD grid, border, zones, title block | NOT_TESTED | Actual 1920×1080 browser screenshot |
| Geometry, alignment, clipping | NOT_TESTED | DOM measurements and screenshot annotations |
| Live selectable text | NOT_TESTED | Browser DOM inspection |
| Approved art and story | HOLD | Separate human-selected reference/approvals |
| Browser render / visual diff | NOT_TESTED | Capture and side-by-side reference comparison |
| PDF and editor adapter fidelity | NOT_TESTED | Export and edit-save-reopen evidence |
| Human CAD acceptance | PENDING | Exact candidate hash and explicit review decision |

**Gate decision:** HOLD at CAD candidate. No composition, PDF release or inferred visual approval.

## Next execution

1. Locate the actual slide renderer and approved CAD grid family in the repository; do not substitute a Python-drawn slide.
2. Implement this as an isolated DraftDeck CAD candidate using existing components/tokens, without altering approved art/story assets.
3. Run the browser at 1920×1080 and capture the genuine screenshot, CAD inspector measurements, and source manifest.
4. Submit CAD screenshot and inspector results for human approval **before** art generation.
