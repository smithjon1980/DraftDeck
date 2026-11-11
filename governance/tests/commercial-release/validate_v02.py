"""Validate candidate v0.2 fixture logic only. No actual deployment authorization."""
import json
from pathlib import Path

FIX = Path(__file__).parent / "fixtures-v02"

def evaluate(d):
    e, p, a = d["evidence_chain"], d["privacy_controls"], d["authorization"]
    if e.get("split_signal_detected") is True and e.get("signal_divergence", {}).get("generated_claim") and e.get("signal_divergence", {}).get("ground_truth_evidence"):
        return "RELEASE_BLOCKED_SPLIT_SIGNAL"
    if e.get("status") != "COMPLETE" or e.get("ipos_trace_verified") is not True or e.get("missing_nodes"):
        return "RELEASE_BLOCKED_EVIDENCE_DEFICIT"
    if a.get("engineering_signoff_required") and a.get("engineering_signoff_recorded") is not True:
        return "RELEASE_BLOCKED_PENDING_SPECIALIST"
    if p.get("retention_schedule_defined") is not True or p.get("minimization_tags_applied") is not True:
        return "RELEASE_BLOCKED_PRIVACY_VIOLATION"
    if a.get("human_approval_recorded") is not True:
        return "RELEASE_BLOCKED_AUTHORIZATION"
    return "RELEASE_ELIGIBLE_FOR_TRUSTED_AUTHORIZATION_CHECK"

cases = {
    "01_golden_path": "RELEASE_ELIGIBLE_FOR_TRUSTED_AUTHORIZATION_CHECK",
    "02a_evidence_deficit": "RELEASE_BLOCKED_EVIDENCE_DEFICIT",
    "02b_split_signal_error": "RELEASE_BLOCKED_SPLIT_SIGNAL",
    "03_unsigned_handoff": "RELEASE_BLOCKED_PENDING_SPECIALIST",
    "04_privacy_deficit": "RELEASE_BLOCKED_PRIVACY_VIOLATION",
}

if __name__ == "__main__":
    for stem, expected in cases.items():
        actual = evaluate(json.loads((FIX / (stem + ".json")).read_text()))
        assert actual == expected, (stem, actual, expected)
        print(stem, actual, "PASS")
    print("5/5 fixture classifications matched; production authorization NOT ESTABLISHED.")
