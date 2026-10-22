#!/usr/bin/env python3
"""Negative-fixture tests: a metadata-only gate cannot authorize release."""
import importlib.util
import json
import pathlib
import tempfile
import unittest

SRC = pathlib.Path(__file__).resolve().parents[1] / "tools" / "visual-poc" / "check_evidence_manifest.py"
spec = importlib.util.spec_from_file_location("evidence_gate", SRC)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

class EvidenceGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = pathlib.Path(self.temp.name)
        self.artifacts = {k: k + ".txt" for k in gate.ARTIFACT_KEYS}
        for p in self.artifacts.values():
            (self.root / p).write_text("sample evidence")
        self.data = {
            "candidate_id":"EP01-test", "source_commit":"012345", "profile":"slide",
            "source_reference":"candidate-script", "dimensions":{"width":1920,"height":1080},
            "reference_status":"REFERENCE_UNAPPROVED",
            "artifacts":dict(self.artifacts),
            "checks":{k:"NOT_TESTED" for k in gate.GATES},
            "human_review":{"decision":"PENDING"}
        }

    def check(self):
        return gate.validate(self.data, self.root)

    def test_hold_is_valid_but_not_approved(self):
        errors, ready = self.check()
        self.assertEqual(errors, [])
        self.assertFalse(ready)

    def test_absent_browser_capture_rejected(self):
        (self.root / self.artifacts["browser_render"]).unlink()
        self.assertTrue(self.check()[0])

    def test_path_traversal_rejected(self):
        self.data["artifacts"]["browser_render"] = "../escape.png"
        self.assertTrue(self.check()[0])

    def test_bad_dimensions_rejected(self):
        self.data["dimensions"]["width"] = 1280
        self.assertTrue(self.check()[0])

    def test_unapproved_reference_blocks_next_gate(self):
        self.data["checks"] = {k:"PASS" for k in gate.GATES}
        self.data["human_review"] = {"decision":"APPROVED_FOR_NEXT_GATE", "reviewer":"person",
          "reviewed_at":"2026-10-21T00:00:00Z", "candidate_sha256":"f"*64, "scope":"page"}
        self.assertFalse(self.check()[1])

    def test_approved_reference_requires_file(self):
        self.data["reference_status"] = "APPROVED"
        self.assertTrue(self.check()[0])

    def test_eligible_is_not_release(self):
        self.data["reference_status"] = "APPROVED"
        self.data["artifacts"]["approved_reference"] = "approved.png"
        (self.root / "approved.png").write_bytes(b"test")
        self.data["checks"] = {k:"PASS" for k in gate.GATES}
        self.data["human_review"] = {"decision":"APPROVED_FOR_NEXT_GATE","reviewer":"person",
          "reviewed_at":"2026-10-21T00:00:00Z","candidate_sha256":"f"*64,"scope":"page"}
        self.assertEqual(self.check(), ([], True))

if __name__ == "__main__":
    unittest.main()
