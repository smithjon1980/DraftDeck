# DraftDeck GrapesJS Open Editor trial
Status: CANDIDATE / BUILD UNDER CI TEST / VISUAL AND PDF QA NOT YET PASSED

## Why
A browser-native visual **HTML/CSS** editor with genuine text editing. GrapesJS core runs within React; the canvas model is HTML/CSS, **not** JSX round-trip. No Canva, compulsory SVG, or PowerPoint.

## How to use
Run `npm install` and `npm run dev` in an isolated Node 22 environment. Select a text component, edit using the sidebar, save project JSON, reload it to check persistence, export HTML/CSS, then generate PDF with `npm run pdf -- /path/to/overview01.html`. The Vite build may also run via a branch-scoped GitHub Actions workflow with downloadable compiled artifacts.

## Acceptance
- React application must compile in GitHub Actions, and run interactively in Chromium.
- A selected text component's change must persist through project JSON save/reload.
- Exported HTML must contain revised text, and Chromium PDF must contain selectable accurate text, with correct white background.
- Visual fidelity to the approved BOSS story reference is **NOT ESTABLISHED**. The sample uses illustrative process blocks pending composition redesign; no automatic production claim.
- No source promotion, credential provision, or public hosting without human approval.
