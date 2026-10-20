# Saluki local-model evaluation — v0.1 candidate

Status: evaluation kit prepared; Saluki inference and target-laptop performance NOT TESTED.

## Purpose

Evaluate whether ConwayResearch/Underdog-Saluki-27B-1.0 merits a bounded role in BOSS, DraftDeck or Market Seven. The video is a discovery lead. Publisher claims are not project results.

Primary source reviewed October 20, 2026:
https://huggingface.co/ConwayResearch/Underdog-Saluki-27B-1.0

The model card identifies a 7.89 GB IQ2-mix GGUF, Apache 2.0 licensing and llama.cpp/Ollama support. It reports an average 96% retention across nine benchmarks, with task-specific weaknesses. Neither Claude equivalence nor suitable latency on Jonathan's device has been established. Download size excludes execution/context memory. Preserve attribution and review the model NOTICE when distributing weights; this kit contains no weights.

## Twenty cases

Five cases per category, embedded in evaluate.py:
- J1–J5: preserve supplied copy and typed page dimensions in structured output.
- S1–S5: select the current synthetic record, ignore superseded data and cite its ID.
- T1–T5: select a simulated authorized read-only tool and exact arguments.
- G1–G5: clarify missing inputs or refuse an explicitly prohibited action.

These are transparent smoke tests with repeated templates and obvious permissions. They are not independent benchmark validation, robust retrieval evaluation, native function-calling evaluation, prompt-injection resistance proof, learner transfer results or a causal study. T cases emit a JSON proposal; the runner never invokes proposed tools. S cases supply records in the prompt; no retrieval system is tested.

## Reproducible setup and run

Use a laptop with Python 3.10+ and a working local OpenAI-compatible llama.cpp endpoint. Follow the current model card's model-specific IQ2-mix download and runtime instructions, rather than automatic widget examples that may select a different variant. Pin model repository revision, actual downloaded weight SHA-256, runtime version/build and kit commit. No model download is performed by this kit.

Start with a declared short context such as 4096 tokens; record the actual server context, threads, GPU offload and cache settings. Keep settings identical across comparison models where supported and document exceptions. The card's example 32768 context is not a requirement for these cases.

Run from the repository root:

```sh
python experiments/saluki-local-v01/evaluate.py --self-test
python experiments/saluki-local-v01/evaluate.py --export-cases
python experiments/saluki-local-v01/evaluate.py --model saluki --model-revision REPO_COMMIT_AND_WEIGHT_SHA256 --runtime-version LLAMA_CPP_BUILD --source-revision KIT_COMMIT --device DEVICE_CPU_RAM_OS --output saluki-run-01.json
```

Use the actual model ID accepted by the server. The endpoint defaults to http://127.0.0.1:8080/v1/chat/completions. Only HTTP loopback endpoints are accepted; environment proxies are disabled and redirects rejected. Do not expose the local model server publicly. The runner sends synthetic fixtures only, issues no real business operations and requires no credentials.

It fixes temperature 0, requests thinking disabled and records the token cap. Verify that the runtime honors those settings; unsupported options require an explicitly documented adapter change. A non-stop finish reason, network error, unexpected native tool call, invalid JSON or contract mismatch fails the case. An existing output filename is rejected to preserve earlier runs. Each case checkpoints the report.

Run a separate warm-up request before the measured suite; record its contents and latency. Perform three complete measured repetitions, preserving failed attempts and unique output names. Do not tune the suite after viewing results and then claim an untouched comparison.

## Scoring and manual review

Machine checks report exact-contract pass counts by category with denominators, JSON validity, full API response, finish reason and elapsed request time. Exact JSON comparison ignores object key order, but preserves types, exact copy, arguments, evidence and field inventory. It is deliberately strict and may penalize otherwise useful wording.

A reviewer must inspect each output independently for substantive correctness, unsupported content and inappropriate COMPLETE/CLARIFY/REFUSE decisions. Preserve machine scores and human judgments separately. Do not reconcile away first results.

For each case retain: case ID, human PASS/FAIL, reason, reviewer, date and evidence. Record assistance. Treat wrong authorized actions and attempted prohibited actions as critical errors. The first pilot is diagnostic: no aggregate passing threshold or production approval is defined.

Measure model-server peak working memory with OS/runtime tools, separately from runner memory. Retain measurement method and evidence. Record CPU/GPU, available RAM, context/cache, runtime, cold/warm state, timeouts, crashes and thermal limitations. Elapsed request time is not tokens/second and includes server overhead.

## Fair model comparison

Use the same suite revision, prompts, output cap, temperature, repeat count and scoring for the comparison model. For this runner the comparison model must also be served locally. A hosted-model comparison requires a separately reviewed adapter with explicit provider/cost authorization; do not point this runner at a remote service or embed a key.

Compare per-category correctness, critical errors, median and slowest case latency, memory and operational effort. Separate hardware differences from model differences. Twenty synthetic cases are insufficient to rank general capability.

Suggested next gate: inspect one complete target-laptop run with revision/weight hash, all 20 responses, manual judgments and measured memory. Then compare repeated runs and decide one narrow next experiment. No automatic migration, release or research-milestone promotion follows.

## Current evidence

- Kit source: drafted; see PR and exact commit.
- Fixture/scorer self-test: CI result must be inspected separately.
- Actual Saluki execution: NOT TESTED.
- Laptop memory/speed: NOT MEASURED.
- Android operation, native tool execution and provider replacement: NOT TESTED.
- Learner results and independent author-methods competence: NOT ESTABLISHED.
