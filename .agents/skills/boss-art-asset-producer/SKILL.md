---
name: boss-art-asset-producer
description: Produce separate source-traceable illustrated BOSS story artwork. Use when photo art, dark HUD treatments, missing illustrations, flattened generated text, or low-quality PDF art compromise instructional fidelity.
---

# BOSS Art Asset Producer — illustrated scene, not photo art

## Required instructions
Read the admitted Story Architect and Visual Storyboard records plus `AGENTS.md` and `design-system/boss-design-contract.json`. The default for Episode 01 narrative art is **hand-crafted-looking technical editorial illustration**. Preserve the original teaching relationship, not an earlier failed raster treatment. Record user requests that modify medium or wordmark status.

## Production decisions
1. Determine `art_medium`: `EDITORIAL_ILLUSTRATION` (default); `TECHNICAL_DIAGRAM` may support it. Treat `PHOTO`, `PHOTOREALISTIC`, and `DARK_HUD` as explicit disallowed candidate media for this Slide 02. Do not transform a rejected photo merely by placing it on white.
2. Source-grounded scene first: create an axonometric/cutaway/sectional business environment with mechanically intelligible activity and evidence of **what was verified and delivered**. For a Market Seven candidate, a functioning POS workflow is illustrative, not a claim of real deployment. Do not invent measured results.
3. **Separate the image component:** generate or recover clean text-free/label-safe illustration artwork without the masthead, BOSS wordmark, original Bioscillate logo, exact teaching copy, reflective question, or CAD title rail baked into pixels. Final editorial text is HTML; its copy source is independently verified.
4. Track two identity assets individually: original recovered Bioscillate logo (known SHA-256 in code) and **new BOSS wordmark selected by the user for concept design** (art-source/hash currently a candidate and must be independently provided or derived with provenance before verified production use). Never claim they are byte-equivalent or overwrite the original.
5. Prefer a true illustration with clear fine lines, limited brand accents, readable operational detail and a pure #FFFFFF field. Reject stock-photo compositions, photorealistic people, fake software screenshots, repetitive boxes/arrows and half-page generic icon grids.
6. Preserve unaltered generated output and prompt/reference lineage. Record actual pixel dimensions, SHA-256, crop regions, displayed CSS dimensions, upscaling factor, and effective print resolution. Do not call PNG a vector or claim that DPI export creates missing detail.
7. Candidate inspection: hide all text and marks; ask whether the illustration alone conveys the operational transition, a working system, test/proof, and a real learner-relevant outcome. Fail if it does not. Machine hashing verifies asset identity, not semantic meaning.

## Handoff and verification
For the bounded offline HTML gate, place the final illustration in a separate `<img>` with a self-contained data URI and record `story_art.sha256`, `source_id` and `teaching_relationship`. Preserve original logo separately when the current gate requires it. An unapproved BOSS-wordmark graphic does not count as story illustration. Cropping a full candidate screenshot does not turn flattened copy into a production layer.

Report media rule PASS/FAIL, illustration quality REVIEW_REQUIRED, source permissions, and remaining unknowns. No release authorization is implied.
