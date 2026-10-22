# Web engineering — bounded rules for BOSS slides and interfaces

**Status:** candidate skill guidance. Source inspiration: user-provided 2026 HTML/CSS course transcript. Do not promote its blanket editor/tool preferences or marketing assertions to doctrine.

## Structure before styling
Use semantic HTML for instructional websites: header, navigation, main, sections, articles, meaningful heading levels, paragraphs, figures/captions and tabular data. Labels must be associated with form controls; use native required/type constraints where appropriate, plus independent server-side validation for persisted data. Check keyboard navigation, focus states, contrast, alt text, captions and reading order. Automated audits are partial evidence only.

## Single token authority
Read `design-system/boss-design-contract.json` and `design-system/tokens/tokens.css` instead of locally improvising values. Reuse `--boss-*` tokens for color, typography, spacing, hairlines and slide sizing. Do not generate alternative blue-gray/orange schemes, substitute the original logo, or mistake a hex match for verified logo artwork. Typography selection beyond candidate defaults requires render review. CSS cascade and specificity should be predictable: reusable classes/tokens, bounded selectors and minimal `!important` exceptions.

## Distinct geometries
- Slide: 1920×1080 **fixed logical coordinates**, CSS scale the containing canvas; no `vh` as primary slide height. Preserve art/text layering. Pixel units are legitimate for deterministic slide geometry.
- Website and bilingual instructional surfaces: accessible responsive reflow using Grid/Flexbox; use `rem`, `em`, percentages, relative viewport units and container queries where supported/appropriate. Test narrow/wide viewports and English/Spanish expansion.
- Print: separately approved page dimensions, text selection and physical proof. Browser-to-PDF parity must be tested against same source and page setup.

## Media and performance
Preserve artwork as separate original asset with provenance. Choose raster/vector form based on content, target adapter and tests rather than an SVG-only or PNG-only rule. Use `srcset`/`sizes` for responsive web image delivery when suitable, meaningful `alt`/captions, lazy loading for noncritical media, and declared image dimensions to minimize layout shift. Do not lazy-load first-view critical images by default. Fonts must load deterministically before screenshots/PDF export.

## Verification
Check DOM semantic structure, token parity, overflow/clipping, image load failures, exact text, actual screenshots, matching PDF dimensions, and separate adapter import/edit-save-reopen. Keep accessibility and visual-story results as independent gates. For unsupported browser CSS features, use a tested fallback, not an unverified assumption.
