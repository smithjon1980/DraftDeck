# e2e browser parity — disposable BOSS experiment

**Candidate only. No production replacement, no private data.** A tiny synthetic fixture tests native headline editing across reload, intact SVG geometry and an explicitly denied unauthenticated UI approval. This is **not** the actual DraftDeck slide editor or a real approval gateway. A UI denial does not establish server-side enforcement.

The isolated trial uses TesterArmy's e2e framework on top of Playwright and no model calls. Upstream docs: https://e2e.tester.army/docs/quickstart . Run from this folder using Node >= 22.22.3 or Node >=24.8:

```bash
npm install
E2E_TELEMETRY_DISABLED=1 npx e2e run
```

Do not run `npx e2e init` in the repository root. No deploy, merge, external writes, model credentials or live system calls are permitted. The package versions are provisional and must be resolved and locked by the CI pilot; a failing install is NOT a test pass.

**Qualification:** confirm dependency install; run tests; introduce one intentional editability failure and require detection; inspect screenshots/traces; compare to a same-scenario existing Playwright baseline. Only after that evaluate an authenticated agent-act trial and cache replay using synthetic data. Current state: SOURCE PREPARED, EXECUTION NOT VERIFIED, PRODUCTION HOLD.
