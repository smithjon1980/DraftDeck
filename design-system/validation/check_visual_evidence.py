#!/usr/bin/env python3
"""Validate metadata for BOSS visual evidence. Never approves art or publication."""
import argparse
import json
from pathlib import Path

ARTIFACTS = (
    "source_manifest", "approved_reference_or_explicit_hold",
    "browser_render_capture", "side_by_side_comparison",
    "difference_annotations", "native_text_and_art_layer_evidence",
    "per_gate_review_states", "human_review_record",
)
STATES = {"PASS", "FAIL", "NOT_TESTED", "HOLD"}
GATES = ("source", "story", "brand", "layout", "native_layers", "export", "adapter")

def validate(record):
    errors = []
    if not isinstance(record, dict):
        return ["evidence record must be an object"]
    if record.get("schema_version") != "1":
        errors.append("schema_version must equal '1'")
    if record.get("profile") not in ("slide", "web", "print"):
        errors.append("profile must be slide, web, or print")
    if not isinstance(record.get("source_commit"), str) or not record["source_commit"].strip():
        errors.append("source_commit is required")
    items = record.get("artifacts")
    if not isinstance(items, dict):
        return errors + ["artifacts must be an object"]
    for name in ARTIFACTS:
        item = items.get(name)
        if not isinstance(item, dict) or item.get("status") not in STATES:
            errors.append(f"{name}: explicit PASS/FAIL/NOT_TESTED/HOLD status required")
            continue
        if item["status"] == "PASS" and not (isinstance(item.get("evidence_ref"), str) and item["evidence_ref"].strip()):
            errors.append(f"{name}: PASS requires evidence_ref")
        if item["status"] == "PASS" and item.get("evidence_ref", "").startswith("http"):
            errors.append(f"{name}: use private evidence IDs, not external links")
    gates = record.get("gates")
    if not isinstance(gates, dict):
        return errors + ["gates must be an object"]
    for gate in GATES:
        if gates.get(gate) not in STATES:
            errors.append(f"gate {gate}: explicit state required")
    if record.get("release_state") != "HOLD":
        errors.append("validator accepts candidate HOLD records only; never authorizes release")
    if record.get("human_authorization") not in ("PENDING", "REJECTED"):
        errors.append("human authorization must be PENDING or REJECTED in CI candidates")
    if any(gates.get(g) == "PASS" for g in ("layout", "export")):
        for k in ("browser_render_capture", "side_by_side_comparison", "difference_annotations"):
            if items.get(k, {}).get("status") != "PASS":
                errors.append(f"{k} must have verified evidence before layout/export PASS")
    if record.get("human_authorization") == "PENDING" and gates.get("source") == "PASS" and items.get("approved_reference_or_explicit_hold", {}).get("status") == "NOT_TESTED":
        errors.append("source PASS requires explicit reference disposition")
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    errors = validate(json.loads(args.record.read_text(encoding="utf-8")))
    if errors:
        raise SystemExit("\n".join(errors))
    print("Visual evidence record STRUCTURE PASS; image fidelity NOT_ESTABLISHED; release HOLD")

if __name__ == "__main__":
    main()
