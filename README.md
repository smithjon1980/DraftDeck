# DraftDeck

DraftDeck is a production engine that transforms visual references into layered, editable 16:9 presentations built from static HTML and CSS. It combines CAD-inspired precision, replaceable story artwork, and live editable text — with no PowerPoint intermediate.

**Core rule:** Editability is necessary but not sufficient. A technically editable slide that destroys the reference composition is a failed DraftDeck build.

## Architecture

| Path | Role |
|---|---|
| `skills/draftdeck/` | Operating instructions for the engine (agent-facing skill) |
| `doctrine/` | Production contract, reference-render protocol, composition standard, Logistics Framework, Prime Process, Prime Process orchestration doctrine, release QA |
| `renderer/` | Scene schema and HTML/CSS build pipeline (roadmap; builder currently lives in the skill) |
| `design-system/` | Tokens, frames, hatches, icons, components (roadmap) |
| `adapters/` | Import targets, each with its own verification status |
| `examples/logistics-framework/` | Flagship reference implementation: 15-slide logistics and proof-of-delivery deck |
| `archive/` | Current archive notes for retained non-deprecated evidence |

## Flagship doctrine

The flagship implementation uses a logistics model governed by `doctrine/logistics-framework.md` and the operational spine in `doctrine/prime-process.md`:

> **Data is cargo. Humans are senders and receivers. Agents are couriers. Models are freight. Verification is proof of delivery.**

Its control spine is:

The executable orchestration extension is defined in `doctrine/prime-process-orchestration.md`. Context severance, cross-session handoff, and return-routing are defined in `doctrine/prime-handoff-context-routing.md`.



> **LOCATION → ACCOUNTING → ADJUDICATION → AUTHORITY**

The repository must not reintroduce deprecated travel/aviation metaphors into source, generated output, design-system components, or user-facing documentation.

## Adapter verification status

| Adapter | Status | Evidence |
|---|---|---|
| Canva | **Verified route; current flagship re-verification pending** | The HTML → Canva route has verified editable text/image records. The logistics-migrated flagship must receive a fresh adapter review before its own verification record is upgraded. |
| Adobe Express | Unverified | Do not claim compatibility until independently tested. |
| Figma | Unverified | No import test completed. |
| Floot | Exploratory | No import test completed. |

## Quick start

Rebuild the flagship deck offline (Python standard library only):

```sh
python3 examples/logistics-framework/source/Build_Deck.py
```

See `doctrine/production-contract.md` before editing anything: generated output is overwritten on rebuild, so authored changes belong in the source, never in generated HTML.
