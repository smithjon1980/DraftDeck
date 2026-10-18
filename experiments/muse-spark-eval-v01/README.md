# BOSS — Muse Spark Open candidate evaluation v0.1

**State:** LOCAL SCORER VERIFIED / MUSE INFERENCE NOT RUN / NO ADMISSION / NO RELEASE. 2026-10-18.

## What this is

A public-safe, **fully synthetic**, three-discipline evaluation gate before deciding whether to add Meta Muse Spark Open to BOSS/DraftDeck:

1. **Visual evidence (V01–V03):** synthetic screenshot of a brand marker in the wrong corner, an orange off-brand accent, or correct marker placement and BOSS cyan/magenta. Brand marker is deliberately NOT the original BOSS logo and is NOT visually approved artwork.
2. **Execution selection (R01–R05):** separate GitHub Actions (repeatable repo CI), Windmill (multi-step human-approved workflows), Kaggle (ephemeral research GPUs), Railway (persistent service), and HOLD when authorization is absent.
3. **Evidence (E01–E03):** reject logo-location and print-certification claims contradicted by supplied evidence; accept accurately scoped PDF geometry/text claims.

Each case records a *blinded* expected decision, required defect codes, any expected environment selection, and allowed evidence IDs. A prediction cannot win by inventing citations. `HOLD`, unanswered, malformed JSON, and refusal are **never** silently counted as correct `PASS` or `FAIL` decisions. Intentional safety holds are scored explicitly when `HOLD` is the gold answer (R05).

## Ground truth and limits

- User feedback: layouts A and B are each valid when their story supports them, not universal design masters. Canonical logo belongs **bottom-right**, with cyan `#00BCEB`, magenta `#E30074`, black ink and white paper. These fixture images are synthetic and contain no unpublished manuscript or original logo.
- Muse release: `https://research.meta.ai/blog/muse-spark-open`; gated model: `https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B`. License: custom **Muse Model License**, not OSI unrestricted. Model access/provider credentials, fees and permitted intended use need separate authorization.
- **No hosted inference, model downloads, provider requests, API-key use, plugin installation, or costs were executed during preparation.** An opt-in Baseten runner is included, but it is default-off and has not been run against a provider. A model result is `NOT_TESTED` until separately approved inference runs and results pass this evaluator.
- This evaluator checks schema, target answers, defect coverage, allowed evidence IDs and wrong `PASS` decisions. It does NOT inspect the pixels, establish physical-print readiness, guarantee reliable tool invocation, or authorize deployment.
- Only deterministic test-controls have been executed so far. `control_expected` is the reference oracle, and `control_intentionally_bad` is a deliberately false response set. Neither is a Muse or competing-model benchmark.

## Offline setup and commands

Python 3.10+ standard library for scoring; Pillow needed only to create the synthetic PNG fixtures.

```bash
cd experiments/muse-spark-eval-v01
python3 make_synthetic_images.py                    # creates synthetic/*.png, NOT real BOSS art
python3 make_blind_requests.py                     # writes private synthetic blind_requests.jsonl
python3 make_control_predictions.py                # writes control_expected.jsonl + control_intentionally_bad.jsonl
python3 evaluate.py --predictions control_expected.jsonl --require-all-pass
python3 evaluate.py --predictions control_intentionally_bad.jsonl
python3 -m unittest -v test_evaluate.py
```

Predictions are JSON Lines with exactly these fields per case:

```json
{"case_id":"V01","decision":"FAIL","route":"NONE","defects":["LOGO_POSITION"],"evidence_ids":["img"],"explanation":"Marker is at upper-right, not lower-right."}
```

`decision`: one of `PASS`, `FAIL`, `HOLD`. `route`: `GITHUB_ACTIONS`, `WINDMILL`, `KAGGLE`, `RAILWAY`, or `NONE` for routing cases. `defects`: required defect codes for failures. `evidence_ids`: IDs **present in that case's provided evidence**; fabricated IDs are scored as failure. Use image bytes from `fixture` for the V cases; evidence metadata in each case is for evaluation, not a substitute for a model seeing the image. For a blinded model run, use the output of `make_blind_requests.py`: it includes the synthetic screenshot bytes as `image_data_url` and deliberately omits the `reference` object and descriptive image filenames. The model must not receive `cases.json`, a local path with a revealing label, or ground truth. Never send private customer or unpublished manuscript assets by substituting them into this exporter.

## GitHub → Baseten connection preparation (zero-charge gate)

The manual Actions preflight is in `.github/workflows/baseten-connection-check.yml`. On PRs, it checks test-fixture generation, blinded JSONL and a three-case dry-run **without injecting an API key**. When manually dispatched from GitHub Actions on the default branch after this PR merges, a second job checks *only whether* the repository secret is configured; it **does not call Baseten**, measure authentication, verify a spend cap, or run Muse. No secrets, synthetic screenshots, transcript or generated payloads are uploaded as workflow artifacts.

**Workspace setup by an authorized human in Baseten:**

1. Confirm this is the intended BOSS workspace and you understand its billing policy. The shown $0 usage does not establish any hard cap.
2. Ask Baseten support or inspect the dashboard to verify whether Model APIs can be limited with a **provider-enforced hard spend cap** at the intended ceiling (for example, $1). Do not treat an alert, estimated token-cost calculation, or client-side budget guard as a hard cap.
3. If creating a Baseten key, prefer an appropriately limited **workspace** key rather than a broad personal administrative key, and restrict permitted operations/models wherever the UI actually supports those permissions. Do not post the key in a PR, a ChatGPT message or an issue.
4. In GitHub **DraftDeck → Settings → Secrets and variables → Actions → New repository secret**, store it under the exact name `BASETEN_API_KEY`. Configure access carefully and remove/rotate it if compromised. The GitHub connector currently cannot read or configure repository secrets for the user.
5. **After** PR review and merge, in **Actions → BOSS Baseten GitHub connection check → Run workflow**, run the non-billable check. It will distinguish an absent repository secret from a present one, but neither outcome validates that Baseten accepts the key.

**Important:** No live/payed inference workflow has been enabled here. The Python adapter's `--account-hard-cap-confirmed` argument records an operator assertion, not a measured provider-side guarantee. Even a confirmed hard spending policy must be inspected for enforcement latency and billing exceptions. Baseten's published Model APIs page mentions budgeting, but as of the preparation date we have not independently verified that this BOSS account can enforce a $1 hard cap. Until that is established and the user explicitly approves chargeable calls, remain `HOLD`.

Relevant official references:
- Baseten Muse API model ID and endpoint: https://www.baseten.co/resources/changelog/muse-spark-open-and-nemotron-35-super-vl-available-on-baseten/
- Baseten workspace API key permissions: https://www.baseten.co/resources/changelog/add-workspace-api-keys-for-more-granular-permissions/
- Baseten read-only usage cost endpoint (not used by preflight): https://www.baseten.co/resources/changelog/model-api-costs/

## Read-only authentication verification after GitHub secret setup

The original exposed Baseten key was reported revoked by the account owner, and GitHub Actions separately confirmed `BASETEN_API_KEY` **exists** without sending an API request. Those checks do not establish whether the replacement key is valid with Baseten.

After approving and merging the separate catalog-check PR, use **GitHub → DraftDeck → Actions → BOSS Baseten catalog authentication (read-only) → Run workflow**, select `main`, check **Authorize one GET to Baseten model catalog; no model inference**, and run.

The check calls only `GET https://inference.baseten.co/v1/models` with an Authorization header read from the Actions secret. This authenticated catalog discovery endpoint is documented in Baseten's own usage tutorial (https://www.baseten.co/blog/how-to-run-any-open-model-inside-deepseek-harness/). It does not POST to `chat/completions`, produce tokens, deploy models or modify workspace configuration. It emits only a small status summary (model count and whether a Muse Spark identifier was listed), never key material or raw provider response. `PASS` means that key was accepted to read the catalog, **not** that an inference call was authorized or that a provider-side cost limit exists.

A missing secret, 401, 403, unexpected catalog structure, connection error or redirect returns `HOLD` and fails the job. This check requires an explicit manual checkbox, runs only on the `main` branch and does not run for pull requests. Paid inference remains `HOLD` until the approved provider-side spending policy and separate billing authorization are established.

## Default-off hosted adapter: Baseten Muse Spark Open

The repository includes `run_baseten.py` to prepare or execute a tightly controlled **synthetic-only** inference run against the official Baseten OpenAI-compatible endpoint:

- Endpoint: `https://inference.baseten.co/v1/chat/completions`
- Model ID: `meta-models/muse-spark-open`
- Key: `BASETEN_API_KEY` environment variable **on the user's approved execution host only**. **Do not paste credentials into a chat or PR.**
- Official endpoint source: https://www.baseten.co/resources/changelog/muse-spark-open-and-nemotron-35-super-vl-available-on-baseten/
- Pricing reference for the Hugging Face Baseten route (not a guarantee for a directly billed Baseten account): https://huggingface.co/inference/models . Baseten direct-account prices and billing terms must be independently confirmed before execution.

First, generate synthetic visuals and blinded requests:

```bash
python3 make_synthetic_images.py
python3 make_blind_requests.py
python3 run_baseten.py --max-calls 11          # SAFE default: dry-run, NO HTTP, NO COST
```

Before enabling live mode, obtain explicit approval of provider, model, maximum calls, cash ceiling and permitted input class (synthetic-only). Verify that the **provider-side account spending cap is in place**. Confirm prices on the selected billing route. Then, *and only then*, the authorized operator can execute live mode:

```bash
# Illustrative template only; DO NOT RUN without user approval and provider-side cap.
python3 run_baseten.py --mode live --max-calls 11 \
  --authorize-billable --account-hard-cap-confirmed \
  --max-usd APPROVED_AMOUNT \
  --input-usd-per-million VERIFIED_INPUT_PRICE \
  --output-usd-per-million VERIFIED_OUTPUT_PRICE \
  --image-token-reserve VERIFIED_IMAGE_TOKEN_RESERVE
```

The `--image-token-reserve` setting is a conservative estimate and **does not establish a guaranteed maximum bill**, especially for multimodal provider metering. The authorized provider account must enforce the real financial ceiling. This script does not discover account settings, verify prices independently or set external spending caps. If API usage is missing, a request fails, the preflight reserve is insufficient, or a response is malformed, it stops without retrying. There are no production tool calls or write capabilities.

After a genuine run, apply `evaluate.py --predictions run_results/predictions.jsonl` and independently review the sidecar audit records, actual provider invoice/usage and refusal counts. Run the *same* synthetic blind cases on a separately authorized baseline model and compare rates; don't count control fixtures as models.

### Current model-evidence status

`MUSE_LIVE_INFERENCE: NOT_TESTED`. `COMPARATOR_LIVE_INFERENCE: NOT_TESTED`.
`ACCOUNT_BUDGET: NOT_CONFIRMED`. `MODEL_ADMISSION: HOLD`.

## Later live evaluation: authorization gate

1. Human approves provider, exact model identifier, customer data scope (synthetic only by default), maximum calls, cost ceiling and region; recorded price/usage information must exist before billing. Reject unknown costs.
2. Keep API keys in the execution host's secret store; never commit keys, user screenshots, manuscript text or responses with sensitive content.
3. Use a vendor adapter in an isolated worker, forbid write-capable production tools, store exact request/response hash, latency, token counts, provider/version and price, and stop at user-approved thresholds. The adapter is default-off; no billable execution has occurred. Provider-side budget enforcement is separately required.
4. Evaluate the **same** synthetic cases against the control model and Muse; apply this scorer to every response and separately report case accuracy, false passes, refusals, hallucinated evidence, latency and cost.
5. Independent reviewer verifies selected failures, source fidelity and hard failures. Any unverified claim, missing visual input, blocked access or source leakage -> `HOLD` and no upgrade to active BOSS dependency.

**Admission rule:** Independent evidence and human authorization govern releases. Passing this synthetic suite would qualify only a more realistic next test, not a production deployment.