---
name: boss-art-asset-producer
description: Produce or recover source-traceable separate story illustration assets for BOSS slides without flattening approved editorial text. Use when a slide contains only a logo, artwork is missing/pixelated, or PDF export appears to lose visual detail.
---

# BOSS Art Asset Producer — preserve real story artwork

## Authority
Read the admitted storyboard, `AGENTS.md`, `design-system/boss-design-contract.json` and `doctrine/visual-evidence-gate.md`. Follow the actual image-generation/editing tool workflow when artwork generation or edits are requested; do not claim to run an unavailable provider.

## Asset production
- Prefer preserved original permitted high-quality artwork where possible. Record source, license/rights status, author/owner, original bytes hash, dimensions, crop and transformation history.
- For new art, use the **required teaching relationship** as the prompt's subject. The drawing must communicate concrete operational activity and consequences; reject generic rectangles, undifferentiated icon clusters and branding-only art.
- Produce a distinct illustration asset separate from the original logo. Never redraw, recolor, recreate or misidentify the original logo. Preserve exact original logo identity.
- **Concept stage:** an exploratory complete composition may contain rough generated typography. **Production stage:** provide a discrete, text-free or text-safe illustration asset; required headings and paragraphs must remain selectable HTML layers.
- Allow an appropriate PNG, JPEG, WebP or standalone vector illustration; choose by target fidelity and adapter support. Never use a single SVG or raster image for the entire slide; never place required editorial text inside SVG.
- Check original pixel dimensions against the artwork's displayed CSS pixel dimensions; report upscaling and print effective resolution. Converting an underspecified source to PNG or exporting at 300 DPI cannot restore omitted or rasterized detail.
- Record hash, source ID, claimed rights status, intended story relationship, profile dimensions, transformation pipeline, and tests actually performed. Unknown source/rights/approval means HOLD, not substitution.

## Machine-checkable handoff
For `tools/visual-poc/check_story_layers.py`, the final HTML must include a discrete `<img>` whose decoded bytes match the `story_art_sha256` in a story-layer manifest and differ from `logo_sha256`. Use a self-contained data URI for isolated/offline verification. This is an **intentionally bounded proof route**; external URLs, CSS backgrounds and other rendering modes require a separate verified adapter before passing this gate.

Never claim a matching hash proves narrative correctness. Actual visual inspection and human selection remain mandatory.
