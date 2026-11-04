# BOSS — Low-cost model qualification for OpenHands

Status: OWNER APPROVED PROCEED WITH $5 MODEL + $5 VM TRIAL / PROVIDER ACCOUNT NOT CONNECTED / NO SPEND / NO AGENT EXECUTION
Date: 2026-11-04
Scope: experiment/editorial-agent-remix-qualification only

## Decision
Start with a low-cost hosted Qwen-family model through a provider's OpenAI-compatible API, conditional on confirmed model ID, tool calling, context window, and OpenHands compatibility. Compare with a stronger model only if the first model fails. This is a cost-first test, not a claim that Qwen passes editorial quality.

## Verified public price references (check again before purchase)
- Fireworks Qwen3 Coder 480B A35B Instruct: $0.45 / 1M input; $1.80 / 1M output. https://fireworks.ai/models?providers=Qwen
- Together Qwen3.7 Plus: $0.32 / 1M input; $1.28 / 1M output. https://www.together.ai/pricing
These are different models; price is not evidence of equivalent quality.
- OpenHands provider configuration and tool-use limitations: https://github.com/OpenHands/docs/blob/main/openhands/usage/llms/llms.mdx

## Test controls
1. Owner approved proceeding with the proposed $10 trial ceiling on 2026-11-04. This authorizes preparation and a bounded trial only after account access, an enforceable cap and provider-specific charge confirmation. No unlimited spend, new long-running server, or production access.
2. Configure a provider account with a hard usage cap where available, otherwise an enforceable proxy cap; never commit keys or screenshots of keys.
3. Approved trial ceiling: $5 model usage and $5 VM usage. A soft billing alert alone is not a hard cap; if provider cannot enforce a limit, stop before paid execution and request a separate bounded mechanism.
4. Verify provider endpoint and exact model ID using authenticated, read-only model listing; do not guess.
5. Verify OpenHands runtime isolation and permissions before repository access. GitHub default read-only; experimental branch PR only.
6. Stage five exact reference images privately with provenance and SHA-256; do not publish their binaries.
7. Smoke test a fictional placeholder React component, then run the three-layout comparison only after evidence gates pass.
8. Record input/output tokens, billable cost, VM runtime, tool errors, source diff, 1920x1080 browser screenshots, visual deviations, and human decision.

## Status
- Pricing comparison: RESEARCHED (not a vendor quote)
- Provider choice: Together AI first, subject to exact model/API compatibility and enforceable spend limit; OWNER APPROVED TRIAL CEILING
- Provider account and spend cap: NOT VERIFIED
- API model authentication: NOT VERIFIED
- OpenHands host: NOT PROVISIONED
- Five reference binary staging: NOT VERIFIED
- Agent execution: NOT RUN
- Production deployment: PROHIBITED
