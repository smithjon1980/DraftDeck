#!/usr/bin/env python3
"""Synthetic (no unpublished script) tests for manuscript integrity gates."""
import hashlib
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
target = ROOT / "tools/editorial-layout/check_editorial_manuscript.py"
spec = importlib.util.spec_from_file_location("editorial_gate", target)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

PARA = ("A drawing does not prove operation. ", "Inspection requires a separate record.")


def fixture(cols=1):
    manifest = {
        "expected_columns": cols,
        "expected_words": len("\n\n".join(PARA).split()),
        "paragraphs": [
            {"id": f"EP01_P{i+1:03}", "sha256": hashlib.sha256(t.encode()).hexdigest()}
            for i, t in enumerate(PARA)
        ],
        "source_sha256": hashlib.sha256("\n\n".join(PARA).encode()).hexdigest(),
    }
    opening = "<main>" + "".join(
        f'<section class="copy-col" data-col="{i}">' for i in range(cols)
    )
    spoken = "".join(
        f'<p class="spoken" data-para-id="EP01_P{i+1:03}" data-run="{i}">{t}</p>'
        for i, t in enumerate(PARA)
    )
    return opening + spoken + "</main>", manifest


class ManuscriptGateTests(unittest.TestCase):
    def test_columns_1_through_4(self):
        for n in (1, 2, 3, 4):
            with self.subTest(columns=n):
                markup, m = fixture(n)
                value = gate.evaluate(markup, m)
                self.assertEqual(value["errors"], [])
                self.assertFalse(value["release_authorized"])

    def test_critical_negation_removed(self):
        markup, m = fixture()
        value = gate.evaluate(markup.replace("does not prove", "does prove"), m)
        self.assertIn("paragraph hash mismatch", str(value["errors"]))

    def test_missing_paragraph(self):
        markup, m = fixture()
        markup = markup.replace(
            f'<p class="spoken" data-para-id="EP01_P002" data-run="1">{PARA[1]}</p>',
            "",
        )
        self.assertEqual(gate.evaluate(markup, m)["status"], "HOLD")

    def test_fake_baked_manuscript_image(self):
        markup, m = fixture()
        markup = markup.replace(
            f'<p class="spoken" data-para-id="EP01_P002" data-run="1">{PARA[1]}</p>',
            '<img src="full-slide.png">',
        )
        self.assertEqual(gate.evaluate(markup, m)["status"], "HOLD")

    def test_svg_text_does_not_replace_native_manuscript(self):
        markup, m = fixture()
        markup = markup.replace(
            f'<p class="spoken" data-para-id="EP01_P002" data-run="1">{PARA[1]}</p>',
            f"<svg><text>{PARA[1]}</text></svg>",
        )
        self.assertEqual(gate.evaluate(markup, m)["status"], "HOLD")

    def test_wrong_column_count(self):
        markup, m = fixture(3)
        m["expected_columns"] = 4
        self.assertIn("column count", str(gate.evaluate(markup, m)["errors"]))

    def test_wrong_segment_index(self):
        markup, m = fixture()
        markup = markup.replace('data-run="0"', 'data-run="11"')
        self.assertIn("fragment order", str(gate.evaluate(markup, m)["errors"]))

    def test_nonspoken_title_not_counted(self):
        markup, m = fixture()
        markup = "<h1>Not spoken by the narrator</h1>" + markup
        self.assertEqual(gate.evaluate(markup, m)["errors"], [])

    def test_duplicate_manifest_id(self):
        markup, m = fixture()
        m["paragraphs"].append(m["paragraphs"][0])
        self.assertEqual(gate.evaluate(markup, m)["status"], "HOLD")

    def test_changed_word_fails(self):
        markup, m = fixture()
        self.assertEqual(gate.evaluate(markup.replace("record.", "receipt."), m)["status"], "HOLD")


if __name__ == "__main__":
    unittest.main()
