# BOSS / Main Street Copy — standards-governed native React diagrams

**CANDIDATE / NOT APPROVED.** Synthetic Episode 01 instructional examples only. Diagram content has not been verified against any real Main Street Copy transaction or finalized narration. This is an **implementation candidate** for the Diagram Standards Contract introduced by merged PR #76.

## What this test solves

A Mermaid/PlantUML-generated SVG embedded as a picture can preserve semantics, but it visually conflicts with the BOSS React/Tailwind slide master. **In this rebuild, React constructs the diagram from a typed, source-derived model.** The diagram engines remain independently executed as syntax oracles, but their SVG output is **not** embedded in the slide.

```text
Reviewed synthetic Mermaid (.mmd) / PlantUML (.puml) sources
    ├── Actual Mermaid CLI / PlantUML CLI compile → SVG evidence of syntax support
    └── Strict, fail-closed semantic adapters → typed JSON IR and source SHA-256
           ↓
    BossFlowDiagram / BossSequenceDiagram React components
           ↓
    BOSS Tailwind + CSS: native HTML cards, technical frame, decision diamonds,
    HOLD, lifelines, alternate sections, selectable labels
           ↓
    Dedicated SVG connector strokes only (no SVG editorial text, no SVG slide)
           ↓
    Chromium 1920×1080 screenshot and DOM graph-parity QA
```

### What is genuinely derived from each notation source?

- Mermaid: **3 phase groups, 8 nodes, 9 directed edges**, true decision nodes, a HOLD step, yes/no paths, and explicit correction cycles.
- PlantUML: **4 actors, 8 ordered messages**, sender/recipient, reply semantics, an `alt`, an `else`, and its closing boundary.
- Each visible node/edge/participant/message has a `data-` attribute. Browser QA compares the exact declared source graph to the rendered DOM; it rejects any missing, invented, or reversed relationship. JSON IR contains SHA-256 fingerprints of the original text sources.
- The restricted adapters **reject unsupported syntax**. They are **not** general Mermaid/PlantUML parsers, do not certify full UML/BPMN compliance, and cannot infer missing business intent. Scaling grammar coverage requires more fixtures and negative tests rather than silent approximations.

### Native styling rules

The React components live in `src/diagram-components.jsx`; all reading text, node labels, branch labels, actor names, sequence labels, commentary, and reflection prompts are native HTML. Connector paths use small SVG elements solely for geometry.

`src/styles.css` defines the shared BOSS design language: white background, black heavy editorial typography, hairline technical rules, cyan `#00BCEB` for accepted flow, magenta `#E30074` for HOLD/conditional emphasis. The approved Bioscillate wordmark still awaits a verified asset selection; the current proof displays an explicit brand HOLD marker **rather than recreating or altering the logo**. The retired waveform is absent.

The output is **React/Tailwind source** first; a browser screenshot or PDF is only the review derivative. Full semantic source editing requires revising the `.mmd` or `.puml` and rebuilding, not manually modifying generated IR.

## Reproduce on GitHub Actions

Workflow: `.github/workflows/boss-diagram-browser-proof.yml`. It installs exact direct npm dependencies, runs offline negative tests for the adapters, independently compiles both standard diagram sources using the real engines, compiles IR, builds React + Tailwind, and captures Chromium screenshots.

Direct package pins exist, but full transitive npm dependency lockfile has not yet been committed. The workflow uploads its generated lockfile and compiler evidence. PlantUML is checked with a provider-hosted SHA-256 sidecar. A fully pinned/verified toolchain is a separate follow-up gate.

Review artifact `boss-mermaid-plantuml-react-browser-proof` contains full-size PNGs/PDFs, raw engine SVG proof files (not used for the React drawing), typed IR JSON, and a DOM-equivalence report. **Passing CI certifies a restricted structural check, not human-approved styling or business meaning.**

## Non-negotiable boundaries

- No unpublished manuscript is committed or sent to Baseten.
- No paid model inference occurs in the Actions workflow.
- Actors/steps are synthetic and source-grounded only to the example fixture, not actual operational evidence.
- Human reviews the full browser screenshots for spacing, clipping, typographic weight, ISO title block, visual hierarchy, and storytelling.
- No `APPROVED` or `RELEASED` state is derived from a CI success.
- The trial remains a candidate until the user approves both visual samples, current source copy, and the final logo treatment.
