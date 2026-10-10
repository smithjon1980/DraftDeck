"""Offline contract tests. These do not establish live Windmill tool availability."""
import importlib.util
from pathlib import Path

module_path = Path(__file__).resolve().parents[1] / "windmill" / "commanders_kit.py"
spec = importlib.util.spec_from_file_location("commanders_kit", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
manifest = {"background_geometry": {}, "art_story": {}, "editable_typography": {}}

def test_discovery_contract_for_all_seven():
    assert len(module.OPERATIONS) == 7
    for tool_id, operations in module.OPERATIONS.items():
        for operation in operations:
            result = module.main(tool_id, operation, "S01", "source:v1", manifest)
            assert result["status"] == "PLAN_ONLY"

def test_missing_layer_rejected():
    result = module.main("opencv", "inspect_geometry", "S01", "source:v1", {"art_story": {}})
    assert result["status"] == "REJECTED"
    assert "missing_three_layer_manifest" == result["reason"]

def test_unlisted_operation_rejected():
    result = module.main("opencv", "arbitrary_shell", "S01", "source:v1", manifest)
    assert result["status"] == "REJECTED"

def test_execute_remains_blocked_until_verified():
    result = module.main("opencv", "inspect_geometry", "S01", "source:v1", manifest, execute=True)
    assert result["status"] == "BLOCKED"
