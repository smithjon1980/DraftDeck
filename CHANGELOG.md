# Changelog

All notable changes to DraftDeck are documented here.

## [Unreleased] — architecture/draftdeck-v1

### Changed
- Restructured the repository into product layers: `skills/`, `doctrine/`, `renderer/`, `design-system/`, `adapters/`, `examples/`, `archive/`.
- Renamed the skill identity from `canva-layered-html-slides` to `draftdeck`; Canva is now one adapter among several, not the product identity.
- Promoted the Logistics Framework experiment to `examples/logistics-framework/` as the flagship reference implementation, with `source/`, `artwork/`, `output/`, `verification/`, and `previews/` separated.
- Rewrote the README to distinguish verified adapters (Canva) from unverified targets (Adobe Express, Figma, Floot); removed the overclaim of a reusable Adobe Express pipeline.

### Added
- `doctrine/` — production contract (source → compiler → generated output), reference-render protocol, composition standard, release QA.
- `CHANGELOG.md`, `LICENSE` (MIT).

## [0.1.0] — 2026-10-05

### Added
- Initial archive import: `canva-layered-html-slides` skill, complete 15-slide layered CAD experiment, original Logistics Framework reference PDF, and Canva verification evidence (15 pages, 1920×1080, 707 richtext records, 24 image records).
