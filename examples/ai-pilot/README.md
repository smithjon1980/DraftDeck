# Logistics Framework — flagship reference implementation

The 15-slide layered CAD deck is DraftDeck's flagship reference implementation for the canonical logistics model:

> **Data is cargo. Humans are senders and receivers. Agents are couriers. Models are freight. Verification is proof of delivery.**

The deck exercises the reference-render protocol, production contract, and verified Canva adapter without aviation metaphors.

## Layout

| Path | Role |
|---|---|
| `source/` | **Authored source of truth** — `Build_Deck.py` and `Slide13_Seed.json` |
| `artwork/` | Logistics-compatible story artwork, generated drafting-frame SVGs, and artwork prompt provenance |
| `output/` | **Generated** — `Scenes.json`, `Slide-01.html` … `Slide-15.html`, combined `Logistics_Framework_15_Slides_Layered.html` |
| `verification/` | Historical Canva import evidence and production notes |

Stale aviation-era previews, contact sheets, and reference binaries are not part of the canonical implementation.

## Rebuild

```sh
python3 source/Build_Deck.py
```

The builder regenerates scene definitions, drafting frames, all 15 slide HTML files, and the combined deck. Edit source, not generated output.

## Verification status

The original Canva import established the adapter mechanism: 15 pages at exactly 1920×1080 with independent editable text and separate image records. That historical evidence is retained as adapter evidence, while current Logistics Framework builds must pass a fresh release QA cycle before being called visually canonical.
