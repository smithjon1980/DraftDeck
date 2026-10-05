# DraftDeck

DraftDeck is a production engine that transforms visual references into layered, editable 16:9 presentations built from static HTML and CSS. It combines CAD-inspired precision, replaceable story artwork, and live editable text — with no PowerPoint intermediate.

**Core rule:** Editability is necessary but not sufficient. A technically editable slide that destroys the reference composition is a failed DraftDeck build.

## Architecture

| Path | Role |
|---|---|
| `skills/draftdeck/` | Operating instructions for the engine (agent-facing skill) |
| `doctrine/` | Production contract, reference-render protocol, composition standard, release QA |
| `renderer/` | Scene schema and HTML/CSS build pipeline (roadmap; builder currently lives in the skill) |
| `design-system/` | Tokens, frames, hatches, icons, components (roadmap) |
| `adapters/` | Import targets, each with its own verification status |
| `examples/ai-pilot/` | Flagship reference implementation: 15-slide layered CAD deck |
| `archive/` | Original archive notes, manifest, and the source reference PDF |

## Adapter verification status

| Adapter | Status | Evidence |
|---|---|---|
| Canva | **Verified** (2026-10-05) | 15 pages at exactly 1920×1080, 707 richtext records, 24 image records; all pages visually reviewed. See `examples/ai-pilot/verification/`. |
| Adobe Express | Unverified | Do not claim compatibility until independently tested. |
| Figma | Unverified | No import test completed. |
| Floot | Exploratory | No import test completed. |

## Quick start

Rebuild the flagship deck offline (Python standard library only):

```sh
python3 examples/ai-pilot/source/Build_Deck.py
```

See `doctrine/production-contract.md` before editing anything: generated output is overwritten on rebuild, so authored changes belong in the source, never in the generated HTML.
