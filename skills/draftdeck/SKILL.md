---
name: draftdeck
description: Build reference-based 16:9 HTML/CSS slides and import them into verified target adapters with editable text and separate artwork layers. Use for layered infographic reconstruction, Canva-editable presentations without PowerPoint, and repeatable in-house slide production. Preserve the reference composition rather than replacing it with generic boxes or an SVG-only layout.
---

# DraftDeck — Layered HTML Slides

DraftDeck is the production engine; this skill is its operating instructions. Target tools are adapters with individual verification status (see `adapters/`).

Product doctrine lives in `doctrine/`: production contract, reference-render protocol, composition standard, Logistics Framework, and release QA. Read those before non-trivial builds.

## Contract

Deliver static HTML/CSS and a native design in the target adapter. Default to exact 1920 × 1080 pages. Keep titles, body copy, labels, annotations, stamp wording and metadata as live HTML text. Keep unique illustrations as separate SVG or PNG assets; internal illustration editing is optional. PNG is raster, SVG is vector. Never describe PNG as vector or a flattened image as an editable presentation.

Use the supplied reference as the visual authority. Read current project files for exact copy and constraints. Preserve focal illustration, title scale, placement, spatial hierarchy, drafting details and title block. A successful import is not proof of visual fidelity. Editability is necessary but not sufficient: a technically editable slide that destroys the reference composition is a failed DraftDeck build.

For the flagship example, obey `doctrine/logistics-framework.md`. The semantic model is shipping and receiving: data is cargo, humans are senders and receivers, agents are couriers, models are freight, and verification is proof of delivery. Do not reintroduce retired travel/aviation metaphors.

## Workflow

1. Inspect the actual reference. For PDF, render the selected page. Do not infer its composition from extracted text.
2. Write a layer plan: artwork, title, annotations, body copy, drafting lines, stamp, metadata. Record exact copy separately from illustration content.
3. Prepare a text-free artwork layer. Reuse supplied clean artwork when possible. For removing text from a raster reference or generating artwork, use the proper image-editing/generation path and inspect the result before use.
4. Author the composition in static HTML/CSS. Use one top-level `section data-document-role="page"` per slide; never nest pages. Set explicit pixel width/height. Place live text in separate positioned HTML elements, not inside a full-page screenshot or SVG text layer.
5. Use `scripts/build_slide.py` with a scene JSON for simple deterministic layouts. For rich layouts, author HTML directly while preserving the same layer contract.
6. Import through the target adapter's current import tool. For Canva, use the local HTML import route; do not use generative design as a substitute for importing authored composition.
7. Verify inside the adapter: dimensions, editability, independent text/image records, and rendered visual fidelity.
8. Separate inspection-only transactions from actual edits. Never discard real edits without preserving them.
9. Save source HTML, consumed artwork, verification evidence, and any remaining limitations.

## Release checks

- Exact 16:9 integer canvas, default 1920 × 1080.
- Reference composition visibly retained; no unsolicited generic card or box-grid redesign.
- Required copy exists as separate editable text in the adapter, not baked into artwork.
- Artwork exists as separately movable assets.
- No missing artwork, clipping, collisions or unreadable required text.
- No deprecated travel/aviation terminology or imagery in current flagship source/output.
- Distinguish import/layer inspection, visual review, and hands-on edit testing.
- No PowerPoint dependency.

Read [the verified pipeline record](references/verified-pipeline.md) for the demonstrated HTML → Canva route and known limits. The current flagship reference implementation lives in `examples/logistics-framework/`.
