#!/usr/bin/env python3
"""Offline BOSS print PDF preflight. Does not approve a design or publish a file.

Usage:
  python tools/visual-poc/check_print_pdf.py print.pdf --expected-pages 2 \
     --private-manifest /path/to/PRIVATE_manifest.json
Requires PyMuPDF, installed intentionally in the chosen execution environment.
Keep the private manifest out of public commits and CI artifact uploads.
"""
import argparse
import json
import re
from pathlib import Path

def normalized(text):
    return re.sub(r"\s+", " ", text).strip()

def run():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", type=Path)
    ap.add_argument("--expected-pages", type=int, default=2)
    ap.add_argument("--private-manifest", type=Path)
    args = ap.parse_args()
    try:
        import fitz
    except ImportError as exc:
        raise SystemExit("PyMuPDF is required; install from a reviewed, pinned package.") from exc

    results = {"status": "PASS", "pdf": str(args.pdf), "checks": [],
               "copy_fidelity": "NOT_TESTED", "human_visual_approval": "NOT_TESTED",
               "printer_acceptance": "NOT_TESTED"}
    doc = fitz.open(args.pdf)
    if len(doc) != args.expected_pages:
        results["checks"].append({"type": "page_count", "status": "FAIL",
                                  "actual": len(doc), "expected": args.expected_pages})
        results["status"] = "FAIL"
    else:
        results["checks"].append({"type": "page_count", "status": "PASS",
                                  "actual": len(doc)})
    extracted = []
    for index, page in enumerate(doc, 1):
        size_ok = abs(page.rect.width - 1224) < 1 and abs(page.rect.height - 792) < 1
        content = normalized(page.get_text())
        selectable = len(content) >= 80
        extracted.append(content)
        status = "PASS" if size_ok and selectable else "FAIL"
        if status == "FAIL":
            results["status"] = "FAIL"
        results["checks"].append({"type": "page", "number": index, "status": status,
                                  "size_pt": [round(page.rect.width, 2), round(page.rect.height, 2)],
                                  "text_chars": len(content),
                                  "embedded_images": len(page.get_images(full=True)),
                                  "geometry_pass": size_ok, "selectable_text_pass": selectable})
    if args.private_manifest:
        m = json.loads(args.private_manifest.read_text(encoding="utf-8"))
        segments = m.get("exact_text_segments", {})
        checked = 0
        for key, paragraphs in segments.items():
            page_no = int(key)
            if page_no > len(extracted):
                results["status"] = "FAIL"
                results["checks"].append({"type": "copy", "page": page_no, "status": "FAIL",
                                          "reason": "missing page"})
                continue
            # The PDF may wrap source lines; only whitespace is normalized.
            for j, para in enumerate(paragraphs, 1):
                ok = normalized(para) in extracted[page_no - 1]
                checked += 1
                results["checks"].append({"type": "copy", "page": page_no, "paragraph": j,
                                          "status": "PASS" if ok else "FAIL"})
                if not ok:
                    results["status"] = "FAIL"
        results["copy_fidelity"] = ("PASS" if results["status"] == "PASS" else "FAIL") if checked else "NOT_TESTED"
    print(json.dumps(results, indent=2))
    raise SystemExit(1 if results["status"] == "FAIL" else 0)

if __name__ == "__main__":
    run()
