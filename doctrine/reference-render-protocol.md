# Reference-Render Protocol

The supplied reference is the visual authority. DraftDeck's job is to render it as layered, editable HTML/CSS — not to redesign it.

## Protocol

1. **Inspect the actual reference.** For PDF, render the page and look at it. Never infer composition from extracted text.
2. **Write a layer plan** before building: artwork, title, annotations, body copy, drafting lines, stamp, metadata. Record exact copy separately from illustration content.
3. **Prepare a text-free artwork layer.** Reuse supplied clean artwork when possible; otherwise remove text with proper image editing or generate replacement artwork while preserving composition and required geometry. Inspect the result before use.
4. **Compose in static HTML/CSS.** One `section[data-document-role="page"]` per slide, exact pixel dimensions (default 1920×1080), live text in separate positioned elements, artwork as separate movable assets, images embedded as data URIs for self-contained import.
5. **Preserve the composition:** focal illustration, title scale and placement, spatial hierarchy, drafting details, title block. No unsolicited generic card or box-grid redesign.

## Honesty rules

- Flag unreadable values; never invent engineering measurements from generated geometry.
- Reference approval stamps are reproduced wording, not new authorization — say so on the slide.
- PNG is raster, SVG is vector. Never describe raster artwork as vector, or a flattened image as an editable presentation.
- A successful import is not proof of visual fidelity. Verify visually, per `doctrine/release-qa.md`.
