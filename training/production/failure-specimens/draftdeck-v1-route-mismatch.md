# DraftDeck Failure Specimen — Route Mismatch and Template Collapse

**Status:** WIP Failure Specimen  
**Failure class:** Production route failure  
**Source event:** Agent-mediated / candidate-state presentation first Canva attempt

## Diagnosis

The failed deck did not fail because of a single bad slide.

It failed because the production route silently changed from browser-native DraftDeck reconstruction to generic Canva presentation generation.

Expected:

```text
REFERENCE PDF
→ HTML
→ CSS
→ SVG
→ BROWSER QA
→ CANVA IMPORT
```

Actual:

```text
CONTENT
→ GENERIC CANVA PRESENTATION GENERATOR
→ TEMPLATE LAYOUT
```

## Named failures

```text
FAIL — PIPELINE_ROUTE_MISMATCH
FAIL — TEMPLATE_COLLAPSE
FAIL — CANVA_HANDOFF_PREMATURE
```

## What made the failure visible

The source specimen contained a rich visual vocabulary:

```text
orientation-map maze
qualification staircase
nested system enclosure
machine schematic
unbounded payload transformation
classification matrix
HOLD gate
PRIME chain
module corridor
exploded envelope stack
diagnostic matrix
routing fork
```

The failed Canva generation reduced that vocabulary to repeated rectangles, connectors, and generic presentation layouts.

## Corrective rule

The failed deck should not be polished.

The correct movement is to discard it as a failed candidate and restart from the HTML/CSS/SVG compile stage.

> **No Canva import until the browser-native deck visually passes.**

## Production lesson

Canva is post-production.

Canva is not authorized to replace the DraftDeck compiler.

A downstream tool may not silently substitute its own production method for the route declared by the package.