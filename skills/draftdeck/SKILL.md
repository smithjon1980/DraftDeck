---
name: draftdeck
description: Source-grounded BOSS instructional visual production. Use for Episode 01, Day Zero, slides, lesson interfaces, and candidate print compositions requiring separate art and editable native text, browser evidence, governed handoff, and human release approval.
---

# DraftDeck — governed visual-production skill (rebuild candidate)

## Authority and scope
Read `AGENTS.md`, `design-system/boss-design-contract.json`, `doctrine/production-contract.md`, `doctrine/reference-render-protocol.md`, `doctrine/visual-evidence-gate.md`, and `doctrine/release-qa.md`. The machine-readable design contract controls current BOSS identity and profile dimensions. Historical demonstration material does **not** override it. This skill is operating guidance, not evidence of approval or a new visual master.

Read these task-focused references:
- `references/editorial-composition.md` for source admission, two-bridge storytelling, and semantic hierarchy.
- `references/web-engineering.md` for React/Tailwind, HTML/CSS, responsive layout, accessibility, and design-token practices.
- `references/visual-acceptance.md` for actual browser renders, PDF/export comparisons, gates, and failure handling.
- `references/verified-pipeline.md` **only when evaluating the historical Canva adapter experiment**; never inherit its retired brand style.

## Mandatory execution: Survey → Evaluate → Validate → Execute → Normalize
1. **Survey**: Obtain authoritative copy, source-art provenance, approved reference (or explicitly record REFERENCE_UNAPPROVED), profile, destination, and teaching assertion. Preserve unknowns; never invent logo source or interpret NotebookLM output as authority.
2. **Evaluate**: Produce the source → teaching story bridge, then story → BOSS screen/print composition bridge. Choose art-led, narrative-led, or hybrid according to the teaching relationship, not a fixed alternating template. Identify geometry and output risks before implementation.
3. **Validate before building**: Check source-copy manifest, art availability/hash, brand contract, design tokens, story completeness and measurable acceptance criteria. Missing canonical reference or logo is HOLD, not permission to substitute generic geometry.
4. **Execute candidate**: Compose source art, story, CAD/ISO-informed geometry, masthead, native editable text, annotations and reflection/notes as separately inspectable layers. Use React/Tailwind for the specified slide viewer, render to static HTML/CSS as appropriate. A slide is a fixed 1920×1080 logical canvas scaled as a unit; the lesson website reflows semantically; print has an independent unapproved geometry unless separately ratified.
5. **Inspect actual output**: Render through a real browser. Compare browser capture with reference for storytelling, copy, art, branding, grid/title plate, readability and collisions. If producing PDF, compare the browser render against PDF at matched physical framing/dimensions; resolution improvement alone does not restore missing art.
6. **Verify release evidence**: Run design-contract checks, brand proof where suitable, and evidence-manifest validation. Preserve FAIL, PASS, NOT_TESTED distinctly. A syntactically complete manifest is not pixel fidelity, human authorization or editability.
7. **Handoff and normalize**: Test import separately in the actual adapter; inspect layer selection, edit/save/reopen and visual fidelity. Store a minimal reproducible manifest and negative regression fixture when a failure is repaired. Never release on silence or on a machine-only PASS.

## Non-negotiables
- Brand: **Bioscillate Operating System by Seven**; original verified logo and canonical white/black/cyan/magenta identity. Do not substitute the historical orange Logistics palette.
- No generic boxes-and-lines simplification of approved illustration. Rich story artwork remains source-traceable; editorial words stay native HTML, never SVG text or full-slide rasterization.
- Avoid retired aviation/parcel metaphors in contemporary work; do not claim ISO/ANSI certification from stylistic influence.
- Preserve exact spoken/script copy where required. Add editorial labels only as explicitly distinct annotations.
- Rendered source and PDF are **derivatives**; fix the source rather than manually polishing derivatives.
- Human review of actual images is obligatory. Generation ≠ verification ≠ approval ≠ authorized release.

## Output contract
For every candidate emit: candidate ID and status; pinned source provenance; source and copy manifests; two-bridge editorial plan; exact profile and dimensions; asset list with hashes or UNKNOWN; implemented source/commit; actual browser screenshot; reference comparison and change annotations; native text/art evidence; gate states; adapter test status; reviewer decision; unresolved risks; next allowed operation. Keep unreleased scripts, binary art and sensitive evidence out of public repositories and CI logs.

## Failure rules
- Missing source/reference/identity → **HOLD: SOURCE**.
- Missing primary story mechanism/art → **FAIL: STORY**, not repaired by DPI, PNG conversion or extra decorative grid.
- CSS/HTML structural pass but composition mismatch → **FAIL: VISUAL**.
- Missing or untested destination editability → **NOT_TESTED: ADAPTER**.
- No explicit scope-bound human approval → **HOLD: RELEASE**.

A candidate without adequate evidence is not an eligible winner, even when all candidates are weak.
