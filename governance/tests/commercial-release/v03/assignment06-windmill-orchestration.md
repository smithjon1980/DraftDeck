# Assignment 06 — Windmill Orchestration Enforcement (NON-PRODUCTION)

Status: READY FOR MANUAL CONFIGURATION; LIVE RUNS NOT ESTABLISHED.
Source branch: `docs/boss-big-three-governance-20261010`
Source folder: `governance/tests/commercial-release/v03`

## Controls and observables
- A: fetch and integrity-check the pinned GitHub SHA and seven fixture files plus schema, gate, independent expectations. No credentials needed for public read-only retrieval. Abort on hash drift.
- B: JSON parse and draft-2020-12 schema validation. Invalid type (fixture 06 has numeric risk_tier) must terminate before policy evaluation.
- C: independently resolve evidence from a fixed test registry; invoke existing `gate.evaluate` only on schema-valid input; each `Hold` must propagate to terminal fail-closed outcome rather than be swallowed.
- D: prohibited fixtures must end with a terminal failed flow status, or an explicitly terminal recorded rejection, and **never** run the mock-release-marker writer. Make the mock writer a separate downstream node, not a log statement in the evaluator.
- E: golden-path fixture is only eligible for a **manual authenticated approval pause**. It must remain suspended during Assignment 06 (do not click resume). Confirm zero release-marker writes.
- Tests compare observed statuses against `expected_enforcement_outcomes.json` using a separate verifier after the runs. The expectations file must not be imported by the policy evaluator.
- Preserve Windmill run IDs, node statuses, timestamps, pseudonymous actor IDs where applicable, file hashes, failure errors, approval state, and mock-marker store contents.

## Implementation warning
Windmill may represent failure as a thrown exception or as a failed branch; classify `NODE_TERMINATED_*` only upon observing the actual platform terminal state and proof of absence of downstream execution. Do not claim that `gate.evaluate` alone verifies an authenticated approver. A Windmill suspension step might require a flow-specific approval configuration; use the supported built-in approval mechanism for the current Windmill version, verify it in UI, and do not simulate this step with a JSON boolean.

## Test-isolation contract
Use non-production workspace drafts only. No deploy, schedule, outbound webhook, real external write, credential setup, or release permissions. The mock marker may write *only* to a dedicated test fixture store if expressly approved; absent that authorization use the Windmill preview output as a simulated marker and report the reduced strength of evidence.

## Expected outcomes
Read `expected_enforcement_outcomes.json`. It defines 7 final states: 6 prohibited terminals and 1 approval suspension. All have `release_marker=false` within the unapproved experiment.

## Required Windmill execution report
`run_id`, `branch`, `pinned_commit`, `blob_hashes`, `fixture_name`, `schema_result`, `policy_disposition`, `observed_terminal_node`, `approval_suspended`, `mock_release_marker_count`, `comparison_to_manifest`, `trace_locations`, `unresolved`.

Distinguish: `SPEC_COMMITTED`, `WINDMILL_FLOW_CONFIGURED`, `WINDMILL_FLOW_EXECUTED`, `ORCHESTRATION_HALT_VERIFIED`, `AUTHORIZATION_VERIFIED`. Do not elevate one state to another without its own evidence.
