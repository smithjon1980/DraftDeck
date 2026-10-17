# Candidate verification — 2026-10-17

- Source pack: 100 original files with family, exact upstream commit and SHA-256; full source/license notices retained. Normal builds verify every hash.
- Import: 368 usable text-free geometry records. Eight text-bearing sources explicitly deferred to editable-label adapters; originals retained.
- Bounds: all 368 records produced nonempty geometry bounds in Chromium 153. A horizontal line's zero geometric height is padded rather than misclassified as an empty component. Crops recorded in `vendor/viewboxes.json`.
- Build: `npm install --ignore-scripts` and `npm run build` passed. Actual React rendering and compiled Tailwind CSS.
- Browser: 368 atlas images loaded. The unused dialog image has no source until selection. No page JavaScript errors observed.
- Interaction: ANSI/IEEE filter returns seven assets; a gate opens the enlarged inspector; heat-exchanger search returns 13 assets; an unmatched search returns zero. SVG export links include the selected geometry and embedded attribution/license metadata.
- Viewport: 390px viewport has document scroll width 390px.
- Visual review: process equipment, ANSI/IEEE gates and GD&T views inspected. Source technical geometry remains separate from native HTML labels.

Not established: independent per-symbol ISO/ANSI/ASME conformance; mechanical or piping correctness of a future composed diagram; detailed connector/assembly illustration equivalence; rendering and acceptance of composition adapters in a final figure; full accessibility conformance; Canva destination editability; human selection of a new slide master. Individual SVG accessibility labels and inspector controls were implemented; this is not a full accessibility audit.
