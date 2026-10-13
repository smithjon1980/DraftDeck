# BOSS Agent Swarm 001 — Deterministic Control Plane
**Status: CANDIDATE / MOCK WORKERS / NO MODEL INVOCATIONS / NO REAL BUILD / NO PERSISTENT STORAGE**.

Open-source LangGraph JS graph with conditional routing and isolated worker functions. Each request selects one branch: `instructional_pdf` (design → PDF), `vector_asset` (vector), or `research_report` (research). All branches pass through independent verification, bounded repair (maximum 2 attempts), HOLD or delivery-pending status.

This **does not** yet create a PDF, launch AI agents, attest source authenticity, invoke REA, or produce a real persistent link. The `source_ref` check only validates presence, **not authenticity**. `DELIVERY_PENDING_STORAGE` is intentionally not `DELIVERED`.

## Running
In an isolated Node 22 environment, `npm install --ignore-scripts`, then `npm test` and `npm run demo`. Dependencies are unpinned until a lockfile is generated and reviewed. CI job verifies the graph executes. LangGraph remains the *sole* agent orchestrator; Puck, React, Sharp, Playwright and SeaweedFS remain single-purpose workers/tools, not additional orchestrators.

## Graduation criteria
1. Exact versions and license checks with dependency lockfile.
2. Pinned source manifest, authenticated source gate (L0), explicit run ID and durable state checkpoint.
3. Real page compilation and Playwright PDF QA; verified artifact hashes.
4. Real object storage writes, read-back and **stable** user link with retention/authorization policy.
5. Independent QA workers; no self-approval, blind replay, unbounded repair or repeated side effects.
6. Zone C human approval for release and capability grants.
No production promotion or end-user download link before these gates pass.
