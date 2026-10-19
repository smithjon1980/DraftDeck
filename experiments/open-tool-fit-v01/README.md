# BOSS open-tool fit test — ten candidates, two bounded smoke checks

**Status: PUBLIC-SAFE CANDIDATE.** Based on a user-supplied October 2026 video transcript naming ten self-hosted alternatives. The video is a *discovery lead*, **not verified parity, licensing, security, zero-cost operations, or endorsement**. Never treat stars as compliance evidence.

## Rule of the test

A tool can enter BOSS only when it improves the **current** React/Tailwind + CAD/ISO/NC visual production, the Main Street Copy teaching scenario, or an authorized future workflow. An attractive adjacent app is not a reason to replace the currently chosen BOSS execution stack.

**Scope tested now:** (1) Penpot-compatible DTCG token export format + exact CSS palette parity, and (2) real browser Mermaid → Excalidraw conversion into mounted Excalidraw React editor. Both use synthetic examples and cost no subscription. They do **not** constitute live Penpot import, multi-user editor workflow, complete UML roundtrip, backend deployment, license adjudication or production approval.

## Ten-tool admission matrix

| Candidate | Actual plausible BOSS role | Trial status / next action | Major boundary |
|---|---|---|---|
| **Penpot** | Shared design systems, design-token portability, art-director layout handoff | **Smoke 1:** verify W3C DTCG/brand-token JSON against canonical BOSS CSS; human Penpot import still HOLD | Producing CSS or code snippets is not the same as exporting maintainable React/Tailwind JSX |
| **Excalidraw** | Editable early storyboard / workshop scratchpad, Mermaid-flow import | **Smoke 2:** convert synthetic Mermaid flowchart using official converter and mount React editor; inspect element/arrow/HOLD preservation | Not the CAD drawing standard and not a replacement for controlled React native labels |
| **n8n** | Already part of the proposed Main Street Copy automation stack | **KEEP / NO DUPLICATE HOST DEPLOY**; later service-flow benchmark | Sustainable Use License; external builder/configuration workflows can require commercial license |
| **Coolify** | Self-host deployment candidate for future sustained apps | **DEFER** until real server cost, access, support and ops comparison with Railway/Vercel | The software may be free but server, updates, backups, security and operations are not |
| **Supabase** | Database/auth/storage alternative when architecture demands | **DEFER**; test migration/recovery against current Railway/Postgres requirements if needed | Avoid migrating a chosen infrastructure merely for feature overlap |
| **NocoDB** | Nondeveloper records/admin UI for teaching operational inspection | **WATCH LICENSE / DEFER**; internal demo vs redistribution must be classified first | Sustainable Use License after January 2026; commercial embedding/access may require a separate license |
| **PostHog** | Audience/course analytics and UI experiment evidence | **DEFER**; prefer assessing managed options before hosting | Officially unsupported self-host deployment; substantial operations burden |
| **Documenso** | Future charter/credential contracts and signatures | **FUTURE CANDIDATE** only when an actual signing process exists | AGPL obligations and production certificate/security requirements |
| **Cal.com** | Discovery call / cohort booking for Academy | **FUTURE CANDIDATE** once booking demand exists | Must independently verify license, calendar permissions, availability and support |
| **Immich** | Media backup only, not curricular authoring or production diagrams | **OUT OF SCOPE** for the current visual stack | Photos/backups do not justify a new server for this goal |

## Tested data and contracts

### Penpot token portability

The W3C Design Tokens Community Group (DTCG) style JSON source at `penpot-boss-tokens.json` uses Penpot's documented **single-file set** format, with a top-level `BOSS` set, color entries with `$value`/`$type`, and dimension entries. Offline test reads the *actual existing* DraftDeck `design-system/tokens/tokens.css` and rejects any missing/mismatched `#FFFFFF`, `#000000`, `#00BCEB`, `#E30074`, or 1920×1080 dimensions. Penpot has **not** been opened and those tokens are **not import-verified**.

References:
- https://help.penpot.app/user-guide/design-systems/design-tokens/
- https://github.com/penpot/penpot

### Excalidraw Mermaid conversion

Official upstream converter `@excalidraw/mermaid-to-excalidraw@2.2.2` consumes only a **reviewed synthetic** print-order/HOLD `.mmd` flowchart. `@excalidraw/excalidraw@0.18.1` receives the converted skeleton, mounted inside an independent React editor. Chromium inspects Excalidraw's public scene API to see whether nodes, arrows and native editor elements exist, preserves the HOLD label, and screenshots the editor. On failure, the CI task must FAIL; green source lint is not enough. No custom diagram reconstruction has been approved as a release.

References:
- https://docs.excalidraw.com/docs/%40excalidraw/mermaid-to-excalidraw/api
- https://docs.excalidraw.com/docs/%40excalidraw/excalidraw/installation
- https://docs.excalidraw.com/docs/%40excalidraw/excalidraw/api/props/excalidraw-api

**Important:** The converter's officially documented scope is limited; not all Mermaid forms become individually editable elements. In particular, never assume PlantUML, BPMN, MECE or every complex Mermaid type is round-trippable. Even if the test passes, Excalidraw stays an optional **concept sandbox**; React/Tailwind components remain authoritative for final slides.

## Licensing and claims registry (upstream primary sources)

- NocoDB: https://nocodb.com/docs/self-hosting/license (2026 Sustainable Use License).
- n8n: https://support.n8n.io/article/can-i-use-your-license-for-my-use-case (not unrestricted OSI open source).
- PostHog: https://posthog.com/docs/self-host (self-host deployments officially unsupported).
- Coolify: https://github.com/coollabsio/coolify (Apache-2.0 project; ops are the user's duty).
- Documenso: https://docs.documenso.com/docs/policies/community-edition (AGPL-3.0).
- Other candidates require current license and service-level review before commercial adoption.

## Verdict rules and publication controls

- **PASS in CI:** a bounded compatibility behavior is demonstrated with synthetic inputs. No claim about visual sophistication, operational costs, runbook burden, platform longevity, or user's actual subscription savings.
- **FAIL in CI:** the tested capability is not established for the pinned test environment. Do not label as proof the package supports it.
- **HOLD:** human visual inspection, actual Penpot editor import/export, production-level accessible React/diagram native labels, redistribution licensing, any real service deployment, and the next 60-slide Muse generation.
- **No replacement authorized:** GitHub Actions, Windmill, Railway, n8n and the existing React Diagram Composer remain in their existing roles until real measurements justify a change.
