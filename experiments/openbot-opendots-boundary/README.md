# BOSS OpenBot + OpenDots — Cross-Governance Qualification

**Status:** Source integration feasibility PASS. Production deployment HOLD.  
**Decision date:** 2026-10-23. **PostgreSQL is not an active acceptance gate.**

## Purpose
Use OpenDots as a candidate BOSS operator interface and OpenBot's policy decision engine as a candidate controlled-execution boundary. Evaluate exact action authorization and attempts to bypass it with synthetic BOSS actions. Keep existing React/Tailwind, GitHub Actions, Windmill, n8n and Railway workflows intact. Do not ingest unpublished Episode 01 narration, company credentials or external accounts.

## Source admission
- OpenBot: `CopilotKit/OpenBot@bd4dc94943a9d62aefd05e5e99073ba58919c9c6`
- OpenDots: `CopilotKit/OpenDots@8091324942b86789ed0da7facbee855145d933b0`
- Both MIT-licensed. Original sources are pinned in disposable CI; OpenBot's CEL policy file is fetched with **Git blob-hash verification** and is unchanged. Local synthetic tests are injected only into ephemeral checkouts.

## Verified latest standalone results
- **OpenBot source policy through real OpenDots ComputerService: 7 / 7 PASS** using an injected test-only computer transport and OpenBot's exact `evaluateActionPolicy` implementation. No PostgreSQL, models or live browser:
  1. Exactly scoped JSX candidate write passes policy and produces recorded synthetic execution.
  2. Protected approved-manuscript write is refused even when OpenDots file permission is enabled.
  3. Shell action is refused even when OpenDots shell permission is enabled.
  4. Broken CEL deny rule is refused, not silently allowed.
  5. Audit insertion failure prevents forwarding the synthetic computer action.
  6. 25 concurrent protected write attempts all refused and produced 25 gate refusal decisions.
  7. **Unmediated path diagnostic:** The native OpenDots `ComputerService`, when granted file permission and connected directly to a mock computer with **no BOSS/OpenBot gate**, forwarded a protected write. That demonstrates the structural bypass risk, not a live compromise.
- OpenDots complete native tests: previously **348/348 PASS**, including the synthetic 150-denial burst and persisted SQLite inspection. Native React/Vite build/typecheck PASS.
- OpenBot agent-computer native safety tests: previously **139/139 PASS** (319 assertions).
- An earlier separate trial performed **172/172 passing native OpenBot PostgreSQL tests** and **74/74 passing gateway tests including three injected failure/burst cases**. These are historical evidence, **not required to adopt a database or repeat DB testing**. Do not sum repeated test subsets.

**CI evidence for active database-free cross-policy test:** [run 40043138396](https://github.com/smithjon1980/DraftDeck/actions/runs/40043138396).

## Architectural conclusion
The actual OpenDots `computerTools` call `ComputerService.action`, which enforces OpenDots's own persisted permission switches. Its default integration with OpenBot computer/supervisor does **not** automatically pass through OpenBot's **server-level CEL gateway** or centralized audit. A BOSS policy adapter can mediate a request in a test harness, but the unmediated direct path remains allowed if network/server configuration permits it.

**No single BOSS enforcement boundary exists yet.** The test-only mediation prototype proves feasibility, not irreversibility. A policy restriction stored in instructions or UI is inadequate if a computer endpoint remains directly reachable.

## Next gates — storage technology neutral
1. Remove **all direct OpenDots-to-computer paths** other than the BOSS-governed gateway, proven using network deny/allow tests in a disposable runtime.
2. Resolve signed human identity, Dot identity and initiator independently of caller-supplied headers. Do not trust `x-openbot-bot-id` alone.
3. Enforce exact payload/target hash and authenticated approval once per high-impact action, with expiration, denial and replay controls. Test retries and restarts.
4. Append a complete, reconstructable evidence receipt **before** execution, and refuse execution if that append fails. The backend may be file/SQLite/other selected storage—**PostgreSQL is not a prerequisite**. The 50-item OpenDots activity window must not substitute for a complete custody archive.
5. Test prompt-injection, shell/network egress, tenant cross-access and credential exposure in isolated disposable containers.
6. Compare integration cost and maintenance to current BOSS workflows; obtain separate human authorization before deploying or merging.

**Human governance:** build candidate / inspect evidence / request approval / authorize release remain different states. Source-passing tests do not authorize production. No user-owned production resources were changed.
