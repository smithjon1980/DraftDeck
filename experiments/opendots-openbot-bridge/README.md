# BOSS / OpenDots + OpenBot enforced bridge trial

**Status:** candidate. No production deployment, source mutation, human authorization, database addition or stack replacement.

This experiment exercises the **actual OpenDots `ComputerService.action`** with a custom synthetic transport adapter that invokes OpenBot's **unmodified, exact-pinned CEL `evaluateActionPolicy`** and **`decideAction` approval policy**. It uses SQLite solely for test decision evidence and a disposable single-use simulated approval ledger. No PostgreSQL, production access, model inference or unpublished BOSS text.

## What this does test

A real OpenDots request must cross the injected adapter before a mock computer receives it. Narrow read permission, denial of executable shell, blocked edits to `approved/`, no premature file writes, fail-closed audit insertion, expired and changed approvals, single-use grants, denial under scheduled initiators, concurrent denied actions and identity-token mismatches are covered.

A test-only signed approval permit is deliberately **NOT** evidence of real user session identity, human UI or remote access protection; production would require the app's signed identity context and audited decision semantics.

## Upstream admission

OpenBot commit `bd4dc94943a9d62aefd05e5e99073ba58919c9c6`, two exact modules hash-verified by Git; OpenDots commit `8091324942b86789ed0da7facbee855145d933b0`. Both MIT. Original modules are downloaded into an isolated runner checkout; test modules are injected there and discarded when CI finishes.

## Critical limitations

1. The bridge is **inside an injected transport fixture**. An OpenDots deployment still contains a direct route to its computer supervisor; tests here **cannot demonstrate** that a malicious process cannot bypass the new gateway. Production requires enforceable network isolation and removal of the direct path.
2. No real authenticated human session, browser takeover, Docker container or MCP system was exercised. No signed multi-user authorization has been proven.
3. A SQLite simulated one-time approval token is a **test prototype**, not a shipped OpenBot approval service. Runtime restart verification is limited to reopening its ledger and confirming a consumed permit stays consumed.
4. The BOSS evidence ledger needs custody, export, immutable retention and failure semantics beyond a standalone demo.
5. This is **not** approval to push any private Episode 01 narration into OpenDots.

**Qualified next steps:** permission gateway as mandatory egress path; deny direct computer requests at network layer; use signed real auth identity and OpenBot's full approval records; test lost network, duplicate delivery, concurrency and work resumption. Preserve GitHub Actions, Windmill, n8n, Railway and React as currently assigned.
