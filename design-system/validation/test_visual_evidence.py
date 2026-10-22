#!/usr/bin/env python3
"""Deterministic positive and negative contract fixtures; no user art needed."""
import copy
import unittest
from check_visual_evidence import ARTIFACTS, GATES, validate

def candidate():
    return {
        "schema_version": "1",
        "profile": "slide",
        "source_commit": "example-sha-for-structural-fixture",
        "artifacts": {k: {"status": "NOT_TESTED"} for k in ARTIFACTS},
        "gates": {k: "NOT_TESTED" for k in GATES},
        "release_state": "HOLD",
        "human_authorization": "PENDING",
    }

class EvidenceContractTests(unittest.TestCase):
    def test_unverified_candidate_is_explicitly_held(self):
        self.assertEqual([], validate(candidate()))
    def test_no_silent_authorization(self):
        data = candidate()
        data["release_state"] = "APPROVED"
        self.assertTrue(validate(data))
    def test_missing_evidence_status_fails(self):
        data = candidate()
        del data["artifacts"]["browser_render_capture"]
        self.assertTrue(validate(data))
    def test_unbacked_pass_fails(self):
        data = candidate()
        data["artifacts"]["browser_render_capture"] = {"status": "PASS"}
        self.assertTrue(validate(data))
    def test_visual_pass_requires_comparison(self):
        data = candidate()
        data["gates"]["layout"] = "PASS"
        self.assertTrue(validate(data))
    def test_unapproved_source_fails(self):
        data = candidate()
        data["gates"]["source"] = "PASS"
        self.assertTrue(validate(data))
    def test_complete_record_is_still_on_hold(self):
        data = candidate()
        for key in ("browser_render_capture", "side_by_side_comparison", "difference_annotations"):
            data["artifacts"][key] = {"status": "PASS", "evidence_ref": "private:sha256:fixture"}
        data["gates"]["layout"] = "PASS"
        self.assertEqual([], validate(data))

if __name__ == "__main__":
    unittest.main()
