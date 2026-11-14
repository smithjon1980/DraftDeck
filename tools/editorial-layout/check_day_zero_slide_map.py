#!/usr/bin/env python3
"""Check Day Zero Candidate 006's exact source-to-slide mapping. Not a visual test."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "manuscripts/day-zero/CANDIDATE-006-100-paragraphs.txt"
MAP = ROOT / "production/day-zero/candidate-006/slide-map.v1.json"
EXPECTED_MANUSCRIPT_BLOB = "514e759abe8308705856f814b4ef88d041113778"
EXPECTED_COMMIT = "dd1a3f89f1eaa4b416d6b5dadc4cd22547835c8c"
PILOTS = ["DZ-001", "DZ-053", "DZ-063"]


def verify():
    failures = []
    raw = SOURCE.read_text(encoding="utf-8")
    data = json.loads(MAP.read_text(encoding="utf-8"))

    computed = subprocess.run(
        ["git", "hash-object", str(SOURCE)],
        cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.strip()
    if computed != EXPECTED_MANUSCRIPT_BLOB:
        failures.append("Pinned source Git blob mismatch")
    if data["manuscript"]["blob_sha"] != EXPECTED_MANUSCRIPT_BLOB:
        failures.append("Manifest blob SHA differs from pinned source")
    if data["manuscript"]["commit_sha"] != EXPECTED_COMMIT:
        failures.append("Manifest commit pin mismatch")

    numbers = [int(n) for n in re.findall(r"(?m)^(\d{3})\.\s", raw)]
    stages = re.findall(r"(?m)^Stage [IVX]+ —", raw)
    scenes = re.findall(r"(?m)^Scene \d{2} —", raw)
    if numbers != list(range(1, 101)) or len(stages) != 5 or len(scenes) != 20:
        failures.append("Manuscript has unexpected structural boundaries")

    slides = data["slides"]
    if len(slides) != 100:
        failures.append("Manifest must cover exactly 100 slides")
    else:
        for index, item in enumerate(slides, start=1):
            code = f"{index:03d}"
            if item["slide_id"] != "DZ-" + code or item["source_paragraph"] != code:
                failures.append(f"Slide mapping wrong at {code}")
            if item["scene"] != (index - 1) // 5 + 1:
                failures.append(f"Scene mapping wrong at {code}")
            if item["stage"] != (index - 1) // 20 + 1:
                failures.append(f"Stage mapping wrong at {code}")
            if item["copy_policy"] != "EXACT_FROM_PINNED_MANUSCRIPT":
                failures.append(f"Source fidelity policy wrong at {code}")
            if item["text_layer"] != "NATIVE_HTML_CSS_REACT":
                failures.append(f"Text editability policy wrong at {code}")
            if item["release"] != "NOT_AUTHORIZED":
                failures.append(f"Unauthorized release status at {code}")
            if item["gates"]["human_acceptance"] != "PENDING":
                failures.append(f"Human slide approval unexpectedly present at {code}")

    if data["pilot_selection"] != PILOTS:
        failures.append("Calibration slide selection drifted")
    if [p["slide_id"] for p in data["pilot_briefs"]] != PILOTS:
        failures.append("Calibration briefs mismatch")
    if data["spark"]["reference_images_required"] != 4:
        failures.append("Spark specification requires exactly four references")
    if data["spark"]["reference_images_verified"] != 0 or data["spark"]["output_status"] != "NOT_GENERATED":
        failures.append("Spark image claim is unsupported")
    if data["status"] != "REVIEW_CANDIDATE_NOT_RELEASED":
        failures.append("Manifest incorrectly asserts release")
    if data["governance"] != "HAVE — Human Authority, Verified Execution":
        failures.append("Governance language drift")

    if failures:
        print("SLIDE_MAP_STRUCTURE_FAIL")
        for failure in failures:
            print(" -", failure)
        return 1
    print("SLIDE_MAP_STRUCTURE_PASS: 100 sourced slide anchors; 3 calibration briefs")
    print("SPARK_HOLD: four reference images unverified; no generated image")
    print("VISUAL_NOT_TESTED; VECTOR_PDF_NOT_TESTED; HUMAN_RELEASE_NOT_AUTHORIZED")
    return 0


if __name__ == "__main__":
    sys.exit(verify())
