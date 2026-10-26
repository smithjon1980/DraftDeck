# BOSS e2e agent and replay benchmark — candidate

This is a **synthetic** fixture benchmark, not a production policy test. No secrets, customer data, deployment, or production mutations.

## Comparison method
Use the same fixed synthetic fixture and viewport for all stages:
1. Playwright deterministic baseline: three repeats, record wall-clock elapsed and count of model calls (zero).
2. e2e live cold run: `--no-cache` with an explicitly authorized test model; capture model calls, elapsed time, observed assertions.
3. e2e cache creation: read-write run with a passing locator assertion; preserve the same cache directory.
4. e2e warm replay: run unchanged against the same cache, capture cache replay/missed/handed-off and model calls.
5. UI drift: change the button label in a temporary fixture copy; test strict-cache replay expecting REPLAY_STALE, then (only with model authorization) test live agent handoff and re-recording.
6. Failure detection: mutate DENIED to APPROVED WITHOUT AUTHORITY; tests must fail at the assertion, not by setup errors.

## Measurements
Record run ID and source SHA, e2e/package version, model/provider, cache mode, total model calls and tokens from e2e summary, elapsed seconds, passes/fails, reason/error code, cache replay/handoff/miss, and replay artifact digest. Compare medians across three repeats, not unlike conditions. Keep stable test id, instructions, model and viewport between cold/replay. Verify generated recordings before sharing.

## Acceptance boundary
Do not assert agentic parity or replacement of Playwright until actual live agent run, cache creation, zero-model-call warm replay, drift failure, and mutation detection are evidenced by logs. GitHub CI without configured model provider should mark the agentic trial **NOT RUN**, not passed. No credentials placed in repository.
