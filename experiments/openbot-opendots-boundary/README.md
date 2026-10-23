# BOSS OpenBot + OpenDots — isolated boundary and persistence stress trial

**Source status:** candidate, no adoption, no external account access. This does not replace React/Tailwind, Windmill, n8n, Railway, GitHub Actions, existing custody, or human release gates.

## What the two programs actually share
OpenDots documents reuse of OpenBot's **computer image/supervisor**. But its `src/server/computer-tools.ts` invokes `ComputerService.action` inside OpenDots directly, which applies **OpenDots per-Dot permissions and audit**. Reusing OpenBot's container supervisor **does not automatically run OpenBot's server/src/computer/policy.ts CEL policy or PostgreSQL audit gateway**. This is a strict cross-product governance qualification blocker until independently connected and tested.

## Pinned source
- OpenBot: `CopilotKit/OpenBot@bd4dc94943a9d62aefd05e5e99073ba58919c9c6` (MIT)
- OpenDots: `CopilotKit/OpenDots@8091324942b86789ed0da7facbee855145d933b0` (MIT)
- Their source, licensing and README assertions are upstream; evaluation is not an endorsement or guarantee.

## Jobs
1. **OpenBot real PostgreSQL**: ephemeral pgvector PostgreSQL 17; upstream production migrator; native integration tests of persisted deny policies, human approvals, audit pagination/retention, snapshots, replica session guards, work queue, publication, and MCP permission revocation. Test data only.
2. **OpenDots React + workspace**: Node 24, `npm ci`, TypeScript typecheck, production UI/server build, and selected native Vitest suites for browser permissions, computer routes, approval-before-save, duplicate prevention, page integrity, scheduled research revocation, runtime isolation, security and shutdown.
3. **Cross-product architecture gate:** explicitly mark automatic shared authorization/audit between OpenDots -> OpenBot server as **NOT ESTABLISHED**; cannot be promoted on either suite passing.

## Operating limits / ethics
- No API keys, private manuscript, live GitHub mutating tokens, payment provider, Slack, phone, email or consumer data.
- No OpenBot/OpenDots services deployed publicly or installed on current BOSS infrastructure.
- No external network browsing by agents; code fetch and dependency installation only in CI.
- No user authorization to publish. PASS of test suites only qualifies corresponding behavior under those test environments.
- Automated test results must not be confused with security proof: Docker runtime isolation, hostile websites, LLM prompt injection and real human approval remain separate tests.
- OpenDots default containers share the host kernel and the project documents no restrictive egress policy by default: avoid giving shells/network credentials to untrusted sessions without additional isolation.

## Future integration authorization gates
- Route **all write and release actions** through one server-side audited permission gateway with explicit actor + initiator identity.
- Record audit intent **before execution** using a real persistent DB, fail closed if the record cannot be written.
- Human approval must bind to exact action digest and fail closed on modified payload/replay.
- Test process restart with pending requests, duplicate tool calls, 2+ tenant users, secret leakage, prompt injection and egress denial.
- Benchmark resource use and maintenance vs BOSS existing orchestration stack.
- Owner must approve exact version and production deployment separately.

Current decision: **controlled trial only**.
