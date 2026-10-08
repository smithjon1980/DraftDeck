# BOSS Editorial Design System v0.1

Use these contracts for current DraftDeck slides, Markdown, and web lesson components. They are editorial specifications, not additional BOSS canonical doctrine. Follow later explicit user requirements over these defaults.

## Foundations

- Adopt named-token and reusable-component practices from USWDS: https://designsystem.digital.gov/design-tokens/ and https://designsystem.digital.gov/how-to-use-uswds/.
- Target W3C WCAG 2.2 Level AA for web output: https://www.w3.org/TR/WCAG22/. Check applicable criteria, including semantic headings, alternatives for meaningful imagery, keyboard access, visible focus, reflow, contrast, and target size. Do not infer conformance from styling or automated checks alone.
- Use BOSS-owned identity and patterns. Prior Apple/Uber references are inspiration, not overriding layout instructions or claimed standards conformance. Avoid mixing multiple external systems ad hoc.
- Preserve #FFFFFF canvas, #20252A ink, #B34700 functional accent, outlined geometry, and open drafting rails. Use orange for active/unresolved/alert cues; labels must convey meaning without color alone.
- Permit cross-hatching and Ben-Day dots in explanatory logistics artwork when appropriate. Avoid decorative gradients, shadows, or filled panels. Separate text from story artwork.
- Set typography roles: display heading, reading body, operational label. Use legible sans-serif for narrative and monospace for fields/code. Store exact fonts, sizes, line-height, spacing, stroke widths, breakpoints and semantic color roles in tokens rather than scattered literal overrides.
- Use an approved spacing scale (8, 16, 24, 32, 48, 64 CSS pixels). Check optical alignment and readable line lengths; do not treat token compliance as visual acceptance.

## Operational language

Apply the Human Accountability Rule in `doctrine/logistics-framework.md` to every component: **software capability does not transfer human accountability.** Describe the operation, identify the evidence, and name the accountable human.

AI, model, and system are permitted subjects of observable operations: “the model returned,” “the system executed,” and “the AI classified.” Avoid human mental states, anatomy, intention, and moral agency. Describe a failure by its observed form, such as an unsupported claim, fabricated citation, source mismatch, or unverified action report. Preserve the distinction between reported and verified operations. Computation, inference, and reasoning as functional operations do not establish human understanding or release authority.

The left column below documents prohibited wording; it is not approved teaching copy. The terminology guard exempts only these four exact comparison rows in the two maintained contract copies. It checks the rest of each file normally.

| Prohibited wording | Operational wording |
|---|---|
| “The AI hallucinated.” | “The output contains an unsupported claim.” |
| “The AI brain.” | “The model” or “processing system.” |
| “The AI understood the assignment.” | “The output satisfied the stated requirements.” |
| “The AI decided to release it.” | “The system applied a release rule,” or “the authorized person approved release.” |

Choose the final row's replacement from the evidence: a recorded rule application and a human approval are different events. Name the rule or approving human when known; retain UNKNOWN where evidence is missing. For Evidence Window, identify the evidence source and scope. For Choose the Route, state the routing condition and authority. For Carry Forward, name the next human responsibility or already authorized operation.

Acceptance: review component copy against this rule, preserve evidence classifications, and run `python3 .github/scripts/check_operational_language.py` from the repository root. The guard catches common constructions and is not a complete semantic review.

## Component registry

Each component requires an identifier, required fields, allowed variants, media behavior and acceptance checks. Use only components needed by a section; do not insert all ten into every page.

| Component | Required fields | Approved presentation | Acceptance check |
|---|---|---|---|
| At the Loading Dock | Scenario, teaching purpose, evidence classification | Integrated illustration with short scene; opener or inline | Scenario supports the lesson; illustrative content is labeled |
| Pause & Consider | One focused reflective question | Open margin rail or inline question block | Question examines reasoning; no invented learner response |
| Inspect the Payload | Source excerpt, candidate, inspection finding | Side-by-side comparison or compact table | Exact source and proposed candidate distinguished; deviation visible |
| Choose the Route | Condition, evidence, labeled outcomes | Compact Mermaid/PlantUML decision diagram or decision exercise | Branches are explicit; no unconditional UNKNOWN-to-execution path |
| The Working Agreement | Relevant frame fields, values, source/version | Monospaced specification strip or full reference | Selected-field strip does not replace the ten-field agreement |
| Evidence Window | Claim, evidence source, scope, limitations | Bordered evidence panel | Receipt/report/sample not upgraded to full verification |
| Recovery Record | Observed problem, recovery action, obtained evidence | Three-column record or stacked steps | Actual versus proposed actions separated; completed work not repeated |
| Before You Release | Verification checks, authorization scope | Two distinct checkpoints | VERIFIED does not grant release; existing authorization may suffice |
| Try the Handoff | Payload, permitted actions, completion criteria, record space | Practice section or exercise page | Task bounded; actual response retained; blanks not fabricated |
| Carry Forward | Principle, reflection, next bounded action | Closing rail | Next action remains within stated scope |

## Layout patterns

- Low copy: illustrated opener or section divider; one focal story element, short lead and concise feature rail. Target roughly 80-120 teaching words when suitable.
- Medium copy: editorial explanation with diagrams aligned to the copy they explain; roughly 250-350 teaching words. Alternate illustration side and composition within approved variants. Avoid artwork pasted after the text is finished.
- High copy: grouped specification, comparison or evidence reference; roughly 400-500 teaching words if legible on the declared canvas. Use structured columns/tables and clear hierarchy.
- Treat counts as planning ranges, not mandatory padding. Include headline, lead, labels and body in recorded teaching counts; declare exclusions such as navigation or writing prompts. Report feature-rail counts separately if excluded.
- Mix opener, editorial, process/swimlane, reference, and practice pages to serve narrative pacing. Do not turn every page into the same card grid or scenic title slide.
- For current 15-slide Day Zero story, preserve all coverage and closing evidence package. Do not silently impose a different slide count from an older brief.
- Markdown: continuous reading with descriptive headings, short paragraphs, inline visuals, captions, feature blocks and explicit placeholders for missing evidence. Do not copy reference publication prose or imagery.
- Website: reflow semantic content and components for narrow screens; use expandable evidence where useful. Do not merely scale a fixed slide page into a mobile website.

## Component contract and generation instruction

For every implemented component record `id`, `variant`, `required_fields`, `tokens`, `responsive_behavior`, `print_behavior`, `accessibility_checks`, and `reference_render`. Preserve a content schema separately from the rendering template. Omit an optional component instead of inventing its missing evidence.

Use this generation instruction:

> Build using the approved BOSS components, layout templates and design tokens. Select an existing variant that fits the supplied content. Do not invent additional styles or component types. Report content that cannot fit the approved patterns. Preserve evidence classifications and limitations.

## Acceptance record

Check content fidelity and visual layout separately. Record browser rendering, browser print, diagram syntax/rendering, Markdown links, accessibility checks, and Canva editability only where actually tested. A ReportLab rendition is not a browser-rendering test. A historical Canva import test does not verify a later deck. Save source, assets, manifest, preview and scoped findings as the requested deliverable package.
