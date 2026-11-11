#!/usr/bin/env python3
"""Validate a PRIVATE BOSS Day Zero 60-slide source map.

No API, model inference, file upload, or approval action.
The JSON source map is private; DO NOT commit it to DraftDeck.
This structure gate does not replace rendered visual inspection or source judgment.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path


def normalize(s):
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r"\*\*(.*?)\*\*", r"\1", s)
    s = re.sub(re.escape(chr(96)) + r"([^" + re.escape(chr(96)) + r"]+)" + re.escape(chr(96)), r"\1", s)
    s = re.sub(r"\[(.*?)\]\((.*?)\)", r"\1", s)
    return " ".join(s.split())


def validate(manifest, private_source_root=None):
    slides = manifest.get("slides", [])
    errors = []
    if len(slides) != 60:
        errors.append("SLIDE_COUNT_NOT_60")
    if manifest.get("status") not in [
        "PRIVATE_CANDIDATE_NOT_MUSE_GENERATED",
        "PRIVATE_CANDIDATE_MUSE_GENERATED_NOT_APPROVED",
    ]:
        errors.append("UNRECOGNIZED_CANDIDATE_STATUS")
    if [s.get("slide") for s in slides] != list(range(1, len(slides) + 1)):
        errors.append("NON_SEQUENTIAL_SLIDES")
    if [s.get("type") for s in slides[:4]] != ["orientation"] * min(4, len(slides)):
        errors.append("FOUR_ORIENTATION_SLIDES_REQUIRED")

    expected_positions = []
    for i in range(8):
        expected_positions.append((5 + i*7, "studio_open", i + 1))
        expected_positions.extend((6 + i*7 + j, "instruction", i + 1) for j in range(6))
    for n, typ, studio in expected_positions:
        if n > len(slides):
            continue
        s = slides[n-1]
        if s.get("type") != typ or s.get("studio") != studio:
            errors.append(f"STUDIO_SEQUENCE_MISMATCH:{n}")
        if not s.get("source_file") or not s.get("source_sha256"):
            errors.append(f"MISSING_SOURCE_ID:{n}")
        if typ == "instruction" and not s.get("verbatim_source_excerpts"):
            errors.append(f"MISSING_SOURCE_EXCERPT:{n}")

    checked = 0
    file_hashes = {}
    if private_source_root:
        root = Path(private_source_root).resolve()
        for s in slides:
            source_name = s.get("source_file")
            if not source_name:
                continue
            if source_name != Path(source_name).name or "/" in source_name or "\\" in source_name:
                errors.append(f"SOURCE_PATH_NOT_BASENAME:{s.get('slide')}")
                continue
            target = (root / source_name).resolve()
            if not target.is_relative_to(root) or not target.is_file():
                errors.append(f"PRIVATE_SOURCE_MISSING:{s.get('slide')}")
                continue
            if source_name not in file_hashes:
                blob = target.read_bytes()
                file_hashes[source_name] = (hashlib.sha256(blob).hexdigest(),
                                            normalize(blob.decode("utf-8")))
            actual_sha, text = file_hashes[source_name]
            if actual_sha != s.get("source_sha256"):
                errors.append(f"SOURCE_HASH_MISMATCH:{s.get('slide')}")
            if normalize(s.get("source_section") or "") not in text:
                errors.append(f"SOURCE_SECTION_NOT_FOUND:{s.get('slide')}")
            for excerpt in s.get("verbatim_source_excerpts", []):
                checked += 1
                if normalize(excerpt) not in text:
                    errors.append(f"UNSUPPORTED_SOURCE_EXCERPT:{s.get('slide')}")
    return {"status": "PASS" if not errors else "FAIL", "slides": len(slides),
            "private_source_excerpts_compared": checked,
            "human_visual_approval": "NOT_TESTED",
            "source_edits_authorized": "NOT_TESTED",
            "muse_inference_verified": "NOT_TESTED",
            "errors": errors}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("manifest", type=Path)
    p.add_argument("--private-source-root", type=Path)
    p.add_argument("--out", type=Path)
    args = p.parse_args()
    payload = json.loads(args.manifest.read_text(encoding="utf-8"))
    report = validate(payload, args.private_source_root)
    txt = json.dumps(report, indent=2)
    print(txt)
    if args.out:
        args.out.write_text(txt + "\n", encoding="utf-8")
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
