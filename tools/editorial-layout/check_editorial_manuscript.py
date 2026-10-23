#!/usr/bin/env python3
"""Check exact, native BOSS manuscript text in single-slide HTML.

Structural hash gate only. Does not evaluate layout pixels, actual font sizes,
illustration semantics, downstream editability, or human release.
No private BOSS narration or hashes are embedded in this public tool.
"""
import argparse
import hashlib
from html.parser import HTMLParser
import json
import re
import sys
from pathlib import Path

PID = re.compile(r"^EP01_P\d{3}$")
SHA = re.compile(r"^[a-f0-9]{64}$")


class NarrationParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.chunks = []
        self.columns = []
        self.active = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = a.get("class", "").split()
        if tag == "section" and "copy-col" in classes:
            self.columns.append(a.get("data-col"))
        if tag == "p" and "spoken" in classes:
            if self.active is not None:
                raise ValueError("Nested manuscript p tags")
            self.active = {"id": a.get("data-para-id"), "run": a.get("data-run"), "text": ""}

    def handle_data(self, data):
        if self.active is not None:
            self.active["text"] += data

    def handle_endtag(self, tag):
        if tag == "p" and self.active is not None:
            self.chunks.append(self.active)
            self.active = None


def evaluate(html, manifest):
    errors = []
    if not isinstance(manifest, dict):
        return {"status": "HOLD", "errors": ["manifest must be an object"]}
    expected = manifest.get("paragraphs")
    if not isinstance(expected, list) or not expected:
        return {"status": "HOLD", "errors": ["paragraphs missing"]}
    p = NarrationParser()
    p.feed(html)
    p.close()
    ids = []
    hashes = []
    for item in expected:
        pid = item.get("id", "") if isinstance(item, dict) else ""
        sha = item.get("sha256", "") if isinstance(item, dict) else ""
        if not PID.fullmatch(pid) or not SHA.fullmatch(sha):
            errors.append("invalid paragraph manifest record")
        ids.append(pid)
        hashes.append(sha)
    if len(ids) != len(set(ids)):
        errors.append("duplicate paragraph IDs in manifest")
    try:
        runs = [int(x["run"]) for x in p.chunks]
        if runs != list(range(len(runs))):
            errors.append("fragment order not contiguous")
    except (TypeError, ValueError):
        errors.append("invalid fragment index")

    original = {pid: "" for pid in ids}
    seen_ids = []
    for frag in p.chunks:
        pid = frag["id"]
        if pid not in original:
            errors.append("unmanifested spoken fragment")
            continue
        original[pid] += frag["text"]
        if pid not in seen_ids:
            seen_ids.append(pid)
    if ids != seen_ids:
        errors.append("paragraphs missing or out of order")
    for pid in ids:
        at = [i for i, frag in enumerate(p.chunks) if frag["id"] == pid]
        if at and at != list(range(at[0], at[-1] + 1)):
            errors.append("paragraph fragments not contiguous: " + pid)
    for pid, sha in zip(ids, hashes):
        if hashlib.sha256(original[pid].encode()).hexdigest() != sha:
            errors.append("paragraph hash mismatch: " + pid)

    complete = "\n\n".join(original[pid] for pid in ids)
    if hashlib.sha256(complete.encode()).hexdigest() != manifest.get("source_sha256"):
        errors.append("slide narration hash mismatch")
    words = len(complete.split())
    if words != manifest.get("expected_words"):
        errors.append("spoken word count mismatch")
    count = manifest.get("expected_columns")
    if type(count) is not int or count not in (1, 2, 3, 4):
        errors.append("invalid expected column count")
    elif p.columns != [str(i) for i in range(count)]:
        errors.append("column count/identity mismatch")

    return {
        "status": "HOLD" if errors else "STRUCTURAL_COPY_PASS_VISUAL_REVIEW_REQUIRED",
        "errors": sorted(set(errors)),
        "spoken_words": words,
        "columns_detected": len(p.columns),
        "human_visual_approval": "NOT_TESTED",
        "pdf_text_selectability": "NOT_TESTED",
        "release_authorized": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("rendered_html", type=Path)
    parser.add_argument("manifest_json", type=Path)
    args = parser.parse_args()
    try:
        result = evaluate(
            args.rendered_html.read_text(encoding="utf-8"),
            json.loads(args.manifest_json.read_text(encoding="utf-8")),
        )
    except (OSError, ValueError) as exc:
        result = {"status": "HOLD", "errors": [str(exc)], "release_authorized": False}
    print(json.dumps(result, indent=2))
    return 2 if result["status"] == "HOLD" else 0


if __name__ == "__main__":
    sys.exit(main())
