#!/usr/bin/env python3
"""Validate the STRUCTURE of a BOSS candidate visual evidence bundle.

Does not inspect pixels, confirm art fidelity, verify reviewer identity, or authorize release.
Works offline with Python standard library. Paths are relative to --evidence-root.
"""
import argparse
import json
import pathlib
import sys

GATES = ("source_copy", "story_art", "logo", "cad", "legibility_contrast",
         "clipping_collisions", "browser_behavior", "adapter_fidelity", "target_editability")
STATES = {"PASS", "FAIL", "NOT_TESTED"}
ARTIFACT_KEYS = ("source_manifest", "copy_manifest", "browser_render",
                 "comparison", "difference_annotations", "native_text_art_evidence")
DECISIONS = {"PENDING", "REJECTED", "APPROVED_FOR_NEXT_GATE"}

def validate(data, root):
    errors = []
    if not isinstance(data, dict):
        return ["manifest must be a JSON object"]
    for k in ("candidate_id", "source_commit", "profile", "source_reference"):
        if not isinstance(data.get(k), str) or not data[k].strip():
            errors.append(f"missing nonempty {k}")
    dims = data.get("dimensions", {})
    if not isinstance(dims, dict) or not all(type(dims.get(k)) is int and dims[k] > 0 for k in ("width", "height")):
        errors.append("dimensions need positive integer width/height")
    elif data.get("profile") == "slide" and (dims["width"], dims["height"]) != (1920, 1080):
        errors.append("slide profile must render at 1920x1080")
    reference = data.get("reference_status")
    if reference not in ("APPROVED", "REFERENCE_UNAPPROVED"):
        errors.append("reference_status must be APPROVED or REFERENCE_UNAPPROVED")
    artifacts = data.get("artifacts", {})
    if not isinstance(artifacts, dict):
        errors.append("artifacts must be an object")
        artifacts = {}
    for key in ARTIFACT_KEYS:
        value = artifacts.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"missing artifact: {key}")
            continue
        p = pathlib.Path(value)
        if p.is_absolute() or ".." in p.parts:
            errors.append(f"unsafe artifact path: {key}")
        elif not (root / p).is_file():
            errors.append(f"artifact not found: {key}")
    if reference == "APPROVED":
        ref = artifacts.get("approved_reference")
        if not isinstance(ref, str) or not ref.strip():
            errors.append("approved reference must have an artifact")
        elif pathlib.Path(ref).is_absolute() or ".." in pathlib.Path(ref).parts or not (root / ref).is_file():
            errors.append("approved reference artifact missing or unsafe")
    checks = data.get("checks", {})
    if not isinstance(checks, dict):
        checks = {}
    for gate in GATES:
        if checks.get(gate) not in STATES:
            errors.append(f"invalid or missing check {gate}")
    decision = data.get("human_review", {})
    if not isinstance(decision, dict) or decision.get("decision") not in DECISIONS:
        errors.append("missing or invalid human review decision")
        decision = {}
    if decision.get("decision") == "APPROVED_FOR_NEXT_GATE":
        for field in ("reviewer", "reviewed_at", "candidate_sha256", "scope"):
            if not isinstance(decision.get(field), str) or not decision[field].strip():
                errors.append(f"human approval missing {field}")
    release_ready = (
        not errors and reference == "APPROVED"
        and all(checks.get(g) == "PASS" for g in GATES)
        and decision.get("decision") == "APPROVED_FOR_NEXT_GATE"
    )
    # This is explicitly NOT release authorization; adapter review and a separate
    # human release act remain required regardless of the result.
    return errors, release_ready

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("manifest", type=pathlib.Path)
    p.add_argument("--evidence-root", type=pathlib.Path)
    a = p.parse_args()
    root = (a.evidence_root or a.manifest.parent).resolve()
    try:
        data = json.loads(a.manifest.read_text(encoding="utf-8"))
        errors, ready = validate(data, root)
    except (OSError, ValueError) as exc:
        errors, ready = [str(exc)], False
    status = "INVALID" if errors else ("ELIGIBLE_FOR_NEXT_GATE" if ready else "HOLD")
    print(json.dumps({"status": status, "errors": errors,
                      "human_release_authorized": False,
                      "visual_fidelity_verified_by_script": False}, indent=2))
    sys.exit(1 if errors else (0 if ready else 2))

if __name__ == "__main__":
    main()
