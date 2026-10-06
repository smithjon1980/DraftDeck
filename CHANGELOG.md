# Changelog

All notable changes to DraftDeck are documented here.

## [Unreleased] — refactor/logistics-framework-v1

### Changed
- Replaced the deprecated travel/aviation framing with the canonical Logistics Framework.
- Renamed the flagship example to `examples/logistics-framework/`.
- Replaced aviation-derived control vocabulary with shipping, receiving, routing, cargo-class, route-plan, proof-of-delivery, and human release terminology.
- Removed deprecated reference artifacts and previews that could preserve the former theme.
- Updated the flagship source so generated output is logistics-native.

### Added
- `doctrine/logistics-framework.md` — canonical semantic model for cargo, senders/receivers, couriers, freight, proof of delivery, and the LOCATION → ACCOUNTING → ADJUDICATION → AUTHORITY spine.

## [0.1.0] — 2026-10-05

### Added
- Initial DraftDeck engine, skill, doctrine, adapter structure, 15-slide layered CAD reference implementation, and Canva route verification evidence.
