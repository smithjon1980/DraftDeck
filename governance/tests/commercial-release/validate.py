"""Candidate BOSS release policy evaluator; does not verify external evidence or authorize deployment."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent
SCHEMA = json.loads((ROOT.parent.parent / "specs" / "boss-release-gate.schema.json").read_text())

def assess(r):
    errors = list(Draft202012Validator(SCHEMA).iter_errors(r))
    if errors:
        return "RELEASE_BLOCKED_SCHEMA"
    for key in ("input", "process", "output", "storage"):
        if r[key]["state"] != "OBSERVED" or not r[key]["evidence_refs"]:
            return "RELEASE_BLOCKED_EVIDENCE_DEFICIT"
    if r["controls"]["evidence"]["status"] != "PASS":
        return "RELEASE_BLOCKED_EVIDENCE_DEFICIT"
    if r["risk"]["tier"] in ("T3", "T4") and r["controls"]["specialist_referral"]["status"] != "PASS":
        return "RELEASE_BLOCKED_PENDING_SPECIALIST"
    if r["controls"]["privacy"]["status"] != "PASS" or not r["controls"]["privacy"]["evidence_refs"]:
        return "RELEASE_BLOCKED_PRIVACY_VIOLATION"
    if any(r["controls"][key]["status"] != "PASS" or not r["controls"][key]["evidence_refs"] for key in ("specialist_referral", "incident_route")):
        return "RELEASE_BLOCKED_CONTROL"
    if r["risk"]["tier"] == "UNKNOWN" or not r["risk"]["assessment_ref"] or not r["risk"]["reviewer"]:
        return "RELEASE_BLOCKED_RISK"
    if not r["authorization"]["human_approver"] or not r["authorization"]["approval_ref"] or r["disposition"] != "APPROVED":
        return "RELEASE_BLOCKED_AUTHORIZATION"
    # A mock reference never establishes approval; production approval needs trusted resolver.
    return "ELIGIBLE_FOR_INDEPENDENT_EVIDENCE_REVIEW"

def test_fixtures():
    expected = {
        "01_golden_path": "ELIGIBLE_FOR_INDEPENDENT_EVIDENCE_REVIEW",
        "02_anti_hallucination": "RELEASE_BLOCKED_EVIDENCE_DEFICIT",
        "03_unsigned_handoff": "RELEASE_BLOCKED_PENDING_SPECIALIST",
        "04_privacy_deficit": "RELEASE_BLOCKED_PRIVACY_VIOLATION",
    }
    for name, expected_status in expected.items():
        actual = assess(json.loads((ROOT / "fixtures" / (name + ".json")).read_text()))
        assert actual == expected_status, (name, actual, expected_status)
        print(name + ": " + actual)
    print("4/4 fixture outcomes matched; no real authorization validated.")

if __name__ == "__main__":
    test_fixtures()
