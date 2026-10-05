# Logistics Framework — flagship reference implementation

The complete 15-slide layered CAD deck for DraftDeck's shipping-and-receiving Logistics Framework. This flagship exercises the reference-render protocol, production contract, logistics doctrine, and adapter-verification workflow.

## Canonical doctrine

> **Data is cargo. Humans are senders and receivers. Agents are couriers. Models are freight. Verification is proof of delivery.**

Control spine:

> **LOCATION → ACCOUNTING → ADJUDICATION → AUTHORITY**

See `doctrine/logistics-framework.md`.

## Layout

| Path | Role |
|---|---|
| `source/` | **Authored source of truth** — `Build_Deck.py` and `Slide13_Seed.json` |
| `artwork/` | Generated drafting-frame SVGs and optional future artwork provenance |
| `output/` | Generated HTML/scene output; not canonical source |
| `verification/` | Current production notes and adapter-verification status |

## Rebuild

```sh
python3 source/Build_Deck.py
```

The builder is self-contained and code-authors the current logistics diagrams. It regenerates frame SVGs, scene definitions, all 15 individual HTML slides, and the combined `Logistics_Framework_15_Slides_Layered.html`.

## Verification status

The HTML → Canva route has prior method evidence, but this logistics-native flagship requires a fresh import, rendered review, and edit/save/reopen cycle before it is marked current at levels 1–3.
