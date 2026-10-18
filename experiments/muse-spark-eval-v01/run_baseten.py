#!/usr/bin/env python3
"""Opt-in Muse Spark Open Baseten adapter; DRY-RUN by default.

No network request without explicit live flags, price inputs, an account-side
hard cap acknowledgment, a provider API key, and preflight worst-case reserve.
The reserve is NOT a guarantee of provider billing. NEVER send private assets.
Run only the synthetic blind request JSONL created by make_blind_requests.py.
Requires Python 3.10+ standard library; no third-party SDK.
"""
import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ENDPOINT = "https://inference.baseten.co/v1/chat/completions"
MODEL = "meta-models/muse-spark-open"
SYSTEM = (
    "You are an evidence-constrained BOSS evaluation respondent. Return one "
    "JSON object with decision (PASS|FAIL|HOLD), route "
    "(GITHUB_ACTIONS|WINDMILL|KAGGLE|RAILWAY|NONE), defects (array of "
    "strings), evidence_ids (array of identifiers explicitly provided), "
    "and explanation (short text). Inspect the supplied image, if any. "
    "No invented evidence, false verification or assumed tool execution. "
    "A refusal is not a successful evaluation."
)


def read_cases(path):
    cases = []
    seen = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        if not isinstance(item, dict) or set(item) - {
            "case_id", "category", "prompt", "evidence", "response_schema", "image_data_url"
        }:
            raise ValueError("Unapproved blind-case fields; refusing to send")
        if item["case_id"] in seen:
            raise ValueError("Duplicate case")
        seen.add(item["case_id"])
        image = item.get("image_data_url")
        if image is not None and not image.startswith("data:image/png;base64,"):
            raise ValueError("Only inline synthetic PNG images are permitted")
        if image is not None and item.get("category") != "visual":
            raise ValueError("Image attached to nonvisual test")
        cases.append(item)
    if not cases:
        raise ValueError("No cases to run")
    return cases


def build_payload(case, max_output_tokens):
    evidence = case["evidence"]
    prompt = (case["prompt"] + "\nEvidence (allowed IDs only):\n" +
              json.dumps(evidence, sort_keys=True) +
              "\nUse those exact IDs in evidence_ids.")
    content = [{"type": "text", "text": prompt}]
    if "image_data_url" in case:
        content.append({"type": "image_url",
                        "image_url": {"url": case["image_data_url"]}})
    return {"model": MODEL, "messages": [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": content}],
        "max_tokens": max_output_tokens, "temperature": 0}


def reserved_usd(payload, max_output_tokens, image_reserve_tokens,
                 input_usd_per_million, output_usd_per_million):
    text_len = sum(
        len(e["content"]) if isinstance(e["content"], str)
        else sum(len(part.get("text", "")) for part in e["content"])
        for e in payload["messages"]
    )
    image_count = sum(
        sum(part.get("type") == "image_url" for part in e["content"])
        for e in payload["messages"] if isinstance(e["content"], list)
    )
    # Conservative text heuristic, but image token reserve is user-supplied
    # and must be validated against provider policy before any live calls.
    input_reserve = (text_len + 2) // 3 + image_count * image_reserve_tokens
    return (input_reserve * input_usd_per_million +
            max_output_tokens * output_usd_per_million) / 1_000_000


def parse_completion(raw, case_id):
    choices = raw.get("choices", [])
    content = choices[0].get("message", {}).get("content") if choices else None
    if not isinstance(content, str):
        return {"case_id": case_id, "decision": "REFUSE",
                "defects": [], "evidence_ids": [], "explanation": "No text response"}
    try:
        obj = json.loads(content)
        if not isinstance(obj, dict):
            raise ValueError("response is not an object")
        return {"case_id": case_id, "decision": obj.get("decision"),
                "route": obj.get("route", "NONE"),
                "defects": obj.get("defects", []),
                "evidence_ids": obj.get("evidence_ids", []),
                "explanation": obj.get("explanation", "")}
    except (json.JSONDecodeError, ValueError):
        return {"case_id": case_id, "decision": "REFUSE",
                "defects": [], "evidence_ids": [],
                "explanation": "Invalid JSON output"}


def options():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--blind-requests", type=Path,
                        default=Path(__file__).with_name("blind_requests.jsonl"))
    parser.add_argument("--out-dir", type=Path,
                        default=Path(__file__).with_name("run_results"))
    parser.add_argument("--mode", choices=("dry-run", "live"), default="dry-run")
    parser.add_argument("--authorize-billable", action="store_true")
    parser.add_argument("--account-hard-cap-confirmed", action="store_true")
    parser.add_argument("--max-usd", type=float)
    parser.add_argument("--max-calls", type=int, default=11)
    parser.add_argument("--max-output-tokens", type=int, default=256)
    parser.add_argument("--image-token-reserve", type=int, default=20000)
    parser.add_argument("--input-usd-per-million", type=float)
    parser.add_argument("--output-usd-per-million", type=float)
    parser.add_argument("--timeout-seconds", type=int, default=90)
    return parser.parse_args()


def main():
    args = options()
    cases = read_cases(args.blind_requests)
    if not 1 <= args.max_calls <= len(cases):
        raise SystemExit("Set --max-calls from 1 to the number of cases")
    cases = cases[:args.max_calls]
    if args.max_output_tokens < 1 or args.image_token_reserve < 0:
        raise SystemExit("Invalid token ceilings")
    payloads = [build_payload(x, args.max_output_tokens) for x in cases]
    plan = {"status": "NO_INFERENCE_RUN", "mode": args.mode,
            "endpoint": ENDPOINT, "model": MODEL, "cases": len(cases),
            "contains_images": sum("image_data_url" in x for x in cases),
            "max_output_tokens_each": args.max_output_tokens,
            "image_token_reserve_each": args.image_token_reserve}
    if args.mode == "dry-run":
        print(json.dumps(plan, indent=2))
        return
    if not (args.authorize_billable and args.account_hard_cap_confirmed):
        raise SystemExit("LIVE HOLD: explicit billing and provider hard-cap flags required")
    if args.max_usd is None or args.max_usd <= 0:
        raise SystemExit("LIVE HOLD: positive --max-usd required")
    if any(x is None or x < 0 for x in (args.input_usd_per_million,
                                         args.output_usd_per_million)):
        raise SystemExit("LIVE HOLD: verified provider token prices required")
    if not 1 <= args.timeout_seconds <= 120:
        raise SystemExit("LIVE HOLD: timeout must be 1 to 120 seconds")
    key = os.environ.get("BASETEN_API_KEY", "")
    if not key:
        raise SystemExit("LIVE HOLD: BASETEN_API_KEY environment variable missing")
    budget_reservations = [
        reserved_usd(p, args.max_output_tokens, args.image_token_reserve,
                     args.input_usd_per_million, args.output_usd_per_million)
        for p in payloads
    ]
    if sum(budget_reservations) > args.max_usd:
        raise SystemExit("LIVE HOLD: reserved request costs exceed approved ceiling")
    args.out_dir.mkdir(parents=True, exist_ok=True)
    preds = args.out_dir / "predictions.jsonl"
    audit = args.out_dir / "audit.jsonl"
    if preds.exists() or audit.exists():
        raise SystemExit("LIVE HOLD: output files exist; preserve prior run evidence")
    spent_estimate = 0.0
    with preds.open("x", encoding="utf-8") as out, \
            audit.open("x", encoding="utf-8") as log:
        for index, (case, payload) in enumerate(zip(cases, payloads)):
            if spent_estimate + budget_reservations[index] > args.max_usd:
                break
            data = json.dumps(payload, separators=(",", ":")).encode("utf-8")
            req = urllib.request.Request(
                ENDPOINT, data=data, method="POST",
                headers={"Content-Type": "application/json",
                         "Authorization": "Bearer " + key})
            started = time.monotonic()
            try:
                with urllib.request.urlopen(req, timeout=args.timeout_seconds) as response:
                    body = response.read(2_000_001)
                    if len(body) > 2_000_000:
                        raise ValueError("Oversized provider response")
                received = json.loads(body)
                usage = received.get("usage")
                if not isinstance(usage, dict):
                    raise ValueError("Provider returned no usage counters")
                input_tokens = usage.get("prompt_tokens")
                output_tokens = usage.get("completion_tokens")
                if not all(isinstance(x, int) and x >= 0
                           for x in (input_tokens, output_tokens)):
                    raise ValueError("Missing numerical token usage counters")
                observed_cost = (input_tokens * args.input_usd_per_million +
                                 output_tokens * args.output_usd_per_million) / 1_000_000
                spent_estimate += observed_cost
                prediction = parse_completion(received, case["case_id"])
                out.write(json.dumps(prediction, sort_keys=True) + "\n")
                log.write(json.dumps({
                    "case_id": case["case_id"], "model": MODEL, "endpoint": ENDPOINT,
                    "request_sha256": hashlib.sha256(data).hexdigest(),
                    "response_sha256": hashlib.sha256(body).hexdigest(),
                    "prompt_tokens": input_tokens, "completion_tokens": output_tokens,
                    "estimated_token_cost_usd": round(observed_cost, 8),
                    "duration_seconds": round(time.monotonic() - started, 3)
                }, sort_keys=True) + "\n")
                out.flush()
                log.flush()
                if observed_cost > budget_reservations[index] or spent_estimate > args.max_usd:
                    raise ValueError("Usage exceeded reserved estimate: STOP; manual billing check")
            except (urllib.error.HTTPError, urllib.error.URLError,
                    ValueError, json.JSONDecodeError) as err:
                print("HOLD: provider error or unpriced usage, stopping; check private audit",
                      file=sys.stderr)
                # Do not retry or leak raw prompt, key, provider response or
                # potentially sensitive headers into logs.
                raise SystemExit(2) from None
    print(json.dumps({"status": "LIVE_RESPONSES_RECORDED_NOT_EVALUATED",
                      "calls": sum(1 for _ in preds.open(encoding="utf-8")),
                      "estimated_token_cost_usd": round(spent_estimate, 8),
                      "provider_invoice_checked": False,
                      "human_review": "PENDING",
                      "result_dir": str(args.out_dir)}, indent=2))


if __name__ == "__main__":
    main()
