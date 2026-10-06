# Logistics Framework — flagship reference implementation

The complete 15-slide layered CAD deck, rebuilt from the Logistics Framework specification through the DraftDeck skill (`skills/draftdeck/`). This is DraftDeck's flagship test case: it exercises the full reference-render protocol, the production contract, and the verified Canva adapter.

## Layout

| Path | Role |
|---|---|
| `source/` | **Authored source of truth** — `Build_Deck.py` (slide copy and geometry) and `Slide13_Seed.json` (validated seed scene) |
| `artwork/` | Text-free story artwork (PNG masters, quality-95 WebP for Canva import), generated drafting-frame SVGs, contact sheets, and `Artwork_Prompts.json` provenance |
| `output/` | **Generated** — `Scenes.json`, `Slide-01.html` … `Slide-15.html`, combined `Logistics_Framework_15_Slides_Layered.html`. Do not edit directly; rebuild overwrites it |
| `verification/` | `Canva_Verification.json` (707 richtext records, 24 image records, per-page dimensions) and `Production_Notes.md` |
| `previews/` | Rendered per-slide previews |

## Rebuild

Python standard library only; no API key, no PowerPoint, no image generation service:

```sh
python3 source/Build_Deck.py
```

The builder regenerates the scene definitions, drafting frames, all 15 individual HTML slides, and the combined deck. Edit `source/Build_Deck.py` (or `Slide13_Seed.json` for slide 13) to change the deck; replace files in `artwork/` to change the story layer. See `doctrine/production-contract.md`.

## Verified result

Canva import verified 2026-10-05: 15 pages at exactly 1920×1080, 707 separate richtext records, 24 separate image records; all pages editable and visually reviewed. Limits: text edit/save/reopen round trip untested; native SVG preservation unverified; story artwork is raster. Full detail in `verification/`.
