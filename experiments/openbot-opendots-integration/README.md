# BOSS OpenDots → OpenBot policy integration: synthetic proof and bypass finding

**Test status: 6/6 PASS** — [workflow](https://github.com/smithjon1980/DraftDeck/actions/runs/40045864025)  
**Upstream OpenDots pinned:** `8091324942b86789ed0da7facbee855145d933b0`.  
**Upstream OpenBot pinned:** `bd4dc94943a9d62aefd05e5e99073ba58919c9c6`.  
**Configuration:** Node 24, actual OpenDots `ComputerService.action`, actual unmodified OpenBot CEL `evaluateActionPolicy`, synthetic HTTP transport with an optional injected gate. No PostgreSQL, external credentials, account access, live container, private narration or production deployment.

## What passed
1. OpenDots permitted synthetic source read evaluated by real OpenBot policy.
2. Protected narration write refused by OpenBot despite OpenDots allowing file actions.
3. Exactly scoped candidate JSX write permitted and audited by OpenDots.
4. Synthetic gateway audit failure refused before downstream mock dispatch.
5. **Bypass discovery:** unmodified OpenDots without the injected gate forwarded a protected file write when its own files permission was enabled.
6. Unlisted write default-denied when gateway was applied.

## Real distinction
The injected OpenBot CEL evaluator is a **test-only transport wrapper**. It was not integrated into OpenDots' deployment or OpenBot's real server gateway. OpenDots currently talks to the computer service using its own `ComputerService` and per-Dot permissions; reuse of OpenBot's computer supervisor does not automatically route through OpenBot's server-side policy.

The bypass test deliberately expects the ungoverned protected write to forward. Its PASS is **evidence of an integration vulnerability/gap in the proposed BOSS topology**, not evidence that this topology is safe.

The synthetic audit gate is implemented inside the mock transport, not persisted to an immutable ledger; it cannot establish database or system-level guarantees.

## BOSS acceptance decision
**Integration feasibility PASS. Production-authoritative governance HOLD.**

For actual BOSS deployment:
- Physically route all OpenDots computer/MCP writes through a single audited server-side authority.
- Restrict network routes so the OpenDots app cannot reach direct computer/action endpoints except through the authority. UI toggles and model instructions are insufficient.
- Bind human approvals to exact action and actor; validate against replay/changed payload.
- Verify default-deny, approval-required, failure and retry behavior under process restarts.
- Preserve existing GitHub Actions/Windmill/n8n/Railway stack until a deliberately authorized change.

No production system modified and no existing approvals superseded.
