# Production Contract

DraftDeck builds follow one direction of authority:

```
SOURCE  →  COMPILER / RENDERER  →  GENERATED OUTPUT
```

## Source

The authored inputs. For the flagship example these live in `examples/logistics-framework/source/` and `examples/logistics-framework/artwork/`:

- `Build_Deck.py` — authored slide copy and geometry. This is the canonical source of truth for the deck.
- `Slide13_Seed.json` — validated seed scene for slide 13.
- `artwork/` — text-free story artwork, drafting backgrounds, and artwork-prompt provenance.

## Compiler / renderer

The deterministic builder (`skills/draftdeck/scripts/build_slide.py`, driven by the deck's build script). It embeds assets and emits live text. It has no authoring authority: it renders what the source says.

## Generated output

`examples/logistics-framework/output/`: `Scenes.json`, `Slide-01.html` … `Slide-15.html`, and the combined `Logistics_Framework_15_Slides_Layered.html`. Frame SVGs under `artwork/` are also regenerated on each build.

## The rule

**Rebuilding overwrites generated output.** Never edit generated files directly — a later rebuild will silently erase the edit. If a generated slide needs a change, transfer the change into source (builder, seed, or artwork) and rebuild.

If a temporary hand edit to generated output must survive, record it in verification notes and port it into source before the next build.

## Semantic authority

The current flagship source must conform to `doctrine/logistics-framework.md`. Deprecated travel/aviation vocabulary is not a compatibility alias and must not be emitted by the renderer.
