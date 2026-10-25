import importlib.util
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("boss_okf_query", HERE / "query.py")
query = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = query
spec.loader.exec_module(query)


class TestKnowledgePilot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = query.load_records()

    def test_three_public_safe_records(self):
        self.assertEqual({r["id"] for r in self.records}, {"pr-95", "pr-106", "pr-107"})

    def test_original_source_links_required(self):
        for record in self.records:
            self.assertTrue(record["sources"])
            self.assertTrue(all(s.startswith("https://github.com/") for s in record["sources"]))

    def test_no_false_independent_verification(self):
        self.assertFalse(any(r["verified"] for r in self.records))

    def test_bypass_retrieves_pr95(self):
        ids = [r["id"] for r in query.lexical("OpenBot direct transport bypass", self.records)]
        self.assertEqual(ids[0], "pr-95")

    def test_private_worker_retrieves_pr107(self):
        ids = [r["id"] for r in query.lexical("private SVG worker Inkscape", self.records)]
        self.assertEqual(ids[0], "pr-107")

    def test_unknown_question_refuses(self):
        self.assertEqual(query.lexical("quantum penguin asteroids", self.records), [])

    def test_pr106_is_merged_but_not_production_ready(self):
        r = next(r for r in self.records if r["id"] == "pr-106")
        self.assertEqual(r["status"], "active")
        self.assertIn("Production integration remains HOLD", r["body"])

    def test_drafts_are_not_promoted(self):
        for id_ in ("pr-95", "pr-107"):
            r = next(r for r in self.records if r["id"] == id_)
            self.assertEqual(r["status"], "draft")
            self.assertIn("HOLD", r["body"])


if __name__ == "__main__":
    unittest.main()
