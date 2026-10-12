"""Windmill-compatible discovery entry point. No tool execution until adapters are audited."""
from __future__ import annotations
from typing import Any

OPERATIONS = {
    "vtracer": {"trace_color_svg"},
    "opencv": {"inspect_geometry"},
    "sam2": {"segment_objects"},
    "tesseract": {"audit_text_ocr"},
    "potrace": {"trace_monochrome"},
    "imagemagick": {"prepare_raster"},
    "resvg": {"render_svg_preview"},
}
REQUIRED_LAYERS = ("background_geometry", "art_story", "editable_typography")


def main(tool_id: str, operation: str, slide_id: str, source_ref: str,
         layer_manifest: dict[str, Any] | None = None, execute: bool = False) -> dict[str, Any]:
    if tool_id not in OPERATIONS:
        return {"status": "REJECTED", "reason": "unknown_tool", "allowed_tools": sorted(OPERATIONS)}
    if operation not in OPERATIONS[tool_id]:
        return {"status": "REJECTED", "reason": "unknown_operation", "allowed_operations": sorted(OPERATIONS[tool_id])}
    if not slide_id or not source_ref:
        return {"status": "REJECTED", "reason": "slide_id_and_source_ref_required"}
    missing = [key for key in REQUIRED_LAYERS if not isinstance(layer_manifest, dict) or key not in layer_manifest]
    if missing:
        return {"status": "REJECTED", "reason": "missing_three_layer_manifest", "missing": missing}
    if execute:
        return {"status": "BLOCKED", "reason": "execution_adapter_not_installed_or_verified", "tool_id": tool_id}
    return {"status": "PLAN_ONLY", "tool_id": tool_id, "operation": operation,
            "slide_id": slide_id, "source_ref": source_ref,
            "layer_policy": "three_layers_and_native_editable_text_required",
            "next_gate": "Install, pin, license-review, sandbox, test, then authorize execution adapter."}
