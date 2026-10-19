# BOSS / DraftDeck — Semantic Diagram & Technical Figure Standards Pack v0.1

**Status: CANDIDATE / HUMAN REVIEW REQUIRED / NOT DEPLOYED.** This specification supplements, but does **not** amend or supersede, `AGENTS.md`, `design-system/boss-design-contract.json`, `doctrine/visual-evidence-gate.md`, and `doctrine/production-contract.md`. It is intended to constrain future diagram requests sent to Muse Spark or other models; no live model calls, paid inference, or secret access were performed. Current Episode 01 source text remains private and candidate; project-dependent facts require source evidence.

## Audit evidence (2026-10-18, main)

- `design-system/boss-design-contract.json`: 1920 × 1080 fixed slide, brand palette, native HTML text, CAD grid/title plate gate; no per-diagram syntax/semantic validation.
- `design-system/components.md`: `SequenceDiagram` is a component *specification*, not implementation proof or a grammar; no plantUML/Mermaid routing.
- `design-system/tokens/tokens.css`: still specifies Arial/Helvetica and Courier New fallbacks; approved display font and exact brand logo/hash remain outstanding.
- `renderer/README.md` and `skills/draftdeck/scripts/build_slide.py`: old JSON/HTML builder is recorded; this does **not** verify production React/Tailwind diagram rendering.
- `doctrine/visual-evidence-gate.md`: requires a real browser capture, CAD zone markers/title plate, per-layer verification and human sign-off. Diagram syntax checks cannot replace this.
- `experiments/muse-spark-eval-v01/`: the Muse evaluation is scoped to synthetic classification/routing/evidence, **not** 60-slide diagram generation. Baseten API catalog authentication was verified earlier; model diagram generation has not been tested or approved.

## 1. Four-layer standards architecture

1. **Semantics**: identify what a diagram *claims*: UML 2.5.1 for roles, interactions, state and software structure; BPMN 2.0.2 for multi-actor business procedures; DMN 1.5 for rule decisions; C4 model for software architecture; partition logic for MECE trees. Informative teaching IPOS and SEVEN examples are defined in BOSS doctrine, not ISO/OMG certifications.
2. **Interchange / diagram-as-code**: use one grammar per diagram. Mermaid flowchart/state/ER for small lessons, PlantUML for UML and C4-PlantUML where admitted, BPMN 2.0 XML for real BPMN, DMN XML or independently validated decision table for DMN, Graphviz DOT for dense issue trees. Mermaid-looking boxes are NOT BPMN or UML merely by decoration.
3. **Visual composition**: React + Tailwind owns every slide; editorial words and labels essential to instruction remain native DOM text. Vector/raster technical figure assets can be placed within dedicated figure regions; do not render the *entire* slide using SVG/PDF drawing primitives. Preserve white `#FFFFFF`, black `#000000`, cyan `#00BCEB`, magenta `#E30074`. The previously retired waveform must not reappear. Current user's favored bold Bioscillate + cyan/magenta diagonal treatment is a **design direction awaiting exact approved/hard-pinned master**. Do not reconstruct the mark from a made-up font, declare a guessed hash, or fetch old waveform art as a default.
4. **Evidence / QA**: validate proposed diagram spec with JSON Schema Draft 2020-12; compile exact diagram source with a pinned runtime; compare required IDs/edges/guard conditions to source manifest; independently inspect Chromium 1920×1080 screenshots, source equality, clip/overflow, accessible descriptions, story/art layer and native text, and retain human release decision. Formal standards compliance requires separate conformance assessment.

## 2. Routing table: use the *smallest sufficient* notation

| Intent | Semantics | Allowed default renderer | Acceptance emphasis |
|---|---|---|---|
| Simple operational procedure or IPOS path | explicit directed graph / guarded transitions | Mermaid flowchart LR/TD | unique node IDs, all arrows/decision labels, STOP/HOLD path |
| Actor/system interaction over time | UML sequence 2.5.1 | PlantUML sequence | truthful lifelines, order, `alt`/`opt` guards, messages |
| User roles and capabilities | UML use case 2.5.1 | PlantUML use case | system boundary, actor associations, correctly applied `include`/`extend` |
| Lifecycle / HOLD-RELEASE | UML state machine 2.5.1 | PlantUML state or Mermaid stateDiagram-v2 (choose ONE per figure) | state invariants; valid triggers; no false automatic release |
| Swimlane business process and handoffs | BPMN 2.0.2 | BPMN 2.0 XML via bpmn-js viewer | starts, tasks, lanes, gateways, message-vs-sequence semantics; BPMN lint |
| Rules such as missing field ⇒ HOLD | DMN 1.5 decision model | DMN table / XML via dmn-js if available | hit policy, explicit unknown case, test cases, rule precedence |
| Context / container / component structure | C4 model | C4-PlantUML after separately admitted pinned library; else labeled PlantUML components | correctly distinct abstraction levels, boundaries, technology, relationships |
| Dense MECE issue tree | explicit partition logic (MECE is an analytical method, not an ISO notation) | Mermaid small tree; Graphviz DOT for dense tree | clear universe, no overlapping categories, defined residual/unknown cases, source-supported exhaustiveness |
| Data entities and relations | ER model with cardinality | Mermaid erDiagram or PlantUML ER | PK/FK only if known; relationship direction/cardinality verified |
| Technical figure, cutaway, assembly | CAD/ISO-informed *art direction* | original story artwork + DOM annotations in React | meaningful callouts, title block, NTS unless measured; no false manufacturing claims |
| API or event contract figure | OpenAPI 3.1.x for HTTP / AsyncAPI for events (when needed) | source contract → PlantUML/Mermaid | never invent API operations or responses; compile/schema-validate actual interface |

**Avoid notation inflation:** do not encode the same teaching event simultaneously as BPMN, UML activity, Mermaid and DOT unless comparing semantics is itself the learning objective. A diagram has exactly one declared notation and compiled source.

## 3. CAD/ISO constraints: style ≠ certification

Relevant reference families: ISO 128-2:2022 (technical drawing lines, leader/reference lines); ISO 7200:2004 (technical documentation title-block data fields); ISO 3098-1:2015 (technical documentation lettering); ISO 5457:1999 (physical engineering sheet sizes/layout); ISO 129-1:2018 (actual dimensions/tolerance presentation, only when verified). These are copyrighted technical standards; refer to their public abstracts and procure the standards for any true compliance program. We do **not** reproduce their tables or claim ISO conformance.

- For BOSS slides use **ANSI/ISO-INFORMED**, not ISO-CERTIFIED. Slide size is **16:9 / 1920×1080**, *not* an ISO 5457 A-series engineering drawing sheet.
- Figures use thin construction axes, restrained hatching, labeled leader lines, numbered callouts, technical title plate (diagram ID, title, source version, revision, `NTS`, status), zones, black-ink mechanical detail and controlled cyan/magenta operational meaning.
- Never hallucinate dimensions, engineering units, tolerances, operative machine settings, or numeric-control G-code. `NC` is a design cue for technical precision, **not** a license to generate manufacturing instructions.
- Concept art and diagrams carry different responsibilities: model generates or proposes story artwork; a parser/compiler renders formally specified relationships; native React text integrates the lessons.

## 4. MECE qualification (not merely a four-branch diagram)

Every claimed MECE partition specifies (a) **universe** of cases, (b) **classification rule**, (c) **categories and edge cases**, (d) **non-overlap demonstration**, and (e) **coverage evidence**. A visually tidy tree proves none of those properties. If exclusivity or completeness is not established, label it `CANDIDATE ISSUE TREE / MECE NOT VERIFIED`. Include explicit `OTHER_OR_UNDETERMINED` when justified, but that label alone does not establish exhaustiveness. Prefer evaluation fixtures with overlapping and uncovered cases to demonstrate a failure when rules are weak.

## 5. Accessibility and React/Tailwind rendering

- WCAG 2.2 AA *target*: meaningful alternative text for figures, logical DOM reading order, adequate contrast (normally 4.5:1 for ordinary text and 3:1 for large text), no tiny diagram labels; no visual-only critical distinctions. Logotypes have a WCAG contrast exception, but legibility still matters.
- Use one font registry with explicit weight and browser-verified metrics; do not let Mermaid default to Trebuchet/Arial while React uses another font. Pin Mermaid theme/font settings and use strict security mode for untrusted text.
- Render diagram assets inside bounded React `<figure>` components. Diagram-as-code outputs may be SVG **inside the figure**; no SVG for the entire slide/hero editorial text. If diagram SVG contains instructional labels, maintain an accessible native-HTML transcript/legend, and verify which PDF content is actually selectable rather than assuming embedded SVG text remains editable.
- Source > model structured plan > validated notation > deterministic compiler > React/Tailwind composition > Chromium screenshot/browser PDF > human visual QA. Do not rely on the model to place every line, infer business meaning from an image, or certify its own output.

## 6. Model response contract

Use `diagram-spec.schema.json` and `diagram-routing.v0.1.json`. Ask models for:
`diagram_id`, `slide_id`, `intent`, `semantic_standard`, `renderer`, `source_refs`, `status`, `nodes`, `edges`, `branches`, `source_code`, `caption`, `accessible_summary`, `unresolved`. A missing source/contradictory edge -> `HOLD`, not fictitious completion. The model can choose **from the allowed router list only**, not introduce a new DSL by taste.

**Security:** never transmit unpublished manuscripts, actual internal logo binary, customer data, credentials, or proprietary artifacts to hosted model services without explicit user authority. Use synthetic examples until source admission is authorized. This packet authorizes no billable Baseten calls and does not change provider spending-policy HOLD.

## 7. Baseline evaluation matrix

| Gate | Machine-checkable | Human-checkable | State before implementation |
|---|---|---|---|
| JSON structure/enum/source IDs | JSON Schema / custom assertions | source authority | NOT TESTED |
| Diagram syntax | renderer parser/CLI exit | terminology accuracy | NOT TESTED |
| Meaning vs source | required node/edge assertions + negative fixtures | story and operator truth | NOT TESTED |
| MECE partition | domain examples / contradictions | whether universe is properly defined | NOT TESTED |
| Diagram visual fidelity | clipped bounds / font metric tests / screenshot | editorial composition | NOT TESTED |
| Brand / figure CAD framing | palette/placement checks | approved mark, hierarchy, narrative art | NOT TESTED |
| PDF / import/editability | selectable text/page bounds / import-specific checks | edit-save-reopen | NOT TESTED |
| Deployment / release | authorizations logged | human permission | HOLD |

## Public standard references

- UML 2.5.1: https://www.omg.org/spec/UML/2.5.1/
- BPMN 2.0.2: https://www.omg.org/spec/BPMN/2.0.2/
- DMN 1.5: https://www.omg.org/spec/DMN/1.5/
- PlantUML: https://plantuml.com/
- Mermaid: https://mermaid.ai/open-source/
- Graphviz DOT: https://graphviz.org/doc/info/lang.html
- C4-PlantUML: https://github.com/plantuml-stdlib/C4-PlantUML
- ISO line conventions: https://www.iso.org/standard/83355.html
- ISO title blocks: https://www.iso.org/standard/35446.html
- ISO lettering: https://www.iso.org/standard/65679.html
- ISO sheet layout: https://www.iso.org/standard/29017.html
- JSON Schema: https://json-schema.org/draft/2020-12
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- OpenAPI 3.1.1: https://spec.openapis.org/oas/v3.1.1.html
