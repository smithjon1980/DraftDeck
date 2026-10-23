# OpenBot governance — isolated BOSS acceptance trial

**Evaluation status:** SOURCE-LEVEL POLICY + MOCKED GATEWAY PASS / LIVE INTEGRATION HOLD. No OpenBot service was installed, and the BOSS production stack remains unchanged.

## Upstream source custody
- Public MIT upstream: `https://github.com/CopilotKit/OpenBot`.
- Pinned source revision: `bd4dc94943a9d62aefd05e5e99073ba58919c9c6`.
- Direct BOSS decision tests download and Git-hash-verify OpenBot's **unmodified** policy module (`94bc46ad3a74bdb56ad84f86527057ecba6c735e`) and approval module (`56606eeda7f58fbac7f9ba29806c31c4e4118314`).
- Native gateway tests fetch the same exact repository commit in a disposable runner. The upstream source is not vendored into DraftDeck.

## Executed tests

**Stage A — BOSS synthetic decisions:** 22 / 22 PASS. Authoritative OpenBot functions `evaluateActionPolicy` and `decideAction` executed on synthetic BOSS actions. Scenarios include:
- Permitted public-source read and exactly scoped candidate JSX write.
- Denied protected narration edit, `.env`, shell, external MCP writes, browser Publish click and Enter activation.
- Scheduled candidate write refused, scheduled read permitted.
- Absent/broken policy fail closed, deny beats permissive allow, unknown tool denied.
- Dry-run **forwards refused actions** (documented unsafe mode), enforced denial stops forwarding.
- Merge requires team-level human handoff; unreviewed writes require approval; missing approval reviewer fails closed; payment safety is a human handoff.
- Team restrictions take precedence over a conflicting personal allow.

**Stage B — OpenBot original gateway and approval suite:** 101 / 101 PASS; 295 assertions. Runs `bun test server/tests/computer-gateway.test.ts server/tests/approvals-policy.test.ts` on the pinned original upstream repository. The suites use mocked computers and in-memory audit stores to test refused action forwarding, audit record generation for allowed/refused/failed operations, resolved browser target integrity, secret-content avoidance in audit payloads, approval decision semantics, stale browser snapshots and restart-like mock states.

Evidence: [GitHub Actions run 39980063035](https://github.com/smithjon1980/DraftDeck/actions/runs/39980063035). CI's native suites did **not** connect to a production PostgreSQL database.

## Constraints that matter before promotion
- **OpenBot's shipped configured policy is broadly permissive** (`deny: []`, `allow: ["true"]`); replace this for any BOSS deployment. An *absent* policy fails closed, but the upstream starter config is not absent.
- **Dry-run is not enforcement:** it forwards refused actions. Deploy `enforce` with narrow allowlists.
- `OPENBOT_SINGLE_USER` is a developer convenience, not a production identity/access model.
- A shell command's text filter is not a sandbox; the actual container/host isolation must be verified.
- The above results do not prove the real database transaction boundary, multi-tenant authentication, durable human approval, idempotency across restarts, per-agent container isolation, egress policy or full lifecycle security.
- CopilotKit Intelligence, Docker, Bun and model credentials add operating requirements; compare total cost and risk to continuing with GitHub Actions/Windmill.

## Next admission gate (separate authorization)
Run a **disposable integration** with only synthetic data and an actual PostgreSQL instance and isolated computer provider. Inject audit-write failure before forwarding and post-forward failure after allowed actions. Test a human-approval lifecycle, interrupted/retried action identifiers, browser target resolution, strict service credentials and network egress. Compare the result to the existing BOSS workflow. No live organization accounts.

**Disposition:** Governance source/policy candidate qualified for further evaluation; production adoption HOLD. OpenDots intentionally deferred. No change to approved Episode 01 narration or visual stack.
