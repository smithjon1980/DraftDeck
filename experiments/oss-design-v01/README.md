# BOSS — Open-source design interoperability trials, v0.1 CANDIDATE

**Scope:** Current DraftDeck / Episode 01 React+Tailwind presentation pipeline. Source: user-supplied 10-tool video transcript. This is a selective experiment, **not** authorization to install production apps, replace Railway/n8n/Figma/Canva, or publish private narrated materials.

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
