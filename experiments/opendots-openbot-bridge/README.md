# BOSS OpenDots + OpenBot — direct bridge qualification (October 23, 2026)

**Status: TEST HARNESS QUALIFIED / UNMEDIATED DIRECT PATH CONFIRMED / DEPLOYMENT HOLD.**
This is an experimental bridge, **not a production modification**.

## Execution and source evidence

- **21/21 Vitest cases PASSED** in the verified [GitHub Actions run #40043606600](https://github.com/smithjon1980/DraftDeck/actions/runs/40043606600).
- DraftDeck ontology guard PASSED on the same commit.
- Actual OpenDots `ComputerService` and `computerTools` modules, not a rewritten agent tool facade.
- Real OpenBot upstream CEL `evaluateActionPolicy` and approval `decideAction` modules copied unchanged into disposable OpenDots checkout and hash verified:
  - `server/src/computer/policy.ts`: Git blob `94bc46ad3a74bdb56ad84f86527057ecba6c735e`.
  - `server/src/approvals/policy.ts`: Git blob `56606eeda7f58fbac7f9ba29806c31c4e4118314`.
- Pinned OpenBot commit `bd4dc94943a9d62aefd05e5e99073ba58919c9c6`; pinned OpenDots commit `8091324942b86789ed0da7facbee855145d933b0`.
- No PostgreSQL, production database, personal accounts, private manuscript, model provider, actual email or remote browser. A disposable **SQLite** approval/evidence ledger is used only by the test harness.

## What passes through the bridge

- Real OpenDots agent tool entrypoint `computer_files_read` -> OpenDots ComputerService -> BOSS synthetic transport -> original OpenBot CEL policy -> original approval decision -> simulated computer. Read allowed and logged before execution.
- Real OpenDots `computer_exec` is stopped by OpenBot policy even if OpenDots shell permission is enabled.
- Protected `approved/` manuscript mutation blocked; exact candidate file writes demand explicit human approval.
- Prototype test-only signed, hash-bound, expiring approval consumed exactly once; changed payload, expired approval, forged identity and replay rejected. The consumed record persists on reopening the SQLite ledger.
- Scheduled/unattended writes refused even when a signature exists. A simulated audit insertion failure stops dispatch.
- 75 concurrent denied shell attempts create 75 evidence rows with **zero mock computer calls**.
- Browser Enter-activation path refused; malicious contents do not gain authority; missing, dry-run or broken CEL policy fails closed.
- Policy is reevaluated on every action: mid-session revocation blocks subsequent reads; per-Dot HMAC token mismatch is rejected by the bridge.

## Important **confirmed bypass** (negative control)

One test deliberately uses **unmodified OpenDots ComputerService with a direct transport**, no bridge. Although the *separate OpenBot policy* would deny a write to `approved/ep01.md`, OpenDots' own permissions are enabled and the direct mock computer receives that write.

**Result: BYPASS PATH REPRODUCED.** The test is GREEN because it is a negative-control assertion that correctly detected a design gap. It is **not** an authorization PASS. Without a mandatory enforced network topology, simply placing an optional adapter between OpenDots and OpenBot does not make all executions subject to BOSS governance.

## Necessary further qualifications (HOLD)

1. Replace injectable bridge with a **mandatory authenticated network gateway**; restrict computers and supervisor to accept requests **only from that gateway**. Deliberately try a direct service-to-computer request and require a hard network-level refusal.
2. Bind authorization to a real server-side authenticated person, roles and signed run initiator. The synthetic `HUMAN` key in the harness is not a real authentication mechanism.
3. Replace prototype SQLite approval with audited, durable production-grade single-use action approvals. Verify process-kill/restart, 2+ users, and actual incomplete side-effect recovery.
4. Browser/terminal/egress hostile-input tests in disposable containers, not mocks, and maintain redacted complete evidence custody.
5. Do not treat passing a CI test suite as human release authorization; compare overhead against GitHub Actions, Windmill, n8n and Railway.

The current BOSS production stack, unpublished Episode 01 materials and GitHub `main` remain unchanged. The PR is a draft review candidate.
