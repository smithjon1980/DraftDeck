#!/usr/bin/env python3
"""BOSS preliminary raster evidence brand guard. NOT a visual or print approval.

Requires Pillow and NumPy. A detected canonical logo source plus color pixels
is necessary, but never sufficient, for exact logo identity in the composition:
a human must visually inspect the output and approve each page.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image

EXPECTED_SHA = "95f56729fe279a07b151ba5169a764a0aa387a1fac8cf283424ea783f950b146"
CYAN = np.array([0, 188, 235], dtype=np.float32)
MAGENTA = np.array([227, 0, 116], dtype=np.float32)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--original-logo", type=Path, required=True,
                    help="Unmodified canonical BOSS original JPEG binary")
    ap.add_argument("page_png", type=Path, nargs="+",
                    help="Actual rendered screenshots, not just source CSS")
    args = ap.parse_args()
    sha = hashlib.sha256(args.original_logo.read_bytes()).hexdigest()
    result = {"status": "PASS", "source_logo_sha": sha,
              "source_logo_match": sha == EXPECTED_SHA,
              "pages": [], "human_visual_acceptance": "NOT_TESTED"}
    if sha != EXPECTED_SHA:
        result["status"] = "FAIL"
    for path in args.page_png:
        rgb = np.asarray(Image.open(path).convert("RGB")).reshape(-1, 3).astype(np.float32)
        chroma = rgb.max(axis=1) - rgb.min(axis=1)
        colored = (chroma > 50) & (rgb.max(axis=1) < 250)
        d_cyan = np.linalg.norm(rgb - CYAN, axis=1)
        d_magenta = np.linalg.norm(rgb - MAGENTA, axis=1)
        cyan = int((colored & (d_cyan < 60)).sum())
        magenta = int((colored & (d_magenta < 60)).sum())
        other = int((colored & (np.minimum(d_cyan, d_magenta) > 110)).sum())
        other_limit = max(1000, int(len(rgb) * .002))
        status = "PASS" if cyan >= 35 and magenta >= 35 and other <= other_limit else "FAIL"
        if status == "FAIL":
            result["status"] = "FAIL"
        result["pages"].append({
            "file": str(path), "status": status,
            "near_cyan_px": cyan, "near_magenta_px": magenta,
            "other_colored_px": other, "other_colored_limit": other_limit,
        })
    print(json.dumps(result, indent=2))
    raise SystemExit(1 if result["status"] == "FAIL" else 0)


if __name__ == "__main__":
    main()
