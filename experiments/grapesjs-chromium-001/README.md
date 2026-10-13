# DraftDeck open-source visual editor trial 001
Status: CANDIDATE / NOT_BUILT / NOT_VISUALLY_ACCEPTED / PRODUCTION HOLD

## Why
Use **GrapesJS core** (open-source visual HTML/CSS editor) inside a React 19 editor shell. Replace the Canva intermediate step; retain editable HTML/CSS and Chromium PDF release file. No compulsory SVG. The included BOSS page is a disposable example, **not** a faithful reconstruction of the approved blueprint story layer.

## Run when network/package access is available
```bash
npm install
npm run dev
```
Edit text/styles on the canvas. Download **editable project JSON** and **HTML/CSS** from top bar. Then:
```bash
npm run pdf -- /absolute/path/to/overview01.html
```
Install Chromium for Playwright separately if absent (`npx playwright install chromium`). Never run unreviewed package install hooks in production. Project JSON is the editable GrapesJS model; the HTML is Chromium input.

## Important limit
The `@grapesjs/react` official wrapper integrates editor UI with React; it does *not* mean GrapesJS canvas objects are authored JSX/React components. Our initial editor uses grapesjs core mounted by React; do not claim native JSX round-trip. Proprietary GrapesJS Studio SDK and its React renderer are **not** required here.

## Acceptance gates
- Human can visually edit headline and proof-of-delivery captions.
- Save/reload project JSON without dropping text or styles.
- Export HTML/CSS and Chromium PDF with white page and exact text.
- Inspect PDF text objects and visual reference fidelity; reject generic boxed scenes.
- Richer story artwork is a separate human-approved design task; photo/illustration may be raster as a separate layer, **never rasterize live text**.
- Test any dependencies and lockfile in an isolated runtime, record versions and license compliance.
- Do NOT claim visual success before running an actual editor instance.
