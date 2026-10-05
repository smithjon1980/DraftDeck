# Logistics Framework production notes

The current 15-sheet flagship is built from authored Python source, generated CAD-style SVG frames, and live HTML text.

## Semantic model

The deck is governed by `doctrine/logistics-framework.md`:
- data is cargo;
- humans are senders and receivers;
- agents are couriers;
- models are freight;
- verification is proof of delivery;
- final release authority remains human.

## Build architecture

Source lives in `source/`. Generated files belong in `output/`. Rebuilding may overwrite all generated output.

The current source is self-contained and no longer depends on predecessor raster story assets or deprecated reference bundles.

## Adapter status

The Canva route is historically demonstrated, but the current logistics-native build has not yet completed a fresh import/visual-review/edit-cycle verification.
