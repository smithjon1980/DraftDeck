# DraftDeck Brand and Instructional Design Guide

Version 1.0 · 2026-10-09 · Working specification

This Markdown guide consolidates established BOSS requirements and proposed implementation rules. Proposed values require rendered validation; missing assets and evidence remain explicit.

DraftDeck Style Guide and Planning Template

Version 1.0  |  9 October 2026  |  Jonathan Smith  |  BOSS

Use this editable reference to give articles, slides, student workbooks, and instructor guides a shared visual and instructional identity. React and Tailwind are the default authoring tools for new slide families. Preserve approved teaching content independently from its layout.

## Visual foundations

Typography implementation proposal: use Arial for this document and an approved sans-serif token for slide narrative; use JetBrains Mono for operational labels. Lock exact slide font sizes and line heights after the first rendered preview rather than presenting untested values as accepted standards.

## Icon discipline

Import real Lucide SVG icons and record names and package versions. Material Symbols Outlined is secondary; Phosphor is fallback. Use a consistent 24 or 32 pixel grid, outline strokes, and approved stroke tokens. Do not generate substitute library icons. Keep custom story artwork separate.

## Shared teaching components

Select components that serve the lesson. Do not force all ten into each page. Preserve the shipping logistics frame for current Day Zero.

## Continuity across formats

Maintain one lesson map with stable IDs for objectives, claims, sources, approved wording, exercises, and evidence limitations. Tie each artifact to a source revision. The article explains; slides foreground relationships; the workbook provides response space; the instructor guide supplies facilitation and assessment guidance.

Public materials use approved wording. Deep dives and source decks belong to the private backstage when designated. Keep their release scope explicit; a public repository branch is not private storage.

## Layout selection

Use an opener for one focal relationship, an editorial layout for explanation, a process layout for decisions, a reference layout for comparisons, and a practice layout for learner action. Fit depends on the declared canvas and actual rendering. Never hide required caveats or shrink text silently to make it fit.

## Reusable page planning template

Duplicate this page for each planned slide or lesson section. Bracketed fields are prompts to complete, not source evidence.

## Identity and revision

[Lesson ID]  [Page ID]  [Source commit or tag]  [Author]  [Review status]

## Teaching purpose

[Learner objective]  [Supported takeaway title]  [Public or private scope]

## Approved content

[Exact wording]  [Sources]  [Evidence classification]  [Limitations or UNKNOWN values]

## Composition

[Canvas dimensions]  [Layout variant]  [Component IDs]  [Icon names and versions]

## Layer plan

[Live title and body text]  [Separate artwork]  [Drafting lines]  [Operational metadata]

## Cross format links

[Article section]  [Slide]  [Workbook exercise]  [Instructor guidance]

## Review and release

[Reviewer]  [Changes needed]  [Authorization scope]  [Release destination]

## Build and acceptance checks

Build React components with shared Tailwind tokens. Compile CSS and export self-contained static HTML with live text and embedded assets. Use the available static HTML Canva route; treat PDF as a separately tested alternative. Canva does not import React source as native components.

Record PASS, FAIL, or NOT TESTED separately for content fidelity, browser rendering, print export, accessibility, and destination layers. Inspect clipping, overlap, fonts, dimensions, exact wording, and separate editable text and artwork. Extractable PDF text does not prove Canva editability. Do not claim destination acceptance before inspection.

Foundation: USWDS token and component practices; WCAG 2.2 AA is the web accessibility target. These references do not establish conformance. This document is a style reference and planning template, not a tested Canva slide or a completed course.

## Verified source register

Reviewed 9 October 2026. The mapping below is DraftDeck's interpretation of published documentation, not endorsement or equivalence with those brands.

| Published guide | Structural correspondence | What DraftDeck retains |
|---|---|---|
| [IBM Design Language](https://www.ibm.com/design/language/) | Grid, typography, iconography, illustration, data visualization, technical diagrams, layout and animation | Technical precision and distinct rules for each visual medium |
| [Atlassian foundations](https://atlassian.design/foundations) | Tokens, content, accessibility, spacing, grid, color, typography, icons, borders and release phases | Named decisions and reusable component contracts |
| [Microsoft Fluent React](https://fluent2.microsoft.design/components/web/react) and [design handoff](https://fluent2.microsoft.design/get-started/design) | Design resources map to working code libraries | React component identity must match the design specification |
| [Mailchimp content guide](https://styleguide.mailchimp.com/) and [voice and tone](https://styleguide.mailchimp.com/voice-and-tone/) | Consistent editorial voice with situational tone | Clear authorial language across article, narration, exercises and facilitation |
| [Shopify brand assets](https://www.shopify.com/brand-assets) | Explicit asset usage and affiliation rules | BOSS logo inventory, permitted variants and release scope |
| [USWDS tokens](https://designsystem.digital.gov/design-tokens/) | Shared named values that build component styles | Existing implementation foundation; BOSS identity remains independent |

Do not import another brand's logo, palette, proprietary typography or component appearance by default. Structural correspondence means adopting an applicable documentation or production relationship. It does not make BOSS IBM, Fluent, Atlassian or a government design system.

## Requirement vectors and completion state

These 24 vectors are a design coverage inventory, distinct from the Seven Vector TRIP framework and canonical BOSS fields. Defined means a written rule exists; it does not mean a rendered artifact has passed review.

| ID | Vector | Required rule or deliverable | State |
|---|---|---|---|
| V01 | Identity | BOSS and DraftDeck naming, author attribution and purpose | Defined |
| V02 | Logo | Supplied master, approved lockups, clear space and minimum size | Pending authoritative logo asset |
| V03 | Color | White canvas, dark ink, functional burnt orange; meaning conveyed in words | Defined |
| V04 | Type roles | Display, narrative and operational label | Defined; exact font set pending |
| V05 | Type scale | Per-format sizes, line height, fallback and maximum line length | Proposed below; render test pending |
| V06 | Spacing | 8, 16, 24, 32, 48, 64 px scale | Defined |
| V07 | Grid | Explicit canvas, margins, alignment and density | Defined; per-layout geometry pending |
| V08 | Icons | Lucide primary, named imports, package versions and consistent grid | Defined |
| V09 | Illustration | Separate story assets, source provenance and evidence labels | Defined |
| V10 | Photography | Use only when instructional; source, permission and caption required | Defined; no photographic brand signature selected |
| V11 | Diagrams | Deterministic shapes, labeled branches, UNKNOWN retained | Defined |
| V12 | Charts | Source, units, timeframe, scale, limitation and text alternative | Defined |
| V13 | Editorial voice | Precise, reflective, direct; no invented certainty | Defined |
| V14 | Terminology | Current shipping frame; canonical terms checked against source | Defined |
| V15 | Components | Ten editorial features with fields and acceptance checks | Defined |
| V16 | Templates | Opener, editorial, process, reference and practice | Defined; reference renders pending |
| V17 | Cross-format continuity | Stable lesson IDs and source revision across four media | Defined; actual lesson map pending |
| V18 | Accessibility | WCAG 2.2 AA target for web plus applicable document checks | Target defined; conformance not tested |
| V19 | Responsive behavior | Semantic reflow for web; fixed print and slide geometry | Defined; breakpoints proposed |
| V20 | Interaction and motion | Keyboard behavior and reduced motion; no decorative motion in print | Defined; app behavior not implemented |
| V21 | React and Tailwind | Shared components and tokens; static compiled export | Defined; build not tested |
| V22 | Destination layers | Live text, separate artwork, actual Canva inspection | Defined; current preview not tested |
| V23 | Governance | Owner, version, evidence, review and authorization fields | Defined |
| V24 | Distribution | Public front stage and private backstage with explicit release scope | Defined; storage migration pending |

## Visual tokens

| Token | Value | Use |
|---|---|---|
| color.canvas | #FFFFFF | All default canvases |
| color.ink | #20252A | Narrative and primary text |
| color.action | #B34700 | Functional accent with explicit status labels |
| space.scale | 8, 16, 24, 32, 48, 64 px | Layout spacing |
| icon.grid | 24 or 32 px | Consistent family per composition |
| icon.stroke | 1.5 to 2 px at 24 px | Project geometry default; visually validate imported paths |
| line.cap | square | Custom drafting geometry |
| line.join | miter | Custom drafting geometry |
| artwork.fill | none by default | Outlined story forms; explanatory hatching permitted |

Preserve library icon geometry unless a deliberate, documented adaptation is required. Custom drafting rules must not silently deform imported Lucide symbols.

### Proposed type and responsive tokens

The following are implementation candidates, not accepted measurements. They require browser and print review at the intended reading distance.

- Web narrative: 18 px body, 1.55 line height, reading measure 60 to 75 characters; heading levels must remain semantic.
- 1920 by 1080 slide: 56 to 72 px title, 28 to 34 px body, 20 to 24 px metadata; adjust layout before reducing required text.
- Print reading document: 11 to 12 pt body, 1.15 to 1.35 line spacing; workbook writing areas must allow handwriting.
- Operational labels: approved monospace, tabular numbers where appropriate; avoid long paragraphs in all caps.
- Web breakpoint candidates: 640 and 1024 px. Reflow columns rather than shrinking a fixed page. Test 320 CSS px width and zoom where applicable.
- Font choice: legible sans-serif for narrative and JetBrains Mono as an operational candidate. Check license, embedding and destination availability before locking a family.

## Component contracts

| Component | Required fields | Suitable variants | Acceptance |
|---|---|---|---|
| At the Loading Dock | Scenario, purpose, evidence class | Illustrated opener or inline scene | Label illustrative scenarios |
| Pause & Consider | One focused question | Open rail or inline prompt | No fabricated learner answer |
| Inspect the Payload | Source, candidate, finding | Comparison or table | Preserve exact source distinction |
| Choose the Route | Condition, evidence, outcomes | Decision diagram or exercise | No UNKNOWN to execution shortcut |
| The Working Agreement | Frame fields, values, source version | Specification strip or reference | A subset does not replace the whole frame |
| Evidence Window | Claim, source, scope, limitation | Open evidence panel | Do not upgrade sample to verification |
| Recovery Record | Problem, action, obtained evidence | Three columns or steps | Separate actual and proposed actions |
| Before You Release | Verification and authorization | Distinct checkpoints | Verification does not grant release |
| Try the Handoff | Payload, scope, completion, response space | Practice section or page | Keep the task bounded |
| Carry Forward | Principle, reflection, next action | Closing rail | Respect authorized scope |

Every component specification records: ID, version, purpose, required and optional fields, variants, tokens, density limits, reading order, responsive behavior, print behavior, keyboard behavior where relevant, accessibility checks, source revision and reference render.

## Editorial and brand requirements

Use the author's approved wording for public teaching content. Distinguish observed fact, reported case, inference, proposed action and unknown information. Keep limitations beside the claims they qualify. Avoid clinical, legal, moral or motive conclusions unsupported by the source. Use shipping logistics for current Day Zero; historical aviation material is reproduced only within an explicitly requested historical reconstruction.

Use consistent names for the ten editorial features. Do not confuse them with shared-frame fields. Maintain a terminology register with canonical term, definition, source, forbidden ambiguous substitutes and introduction point. Expand unfamiliar acronyms on first use. Status labels must communicate meaning without color alone.

For public audio, approve and version the exact script before speech generation. Keep exploratory deep dives separately classified. Generated audio requires comparison against the approved script before an exact-wording claim; tool choice alone does not guarantee verbal fidelity.

## Diagram and evidence rules

Use source-controlled geometry for exact processes. Record diagram language and version; validate syntax and inspect the actual render. Distinguish reading-order connectors from operational decision branches. Give every decision a labeled condition and outcome. Preserve missing-source recovery and UNKNOWN states. Do not fabricate screenshots, receipts, measurements or completed actions.

Charts require the underlying dataset, units, timeframe, scale rationale, caption and limitation. Avoid decorative 3D or scales that disguise comparisons. Provide an accessible text summary. Illustrations may explain a structural relationship but must not be presented as measurements or literal physical equivalence.

## Implementation and handoff contract

1. Read current content and approved visual constraints.
2. Create the lesson map and record approved wording independently from rendering.
3. Select component and layout variants; record asset provenance and icon names.
4. Implement React components with shared Tailwind tokens. Pin dependency versions in the project lockfile.
5. Compile styles and render self-contained static HTML. Embed required assets; do not depend on a development server or remote CDN at import.
6. Inspect browser output for geometry, reading order, clipping and legibility. Keep actual browser print distinct from an independently drawn PDF.
7. Use the supported destination import route. Static HTML is the existing documented Canva path; PDF is a separately tested alternative.
8. Inspect destination dimensions, wording, text records, artwork records and thumbnails. Count alone does not prove fidelity. Record font substitutions and hands-on edit status.
9. Link released artifacts to the source revision, lesson IDs and acceptance record. Preserve public and private scope.

React and Tailwind provide authoring discipline; they do not guarantee design quality or native Canva components. Avoid claiming import capability until the current connector schema and returned result support it.

## Reusable lesson and slide template

```yaml
lesson_id: "[stable lesson ID]"
page_id: "[stable page ID]"
source_revision: "[commit or tag]"
audience: "[learner or instructor]"
release_scope: "[public or private]"
objective: "[observable learning objective]"
takeaway_title: "[supported statement]"
approved_copy: "[exact approved wording]"
evidence:
  classification: "[observed / reported / inferred / illustrative / unknown]"
  sources: []
  limitations: []
composition:
  canvas: "[width and height with units]"
  layout_variant: "[approved variant]"
  component_ids: []
  icon_library: "lucide"
  icon_names: []
  package_version: "[locked version]"
  artwork_assets: []
cross_format:
  article_section: "[ID]"
  slide: "[ID]"
  workbook_exercise: "[ID]"
  instructor_guidance: "[ID]"
acceptance:
  content: "NOT TESTED"
  browser: "NOT TESTED"
  print: "NOT TESTED"
  accessibility: "NOT TESTED"
  destination_layers: "NOT TESTED"
release:
  reviewer: "[name]"
  authorization_scope: "[existing authorization]"
  destination: "[destination]"
```

## QA and change governance

Require each acceptance entry to include result, scope, date, artifact revision, method, reviewer and remaining limitation. Use PASS, FAIL and NOT TESTED. Do not treat a prior deck's success as evidence for a new artifact.

Review changes to tokens and shared components for effects across all four formats. Record the old rule, new rule, reason, affected IDs and migration requirement. Maintain deprecated variants explicitly until their dependent artifacts are updated. Keep verification distinct from release authorization.

### Open decisions

- Authoritative BOSS and DraftDeck logos, approved lockups and clear-space values.
- Final narrative fonts and per-format type scales.
- First accepted reference renders for each layout variant.
- Actual lesson map and workbook/instructor schemas.
- Canva verification of the requested three-slide preview.

These gaps remain visible so future AI runs cannot replace missing decisions with invented brand rules.