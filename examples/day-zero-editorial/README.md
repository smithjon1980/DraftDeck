# BOSS Day Zero editorial companion v0.4

15-slide, 17 x 11 landscape companion and matching Markdown article. Shipping-logistics teaching frame; low, medium and high copy; ten editorial features. These features are not additional canonical shared-frame fields.

- `slides/`: static HTML/CSS, separate SVG geometry, preview, manifests and diagram source. The PDF review rendition is regenerated locally with `python editorial-deck/build.py` (run from `source/`).
- `article/`: Markdown and relative PNG/SVG images. One actual-relay screenshot placeholder remains intentionally unfilled.
- `source/`: build inputs and dependencies. Run from this directory: `python editorial-deck/build.py`. Requires Python ReportLab and DejaVu Sans fonts. Output appears in `source/editorial-deck/`; copy reviewed output to `slides/` after inspection.

## What changed in v0.4

Revised against the editorial review of v0.3 (USWDS token and component practices, BOSS visual identity, WCAG 2.2 AA target):

1. **Slide 6 corrected first.** The SOURCE block carries the exact Community Workshop source only — title, schedule, materials, and the open question about the room number. Acceptance commentary moved to its own block; the Inspect the Payload component presents exact source, candidate value, and inspection finding as three distinct columns.
2. **Repetitive copy removed.** Slides 2, 5, 10, 12 and 13 no longer share padding paragraphs; each medium page carries one explicit teaching relationship.
3. **Components implemented through shared tokens.** All ten editorial features render as distinct components per `design-system/editorial-components.md`, styled from `design-system/tokens/tokens.css` (BOSS color, type, spacing and stroke tokens). The generated HTML contains zero inline style attributes.
4. **Distinct layouts per teaching purpose.** Fifteen named layouts replace the repeated three-block arrangement: opener, duo, payload-flow, reference-ten, compare, inspect, steps, reference-seven, recovery, case, route, map, quad, checkpoints, checklist.
5. **Structured features.** Slide 4 fields numbered 01–10 in a consistent reading order; slides 7 and 9 carry stepped practice/recovery layouts with ruled record space; slides 8 and 10 use the Evidence Window component (claim, support, scope, limitations); slide 11 routes through explicit conditional branches (within authorization / scope expands); slide 14 presents acceptance and authorization as two distinct checkpoints; slide 15 is a numbered submission checklist.
6. **Consulting exhibits added.** Seven decision-grade visuals break up the sequence diagrams, one per teaching point, drawn from the token palette: slide 3 MECE tree (ten fields, three branches, no overlap), slide 7 chevron flow (prepare, transfer, compare), slide 9 recovery loop (omit, recover, recheck until the comparison passes), slide 11 routing decision tree (capability and authorization gates), slide 12 automation maturity staircase (manual, assisted, automated), slide 13 two-by-two mechanism selection matrix (task logic against external action), slide 15 evidence funnel (six items, three verified claims, one release decision). The PDF carries a sixteenth appendix page, CONSULTING EXHIBITS, indexing all seven.
7. **Semantic, reflowing HTML.** One `h1` per slide, `h2` per block, landmarks and labelled regions. Below the 1100px breakpoint the fixed canvas reflows to a single-column lesson layout (the website reflows rather than scales, per contract). Drafting geometry is drawn for the PDF canvas and kept as standalone `geometry-NN.svg` artifacts; the HTML edition relies on semantic reading order instead of embedding PDF-coordinate geometry, which collided with the component layouts.

## Verification

Browser rendering verified with headless Chromium at 1632 x 1056 (slide canvas) and 800 px width (reflow) against the generated HTML; slides 3, 6, 7, 9, 11, 12, 13, 14 and 15 inspected visually, including all seven consulting exhibits and the PDF appendix page. Build check: 15 slides, 15 `h1`, 0 inline style attributes. The PDF uses ReportLab with matching coordinates; it is not a browser export. Accessibility conformance audit and current Canva compatibility remain untested. Rendered PDF pages were reviewed and five Markdown image references resolve.

The supplied 22-minute script anchors these artifacts; they do not represent a regenerated 60-minute audio overview. NotebookLM examples are reported with limited evidence; sampled excerpts do not establish exhaustive fidelity. Preserve source requests, responses, comparisons, recovery records and unknowns. No release authority follows from VERIFIED alone.
