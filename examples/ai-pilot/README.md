# Logistics Framework — flagship reference implementation

The complete 15-slide layered CAD deck for DraftDeck's shipping-and-receiving Logistics Framework. This is the flagship test case for the reference-render protocol, production contract, logistics doctrine, and adapter verification workflow.

## Canonical doctrine

> **Data is cargo. Humans are senders and receivers. Agents are couriers. Models are freight. Verification is proof of delivery.**

Control spine:

> **LOCATION → ACCOUNTING → ADJUDICATION → AUTHORITY**

See `doctrine/logistics-framework.md`.

## Layout

| Path | Role |
|---|---|
| `source/` | **Authored source of truth** — `Build_Deck.py` and `Slide13_Seed.json` |
| `artwork/` | Text-free story artwork, generated drafting-frame SVGs, and `Artwork_Prompts.json` provenance |
| `output/` | **Generated** — `Scenes.json`, `Slide-01.html` … `Slide-15.html`, combined `Logistics_Framework_15_Slides_Layered.html`. Do not edit directly |
| `verification/` | Baseline adapter evidence and current production notes |
| `previews/` | Fresh previews may be generated after current adapter re-verification |

## Rebuild

```sh
python3 source/Build_Deck.py
```

The builder regenerates scene definitions, drafting frames, all 15 individual HTML slides, and the combined deck. Edit source to change the deck; replace artwork to change independent story layers.

## Verification status

The HTML → Canva route has historical verification evidence. Because this flagship underwent a semantic and visual migration to the Logistics Framework, the current build requires fresh adapter inspection before being marked current at levels 1–3.
