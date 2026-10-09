"""Regression checks for prohibited copy, operational wording and narrow exceptions."""

from pathlib import Path
import subprocess
import tempfile
import unittest

from check_operational_language import COMPARISON_ROWS, CONTRACT_FILES, findings


class OperationalLanguageTests(unittest.TestCase):
    def test_prohibited_copy(self):
        examples = (
            "A hallucination appeared in the output.",
            "The AI hallucinated.",
            "Hallucinating output is acceptable.",
            "An AI brain performs the task.",
            "The AI's brain performs the task.",
            "THE AI WANTS permission.",
            "The AI understands the assignment.",
            "The AI understood the assignment.",
            "The AI decided to release it.",
            "The AI knows the answer.",
            "The model understands the assignment.",
            "The model decides to release it.",
            "AI thinks it has finished.",
            "The model believes the source.",
            "The AI intends to act.",
            "The AI\nknows the answer.",
            "The **AI** knows the answer.",
            "The <strong>AI</strong> knows the answer.",
        )
        for example in examples:
            with self.subTest(example=example):
                self.assertTrue(findings("lesson.md", example))

    def test_operational_and_human_subjects(self):
        examples = (
            "The model returned a candidate.",
            "The system executed the authorized operation.",
            "The AI classified the package.",
            "The model inferred a likely route.",
            "The model's tone is not evidence of execution.",
            "The human understands the assignment and decided to release it.",
            "The model does not possess release authority.",
            "The aimodel knows field is not a software subject.",
            "The AI knowingly field is not a matched verb.",
        )
        for example in examples:
            with self.subTest(example=example):
                self.assertEqual([], findings("lesson.md", example))

    def test_comparison_rows_only_in_contracts(self):
        for path in CONTRACT_FILES:
            for row in COMPARISON_ROWS:
                with self.subTest(path=path, row=row):
                    self.assertEqual([], findings(path, row + "\n"))
                    self.assertTrue(findings("lesson.md", row + "\n"))
                    self.assertTrue(findings(path, row.replace(" | ", " | added ", 1)))

    def test_remaining_contract_copy_is_protected(self):
        text = next(iter(COMPARISON_ROWS)) + "\n\nThe AI knows the answer.\n"
        for path in CONTRACT_FILES:
            self.assertEqual(3, findings(path, text)[0][0])

    def test_guard_and_fixture_meta_files(self):
        for path in (
            ".github/scripts/check_operational_language.py",
            ".github/scripts/test_operational_language.py",
        ):
            self.assertEqual([], findings(path, "The AI knows the answer."))
        self.assertTrue(findings(".github/scripts/other.py", "The AI knows the answer."))

    def test_multiline_diagnostics(self):
        result = findings("lesson.html", "Allowed copy.\nThe AI\nunderstands the assignment.")
        self.assertEqual(2, result[0][0])

    def test_cli_checks_tracked_formats_and_returns_failure(self):
        script = Path(__file__).with_name("check_operational_language.py").resolve()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            for suffix in ("md", "py", "html", "css"):
                (root / f"fixture.{suffix}").write_text("The AI knows the answer.\n")
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            result = subprocess.run(
                ["python3", str(script)], cwd=root, text=True, capture_output=True
            )
            self.assertEqual(1, result.returncode)
            for suffix in ("md", "py", "html", "css"):
                self.assertIn(f"fixture.{suffix}:1:", result.stdout)
                (root / f"fixture.{suffix}").write_text("The model returned a candidate.\n")
            # Untracked drafts and binary renditions are outside this text guard.
            (root / "draft.md").write_text("The AI knows the answer.\n")
            (root / "review.pdf").write_bytes(b"The AI knows the answer.")
            subprocess.run(["git", "add", "review.pdf"], cwd=root, check=True)
            result = subprocess.run(
                ["python3", str(script)], cwd=root, text=True, capture_output=True
            )
            self.assertEqual(0, result.returncode)
            self.assertIn("4 tracked text files checked", result.stdout)


if __name__ == "__main__":
    unittest.main()
