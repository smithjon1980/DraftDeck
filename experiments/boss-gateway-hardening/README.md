# BOSS V4 gateway hardening — candidate / NO production integration
This independently reproduces the direct-route vulnerability from merged PR #96 and tests a proposed outbound transport authorization boundary using the real pinned OpenDots ComputerService/agent tools and the original pinned OpenBot CEL policy evaluator. No database server, real tools, user data, credentials, deployments, or change to existing Windmill/n8n/Railway/LiveKit/React stacks.

PASS of the governed mock transport **does not mean the real bypass has been closed**. The negative control MUST still reproduce direct bypass (a passing NEGATIVE CONTROL is evidence of an unclosed vulnerability). This evaluates a design boundary only.

### Gate for subsequent acceptance
Production: HOLD until the actual OpenDots application / gateway is modified so every outbound action is irrevocably routed through a trusted OpenBot/BOSS authorization service; separate process credentials/network ACLs exclude direct computer transport. Prove signature and actor binding through a real human UI, durable denial/authorization ledger across restart, concurrency, cancellation races, upstream browser/MCP access, and independent review. No agent may mint a human approval or self-authorize a protected write. Do not merge this isolated testing candidate without reviewing CI results.
