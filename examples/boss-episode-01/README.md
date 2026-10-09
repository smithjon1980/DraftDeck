# BOSS · Episode 01 · Candidate preview

Separate React/Tailwind implementation for requested Slides **01, 02, and 06**.
The Logistics Framework deck and original ZIP are unchanged.

```sh
cd examples/boss-episode-01
npm install
npm run dev
# Production browser-preview assets, not discrete Canva export:
npm run build
npx playwright install chromium
npm run check:browser
```

## Evidence and unresolved content

Slide 02 uses exact wording recovered in the user's handoff from a Canva
diagnostic; approval remains unknown. Slides 01/06 show `[UNKNOWN]`, rather
than borrowing content from the conflicting 01–03 ZIP. The original logo is
not present; its slot shows `[UNKNOWN]`. No logo is redrawn. There is no
invented production footer. Preview status labels stay outside slide pages.

The ZIP at `episode01/reference/BOSS_Episode01_React_Tailwind_Candidate_0.2.zip`
has verified Git blob hash `ab9b9e78d288a0fa0286d10a5079ec9b639ab728`.
It contains Vite/React/Tailwind source with candidate Slides 01–03:
THE SEQUENCE, PRECEDENCE, GROUPING. Its README explicitly says it is
code-only and unapproved. Its shadows, rounding, orange/gray styling,
and viewport-constrained canvas conflict with the current root AGENTS.md.

## Layer plan and candidate choices

Each slide is a native HTML page section, fixed at 1920×1080. The preview
wrapper scales the whole page through a CSS transform; internal geometry
does not depend on viewport units. Text uses native HTML elements.

Slide 02 layers: original logo slot; diagnostic metadata; title;
two comparison columns with hairline separators; operational-distinction
sidebar. No full-slide image, SVG, canvas, PDF, or decorative fill.

Proposed measurements: 112px metadata rail, 204px title band,
64px left margin, 67%/33% main/sidebar split, 40px comparison gutter.
Proposed fonts: Arial for copy, Consolas/Courier New for metadata.
Ink is #000000; ground is #FFFFFF; borders are 1px.
These measurements and fonts are implementation proposals, not recovered
approved specifications.

`SequenceDiagram` is reusable and data-driven, but not assigned to a slide.
No participants, messages, or gates are invented.

## Validation and approval

Browser checks verify dimensions, viewport scaling, page structure,
native typography, black/white colors, hairline borders, clipping,
copy, and selector behavior at desktop/tablet/mobile widths.
Screenshots and a JSON report are emitted to `verification/artifacts/`.
The CI workflow also builds the extracted original reference separately.

Passing geometry checks does not establish reference fidelity or creative
approval. Jonathan Smith must reconcile copy, provide the canonical logo
and governing visual reference, and approve the composition before
discrete static HTML generation and Canva import.
