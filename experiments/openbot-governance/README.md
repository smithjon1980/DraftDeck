# OpenBot governance isolated evaluation — public synthetic pilot

**Status:** ISOLATED EVALUATION CANDIDATE; NOT deployed or integrated into production.

## Question

Can OpenBot's original policy engine and gateway tests support BOSS's principle that tools may prepare evidence and draft candidates but must not silently rewrite approved narration or publish work?

## Real source / identity

- Upstream repository: https://github.com/CopilotKit/OpenBot
- Immutable upstream source commit: `bd4dc94943a9d62aefd05e5e99073ba58919c9c6`.
- Bun runtime: `1.4.3`. The workflow checks out upstream at that SHA and copies a **synthetic only** BOSS-owned test into `server/tests/`.
- The test imports `../src/computer/policy` from the real upstream source. It does not reimplement CEL or simulate policy decisions.
- Separate upstream tests: `computer-policy.test.ts`, `computer-gateway.test.ts`, and `approvals-policy.test.ts`.

## Test contract

Positive actions: read permitted mock source and write a mock `candidates/slide-02.html`.

Required refusals: approved manuscript path write; release-path write; unknown path; shell; any external MCP write; scheduled routine candidate write; null policy; malformed denial; overbroad allow; actor label spoof.

Special trap: In `dry-run` mode an action denied by policy is **still forwarded**. BOSS must use `enforce`, never `dry-run`, at production authorization boundaries.

## Known boundaries — do not claim to have solved

1. A CEL path policy cannot prove **exact bytes** inside an allowed candidate document. BOSS's source-hash and React manuscript checker remain necessary and independent.
2. Policy checks alone do not prove a real person authorized a protected operation. Upstream approval tests are exercised separately; a future end-to-end user-approval integration is not part of this pilot.
3. The gateway/audit regressions are upstream mock tests, not evidence of a running PostgreSQL-backed service with real credentials or production hooks.
4. Synthetic shell and MCP calls do not execute real tools. This is deliberate: preserve existing GitHub Actions / Windmill / n8n / LiveKit / React production stack.
5. OpenBot is alpha and needs a separate runtime, infrastructure, identity, model/CopilotKit dependencies and a reviewed configuration before pilot deployment.
6. This PR is a *candidate review branch*. Do not merge based on the test alone; no OpenBot tenant, secrets, Docker stack or production permissions are created.

## Evidence requirements

Required: pinned commit, 13 BOSS policy assertions, upstream gateway/refusal/audit and approvals tests, test logs, explicit run conclusion. Any failing or skipped critical test causes **HOLD**.

**Release decision:** HOLD until a separate sandbox installation proves runtime isolation, owner-controlled approval, audit persistence, and credential boundaries. OpenDots remains out of scope.
