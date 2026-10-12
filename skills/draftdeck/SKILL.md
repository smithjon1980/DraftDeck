---
name: draftdeck
description: Build reference-based HTML/CSS slides and corresponding Markdown companions using bounded editorial components and import them into verified target adapters with editable text and separate artwork layers. Use for layered infographic reconstruction, Canva-editable presentations without PowerPoint, and repeatable in-house slide production. Preserve the reference composition rather than replacing it with generic boxes or an SVG-only layout.
---

# DraftDeck — Layered HTML Slides

DraftDeck is the production engine; this skill is its operating instructions. Target tools are adapters with individual verification status (see `adapters/`).

Product doctrine lives in `doctrine/`: production contract, reference-render protocol, composition standard, Logistics Framework, and release QA. Read those before non-trivial builds.

## Contract

Deliver requested HTML/CSS and Markdown artifacts; create a target-adapter design only within authorized handoff scope. Current Day Zero editorial companions use 17 × 11 landscape (1632 × 1056 CSS pixels). Preserve 1920 × 1080 for the existing 16:9 flagship or an explicitly requested 16:9 build. Keep titles, body copy, labels, annotations, stamp wording and metadata as live HTML text. Keep unique illustrations as separate SVG or PNG assets; internal illustration editing is optional. PNG is raster, SVG is vector. Never describe PNG as vector or a flattened image as an editable presentation.

Use the supplied reference as the visual authority. Read current project files for exact copy and constraints. Preserve focal illustration, title scale, placement, spatial hierarchy, drafting details and title block. A successful import is not proof of visual fidelity. Editability is necessary but not sufficient: a technically editable slide that destroys the reference composition is a failed DraftDeck build.

For the flagship example, obey `doctrine/logistics-framework.md`. The semantic model is shipping and receiving: data is cargo, humans are senders and receivers, agents are couriers, models are freight, and verification is proof of delivery. Do not reintroduce retired travel/aviation metaphors.

## Workflow

1. Inspect the actual reference. For PDF, render the selected page. Do not infer its composition from extracted text.
2. Write a layer plan: artwork, title, annotations, body copy, drafting lines, stamp, metadata. Record exact copy separately from illustration content.
3. Prepare a text-free artwork layer. Reuse supplied clean artwork when possible. For removing text from a raster reference or generating artwork, use the proper image-editing/generation path and inspect the result before use.
4. Author the composition in static HTML/CSS. Use one top-level `section data-document-role="page"` per slide; never nest pages. Set explicit pixel width/height. Place live text in separate positioned HTML elements, not inside a full-page screenshot or SVG text layer.
5. Use `scripts/build_slide.py` with a scene JSON for simple deterministic layouts. For rich layouts, author HTML directly while preserving the same layer contract.
6. When handoff is requested and authorized, import through the target adapter's current import tool. For Canva, use the local HTML import route; do not use generative design as a substitute for importing authored composition.
7. Verify inside the adapter: dimensions, editability, independent text/image records, and rendered visual fidelity.
8. Separate inspection-only transactions from actual edits. Never discard real edits without preserving them.
9. Save source HTML, consumed artwork, verification evidence, and any remaining limitations.

## Release checks

- Exact declared canvas; 17 × 11 for current Day Zero editorial companions and 16:9 for the existing flagship.
- Reference composition visibly retained; no unsolicited generic card or box-grid redesign.
- Required copy exists as separate editable text in the adapter, not baked into artwork.
- Artwork exists as separately movable assets.
- No missing artwork, clipping, collisions or unreadable required text.
- No deprecated travel/aviation terminology or imagery in current flagship source/output.
- Distinguish import/layer inspection, visual review, and hands-on edit testing.
- No PowerPoint dependency.

Read [the verified pipeline record](references/verified-pipeline.md) for the demonstrated HTML → Canva route and known limits. The current flagship reference implementation lives in `examples/logistics-framework/`.

## Bounded design system

Before composing BOSS assets, read [editorial component contracts](references/editorial-components.md). Use the approved component registry, tokens, and low/medium/high layout patterns. Treat USWDS token/component practices as an implementation foundation and WCAG 2.2 AA as the web accessibility target; neither establishes that an artifact has passed accessibility review. Preserve BOSS branding rather than reproducing government identity. Do not claim formal USWDS implementation unless its actual components are used and documented.

Use the shipping-logistics frame for current Day Zero. Do not restore airport towers, aviation vocabulary, legacy acronyms, or old schemas merely because a historical reference or the word pilot appears. A specifically requested historical reconstruction may reproduce its supplied content in isolation; label it as such.

Select only approved component variants and templates. If content does not fit, adjust within defined copy/layout bounds or report the fit issue; do not silently shrink required text, delete evidence limitations, invent new visual patterns, or rasterize the text layer. Keep the ten editorial features separate from the ten canonical shared-frame fields.


## Cross-format verification

- Render actual HTML in a browser when available. Inspect representative opener, medium-copy, process, and dense-reference pages plus all pages for clipping. Test mobile reflow for website work; fixed slide canvases are not responsive lesson pages.
- Identify export provenance. A PDF composed independently with a drawing library is a review rendition, not proof that browser HTML or browser print matches it. Never describe Python-drawn shapes as HTML/CSS execution. Do not use PowerPoint intermediates.
- Validate diagram syntax with Mermaid/PlantUML when those sources are used; inspect the rendered output separately. Preserve source and version. Do not call a native SVG schematic a Mermaid/PlantUML render. Label reading-order connectors separately from operational decision branches.
- Match deck and Markdown coverage: ten shared-frame fields, status distinctions, missing-source recovery, missing room as UNKNOWN, mechanism roles, verification versus release, and six evidence-package items. Keep actual source runtime distinct from requested future audio duration.
- Verify Markdown image paths and captions; distinguish supplied evidence, reported cases, proposed logic, illustrative candidates, and unsupplied placeholders. Never fabricate receipts or screenshots.
- Record content, visual, browser, print, accessibility, and destination-layer checks separately as PASS, FAIL, or NOT TESTED with scope. Code generation and generation dispatch alone establish no rendered acceptance.
- Keep release separate from verification. Confirm existing authorization for artifact, action, tool, and destination; obtain additional authorization only where scope expands. Human review before Canva remains required when specified by the user.
