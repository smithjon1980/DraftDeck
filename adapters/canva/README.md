# Canva adapter — VERIFIED ROUTE

**Status:** The HTML → Canva import route is verified. The current Logistics Framework flagship requires a fresh adapter review after the terminology and artwork migration.

## Prior route evidence

- 15 pages at exactly 1920×1080.
- 707 separate richtext records; 24 separate image records.
- All pages reported editable and were visually reviewed from adapter-side previews.
- Historical baseline record: `examples/logistics-framework/verification/Canva_Baseline_Verification.json`.
- Pipeline method: `skills/draftdeck/references/verified-pipeline.md`.

## Route

Import the self-contained local HTML file through Canva's import tool (`design_file=<absolute HTML path>`, intended type `presentation`). Do not use Canva AI design generation for this route — it may reinterpret composition. Never use PowerPoint as an intermediate.

## Current verification requirement

After the Logistics Framework rebuild:
1. inspect dimensions and editable layer records;
2. inspect rendered previews for clipping, text drift, and semantic regressions;
3. perform the edit/save/reopen round trip before upgrading the current flagship to full level-3 verification.

## Known limits

- Native SVG preservation in Canva is not yet verified.
- Raster story artwork is not internally editable.
