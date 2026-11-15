# BOSS 105 — Upgrade control register (implementation candidate)

**Status:** `IMPLEMENTATION_CANDIDATE_NOT_RELEASED` · **Authority:** human operator · **Scope:** DraftDeck skill/governance/validation changes only.

This is a complete crosswalk for the owner's 105-point instruction. Registering a control does **not** prove that its runtime enforcement is implemented or tested. No credential, manuscript, authentic approval ledger, or protected art belongs here. Existing v0.11 and approved editorial sources are unchanged.

## Execution policy
- P0 blocks source admission, authority elevation, narrative qualification, and precomposition admission. P1 is fidelity, workflow and verification. P2 optimizes only after P0/P1 evidence.
- `PROPOSED`, `CODED_UNTESTED`, `SYNTHETIC_PASS`, `INTEGRATION_PASS`, `HUMAN_ACCEPTED`, `HOLD`, and `NOT_TESTED` are separate evidence fields, not interchangeable completion claims.
- All non-public material remains private. New CI handles only synthetic fixtures and cannot authorize/artifact-release or dispatch consequential work.
- Approval identity must include candidate ID, exact source digest, artifact digest, target, profile, composition ID, human record reference and event identity. It is verified by a real approval service, not by the schema alone.

## 105-item crosswalk

| ID | Domain | Priority | Control | Required evidence |
|---|---|---|---|---|
| 001 | 1 | P0 | Decision-rights matrix | human decision + ledger verification |
| 002 | 1 | P0 | Immutable candidate IDs | human decision + ledger verification |
| 003 | 1 | P0 | Explicit scoped approval commands | human decision + ledger verification |
| 004 | 1 | P0 | Approval identity binding | human decision + ledger verification |
| 005 | 1 | P0 | Declaration versus repository evidence | human decision + ledger verification |
| 006 | 1 | P0 | Restricted human ledger | human decision + ledger verification |
| 007 | 1 | P0 | No model/CI approval minting | human decision + ledger verification |
| 008 | 1 | P0 | Approval invalidation on changes | human decision + ledger verification |
| 009 | 1 | P0 | Fresh IDs after rejection | human decision + ledger verification |
| 010 | 1 | P0 | Editorial versus narrative decisions | human decision + ledger verification |
| 011 | 1 | P0 | Independent acceptance states | human decision + ledger verification |
| 012 | 1 | P0 | Separate opener and closer | human decision + ledger verification |
| 013 | 1 | P0 | Escalation ownership | human decision + ledger verification |
| 014 | 1 | P0 | Action-specific human release | human decision + ledger verification |
| 015 | 1 | P0 | Approval integrity audit | human decision + ledger verification |
| 016 | 2 | P0 | Exact approved source per run | source/custody readback or synthetic test |
| 017 | 2 | P0 | Admission record path/ref/blob | source/custody readback or synthetic test |
| 018 | 2 | P0 | Preserve source history | source/custody readback or synthetic test |
| 019 | 2 | P0 | Unrecovered historical v0.12 boundary | source/custody readback or synthetic test |
| 020 | 2 | P0 | Separate SHA and Git blob kinds | source/custody readback or synthetic test |
| 021 | 2 | P0 | Versioned paragraph normalization | source/custody readback or synthetic test |
| 022 | 2 | P0 | P001–P025 per-paragraph hashes | source/custody readback or synthetic test |
| 023 | 2 | P0 | Coverage/ordering/uniqueness | source/custody readback or synthetic test |
| 024 | 2 | P0 | Compare promoted text bytes | source/custody readback or synthetic test |
| 025 | 2 | P0 | Protect private manuscript | source/custody readback or synthetic test |
| 026 | 2 | P0 | Safe IDs and archive paths | source/custody readback or synthetic test |
| 027 | 2 | P0 | Atomic collision-safe writes | source/custody readback or synthetic test |
| 028 | 2 | P0 | Authenticated decision evidence | source/custody readback or synthetic test |
| 029 | 2 | P0 | Remote exact readback | source/custody readback or synthetic test |
| 030 | 2 | P0 | Custody state machine | source/custody readback or synthetic test |
| 031 | 3 | P0 | Full exact-manuscript qualification | paragraph-level reviewer record |
| 032 | 3 | P0 | Independent narrative dimensions | paragraph-level reviewer record |
| 033 | 3 | P0 | Paragraph-level issue record | paragraph-level reviewer record |
| 034 | 3 | P0 | Executive-to-receiver story arc | paragraph-level reviewer record |
| 035 | 3 | P0 | Campus scale as proposal | paragraph-level reviewer record |
| 036 | 3 | P0 | Human purpose before effects | paragraph-level reviewer record |
| 037 | 3 | P0 | Proposal not contract/construction | paragraph-level reviewer record |
| 038 | 3 | P0 | Nonrepetitive agent mirrors | paragraph-level reviewer record |
| 039 | 3 | P0 | Picard/Data pedagogical placement | paragraph-level reviewer record |
| 040 | 3 | P0 | Execution between authorization and review | paragraph-level reviewer record |
| 041 | 3 | P0 | Distinct RQ and governed ops | paragraph-level reviewer record |
| 042 | 3 | P0 | RQ definitions source lock | paragraph-level reviewer record |
| 043 | 3 | P0 | Investigation does not authorize effects | paragraph-level reviewer record |
| 044 | 3 | P0 | Blocking operational controls | paragraph-level reviewer record |
| 045 | 3 | P0 | Full oral read-through | paragraph-level reviewer record |
| 046 | 4 | P0 | Episode Zero medium decision | medium + separate visual approval |
| 047 | 4 | P0 | Episode/target medium scope | medium + separate visual approval |
| 048 | 4 | P0 | Standalone ART layer purity | medium + separate visual approval |
| 049 | 4 | P0 | Preserve mixed P001A candidate | medium + separate visual approval |
| 050 | 4 | P0 | Source-traceable original art | medium + separate visual approval |
| 051 | 4 | P0 | Separate logo/text from art | medium + separate visual approval |
| 052 | 4 | P0 | Art hashes/crop/scale | medium + separate visual approval |
| 053 | 4 | P0 | Inspect anatomy/perspective | medium + separate visual approval |
| 054 | 4 | P0 | Proposed-campus claim guard | medium + separate visual approval |
| 055 | 4 | P0 | Human ART before STORY | medium + separate visual approval |
| 056 | 4 | P0 | Independent causal STORY | medium + separate visual approval |
| 057 | 4 | P0 | P001A purpose-to-proposal story | medium + separate visual approval |
| 058 | 4 | P0 | No duplicate ART or slide text | medium + separate visual approval |
| 059 | 4 | P0 | Hidden-label story test | medium + separate visual approval |
| 060 | 4 | P0 | Two matching approvals before composition | medium + separate visual approval |
| 061 | 5 | P0 | Opener/closer gates | browser/PDF/native-text evidence |
| 062 | 5 | P0 | Seven established layouts only | browser/PDF/native-text evidence |
| 063 | 5 | P0 | Exact source+layer composition bind | browser/PDF/native-text evidence |
| 064 | 5 | P0 | React/Tailwind authoritative | browser/PDF/native-text evidence |
| 065 | 5 | P0 | Selectable native HTML text | browser/PDF/native-text evidence |
| 066 | 5 | P0 | Exact narration reproduction | browser/PDF/native-text evidence |
| 067 | 5 | P0 | Fresh segmentation after qualification | browser/PDF/native-text evidence |
| 068 | 5 | P0 | Sentence-boundary exact reconstruction | browser/PDF/native-text evidence |
| 069 | 5 | P1 | 1–4 columns by legibility | browser/PDF/native-text evidence |
| 070 | 5 | P1 | Measure overflow/read order | browser/PDF/native-text evidence |
| 071 | 5 | P1 | Slide/web/print profile separation | browser/PDF/native-text evidence |
| 072 | 5 | P1 | Protect crop/text zones | browser/PDF/native-text evidence |
| 073 | 5 | P1 | Real browser inspect | browser/PDF/native-text evidence |
| 074 | 5 | P1 | PDF selection/parity | browser/PDF/native-text evidence |
| 075 | 5 | P1 | Destination edit-save-reopen test | browser/PDF/native-text evidence |
| 076 | 6 | P0 | Dependency graph | least-privilege runtime/negative test |
| 077 | 6 | P0 | Skills are instructions not authorization | least-privilege runtime/negative test |
| 078 | 6 | P1 | Versioned skill change rationale | least-privilege runtime/negative test |
| 079 | 6 | P0 | Synthetic tests before real source | least-privilege runtime/negative test |
| 080 | 6 | P0 | Missing content/metadata negative tests | least-privilege runtime/negative test |
| 081 | 6 | P0 | Manual dispatch for consequential work | least-privilege runtime/negative test |
| 082 | 6 | P0 | No auto hash-triggered production | least-privilege runtime/negative test |
| 083 | 6 | P0 | Least-privilege credentials | least-privilege runtime/negative test |
| 084 | 6 | P0 | Public code/private source isolation | least-privilege runtime/negative test |
| 085 | 6 | P0 | Secret/reference isolation | least-privilege runtime/negative test |
| 086 | 6 | P1 | Pinned workflows/dependency inventory | least-privilege runtime/negative test |
| 087 | 6 | P1 | Inspect real VTracer runs | least-privilege runtime/negative test |
| 088 | 6 | P0 | Idempotent external retries | least-privilege runtime/negative test |
| 089 | 6 | P1 | Containment vs compensation | least-privilege runtime/negative test |
| 090 | 6 | P0 | Separate deployment/payments/releases | least-privilege runtime/negative test |
| 091 | 7 | P0 | Evidence state schema | independent evidence + retrospective |
| 092 | 7 | P1 | Separate test dimensions | independent evidence + retrospective |
| 093 | 7 | P1 | Exact readback receipts | independent evidence + retrospective |
| 094 | 7 | P1 | Negative action/source tests | independent evidence + retrospective |
| 095 | 7 | P0 | Approval replay/expiry/scope tests | independent evidence + retrospective |
| 096 | 7 | P1 | Retrieval/corruption fault injection | independent evidence + retrospective |
| 097 | 7 | P1 | Paragraph findings lifecycle | independent evidence + retrospective |
| 098 | 7 | P1 | ART/STORY defect categories | independent evidence + retrospective |
| 099 | 7 | P1 | Text/PDF metrics non-aesthetic | independent evidence + retrospective |
| 100 | 7 | P0 | Configured/dispatched/completed/accepted states | independent evidence + retrospective |
| 101 | 7 | P0 | Controlled evidence index | independent evidence + retrospective |
| 102 | 7 | P1 | Qualified independent reproduction | independent evidence + retrospective |
| 103 | 7 | P1 | Audit permissions/triggers | independent evidence + retrospective |
| 104 | 7 | P1 | Versioned retrospective | independent evidence + retrospective |
| 105 | 7 | P2 | P0 then P1 then P2 ordering | independent evidence + retrospective |

## Implementation states and verification boundary

- **Registered:** 105/105 requirements are catalogued here as proposed controls; this does not imply 105 operational implementations.
- **Automated synthetic gate:** `tools/boss105/validate.mjs` and `tools/boss105/test.mjs` are separately scoped; consult their own test results before claiming PASS.
- **Human-dependent:** actual source admission, narrative qualification, visual selection, custody readback, authenticated ledger, browser/PDF fidelity, external editability and release remain `NOT_TESTED` until evidenced.
- **Conflicts:** Episode Zero's provided photographic campus references are an owner-supplied visual direction; Episode 01's separate illustration-only policy remains untouched. A target-scoped medium gate is required, never silent global replacement.
- **Source mismatch:** the reported `APPROVED-EDITORIAL-001` historical commit could not be retrieved during an earlier connector check. Do not use its digest or text as live-verified until authenticated readback succeeds.

## Skill dependency order

`SOURCE_ADMISSION → STORY_ARCHITECT_BRIDGE1 → VISUAL_STORYBOARD_BRIDGE2 + MEDIUM_GATE → ART_ISOLATION → HUMAN_ART → STORY_ISOLATION → HUMAN_STORY → (OPENER+CLOSER) → EDITORIAL_LAYOUT → REACT/HTML_COMPOSITION → BROWSER+PDF+ADAPTER_QA → HUMAN_RELEASE`

Narrative planning occurs before ART; dependent STORY visual production occurs only after ART approval. A preapproval layout zoning study is not a composed slide. Execution is strictly bounded by approval state.

## Per-item progress contract

A future evidence index must carry `{id, owner, existing_path, enforcement_path, implementation_state, synthetic_test_ref, integration_test_ref, human_decision_ref, unresolved_hold}` for each of the 105 items. Until those entries are verified, no blanket claim that 'all 105 upgrades are complete' is permitted.

