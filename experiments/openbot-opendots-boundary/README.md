# BOSS — OpenBot + OpenDots Governed Execution Stress Trial

**Record date:** 2026-10-23  
**Status:** SOURCE / ISOLATED INTEGRATION TESTS PASS. CROSS-SYSTEM ENFORCEMENT AND PRODUCTION ADOPTION HOLD.  
**Owner decision:** lead with OpenBot and OpenDots in testing, preserve the current BOSS production stack and human authority.

## Exact source admission
- OpenBot: `CopilotKit/OpenBot@bd4dc94943a9d62aefd05e5e99073ba58919c9c6` (MIT)
- OpenDots: `CopilotKit/OpenDots@8091324942b86789ed0da7facbee855145d933b0` (MIT)
- Original upstream source is cloned and SHA-checked on disposable CI runners. Supplemental BOSS tests are copied/appended **only in those throwaway runner checkouts**, not committed upstream. The DraftDeck PR contains only public synthetic harness code and documentation.
- **Canonical successful evidence:** [GitHub Actions 40021472637](https://github.com/smithjon1980/DraftDeck/actions/runs/40021472637).

## Verified execution outcomes

| Separate native/test suite | Result | Boundary tested |
| --- | ---: | --- |
| OpenBot PostgreSQL + pgvector database integration (16 files) | 172/172 PASS; 469 assertions | Persisted policy, approval stores and reviews, audit identity/cursor/retention, service coordination, publication and revocation |
| OpenBot agent-computer boundary (7 files) | 139/139 PASS; 319 assertions | Egress policy module, action barrier, authorisation, request validation, workspace, control |
| OpenBot mocked gateway including 3 injected BOSS cases (1 file) | 74/74 PASS; 221 assertions | Audit insertion failure stops otherwise allowed action; 75 concurrently refused actions do not reach mock computer; 75 concurrently allowed actions produce matching decision records |
| OpenDots complete native suite with 2 injected BOSS cases (56 files) | 348/348 PASS | Computer permissions, audit, page approval, task/retry/storage, security, workspace; 75 disabled-shell and 75 globally paused attempts denied without mock transport calls |
| OpenDots typecheck and real Vite/React/server build | PASS | Real JS/TS build integrity |
| OpenDots focused 17-file rerun | 130/130 PASS | Overlap with full suite; **do not add** to distinct total |
| DraftDeck ontology guard | PASS | Repository candidate naming |

**733 distinct executed tests in latest successful stress workflow:** 172 + 139 + 74 + 348. This count includes original upstream and 5 added synthetic test cases, excludes overlapping focused OpenDots rerun and all previous PR #94 tests.

## Subtle audit observation: visibility vs durability
Initial extra OpenDots tests expected 75 audit rows from `w.computers.audit(id)`; the method intentionally returns **only the latest 50**. Its `ComputerStore.finish` retains **up to 1,000 completed rows per Dot**. That first assertion was invalid because it conflated UI query scope with database persistence. The final corrected tests require **50 returned by the query and 75 matching rows persisted in SQLite after closing and reopening the workspace database**. Both tests pass.

For BOSS, 50 visible / 1,000 retained is **not** a complete long-term evidence archive. A separately controlled, immutable audit archive/export, retention rules, pagination and provenance must be designed before operator/charter production use.

## Critical shared-policy gap — NOT TESTED, do not imply integration
OpenDots uses OpenBot's *computer image/supervisor* but calls its **own** `ComputerService.action` and `ComputerStore` from `computerTools`, subject to OpenDots per-Dot permissions. It **does not automatically traverse OpenBot's server-level CEL policy decision gateway or OpenBot PostgreSQL audit store**.

Therefore, a successful OpenDots task is **NOT evidence** that OpenBot's BOSS policy authorized it. A BOSS boundary must become physically unavoidable through a dedicated server-side adapter/gateway and network isolation—not simply an agent instruction, OpenDots checkbox, or superficial UI approval.

## Production-admission gaps / adversarial next test
1. **Cross-system route:** OpenDots -> BOSS authority -> isolated computer; deny must block at network boundary, even if OpenDots would otherwise permit. No direct app-to-supervisor bypass.
2. **Real fault injection:** disconnect/fail **actual PostgreSQL** during intent audit write, verify no downstream dispatch. Current failure injection covered gateway behavior with a fake failing audit store; persistence integration used healthy PostgreSQL.
3. **End-to-end approval:** bind exact action digest to authenticated human decision and current source identity; refuse replay, changed payload, expired request and unattended self-approval. Survive application restart.
4. **Host/container attacks:** test unexpected egress including DNS, internal addresses/SSRF and shell/network abuse using disposable runtime, not merely egress-policy unit tests. OpenDots docs say restrictive network egress is **not** configured by default, and stock Docker containers share host kernel.
5. **Multi-tenant and storage:** two users/dots must not share credentials, approval scopes, file stores or hidden browser profiles. Validate 1000-row retention and long-term evidence export.
6. **Cost of integration:** compare maintenance, CopilotKit Intelligence/self-hosted licence and per-computer resources against existing GitHub Actions/Windmill/n8n/Railway.
7. **Real BOSS build:** synthetic React candidate only until protected narration and brand assets can be provisioned through a safe private source path with exact-copy hashes.

## Architecture under evaluation

**OpenDots = operator workspace and review surface (candidate)** → **BOSS authoritative policy, custody and approval gateway using OpenBot governance patterns (candidate)** → **scoped MCP / browser/compute adapters** → **existing Windmill / GitHub Actions / n8n / Railway for their designated jobs**. Store full immutable evidence independently. Humans retain authorization over releases, charter actions and claims.

No BOSS production services were modified, no user accounts/credentials or unpublished narrations were passed, no new service was deployed. PR remains draft and merge requires human review. OpenBot/OpenDots are still candidates despite passing isolated suites.
