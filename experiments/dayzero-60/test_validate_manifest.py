import hashlib
import tempfile
import unittest
from pathlib import Path

from validate_manifest import validate


def specimen(root):
    slides = []
    for i in range(4):
        slides.append({"slide": i + 1, "type": "orientation",
                       "status": "CANDIDATE_UNPUBLISHED_NOT_MUSE_GENERATED"})
    for studio in range(1, 9):
        fname = f"STUDIO{studio:02d}.md"
        original = ("## Topic\n\nThe exact source statement belongs here.\n").encode("utf-8")
        (root / fname).write_bytes(original)
        sha = hashlib.sha256(original).hexdigest()
        slides.append({"slide": len(slides)+1, "studio": studio, "type": "studio_open",
                       "source_file": fname, "source_sha256": sha,
                       "source_section": "Topic", "verbatim_source_excerpts": []})
        for _ in range(6):
            slides.append({"slide": len(slides)+1, "studio": studio, "type": "instruction",
                           "source_file": fname, "source_sha256": sha,
                           "source_section": "Topic",
                           "verbatim_source_excerpts": ["The exact source statement belongs here."]})
    return {"status": "PRIVATE_CANDIDATE_NOT_MUSE_GENERATED", "slides": slides}


class TestDayZeroStructure(unittest.TestCase):
    def test_full_60_and_source_provenance(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = specimen(Path(tmp))
            report = validate(doc, tmp)
            self.assertEqual(report["status"], "PASS")
            self.assertEqual(report["slides"], 60)
            self.assertEqual(report["private_source_excerpts_compared"], 48)

    def test_short_deck_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = specimen(Path(tmp))
            doc["slides"].pop()
            self.assertIn("SLIDE_COUNT_NOT_60", validate(doc)["errors"])

    def test_wrong_studio_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = specimen(Path(tmp))
            doc["slides"][11]["studio"] = 1
            self.assertTrue(any(x.startswith("STUDIO_SEQUENCE_MISMATCH:")
                                for x in validate(doc)["errors"]))

    def test_text_not_in_source_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = specimen(Path(tmp))
            doc["slides"][5]["verbatim_source_excerpts"] = ["Invented output."]
            self.assertIn("UNSUPPORTED_SOURCE_EXCERPT:6",
                          validate(doc, tmp)["errors"])

    def test_source_checksum_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = specimen(Path(tmp))
            doc["slides"][5]["source_sha256"] = "bad-sha"
            self.assertIn("SOURCE_HASH_MISMATCH:6",
                          validate(doc, tmp)["errors"])


if __name__ == "__main__":
    unittest.main()
