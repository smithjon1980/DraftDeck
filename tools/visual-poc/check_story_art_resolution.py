#!/usr/bin/env python3
"""Bounded story-art pixel-density gate using MEASURED browser DOM images.

Requires actual 1920x1080 browser measurements (natural image and display sizes).
Does not establish story meaning, source authority, adapter editability or release.
"""
import argparse
import json
from pathlib import Path
import sys

MIN_SOURCE_PIXEL_PER_DISPLAY_PX = 1.0
ALLOWED_FIT = {"cover", "contain", "fill", "none"}

def evaluate(data):
    errors, records = [], []
    if not isinstance(data, dict):
        return ["measurements must be an object"], records
    if data.get("profile") != "slide" or data.get("viewport") != [1920, 1080]:
        errors.append("expected actual slide render viewport 1920x1080")
    images = data.get("images")
    if not isinstance(images, list):
        return errors + ["images must be an array"], records
    art = [x for x in images if isinstance(x, dict) and x.get("role") == "story-art"]
    if not art:
        errors.append("no measured story-art image")
    for i, item in enumerate(art):
        values = [item.get(k) for k in
                  ("natural_width", "natural_height", "display_width", "display_height")]
        if not all(type(v) in (int, float) and v > 0 for v in values):
            errors.append(f"story art {i}: invalid intrinsic/display dimensions")
            continue
        fit = item.get("object_fit")
        if fit not in ALLOWED_FIT:
            errors.append(f"story art {i}: unsupported object-fit")
            continue
        nw, nh, dw, dh = values
        if fit in ("cover", "fill"):
            density = min(nw / dw, nh / dh)
        elif fit == "contain":
            density = max(nw / dw, nh / dh)
        else:
            density = 1.0  # none retains source pixels, but may crop; inspect manually.
        records.append({"role": "story-art",
                        "source_pixels_per_css_pixel": round(density, 4),
                        "source": [nw, nh], "display": [dw, dh], "fit": fit})
        if density < MIN_SOURCE_PIXEL_PER_DISPLAY_PX:
            errors.append(f"story art {i}: upscaled source ({density:.3f} source px per displayed CSS px)")
    return errors, records

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("browser_metrics_json", type=Path)
    args = parser.parse_args()
    try:
        errors, records = evaluate(json.loads(args.browser_metrics_json.read_text(encoding="utf-8")))
    except (OSError, ValueError) as exc:
        errors, records = [str(exc)], []
    print(json.dumps({"status": "HOLD" if errors else "PIXEL_DENSITY_READY_FOR_VISUAL_REVIEW",
                      "errors": errors, "records": records,
                      "visual_story_approved": False,
                      "release_authorized": False}, indent=2))
    sys.exit(2 if errors else 0)

if __name__ == "__main__":
    main()
