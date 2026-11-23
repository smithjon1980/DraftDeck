# BOSS — Open-source design interoperability trials, v0.1 CANDIDATE

**Scope:** Current DraftDeck / Episode 01 React+Tailwind presentation pipeline. Source: user-supplied 10-tool video transcript. This is a selective experiment, **not** authorization to install production apps, replace Railway/n8n/Figma/Canva, or publish private narrated materials.

## Executed evidence (2026-10-19; synthetic only)

GitHub Actions run [39252667341](https://github.com/smithjon1980/DraftDeck/actions/runs/39252667341) completed successfully. The repository terminology guard also passed on the same PR head.

**Penpot token-export structural gate — PASS (five unit tests).** Generated a candidate single-JSON-set import file with four exact current BOSS color tokens (white `#FFFFFF`, black `#000000`, cyan `#00BCEB`, magenta `#E30074`) and 1920px/1080px slide-dimension tokens. Negative cases reject missing colors, substituted colors, incorrect canvas sizing and CSS/contract drift. **Actual Penpot import, edit-save-reopen, font parity, component fidelity and design review remain NOT_TESTED.**

**Excalidraw actual React editor + browser roundtrip — PASS for technical editability only.** `@excalidraw/excalidraw@0.18.1` compiled using esbuild's explicit `production` condition; Chromium loaded **11 scene elements** representing four labeled nodes and three lines, kept all four expected stable source IDs after `convertToExcalidrawElements(scene.elements,{regenerateIds:false})`, changed the `msc-hold` node's stroke to `#000000`, and exported **11 elements** through the library JSON serializer. No browser runtime errors were reported. Artifacts include `screenshots/excalidraw-before.png`, `screenshots/excalidraw-edited.png`, a serializable scene JSON and report JSON.

**Visual assessment — FAIL as BOSS production diagram.** Inspection of the two real browser screenshots showed a text overflow/clipping problem in the customer-request node, awkward word splitting in the decision diamond and handwritten/default-editor label appearance that diverges from BOSS's bold typography and technical CAD/ISO control. Successful JSON roundtrip does **not** qualify this editor's visual rendering as the approved React master.

**Important intermediate failures and fixes:** the Excalidraw CSS conditional export required `esbuild --conditions=production`. The initial scene-conversion behavior regenerated object IDs, breaking provenance until `regenerateIds:false` was used. These are now documented integration constraints. No editor account was connected and no production migration or hosted service was performed.

**Human decision requested:** keep Penpot as a candidate **design-token review tool**, and keep Excalidraw only as an optional **concept/storyboard aid**. The original reviewed Mermaid/PlantUML source plus BOSS React semantic composer remains the stronger direction for production diagrams. No evidence justifies replacing the production renderer.

## Test questions

**Penpot.** Can we turn the existing DraftDeck design tokens into a Penpot single-JSON-set import candidate **without reinterpreting brand values**? Run `python -m unittest discover -s experiments/oss-design-v01/scripts -p test_*.py -v`, then `python experiments/oss-design-v01/scripts/export_penpot_tokens.py --output <path>`. The output has the `Global` top-level set and DTCG `$type`, `$value`, `$description` fields prescribed by Penpot's official documentation. Six tokens: four colors, fixed slide width and height. An offline schema/parity pass DOES NOT establish an actual Penpot UI import, native layer fidelity, or React code generation. Penpot account and import are **NOT CONNECTED / NOT TESTED**. See https://help.penpot.dev/user-guide/design-systems/design-tokens/ .

**Excalidraw.** Can the actual MIT-licensed `@excalidraw/excalidraw@0.18.1` React component import a **synthetic** Main Street Copy 4-node concept scene, preserve editable objects, modify the HOLD node, and serialize an editable JSON scene? In GitHub CI, `npm install` + `esbuild` + real Chromium exercise the mounted component, imperative update API and `serializeAsJSON`. On success, the artifact supplies before/after screenshots, source-side JSON, and a machine-readable report. The trial is strictly a **storyboard scratchpad**, **NOT** a replacement for source-traceable Mermaid/PlantUML meaning or the React CAD/ISO presentation master. See https://docs.excalidraw.com/ and https://github.com/excalidraw/excalidraw/blob/master/LICENSE .

## Whole-list screening

| Source candidate | Proposed role | Decision before experiments |
| --- | --- | --- |
| Penpot | Design token parity, visual review and developer handoff | ACTIVE trial (tokens only) |
| Excalidraw | Early storyboard and informal concept sketches | ACTIVE trial (real editor import/edit/export) |
| NocoDB | Human-readable asset inventory/QA records later | Hold — license and data-provenance review needed; no DB migrated |
| Coolify | Self-managed hosting alternative | Hold — infrastructure, TLS, backups, security and ongoing operation costs |
| PostHog | LMS product analytics after public launch | Hold — current self-hosting discouraged/unsupported by its docs |
| Supabase | Optional future backend/auth/data | Hold — already has Railway/Postgres pilot plans; no replacement required |
| n8n | Existing candidate workflow orchestrator | Retain selectively; licensing must be reviewed for client-editable/licensed teaching services |
| Cal.com | Scheduling/academy office hours | Low current relevance |
| Documenso | Charter or agreement signing | Low current relevance; signature legal compliance must be separately reviewed |
| Immich | Photo archival | Not a DraftDeck renderer; do not add to slide build |

No broad claims that the free editions are equivalent to subscription services, universally license-compatible, zero-cost to operate, or production ready. Validate current software licensing with official sources: n8n https://support.n8n.io/article/can-i-use-your-license-for-my-use-case; NocoDB https://github.com/nocodb/nocodb/blob/develop/LICENSE.md; Coolify https://coolify.io/docs/choose-your-path; PostHog https://posthog.com/docs/self-host .

## Required BOSS test gates

1. **STRUCTURE:** Penpot export exactly matches existing `design-system` brand tokens and rejects wrong colors/sizing; Excalidraw scene has four source IDs and proof of editable, exported entities.
2. **ENVIRONMENT:** Runner/tool versions and exact source revision recorded; no paid APIs, credentials, permanent deployment or private sources.
3. **VISUAL:** Human inspection of Chromium before/after screenshots; BOSS original identity is not to be fabricated. The storyboard is *not* a CAD production illustration, even if lines appear straight.
4. **ADAPTER:** Explicit in-account Penpot import and edit-save-reopen still required if we choose to use it. A DTCG JSON pass does not prove import works.
5. **AUTHORITY:** Candidate results remain HOLD for integration until authorized human assessment. Do not silently switch the released diagram format away from React/Tailwind.

## Possible follow-up decision

If Penpot tokens pass and the actual UI import is verified later, use **Penpot only for controlled human visual/token review**, with React remaining the authored presentation. If Excalidraw can round-trip editable objects, make it an optional lesson/storyboard aid; do not use its hand-drawn canvas as Episode 01's engineered presentation layer.

**Expected cost:** No provider inference, no purchased services. GitHub Actions compute/network usage can be metered against repo/account allowances. No hosted instance deployed.
