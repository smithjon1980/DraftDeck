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
- **No hosted inference, model downloads, provider requests, secret handling, plugin installation, or costs occur in this version.** A model result is `NOT_TESTED` until a separately approved inference adapter runs the same cases and passes through this evaluator.
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

## Later live evaluation: authorization gate

1. Human approves provider, exact model identifier, customer data scope (synthetic only by default), maximum calls, cost ceiling and region; recorded price/usage information must exist before billing. Reject unknown costs.
2. Keep API keys in the execution host's secret store; never commit keys, user screenshots, manuscript text or responses with sensitive content.
3. Use a vendor adapter in an isolated worker, forbid write-capable production tools, store exact request/response hash, latency, token counts, provider/version and price, and stop at user-approved thresholds. No payment-enabled adapter is included here.
4. Evaluate the **same** synthetic cases against the control model and Muse; apply this scorer to every response and separately report case accuracy, false passes, refusals, hallucinated evidence, latency and cost.
5. Independent reviewer verifies selected failures, source fidelity and hard failures. Any unverified claim, missing visual input, blocked access or source leakage -> `HOLD` and no upgrade to active BOSS dependency.

**Admission rule:** Independent evidence and human authorization govern releases. Passing this synthetic suite would qualify only a more realistic next test, not a production deployment.