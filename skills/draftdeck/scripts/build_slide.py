#!/usr/bin/env python3
"""Retired legacy Canva/SVG builder. Fail closed; see skills/draftdeck/SKILL.md.

The active rendering trial uses Go templates, Tailwind CSS and Chromium.
This file is intentionally left as a guarded compatibility entry point so that
old automation cannot silently execute a deprecated pipeline.
"""
raise SystemExit(
    "RETIRED_PIPELINE: Python/Canva/SVG slide builder is not authorized. "
    "Use experiments/boss-go-tailwind-001 and skills/draftdeck/SKILL.md."
)
