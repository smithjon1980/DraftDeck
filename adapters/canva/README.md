# Canva adapter — VERIFIED

**Status:** Verified 2026-10-05 against the AI Pilot 15-slide build.

## Evidence

- 15 pages at exactly 1920×1080.
- 707 separate richtext records; 24 separate image records.
- All 15 pages reported editable and were visually reviewed from adapter-side previews.
- Full record: `examples/ai-pilot/verification/` and `skills/draftdeck/references/verified-pipeline.md`.

## Route

Import the self-contained local HTML file through Canva's import tool (`design_file=<absolute HTML path>`, intended type `presentation`). Do not use Canva AI design generation for this route — it may reinterpret composition. Never use PowerPoint as an intermediate.

## Known limits

- Text edit/save/reopen round trip not yet tested.
- Native SVG preservation in Canva not verified; background SVGs may rasterize.
- Story artwork is raster; its internal content is not independently editable.
