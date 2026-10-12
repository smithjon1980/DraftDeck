#!/usr/bin/env python3
"""Emit an auditable, redacted transcript receipt without private URLs or paths."""
import argparse
import json
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument("--receipt", required=True)
p.add_argument("--out", required=True)
p.add_argument("--expected-sha256", required=True)
p.add_argument("--source-id", required=True)
args = p.parse_args()
original = json.loads(Path(args.receipt).read_text())
if original["sha256"] != args.expected_sha256:
    raise SystemExit("SOURCE_HASH_MISMATCH")
safe = {
    "source_id": args.source_id[:80],
    "source_sha256": original["sha256"],
    "duration_seconds": original["duration_seconds"],
    "upstream_commit": original["upstream_commit"],
    "model_file": Path(original["model"]).name,
    "asr_execution": "COMPLETED",
    "speaker_diarization": "NOT_ESTABLISHED",
    "verbatim_accuracy": "NOT_ESTABLISHED",
    "human_release": "HOLD",
}
Path(args.out).write_text(json.dumps(safe, indent=2) + "\n")
print("REDACTED_RECEIPT_CREATED")
