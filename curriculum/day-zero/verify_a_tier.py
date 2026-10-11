#!/usr/bin/env python3
"""Verify BOSS A-tier UTF-8 source files against the committed manifest. No network calls."""
from pathlib import Path
import hashlib, json, sys

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "curriculum/day-zero/integrity-manifest.json"

def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    entries = manifest.get("entries", [])
    if len(entries) != 7 or len({e["episode"] for e in entries}) != 7:
        raise SystemExit("FAIL: Expected exactly seven unique episodes")
    failures = []
    for e in entries:
        relative = Path(e["path"])
        if relative.is_absolute() or ".." in relative.parts or not str(relative).startswith("curriculum/day-zero/episodes/"):
            failures.append(f'{e["episode"]}: path outside approved A-tier')
            continue
        source = ROOT / relative
        if not source.is_file():
            failures.append(f'{e["episode"]}: source missing')
            continue
        raw = source.read_bytes()  # Exact Git checkout bytes, including BOM/CRLF.
        actual = hashlib.sha256(raw).hexdigest()
        expected = e["sha256_utf8"]
        size_matches = len(raw) == e["byte_length"]
        correct = actual == expected and size_matches
        print(f'{e["episode"]}: {"PASS" if correct else "FAIL"} sha256={actual} bytes={len(raw)}')
        if not correct:
            failures.append(f'{e["episode"]}: hash/length mismatch')
    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        raise SystemExit(1)
    print("PASS: 7/7 committed A-tier UTF-8 files match manifest; production source approval is separate.")

if __name__ == "__main__":
    main()
