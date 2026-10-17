# Design System

## Implemented slide components

[`slide-kit/`](slide-kit/README.md) contains a candidate React/Tailwind component library, pinned Lucide icons, a standalone HTML catalogue build, and a page-level reference audit. It declares the Episode 01 interface profile explicitly. This implementation does not silently adopt the older roadmap palette or metaphors below.

## Earlier roadmap

Roadmap home of reusable DraftDeck design assets:

- `tokens/` — palette, stroke hierarchy, typography (see `doctrine/composition-standard.md`).
- `frames/` — drafting frames, margin rails, title blocks.
- `hatches/` — state textures (DEFAULT / ROUTED / HELD / BLOCKED / VERIFIED).
- `icons/` — semantic icon selections.
- `components/` — registered native components (Shipping & Receiving Control Desk, Verification Tag, D.A.T.A. Connector, Claim Comparator, Consignee Release Latch).

Custom components are registered here, not improvised per build. Component naming and geometry must remain logistics-native and must not reintroduce deprecated travel/aviation metaphors.
