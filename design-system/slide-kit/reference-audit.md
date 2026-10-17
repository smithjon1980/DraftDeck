# Reference audit and library selection

Inspected 2026-10-17. Source: `Enterprise_AI_Operations_Manual (1).pdf`, 20 pages, 1376×768 pt. Library identity: `libfile_8b3e10272bd88191bb9f1683c628983d`. SHA-256: `a67899f72764c52d18cdaf2d8f4129721b2c3ed48448ca7b6c8f63f20c1dea76`.

All 20 pages were rendered and inspected as a contact sheet. Pages 5, 6, 9 and 19 were also inspected individually. A Gemini Notebook footer is visible. This is one available reference deck, not a claim that every NotebookLM deck has been reviewed. The original PDF is not duplicated in the repository.

| Source page | Observed structure | Reusable component | Limits |
| --- | --- | --- | --- |
| 5 | Two labeled structures separated by a mechanical mismatch illustration | ComparisonPanel plus separate story artwork | Component captures comparison geometry; does not recreate the illustration or reuse its lesson wording |
| 6 | Six horizontal layers, aligned labels, directional overlays | LayerStack | Starter captures ordered layers only; directional connector overlays remain future work |
| 9 | Two axes and four labeled quadrants | DecisionMatrix | Preserve relationships when supplying new content; do not silently reuse source routing claims |
| 19 | Labeled rows and column headings with repeated audit marks | AuditTable | Use semantic row/column headers; explicit textual status rather than color-only checks |
| Throughout | Kicker, title, drafting rules, short closing rail, annotated technical artwork | TopMetadataRail, SlideCanvas, ArtworkWithCaption | ReflectionFooter adds the project reflection/notes convention; it is not claimed as an exact source reproduction |

## Choice

Use React + Tailwind for the repository-owned slide patterns, with `lucide-react` as the downloaded standardized icon component library. Lucide's independently imported React icons fit the line-art vocabulary and allow explicit size/stroke control. Sources: https://lucide.dev/guide/react/ and https://lucide.dev/license (reviewed 2026-10-17). Exact package versions and integrity hashes live in the lockfile.

A generic app-widget theme would add controls without supplying the observed slide structures. A chart library is deferred until an actual quantitative chart and editable-label requirement justify it. Source page 18 contains a plotted relationship, but this audit does not establish source numerical data and no chart values are invented.

## Transformation boundaries

This work extracts structural patterns only. It does not compose or approve a new teaching slide. The deck's aviation language, orange accent, serif titles and mechanical story art are not imported as new project authority. The root Episode 01 instructions supply the explicit cyan/magenta/black interface profile. The older repository core remains separately defined.

For a later lesson composition, inspect its actual source page, record the teaching point and exact-copy manifest, complete both story and visual bridges, then render the required A–D candidates. Component selection does not replace those steps. Original artwork, actual logos and approved lesson copy remain separate inputs; unknowns stay explicit.

## Acceptance

Build and browser findings are recorded below after verification. Human visual selection: PENDING. Canva import and destination editability: NOT TESTED. Full WCAG conformance: NOT ESTABLISHED. The catalogue is library infrastructure, not a replacement for the existing Episode 01 slide master.

Verified on 2026-10-17:

- `npm run build`: PASS; React server rendering and compiled Tailwind output.
- Standalone HTML inspection: PASS; native heading and table, no external script/stylesheet references, no canvas or SVG editorial text; demonstration image embedded separately.
- Chromium 153 render at 1920×1080: inspected; no content beyond the canvas. Catalogue bottom y=917.09, footer starts y=951; no overlap. All images loaded. Earlier overflow was repaired before this final check.
- 390px viewport: entire logical slide scales to 390px; document scroll width 390px. This is preview scaling, not readable mobile lesson reflow.
- Browser print: one page, 1440×810 pt (20×11.25in), visually inspected after rendering. This verifies print geometry only.
- `git diff --check`: PASS.
