# DraftDeck slide kit — candidate 0.1

Reusable React components, compiled Tailwind CSS, and actual Lucide React icons. This is a small slide-specific library, not a generic application widget theme. Source lives in this repository; pinned packages are downloaded by `npm ci` and recorded in `package-lock.json`. Do not commit `node_modules`.

```sh
cd design-system/slide-kit
npm ci
npm run build
```

Open `dist/index.html`. It contains compiled CSS and native HTML text, needs no CDN, and scales the fixed 1920×1080 canvas to the viewport. The tiny scaling script is only for preview; it does not generate slide content. Print uses the logical canvas. The component catalogue is a specimen sheet, not a composed lesson slide or approved visual master.

## Reuse

Import components from `src/components.tsx` and styles from `src/tokens.css`. Supply lesson data separately. `src/catalogue.tsx` demonstrates composition. Use `TopMetadataRail` with an actual original logo asset when supplied; no replacement logo is fabricated. `ArtworkWithCaption` takes a separate image, alternative text, caption, and provenance. Every icon has a visible text label; icons alone do not carry a status.

| Component | Required content | Variant / behavior | Checks |
| --- | --- | --- | --- |
| SlideCanvas | title, children, footer | Fixed 1920×1080; scale entire canvas | No clipping; native title; declared language |
| TopMetadataRail | section, identifier | Horizontal rail; optional original logo | Actual logo provenance; labels remain readable |
| ComparisonPanel | left/right title and body | Equal columns | Distinguish source and candidate; preserve exact copy |
| LayerStack | unique id, label, description per layer | Ordered rows | Order must reflect source; no invented dependencies |
| DecisionMatrix | axis descriptions; four titled cells | Row-major 2×2; labels explain axis direction | Relationships supported; text remains selectable |
| AuditTable | caption, columns, row labels and matching values | Semantic native table | Header association; column parity; unknowns explicit |
| ArtworkWithCaption | src, alt, caption, provenance | Separate image and live caption | Artwork rights/provenance; meaningful alternative text |
| ReflectionFooter | question | Question plus notes line; configurable notes label | One focused question; no fabricated learner response |

All components use the named `episode01-interface` profile in `src/tokens.css`: pure white, black, 1px rules, Arial/Helvetica reading copy, Courier New metadata, and measured spacing. Exact cyan/magenta identity tokens are reserved. This profile follows root AGENTS.md; it does not replace the older core orange/serif profile. Components use fixed slide geometry for preview and print. They are not a mobile lesson website: a separate reflow layout is needed for that use.

Reference render: generated `dist/index.html` component catalogue. No full-slide SVG, SVG editorial text, rasterized headings, or canvas text. Lucide uses isolated SVG pictograms and one isolated demonstration image. Keep actual story illustrations separate when composing lessons.

## Dependencies and notices

- React and React DOM: rendering foundation (MIT).
- Tailwind CSS and CLI: compiled utilities and named tokens (MIT).
- Lucide React: downloaded component library for line icons (ISC, with Feather-derived icons under MIT). Imports: `Columns2`, `Layers`, `Grid2X2`, `Table2`, `Image`, `MessageSquare`. Full installed Lucide license is copied to `dist/LUCIDE-LICENSE` and embedded in the standalone HTML.
- tsx: local TypeScript/JSX build runner (MIT).

See [reference-audit.md](reference-audit.md) for source scope and pattern decisions. A successful build or text check does not establish Canva editability, source fidelity for a future lesson, full accessibility conformance, or human approval. Those require their own checks on the composed output.
