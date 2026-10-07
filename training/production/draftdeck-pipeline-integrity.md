# DraftDeck Pipeline Integrity & Failure Gates

**Status:** Candidate Production Control

**Scope:** DraftDeck browser-native slide production, Canva handoff, and QA.

## Why this exists

A recent production attempt failed because the intended DraftDeck pipeline did not run. The content was sent into a generic Canva presentation generator instead of being compiled as browser-native HTML/CSS/SVG and then handed to Canva for post-production.

The failure was not merely aesthetic. It was a route error.

```text
EXPECTED
REFERENCE PDF
→ HTML
→ CSS
→ SVG
→ BROWSER QA
→ CANVA IMPORT
```

```text
ACTUAL
CONTENT
→ GENERIC PRESENTATION GENERATOR
→ TEMPLATE COLLAPSE
```

The result reduced a reference-rich visual specimen into repeated presentation primitives: boxes, arrows, and generic grids. That output is not DraftDeck.

## Correct DraftDeck route

```text
NOTEBOOKLM PDF
      │
      │ visual reference / creative seed
      ▼
DRAFTDECK RECONSTRUCTION
      │
      ├── HTML semantic structure
      ├── CSS composition
      ├── live editable text
      ├── inline SVG / vector geometry
      ├── explicit z-order
      ├── CAD drafting layer
      └── optional separate story imagery
      │
      ▼
BROWSER RENDER / VISUAL QA
      │
      ▼
CANVA LAYERED IMPORT
      │
      ▼
CANVA POST-PRODUCTION
      │
      ▼
RELEASE QA
```

No generic Canva generation step belongs in the middle.

No PowerPoint intermediary belongs in this path.

Canva is post-production. It should receive a production artifact that is already designed.

## Route Guard

Before production, the skill must explicitly declare the intended route.

```text
SOURCE_TYPE          = reference PDF
PRODUCTION_MODE      = layered_html
PRIMARY_AUTHORING    = HTML + CSS + SVG
CANVA_ROLE           = post-production import
PPTX_INTERMEDIARY    = forbidden
GENERIC_CANVA_GEN    = forbidden
RASTER_RECONSTRUCT   = forbidden
```

If the available tool call does not satisfy these values, execution stops with:

```text
HOLD — PIPELINE ROUTE MISMATCH
```

## Artifact-shape gate

Before Canva is touched, the expected intermediate artifacts must exist.

```text
index.html                REQUIRED
shared stylesheet         REQUIRED
page sections             REQUIRED
live text                 REQUIRED
vector/SVG layer(s)       REQUIRED
browser render            REQUIRED
contact sheet             REQUIRED
```

Hard rule:

> **NO HTML → NO CANVA HANDOFF.**

## HTML page ABI

Each slide/page must be a browser-native scene with a top-level page element.

```html
<section
  class="slide"
  data-document-role="page"
  data-label="05 — Request Is Not Package"
>
```

The slide deck must be visually inspectable in the browser before any Canva import.

## Template-collapse detector

Named failure mode:

> **FAIL — TEMPLATE COLLAPSE**

This triggers when reference-rich geometry is replaced by repetitive presentation primitives.

Heuristic:

```text
IF
  repeated_rectangular_containers > threshold
AND
  source_unique_visual_motifs_retained < threshold
AND
  slide_layout_similarity > threshold
THEN
  FAIL — TEMPLATE COLLAPSE
```

The system must perform a structured visual audit against the source specimen.

For the Day Zero Blueprint specimen, source motifs included:

```text
maze / routing map
qualification staircase
nested system enclosure
machine schematic
organic unbounded payload
cargo matrix
HOLD gate
PRIME industrial chain
module corridor
exploded envelope
diagnostic matrix
routing fork
```

If most of those become `rectangle → arrow → rectangle`, the deck fails.

## Reference-fidelity manifest

Every slide must carry a production manifest.

```text
SLIDE_ID
SOURCE_PAGE
SOURCE_VISUAL_MOTIF
NEW_DOCTRINAL_CONTENT
RETAINED_GEOMETRIC_IDEA
INTENTIONAL_CHANGES
PROHIBITED_SIMPLIFICATIONS
```

Example:

```text
SLIDE 05
SOURCE_PAGE: 5
MOTIF:
  irregular unbounded mass
  → constraining mechanism
  → bounded package

DO NOT SUBSTITUTE:
  left text box → arrow → right rectangle
```

DraftDeck must specify not only what to create, but what simplification is forbidden.

## Canva admission gate

Before importing into Canva, these gates must pass:

```text
HTML_COMPILED                 PASS
PAGE_COUNT                    PASS
LIVE_TEXT                     PASS
SVG_PRESENT                   PASS
REFERENCE_FIDELITY            PASS
TEMPLATE_COLLAPSE             PASS
METAPHOR_LITERALIZATION       PASS
DOCTRINE                      PASS
BROWSER_RENDER_QA             PASS
```

Only then:

```text
CANVA_HANDOFF = AUTHORIZED
```

## Named errors

```text
PIPELINE_ROUTE_MISMATCH
HTML_ARTIFACT_MISSING
CSS_ARTIFACT_MISSING
VECTOR_LAYER_MISSING
BROWSER_RENDER_NOT_VERIFIED
REFERENCE_FIDELITY_FAILURE
TEMPLATE_COLLAPSE
RASTERIZATION_REGRESSION
CANVA_HANDOFF_PREMATURE
METAPHOR_LITERALIZATION
DOCTRINE_DRIFT
```

## Corrective law

> **A downstream tool may not silently replace an upstream production method.**

## BOSS interpretation

DraftDeck must obey the same architecture it teaches.

```text
DRAFTDECK REQUEST
↓
PACKAGE
↓
ROUTE GUARD
↓
HTML/CSS/SVG COMPILER
↓
BROWSER CANDIDATE
↓
VISUAL ADJUDICATION
↓
CANVA ADMISSION
↓
POST-PRODUCTION
↓
RELEASE QA
```

This is the production equivalent of:

> **Admission governs input. Adjudication governs output. Capability governs neither by itself.**

## Release rule

No DraftDeck artifact may be called complete until the browser-native artifact has passed visual QA and the Canva handoff has been explicitly authorized.
