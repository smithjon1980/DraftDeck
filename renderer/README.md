# Renderer

Roadmap home of the DraftDeck rendering pipeline:

- `scene-schema/` — the scene JSON contract (layers: image, text, border; exact 16:9 canvas).
- `html/` / `css/` — page-section emission.
- `build/` — deterministic build entry points.

The working builder currently lives at `skills/draftdeck/scripts/build_slide.py` and is exercised by `examples/logistics-framework/source/Build_Deck.py`. Promote it here when the schema stabilizes. See `doctrine/production-contract.md`.
