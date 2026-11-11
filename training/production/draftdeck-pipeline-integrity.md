# DraftDeck Pipeline Integrity Guard

**Status:** Candidate Controlled Production Standard  
**Scope:** DraftDeck browser-native production path, Canva handoff, visual-reference reconstruction, and release QA

## Why this exists

The first Canva retry failed because the production route silently changed.

The requested route was:

```text
REFERENCE PDF
→ HTML
→ CSS
→ SVG
→ BROWSER QA
→ CANVA IMPORT
```

The actual route became:

```text
CONTENT
→ GENERIC PRESENTATION GENERATOR
→ GENERIC CANVA LAYOUT
```

That was not a minor aesthetic miss. It was a route error.

DraftDeck must therefore carry a route-validation layer that prevents downstream tools from silently replacing the required browser-native production method.

> **A downstream tool may not silently replace an upstream production method.**

## Core invariant

If the requested production mode is browser-native / layered HTML, no presentation-generation tool, PPTX generator, generic Canva design generator, or raster-first converter may substitute for the required HTML/CSS/SVG compilation path.

If the available route cannot satisfy the declared path, the movement enters:

```text
HOLD — PIPELINE ROUTE MISMATCH
```

## Expected production route

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

Canva is post-production. It is not the visual generator for a DraftDeck compile.

## Route attestation preflight

Before production begins, the skill must explicitly declare:

```text
SOURCE_TYPE          = reference PDF
PRODUCTION_MODE      = layered_html
PRIMARY_AUTHORING    = HTML + CSS + SVG
CANVA_ROLE           = post-production import
PPTX_INTERMEDIARY    = forbidden
GENERIC_CANVA_GEN    = forbidden
RASTER_RECONSTRUCT   = forbidden
```

If those values cannot be truthfully declared, the skill stops.

## Artifact-shape check

Before Canva is touched, the build must prove the expected intermediate artifacts exist.

Required:

```text
index.html or single browser-native HTML deck      REQUIRED
shared stylesheet or embedded CSS                  REQUIRED
all slide/page sections                            REQUIRED
live text                                          REQUIRED
vector/SVG layer(s)                                REQUIRED
browser render                                     REQUIRED
contact sheet                                      REQUIRED
```

The simplest hard rule:

> **NO HTML → NO CANVA HANDOFF.**

If there is no HTML artifact, DraftDeck has not compiled.

## Reference-fidelity manifest

Every slide must carry a reconstruction manifest:

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

DraftDeck must specify not only what to create, but also what simplification is forbidden.

## Template-collapse detector

Named failure mode:

> **FAIL — TEMPLATE COLLAPSE**

Definition:

A reference-rich composition is reduced to generic boxes, cards, arrows, or presentation-template primitives during production.

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

This does not require perfect computer vision. It requires structured visual adjudication against the source specimen.

For the Day Zero reference, the source motifs included:

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

If most of those become rectangle-arrow-rectangle layouts, the deck fails.

## Canva admission gate

Canva handoff is authorized only after these checks pass:

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

## Named error taxonomy

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

## DraftDeck self-application

The production system must practice the doctrine it teaches:

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

## First failure specimen

The failed run is archived as a pipeline specimen with this diagnosis:

```text
FAIL — PIPELINE ROUTE MISMATCH
FAIL — TEMPLATE COLLAPSE
FAIL — CANVA HANDOFF PREMATURE
```

The deck should not be polished. It should be discarded as a candidate artifact and replaced with a browser-native compile.

## Corrective release rule

> **No Canva import until the browser-native deck visually passes.**

If the browser contact sheet does not look like a legitimate descendant of the reference specimen, the pipeline stops before Canva.