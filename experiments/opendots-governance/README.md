# OpenDots governance stress test — BOSS V4
Status: CANDIDATE; non-production.
Pinned OpenDots: `8091324942b86789ed0da7facbee855145d933b0`.
OpenBot previously tested at a separate pinned SHA in PR #93. The two products are NOT integrated by this PR.

## Objective
Run the real OpenDots codebase's security/permission, approval/revision and concurrency regressions against an immutable upstream source checkout. No production connections, model configuration, secrets, database, Docker socket, or deployments.

## Interpretive boundaries
A green run establishes only that the chosen upstream regressions passed on that commit in GitHub Actions. It does not establish reliable operator authorization, durable cross-service audit, replay prevention, hostile prompt robustness, or a full OpenBot–OpenDots execution boundary.
A red or skipped critical test is HOLD.
Even on green: production integration is HOLD.

## Required later live sandbox evaluation (separate, explicitly reviewed)
- Replay approval tokens; actor/origin spoofing; cross-Space and cross-Dot credential misuse
- Interrupted and conflicting approvals; approval cancellation after request dispatch
- Stale document revisions; changed payload after preview; exact approved source bytes
- Gateway refusal with no forwarding; persistent audit failure; denial bypass through browser/shell/MCP
- Reboots, network partitions, late-running actions, simultaneous requests
- Independent human authorization before any publication or protected asset rewrite

## Evidence
CI logs and SHA/status artifact. Human review required. Preserve current GitHub Actions/Windmill/n8n/Railway/LiveKit stack.
