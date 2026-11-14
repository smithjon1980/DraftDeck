# Day Zero Candidate 006 — manuscript-to-slide production map (review candidate)

**Document:** BOSS.DZ.C006.SLIDE.MAP.001  
**Manifest:** [slide-map.v1.json](slide-map.v1.json)  
**Status:** REVIEW CANDIDATE / NOT RELEASED  
**Governance:** HAVE — Human Authority, Verified Execution

## Authoritative source pin

- Repository: `smithjon1980/DraftDeck`
- Manuscript: `manuscripts/day-zero/CANDIDATE-006-100-paragraphs.txt`
- Fixed source commit: `dd1a3f89f1eaa4b416d6b5dadc4cd22547835c8c`
- Fixed manuscript Git blob: `514e759abe8308705856f814b4ef88d041113778`
- Human editorial authorization record: `governance/approvals/APPROVED-EDITORIAL-006.md`
- Integrity coverage: 100 sequential paragraphs, five stages, 20 five-paragraph scenes.
- Historical raw upload SHA-256 is **not** asserted to be the amended manuscript hash; exact restoration of five prior reference paragraphs is **not established**.
- Any subsequent manuscript edit requires a new source pin and impact review. Do **not** infer approval of the updated text.

## Slide rule

Each manifest entry binds exactly one paragraph, `001`–`100`, to one slide ID, `DZ-001`–`DZ-100`. Paragraph text must be retrieved from the pinned manuscript during composition, not manually paraphrased or copied from conversational memory. A slide may have an editorially concise visible headline or caption, but its manuscript content remains the verbatim reference and any adaptation must be explicit and approved.

**The map is a coverage contract, not 100 designed or generated slides.** Layout families for the full sequence remain pending individual visual review.

## Spark Image preflight — HOLD

A new input specification titled **BOSS.VISUAL.SPARK.001, v1.1** requires exactly **four identifiable reference images** and the approved manuscript. Its mission is a *single original Spark Image*, not a finished slide. The four images have not been identified as a controlled reference set in this production record; no Spark image has been generated or approved under it.

The Spark spec concludes with a superseded tagline; current governing usage is **HAVE — Human Authority, Verified Execution**. The specification also introduces controlled yellow while the repository's current design contract pins cyan/magenta/black. This is an unresolved contract-reconciliation item, not authorization for an unexplained palette change.

Before the Spark gate: register the four actual files with identifiers/digests, visually inspect each, compare recurring visual grammar, confirm manuscript source pin, then submit **one** candidate for human approval. Spark approval governs overall visual direction only.

## Three-slide calibration sequence

| Slide | Paragraph | Instructional test | Provisional panel family | Review emphasis |
|---|---|---|---|---|
| DZ-001 | 001 | Activity versus strategic progress | 04 | High-end realistic professional environment, grounded story, typography |
| DZ-053 | 053 | Dispatcher routes precisely to CAD/art/story/text | 06 | Separate protected layers, exact-scope changes, provenance |
| DZ-063 | 063 | Distinguish technical, visual, and editorial failure | 03 | Crisp vectors and PDF export, legibility, visual-story correspondence |

Panel selections are only proposals. No CAD, art, story, or final layout is approved by this document.

## Production execution and approvals

1. Pin/validate the source and review paragraph mapping.
2. Qualify one Spark Image against four supplied references; **stop for human Spark approval**.
3. Build candidate editable CAD geometry, maintaining approved white CAD/ISO background and brand metadata rails; obtain CAD review.
4. Generate original photorealistic art candidate, **stop for human art approval**.
5. Generate independent story-layer candidate, **stop for human story approval**.
6. Compose protected approved layers with native editable HTML/CSS/React manuscript text.
7. Render at 1920 × 1080 in a browser; inspect cropping, print hierarchy and any copy divergence.
8. Test SVG/PDF conversion and zoom sharpness. Do not rasterize vector artwork merely to conceal a broken export. If a genuine photograph remains raster, validate native pixel resolution independently.
9. Human accepts each slide by exact version/digest. Separate human release authority remains mandatory.

**Spark is a direction benchmark, not the same as the art layer.** Preparing a CAD geometry study does not authorize composition before independent art and story approval. Existing React/Tailwind, Windmill, n8n, Railway and GitHub Actions production paths remain unchanged.

## Structural check

Run from the repository root:

```bash
python3 tools/editorial-layout/check_day_zero_slide_map.py
```

The checker can report structural PASS while Spark, visual, render and publication gates remain HOLD/NOT TESTED. A structural PASS must never be described as visual acceptance.

## Next decision

Identify and provide the four reference images to qualify the one Spark Image candidate. After Spark approval, proceed with the three-slide calibration set. Neither this map nor structural validation authorizes publication.
