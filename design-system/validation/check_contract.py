#!/usr/bin/env python3
"""BOSS design contract: schema, cross-file parity and rejection fixtures.
No claim of visual fidelity, adapter editability or human approval.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
CONTRACT = ROOT / "design-system" / "boss-design-contract.json"
CSS = ROOT / "design-system" / "tokens" / "tokens.css"
COMPONENTS = ROOT / "design-system" / "components.md"

def checks(contract, css, components):
    errors = []
    if contract.get("status") != "CANDIDATE_PENDING_HUMAN_REVIEW":
        errors.append("Design contract may not imply human approval")
    brand = contract.get("brand", {})
    required = {
        "--boss-color-ground": brand.get("ground"),
        "--boss-color-ink": brand.get("ink"),
        "--boss-color-brand-cyan": brand.get("cyan"),
        "--boss-color-brand-magenta": brand.get("magenta"),
    }
    css_vars = dict(re.findall(r"(?m)^\s*(--boss-[\w-]+):\s*([^;]+);", css))
    for k, v in required.items():
        if not re.fullmatch(r"#[\da-fA-F]{6}", str(v)):
            errors.append(f"Invalid contract color {k}: {v}")
        if css_vars.get(k, "").strip().lower() != str(v).lower():
            errors.append(f"CSS disagrees with contract: {k}")
    slide = contract.get("profiles", {}).get("slide", {})
    w, h = slide.get("width_px"), slide.get("height_px")
    if (w, h) != (1920, 1080) or w * 9 != h * 16:
        errors.append("Current BOSS slide must be 1920x1080 16:9")
    for key, expected in (("--boss-canvas-width", "1920px"), ("--boss-canvas-height", "1080px")):
        if css_vars.get(key) != expected:
            errors.append(f"Slide CSS wrong or missing {key}")
    if not re.search(r"\.boss-slide-profile\s*\{", css):
        errors.append("Slide dimensions must be scoped to slide profile")
    if "width_px" not in contract.get("profiles", {}).get("web", {}):
        errors.append("Web output needs an independent profile")
    if contract.get("authority", {}).get("logo_source_sha256") is not None:
        value = contract["authority"]["logo_source_sha256"]
        if not re.fullmatch(r"[0-9a-fA-F]{64}", str(value)):
            errors.append("Logo hash must be SHA-256 or null")
    if re.search(r"(?i)\b(cargo|freight|parcel|aircraft|cockpit)\b", components):
        errors.append("Active component registry contains retired storytelling vocabulary")
    for item in contract.get("components", []):
        if not re.search(r"(?m)^\|\s*" + re.escape(item) + r"\s*\|", components):
            errors.append(f"Missing declared component: {item}")
    return errors

def run():
    obj = json.loads(CONTRACT.read_text(encoding="utf-8"))
    css = CSS.read_text(encoding="utf-8")
    comps = COMPONENTS.read_text(encoding="utf-8")
    errors = checks(obj, css, comps)
    assert not errors, "\n".join(errors)

    # Required negative fixtures must fail, never silently pass.
    changed = json.loads(json.dumps(obj))
    changed["profiles"]["slide"]["width_px"] = 1632
    assert checks(changed, css, comps), "invalid canvas unexpectedly passed"
    changed = json.loads(json.dumps(obj))
    changed["status"] = "APPROVED"
    assert checks(changed, css, comps), "implied approval unexpectedly passed"
    assert checks(obj, css.replace("#E30074", "#B34700"), comps), "wrong brand accent unexpectedly passed"
    assert checks(obj, css, comps + "\n| CargoCard | unsupported | n/a | n/a |\n"), "obsolete vocabulary unexpectedly passed"
    print("BOSS design contract structural checks PASS; visual QA NOT_ESTABLISHED; human approval PENDING")

if __name__ == "__main__":
    run()
