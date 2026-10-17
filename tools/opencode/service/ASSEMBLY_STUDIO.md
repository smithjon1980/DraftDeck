# Connector production reconstruction and assembly editor

Extends the existing private Slide Studio with `/tools/slides/assembly/`. No additional service, public sharing or model/provider calls are introduced. The existing Google/Basic gateway protects the page, template, project API and assets. The selected connector concept has already been approved; this change reconstructs it into editable layers rather than asking for concept approval again.

## Skill execution / bridges

Creative brief: BOSS practitioners learning how interface constraints make execution bounded. Single takeaway: “Constraints make an interface executable.” Source spark: `Enterprise_AI_Operations_Manual (1).pdf`, p12. The approved second spark is the connector concept selected in the 2026-10-17 conversation. Preserve exploded mating halves, keyed alignment, cutaway conductors, detailed collars and four integrated callouts. Replace historical D.A.T.A. labels with the approved Define / Anchor / Bound / Record copy. Do not claim mechanical accuracy, deployed software enforcement, standards compliance or additional doctrine.

Visual translation: white 1920 × 1080 canvas, black technical linework and hairlines, original cyan/magenta/black bioscillate logo. The mechanical illustration is a generated separate raster artwork, not vector CAD. Text and leaders are reconstructed as native HTML/CSS. The rejected AND-gate and generic four-template arrangement is not reused.

The engineering atlas remains the source for registered technical symbols; it lacks this detailed connector assembly. Record that gap rather than inventing an atlas asset ID. `connector-v1` is a separate production-artwork ID, not an atlas standard/reference.

## Component contract

`AssemblySlide` (`studio/assembly.jsx`) owns one `section[data-document-role=page]` at fixed logical dimensions. Input: title, reflection, evidence/scope note, separate logo/artwork, and an `assembly` model. Each callout records its stable ID, live title/text, label X/Y, leader side, elbow X/Y and artwork target X/Y. Eight CSS line segments and four terminals remain separate from the raster art. Callout labels support pointer movement and arrow keys; Shift uses a larger step. The editor also offers numeric coordinates and live-text fields. Export removes editor interactions.

`slide-studio.mjs` accepts optional `assembly` alongside the existing slide fields. It permits only the registered `connector-v1` artwork, bounded finite coordinates, unique callout IDs and 1–12 callouts; source IDs and optimistic revisions remain enforced. Existing projects remain valid. The template loads from `/api/templates/connector`; loading it does not create a project or import an approval record. Save explicitly. Current seed contains one slide; the assembly editor rejects multi-slide/non-assembly projects rather than discarding them. The general Studio can restore/export the compatible JSON and render the assembly, and links to its specialized editor for callout editing.

Current editor controls: label positions, titles and text; leader targets/elbows; slide title; reflection and scope; server save/open; reset from concept; static HTML/JSON/Markdown export. Artwork grouping is separate but the internal raster drawing is not editable geometry. This release does not offer arbitrary artwork uploads, automatic source verification, model calls, print generation in the web service, Canva import or Adobe Express import.

## Build and reproduction

`npm ci`, then `npm run build:studio`. The existing Docker `COPY studio` and build stage include the new component, seed, CSS and PNG; no Docker changes are needed.

For static reconstruction, compile `studio/render-connector.jsx` using esbuild with React packages external, then run it from this service root with the output directory as its sole argument. It uses the same production `AssemblySlide` as the editor. Generated HTML contains native text plus two embedded images (artwork and original logo), with no runtime scripts or external requests.

PDF delivery in this task uses WeasyPrint to render the actual HTML/CSS. The Adobe skill's constrained ReportLab exporter is deliberately not used: it cannot reproduce the separate logo/artwork and this component's general CSS. WeasyPrint is not a browser; its PDF/render checks do not establish browser dragging or destination editability.

## Verification scope

PASS: React/Tailwind build; syntax checks; five focused tests (`node --test tests/slide-studio.mjs tests/assembly.mjs`) without starting OpenCode or contacting providers. Checks include template schema, save/restart with independently moved label and retained target, stale-save rejection, invalid artwork/coordinates/duplicate IDs rejection, native escaped text, 4 labels, 8 line segments, 4 terminals and 2 images. Existing project persistence/review tests also pass.

PASS for the delivered local print artifact: one 1440 × 810 point page (20 × 11.25 inches, 16:9), selectable expected copy, separate two-image resources and embedded fonts; Poppler render visually inspected. Cropped logo signature and one wrapped callout were repaired before the final render. Detailed illustration, key plates, relative callout relationships and reflection footer remain visible. Minor geometry changes inherent to generated raster reconstruction are not precision validation.

NOT TESTED: live browser pointer/keyboard interaction, responsive editor visual QA, production-authenticated server saves, browser print, Adobe Express or Canva import/edit/save/reopen. Concept approval is preserved; production visual/destination acceptance remains separate. The broad OpenCode integration test run remains outside this focused validation because of the previously reported provider-network approval block.
