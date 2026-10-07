# DraftDeck Pipeline Integrity & Failure Detection

**Status:** Candidate Production Control  
**Applies to:** DraftDeck HTML/CSS/SVG → Canva production workflow  
**Purpose:** Prevent generic presentation generation, PPTX substitution, raster-first conversion, and template-collapse failures during DraftDeck production.

## 1. The failure this document preserves

A NotebookLM slide-deck PDF was used as a visual specimen for a BOSS Day Zero presentation. The intended production route was DraftDeck:

```text
REFERENCE PDF
→ HTML
→ CSS
→ SVG
→ BROWSER QA
→ CANVA IMPORT
```

The actual route taken was:

```text
CONTENT
→ GENERIC CANVA PRESENTATION GENERATOR
→ TEMPLATE COLLAPSE
```

That was not DraftDeck.

The failure was not merely aesthetic. It was a routing failure: a downstream presentation generator silently replaced the upstream HTML/CSS/SVG production method.

## 2. Core invariant

> **A downstream tool may not silently replace an upstream production method.**

For DraftDeck, Canva is post-production. Canva is not the visual generator and is not permitted to infer the production architecture.

The browser-native artifact must exist and pass visual QA before Canva receives anything.

## 3. Required production route

```text
NOTEBOOKLM PDF / VISUAL SPECIMEN
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

No generic presentation generator, PPTX generator, or raster-first converter may substitute for the required HTML/CSS/SVG compile path.

## 4. Route attestation gate

Before production begins, the skill must explicitly declare:

```text
SOURCE_TYPE          = reference PDF / image specimen / controlled source
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

## 5. Artifact-shape gate

Before Canva is touched, the build must prove that the expected intermediate artifacts exist:

```text
index.html                REQUIRED
shared stylesheet         REQUIRED
page sections             REQUIRED
live text                 REQUIRED
vector/SVG layer(s)       REQUIRED
browser render            REQUIRED
contact sheet             REQUIRED
```

Canonical rule:

> **NO HTML → NO CANVA HANDOFF.**

If there is no browser-native HTML artifact, DraftDeck has not compiled.

## 6. Template-collapse detector

Named failure mode:

> **FAIL — TEMPLATE COLLAPSE**

Definition:

A reference-rich composition has collapsed into repetitive presentation primitives such as generic cards, boxes, arrows, panels, or templated slide layouts.

Useful heuristic:

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

The audit is not purely numerical. A structured visual review must compare the source's visual motifs with the candidate deck.

For the Day Zero Blueprint specimen, expected motifs included:

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

If those motifs become “rectangle + arrow + rectangle,” the deck fails.

## 7. Slide manifest requirement

Every slide must carry a production manifest before Canva handoff:

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

## 8. Canva admission gate

Canva handoff is authorized only after:

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

## 9. Named error codes

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

## 10. Self-application of BOSS

DraftDeck must practice the doctrine it teaches:

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

This is the production equivalent of the candidate-state architecture:

- request is not package;
- capability is not permission;
- generation is not establishment;
- Canva render is not release;
- visual fidelity must be adjudicated before handoff.

## 11. Correction rule

When a pipeline failure is detected, do not polish the failed downstream artifact.

Return to the last valid upstream state:

```text
FAILED CANVA / PPTX / TEMPLATE OUTPUT
↓
HOLD
↓
RETURN TO HTML/CSS/SVG COMPILE
↓
RENDER CONTACT SHEET
↓
VISUAL QA
↓
ONLY THEN CANVA HANDOFF
```

## 12. Release condition

A DraftDeck production run cannot be called successful until the browser-native deck visually passes before Canva import.

> **No Canva import until the browser-native deck visually passes.**
