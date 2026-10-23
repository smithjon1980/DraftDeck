# OpenBot governance pilot — synthetic BOSS slide-production actions

**Scope:** isolated source-level exercise of OpenBot's authentic `evaluateActionPolicy` and `decideAction` functions. No OpenBot service, database, browser computer, agent, model, or production BOSS application is installed by this pilot.

## Source admission
- Upstream: `https://github.com/CopilotKit/OpenBot` (MIT license).
- Full upstream pinned commit: `bd4dc94943a9d62aefd05e5e99073ba58919c9c6`.
- Exactly fetched at job execution, validated with native Git blob hashes:
  - `server/src/computer/policy.ts`: `94bc46ad3a74bdb56ad84f86527057ecba6c735e`
  - `server/src/approvals/policy.ts`: `56606eeda7f58fbac7f9ba29806c31c4e4118314`
- Source is unmodified in the test job; it is not vendored into DraftDeck or used for production.

## Pilot boundaries
- BOSS skills/React/Tailwind, GitHub Actions, Windmill, n8n, Railway, source custody and release workflow remain unchanged.
- No production credentials, approved manuscript, unpublished media, payment tools, model endpoints, or external write actions.
- Only synthetic source IDs, filenames and business metadata.
- Permission policy has `mode: enforce`, narrow allowlist and explicit denies for shell, navigation, GUI activation, external MCP writes, protected files, and scheduled writes.
- Separate OpenBot approval-decision rules require human approval or handoff for consequential actions.
- Includes a **negative demonstration** proving `dry-run` forwards denied actions; it must never be confused with protection.
- CI only writes public-safe JSON evidence to a temporary runner and saves a short-lived action artifact.

## Not tested (explicit HOLD)
- Server gateway path and pre-execution PostgreSQL audit row (needs isolated OpenBot server + test DB and a mocked computer).
- Browser snapshots/resolved targets versus malicious caller labels; browser-click/Enter bypass in actual browser.
- Live persistence/recovery, replay/idempotent tool actions, restart behavior or actual human approval UI.
- Full integration overhead, uptime, CopilotKit Intelligence license, model credentials, and production security.
- Real slide rendering or deployment.
- OpenDots, which remains deferred until operator workspace requirements justify it.

## Proposed admission gates
1. Exact upstream source and license audit, fail-closed policy decisions (this pilot).
2. Gateway + database audit ordering under injected failure in a disposable environment.
3. Human-approval round trip, refusals and idempotent retries across restarts.
4. Cost/maintenance comparison against existing Windmill/GitHub Actions approach.
5. Human inspection and separate adoption authorization. A green test does not install or authorize OpenBot.

**No changes to current stack or Episode 01 narration.**
