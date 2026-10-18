#!/usr/bin/env python3
"""Preliminary Episode 01 print proof logo placement test.

Checks actual PNG screenshots for BOTH canonical accent colors in the lower
right corner. Run together with check_brand_proof.py, which verifies the
unmodified canonical logo source SHA and overall palette. Neither test
authenticates the placement's artwork or replaces a human visual review.

Usage:
  python tools/visual-poc/check_print_logo_placement.py page_1.png page_2.png
Requires Pillow; no installer, network access, or private source in the repo.
"""
import argparse
import json
from pathlib import Path
from PIL import Image

COLORS = {"cyan": (0, 188, 235), "magenta": (227, 0, 116)}


def near(rgb, expected):
    return sum((rgb[i] - expected[i]) ** 2 for i in range(3)) < 60 ** 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("images", type=Path, nargs="+")
    args = ap.parse_args()
    result = {"status": "PASS", "placement": "bottom-right",
              "human_visual_approval": "NOT_TESTED", "pages": []}
    for path in args.images:
        im = Image.open(path).convert("RGB")
        w, h = im.size
        # Reserve the lower-right corner, away from BOSS's upper-left rule
        # and other editorial accents. Tested with 1632x1056 private proof.
        roi = im.crop((int(w * .73), int(h * .80), w, h))
        px = list(roi.getdata())
        counts = {key: sum(near(c, color) for c in px)
                  for key, color in COLORS.items()}
        good = all(counts[key] >= 60 for key in COLORS)
        if not good:
            result["status"] = "FAIL"
        result["pages"].append({
            "file": str(path), "status": "PASS" if good else "FAIL",
            "corner_counts": counts, "image_size": [w, h]})
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
