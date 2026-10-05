# Production Contract

DraftDeck builds follow one direction of authority:

```
SOURCE  →  COMPILER / RENDERER  →  GENERATED OUTPUT
```

## Source

The authored inputs. For the flagship example these live in `examples/ai-pilot/source/` and `examples/ai-pilot/artwork/`:

- `Build_Deck.py` — authored slide copy and geometry. This is the canonical source of truth for the deck.
- `Slide13_Seed.json` — validated seed scene for slide 13.
- `artwork/` — text-free story artwork (PNG/WebP), drafting backgrounds (SVG), and artwork prompt provenance.

## Compiler / renderer

The deterministic builder (`skills/draftdeck/scripts/build_slide.py`, driven by the deck's build script). It embeds assets and emits live text. It has no authoring authority: it renders what the source says.

## Generated output

`examples/ai-pilot/output/`: `Scenes.json`, `Slide-01.html` … `Slide-15.html`, and the combined `AI_Pilot_15_Slides_Layered.html`. Frame SVGs under `artwork/` are also regenerated on each build.

## The rule

**Rebuilding overwrites generated output.** Never edit generated files directly — a later rebuild will silently erase the edit. If a generated slide needs a change, transfer the change into the source (builder, seed, or artwork) and rebuild. Treat any direct edit to generated output as lost work waiting to happen.

If a hand edit to generated output must survive temporarily, record it in the verification notes and port it into the source before the next build.
