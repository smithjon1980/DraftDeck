# BOSS e2e Subscription Runner — Candidate Handoff

**State:** prepared in source, NOT deployed. This plan uses no OpenAI API key. GitHub is the CI control/evidence plane, not the provider of the subscription credentials.

## 1. Persistent worker (human setup required)

Provision a dedicated Linux VM/host under an unprivileged `boss-e2e` operating-system account with persistent home storage. Install a GitHub self-hosted Actions runner as that account with exact labels `self-hosted`, `linux`, `x64`, `boss-e2e-subscription`. Do not attach this label to shared runners or public PR jobs. Limit repository access and disable untrusted workflows on this runner. Follow the official GitHub self-hosted runner documentation; install Node >=24.8, Python 3, and Chromium dependencies. Restrict egress as appropriate and keep the host patched.

No persistent worker is provisioned by this PR. Neither GitHub Actions nor the ChatGPT conversation automatically shares a subscription login with that worker.

## 2. Authenticate interactively — never paste tokens

On the worker **as the same unprivileged account that executes GitHub Actions**, change to `experiments/e2e-browser-parity-v01` after a trusted checkout, install dependencies, and run:

```bash
npm install
npx e2e login openai
npx e2e models
```

Complete the provider's supported interactive authorization flow. Inspect available model IDs and select an eligible ID with `BOSS_E2E_MODEL` set locally on the runner if the default is unavailable. Never copy `~/.config/e2e/oauth.json`, session tokens, browsers' profile data, or environment secrets into GitHub, Actions artifacts, logs, or PR comments. Limit file permissions (home 0700, credential files owner-only). Reauthenticate interactively when the subscription expires. Do not use cookies or undocumented token extraction. Subscription usage remains subject to the provider's plan limits and policies.

## 3. Trigger only from trusted main

Actions > BOSS e2e agent replay benchmark > Run workflow > branch `main` > enable_model_trial: true. The job can only run on `workflow_dispatch` on `main` and requires the dedicated runner label. PR events run hosted deterministic baseline only. No OPENAI_API_KEY repository secret is required.

Stages:
- `synthetic-baseline`: GitHub-hosted Playwright three repetitions, zero model calls by design.
- `subscription-agentic-trial`: test subscription accessibility, cold `--no-cache`, record `read-write` cache, strict replay, log timings and actions. Cache stays under the worker's persistent private HOME and is never uploaded.
- GitHub Actions records stage exit statuses and receives *synthetic-only* logs and metrics for inspection. A success **does not itself prove** zero replay model calls or complete reliability; inspect cache/model counts in reports.

## 4. Governance and hard limits

No production deployment, no live OpenBot policy write, no unpublished content, no real customer records, no credentials in test fixtures. Treat the cache as executable, trusted material: don't accept recordings from untrusted PRs; review action differences before accepting cache changes. Subscription files stay on the host and are not uploaded.

The present benchmark does not include UI-drift recovery or agentic mutation tests and cannot be used to claim these properties. It also does not yet produce a machine-verifiable summary of token/model-call counts; reviewers must examine observed reports. A later PR can add machine-readable evidence gates once formats are established.

## 5. Human acceptance checklist

Require: first cold test passes; a cache recording exists; strict warm replay passes and reports replayed actions; explicit observed model calls from logs; stable model/config/test id; baseline timings; failure logs; human inspection of evidence and target implementation. If any are missing, status **HOLD**. Production Playwright coverage remains unchanged.
