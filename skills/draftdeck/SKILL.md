---
name: draftdeck
description: Build reference-based 16:9 HTML/CSS slides and import them into verified target adapters (Canva verified; Adobe Express, Figma, Floot unverified) with editable text and separate artwork layers. Use for NotebookLM/Gemini visual references, layered infographic reconstruction, Canva-editable presentations without PowerPoint, and repeatable in-house slide production. Preserve the reference composition rather than replacing it with generic boxes or an SVG-only layout.
---

# DraftDeck — Layered HTML Slides

DraftDeck is the production engine; this skill is its operating instructions. Target tools are adapters with individual verification status (see `adapters/`). Canva is the verified adapter. Adobe Express is not a verified destination.

Product doctrine lives in `doctrine/`: production contract, reference-render protocol, composition standard, and release QA. Read those before non-trivial builds.

## Contract

Deliver static HTML/CSS and a native design in the target adapter. Default to exact 1920 × 1080 pages. Keep titles, body copy, labels, annotations, stamp wording and metadata as live HTML text. Keep unique illustrations as separate SVG or PNG assets; internal illustration editing is optional. PNG is raster, SVG is vector. Never describe PNG as vector or a flattened image as an editable presentation.

Use the supplied reference as the visual authority. Read current project files for exact copy and constraints. Do not ask the user to retype a prompt already available in their files. Preserve focal illustration, title scale, placement, spatial hierarchy, drafting details and title block. A successful import is not proof of visual fidelity. Editability is necessary but not sufficient: a technically editable slide that destroys the reference composition is a failed DraftDeck build.

## Workflow

1. Inspect the actual reference. For PDF, load the PDF skill and render the selected page. Do not infer its composition from extracted text. Start with one page unless more are explicitly requested.
2. Write a layer plan: artwork, title, annotations, body copy, drafting lines, stamp, metadata. Record exact copy separately from illustration content. Flag unreadable values rather than inventing engineering measurements. Treat reference approval stamps as reproduced wording, not new authorization.
3. Prepare a text-free artwork layer. Reuse supplied clean artwork when possible. For removing text from a raster reference or generating artwork, load the imagegen skill and use the image tool, preserving composition and required geometry. Inspect output before use. Do not use Python pixel editing as a substitute for the required image-editing tool. Do not claim generated geometry is exact engineering reconstruction.
4. Author the composition in static HTML/CSS. Use one top-level `section data-document-role="page"` per slide; never nest pages. Set explicit pixel width/height. Place live text in separate positioned HTML elements, not inside a full-page screenshot or SVG text layer. Embed image bytes as data URIs for self-contained import. Use CSS for typography, hierarchy, borders and rotations. Start with one image layer if matching a reference; use multiple asset groups when independent movement is needed. React may author the preview, but export static HTML for import.
5. Use `scripts/build_slide.py` with a scene JSON for simple deterministic layouts. The script embeds assets and emits live text. For rich layouts, author HTML directly while preserving the same layer contract. See `assets/example_scene.json` for structure. The example is a syntax fixture, not the user's visual reference.
6. Import through the target adapter's current import tool. For Canva: discover the available schema, then call the local-file route `design_file=<absolute HTML path>`, `intended_design_type="presentation"`, a descriptive `name`, and `user_intent`. Do not use Canva AI design generation for this route: it may reinterpret composition. Do not use PowerPoint as an intermediate or send a local/private file as a public URL. If the local HTML route is unavailable, state that concrete limitation instead of silently flattening or switching formats.
7. Verify inside the adapter. For Canva, open an inspection transaction using the returned design ID. Check exact page dimensions, `is_editable`, separate richtext records, preserved wording, positions, and separate fill/image records. Count layers, but do not treat count alone as fidelity. Retrieve a transaction thumbnail and always show it to the user. Visually inspect the render for font substitutions, missing images, clipping, overlaps, rotations and text drift.
8. Close inspection-only transactions by cancelling; the imported design already exists and cancellation only discards transaction changes. For corrections, prefer revising the HTML and importing a clearly named candidate. For transaction edits, follow Canva's current preview/explicit-approval-before-commit requirement. Never cancel an actual edited transaction without preserving or explaining the changes.
9. Save HTML, final consumed artwork, preview and a verification record using the Library skill. Reuse existing identities when replacing files. Return the actual edit link and HTML source. Report verified dimensions/layers and remaining limitations, including raster artwork and hands-on editing not yet tested. Do not claim Adobe Express compatibility until independently tested.

## Release checks

- Exact 16:9 integer canvas, default 1920 × 1080.
- Reference composition visibly retained; no unsolicited generic card or box-grid redesign.
- Required copy exists as separate editable text in the adapter, not baked into artwork.
- Artwork exists as a separately movable asset; do not promise native vector preservation merely from SVG input.
- No missing artwork, clipping, collisions or unreadable required text.
- Distinguish import/layer inspection, visual review, and the user's hands-on edit test.
- No PowerPoint dependency or per-slide reconstruction service is required by this workflow. Do not promise zero cost; connected services may have quotas or charges.

Read [the verified pipeline record](references/verified-pipeline.md) for the successful AI Pilot run and known limits. Use its evidence as a baseline, not as permission to reuse stale paths, transactions or signed preview URLs. The flagship reference implementation lives in `examples/ai-pilot/`.
