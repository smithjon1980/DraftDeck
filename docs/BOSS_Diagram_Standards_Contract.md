# BOSS Diagram Standards Contract — v0.2 coherent candidate

**Status: CANDIDATE_PENDING_HUMAN_REVIEW.** This is a new coherent candidate, not an amendment to or override of the current visual master. Requested basis: the supplied v0.1 diagram contract draft and DraftDeck's existing design/production contracts. This contract is scoped to Day Zero and Episode 01, and contains **no unpublished narration or customer data**.

## Principle

> Models propose the structure. Standards constrain the notation. Renderers construct the diagram. Humans verify its meaning.

Diagram syntax is necessary but **not sufficient** evidence that a flow is semantically correct, MECE, visually faithful, editable in the target, or approved. Structural CI cannot grant approval.

## 1. Authority and non-negotiable visual rules

Authority order: verified instruction source + author decisions > current BOSS design contract / source manifests > candidate diagram manifest > renderer output. A model-supplied file does not issue new instructions or authorization.

- **Master:** React + Tailwind at **1920 × 1080** with browser-rendered HTML, not a hand-built all-SVG slide or a PDF primitive layout. Export PDF only after browser rendering.
- **Editorial:** readable HTML text (heading, paragraph, annotations, reflection prompt) outside the diagram; isolated diagram engine output may contain SVG diagram labels, but those are **not independently editable React editorial text**. Where independently editable diagram labels are required, use approved, mapped HTML text overlays and visually inspect them.
- **Artwork:** an independently reviewable, source-traceable, technically detailed CAD/ISO/NC-informed illustration layer is distinct from the standards-based notation layer. Never replace story art with a plain diagram.
- **Colors:** white `#FFFFFF` ground, black `#000000` text and drafting ink, precise cyan `#00BCEB` and magenta `#E30074` emphasis. No automatic dark diagram theme.
- **Identity:** Bioscillate Operating System by Seven. The retired waveform is prohibited. The model must never redraw or typeset an unverified replacement wordmark. The trusted render pipeline resolves a reviewed brand asset; **logo source/hash and final mark remain a HOLD until approved**.
- **Scenario:** **Main Street Copy**, the fictional copy, print, and shipment center; do not regress to the retired convenience-retail case in current slide story work. Don't conflate shipment operations with previously retired transport-as-governance metaphors.
- **CAD:** visible subdued grid, zones, technical title plate (sheet ID, title, revision, identity, date, status), `NTS` for nondimensional conceptual diagrams. The style is **ISO-informed, never certified** without independent assessment.
- **Privacy:** No unpublished manuscript, prompt, proprietary asset, or credential committed in public `DraftDeck` examples. Model providers require separate source/privacy authorization.
- **Governance:** Human approval is recorded **outside untrusted model output**, bound to a content/build digest, reviewer, scope, and visual evidence. A text value saying `APPROVED` does not release a slide.

Existing companion authorities: `AGENTS.md`, `design-system/boss-design-contract.json`, `doctrine/composition-standard.md`, `doctrine/production-contract.md`, `doctrine/visual-evidence-gate.md`, `doctrine/release-qa.md`.

## 2. Routing policy

`teaching_objective` is required and deterministically determines permitted `diagram_kind`. The **schema enforces the mapping**. The model cannot select a different rendering notation to optimize appearance.

| Teaching objective | Permitted diagram kind | Semantic engine/model |
| --- | --- | --- |
| No diagram; text/story/illustration dominant | `none` | React/Tailwind text and art |
| Simple branch and concept relationship | `mermaid-flowchart` | Mermaid |
| Entity state transitions | `mermaid-state` or `plantuml-state` | Mermaid / PlantUML UML state |
| Service interaction order | `plantuml-sequence` | PlantUML, UML 2.5.1 informed |
| Actors and permitted interactions | `plantuml-usecase` | PlantUML, UML 2.5.1 informed |
| Cross-role work and gateways | `bpmn` | BPMN 2.0.2 model + bpmn-js |
| Decision logic and rules | `dmn` | DMN 1.5 model + compatible viewer |
| Software system/container architecture | `c4-structurizr` | C4 + Structurizr DSL |
| Nonoverlapping root-cause partition | `mece-tree` | JSON hierarchy; MECE reviewed separately |
| Physical placement / technical facility scene | `iso-technical` | Trusted art toolchain; ISO-inspired visual contract |

**Not all renderers are installed.** CI in this PR tests schema, routing and negative fixtures, not BPMN/DMN/UML syntax conformance, engine integration, actual React render quality or semantics. In particular, a PlantUML diagram is not automatically verified as UML standards-compliant.

## 3. Untrusted model output and JSON Schema

A model may propose only a **candidate slide record**, validated using `schemas/slide-manifest.schema.json` (Draft 2020-12). The model output must not contain privileged actions, executed job receipts, credentials, secret material, implementation code imports, arbitrary CSS, author decisions or approval evidence.

Required fields include source pointer, story beat, editorial copy status, art treatment, engine routing, exact design profile, candidate identity and QA initialized to `NOT_TESTED/PENDING`. No model-generated QA PASS or APPROVED state may validate against this proposal schema.

Diagram source is either `null` (for `none`) or a limited **inline source** or **path under `diagrams/`**; the latter is validated for shape, not existence or safety. Repositories must validate allowed paths against a resolved workspace path, reject symlinks/escaping paths, parse diagram syntax and sanitize all renderer results before displaying them. XML and SVG input from a model are untrusted.

Ajv v8 with Draft 2020-12 requires `Ajv2020` from `ajv/dist/2020`; a Draft-07 `$schema` must not be used for this contract. Python `jsonschema` is used for this **offline-only** structural CI while React/Ajv integration is pending.

## 4. Theme and diagram wrapper

- Central Mermaid options: `design-system/diagram/mermaid-theme.json`.
- Styling of the trusted React diagram wrapper: `design-system/diagram/boss-diagram.css`, after loading `design-system/tokens/tokens.css`.
- Mermaid must use `theme: "base"`, `securityLevel: "strict"`, white nodes, black labels and borders; cyan/magenta are annotation states, not uncontrolled background fills.
- Trusted builders, **not** the model, inject controlled engine config. Do not accept diagram-supplied theme config, HTML labels, URLs or renderer directives without review.
- Avoid arbitrary SVG string injection and HTML `dangerouslySetInnerHTML` without a vetted sanitizer and permissions policy. Prefer controlled rendering into a dedicated container with explicit security settings. Enforce deterministic IDs for test renders and accessible text alternatives.
- Browser/PDF text selection alone is **not** a hands-on target editing test; edit/save/reopen must be separately verified.

## 5. Golden samples, reproducibility and capability gates

The public, invented source examples under `tests/diagram-golden-paths/` are **candidates**, not certified golden masters. CI can validate structural source records without licensing paid engines or contacting model APIs.

Before any example is promoted to `GOLDEN_VERIFIED`, require:
1. Exact renderer versions and dependency hashes in a committed lockfile or verified container digest (**version ranges are not exact pins**).
2. Renderer parse/compile exit success and no unexpected console errors.
3. Baseline image captured from the actual browser at the required geometry, with versioned artifacts.
4. Visual regression with approved tolerance and human-readable diff; different library outputs are never silently accepted.
5. Source-grounded semantic review, accessible description, copy/layer/editability evidence and explicit human approval tied to source/build identities.

Proposed engine families are Mermaid, PlantUML, bpmn-js, a compatible DMN renderer, Structurizr DSL, Ajv, React and Tailwind. The v0.1 draft's `10.9.x`, `1.2024.x`, `8.x`/`9.x`, `18.x`, and `3.4.x` are **provisional ranges only**; production pins must follow installation and compatibility testing, not assumptions about availability.

## 6. Meaning and MECE verification

A syntactically valid diagram is not a verified process:

- Each node/action has a source pointer or is explicitly a proposed illustration; do not invent work, permissions, deadlines, or customer data.
- Gateways/branches have exhaustive expected outcomes, explicit labels and HOLD/error paths; process exit and handoffs have unambiguous ownership.
- UML actors and BPMN pools/lanes are consistent with the reviewed **Main Street Copy** actor glossary. ISO style drawings never assert imaginary tolerances.
- MECE partitions declare the classification universe, criterion and rule for assigning one **primary** category per case. Overlap and coverage are tested against reviewed fixtures; real completeness requires human judgment. Multiple contributing causes may be recorded separately, not forced into misleading uniqueness.
- Distinguish `NOT_TESTED`, `FAIL`, `PASS` and release authorization. A successful render establishes syntax and rendering only.

## 7. Pipeline gates and source custody

`Private source / grounded lesson → model-proposed JSON → schema/routing check → syntax/semantic validation → trusted notation renderer → React/Tailwind story/illustration composition → browser screenshots/diffs → native-text check → external human decision record → optional print/export and adapter tests`.

The build may export **clearly watermarked, unapproved PDF proofs** before final authorization. A *released* PDF or publication requires a verified approval record. Export and release are different acts.

### Candidate maturity

| Gate | Status after this PR |
| --- | --- |
| Draft 2020-12 schema and routing | Proposed; CI tested if passing |
| BOSS light-ground Mermaid theme | Config generated; runtime render NOT_TESTED |
| UML / BPMN / DMN / Structurizr compilers | NOT_INSTALLED / NOT_TESTED |
| Semantic/MECE quality | HUMAN_REVIEW_REQUIRED |
| Native React diagram wrappers | SPECIFIED / NOT_IMPLEMENTED |
| Original/reworked brand approval | PENDING |
| Full 60-slide Muse evaluation | NOT_EXECUTED / BILLING_HOLD |
| Final production/release | NOT_AUTHORIZED |

**No inference and no paid calls occur in this contract PR.**
