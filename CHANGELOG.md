# Changelog

All notable changes to DraftDeck are documented here.

## [Unreleased] — refactor/logistics-framework

### Changed
- Replaced the deprecated aviation/pilot metaphor with the canonical Logistics Framework.
- Canonical doctrine: **Data is cargo. Humans are senders and receivers. Agents are couriers. Models are freight. Verification is proof of delivery.**
- Renamed the flagship implementation from `examples/ai-pilot/` to `examples/logistics-framework/`.
- Replaced aviation-era authority and routing language with shipping, receiving, dispatch, cargo-class, route-manifest, and proof-of-delivery terminology.
- Removed stale aviation-era previews, contact sheets, binary reference material, and unused artwork.
- Renamed combined generated output to `Logistics_Framework_15_Slides_Layered.html`.

## [1.0.0] — 2026-10-05

### Changed
- Restructured the repository into product layers: `skills/`, `doctrine/`, `renderer/`, `design-system/`, `adapters/`, `examples/`, `archive/`.
- Renamed the skill identity from `canva-layered-html-slides` to `draftdeck`; Canva became a verified adapter rather than the product identity.
- Established the flagship layered CAD reference implementation with source/artwork/output/verification separation.
- Rewrote the README to distinguish verified adapters from unverified targets.

### Added
- `doctrine/` — production contract, reference-render protocol, composition standard, release QA.
- `CHANGELOG.md`, `LICENSE`.
