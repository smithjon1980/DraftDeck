"""BOSS V4 — candidate JSON Schema structural fixture checks only."""
from pathlib import Path
import json
from jsonschema import Draft202012Validator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
schema = json.loads((ROOT / "schemas/work-commission-v4.schema.json").read_text(encoding="utf-8"))
Draft202012Validator.check_schema(schema)
validator = Draft202012Validator(schema)

def test_valid_draft():
    sample = json.loads((HERE / "fixtures/valid_draft.json").read_text(encoding="utf-8"))
    assert validator.is_valid(sample), "Synthetic Section 6 specimen must pass"
    assert sample["status"] == "DRAFT"
    assert sample["authority_ref"].endswith("PENDING")

def test_invalid_fixtures():
    names = sorted((HERE / "fixtures").glob("invalid_*.json"))
    assert len(names) == 6, f"Expected six negative fixtures, got {len(names)}"
    for path in names:
        payload = json.loads(path.read_text(encoding="utf-8"))
        assert not validator.is_valid(payload), f"Invalid fixture unexpectedly passed: {path.name}"

def run():
    test_valid_draft()
    test_invalid_fixtures()
    print("PASS: 1 synthetic valid fixture and 6 invalid fixtures; structure only.")
    print("NOT ESTABLISHED: authentication, authorization, state transitions or implementation QA.")

if __name__ == "__main__":
    run()
