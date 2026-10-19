#!/usr/bin/env python3
"""Offline contract tests. Schema validity != engine render, semantics or approval.

No customer sources, model calls, protected secrets, or downloaded binaries.
"""
import copy
import json
import pathlib
import unittest
from jsonschema import Draft202012Validator, ValidationError

ROOT = pathlib.Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas/slide-manifest.schema.json"
EXAMPLE_PATH = ROOT / "tests/diagram-golden-paths/example-slide.json"
MERMAID_THEME = ROOT / "design-system/diagram/mermaid-theme.json"
DIAGRAM_CSS = ROOT / "design-system/diagram/boss-diagram.css"
TOKENS = ROOT / "design-system/tokens/tokens.css"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


class ContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = load(SCHEMA_PATH)
        Draft202012Validator.check_schema(cls.schema)
        cls.validator = Draft202012Validator(cls.schema)
        cls.fixture = load(EXAMPLE_PATH)

    def assert_invalid(self, obj):
        with self.assertRaises(ValidationError):
            self.validator.validate(obj)

    def test_synthetic_candidate_passes_structural_schema(self):
        self.validator.validate(self.fixture)

    def test_only_draft_2020_12(self):
        self.assertEqual(self.schema["$schema"],
                         "https://json-schema.org/draft/2020-12/schema")

    def test_unapproved_markers_cannot_be_promoted_by_model(self):
        for path, value in [
            (("qa", "syntax"), "PASS"),
            (("qa", "visual"), "PASS"),
            (("qa", "human_approval"), "APPROVED"),
            (("candidate_status",), "RELEASED"),
        ]:
            with self.subTest(path=path):
                obj = copy.deepcopy(self.fixture)
                pointer = obj
                for key in path[:-1]:
                    pointer = pointer[key]
                pointer[path[-1]] = value
                self.assert_invalid(obj)

    def test_route_rejects_different_diagram_kind(self):
        obj = copy.deepcopy(self.fixture)
        obj["diagram_kind"] = "plantuml-sequence"
        obj["diagram_source"]["language"] = "plantuml"
        self.assert_invalid(obj)

    def test_language_matches_kind(self):
        obj = copy.deepcopy(self.fixture)
        obj["diagram_source"]["language"] = "plantuml"
        self.assert_invalid(obj)

    def test_no_diagram_is_legal_for_editorial_slide(self):
        obj = copy.deepcopy(self.fixture)
        obj["slide_role"] = "editorial"
        obj["teaching_objective"] = "no-diagram"
        obj["diagram_kind"] = "none"
        obj["diagram_source"] = None
        obj["art"]["treatment"] = "technical-engraving"
        self.validator.validate(obj)
        obj["diagram_source"] = self.fixture["diagram_source"]
        self.assert_invalid(obj)

    def test_all_required_diagram_families_covered(self):
        mapping = {
            "entity-state": ("plantuml-state", "plantuml"),
            "service-interaction": ("plantuml-sequence", "plantuml"),
            "roles-permissions": ("plantuml-usecase", "plantuml"),
            "business-handoffs": ("bpmn", "bpmn-xml"),
            "business-rules": ("dmn", "dmn-xml"),
            "system-architecture": ("c4-structurizr", "structurizr"),
            "root-cause": ("mece-tree", "json-tree"),
            "facility-mechanics": ("iso-technical", "illustration-spec"),
        }
        for objective, (kind, language) in mapping.items():
            with self.subTest(objective=objective):
                obj = copy.deepcopy(self.fixture)
                obj["teaching_objective"] = objective
                obj["diagram_kind"] = kind
                obj["diagram_source"] = {"mode": "inline", "language": language,
                                          "body": "Synthetic nonexecuting illustration source"}
                self.validator.validate(obj)

    def test_brand_and_render_master_are_immutable_in_candidate(self):
        for field, value in [
            ("ground", "#00284D"),
            ("cyan", "#00ABCD"),
            ("magenta", "#EEAA00"),
            ("retired_waveform", True),
            ("identity", "MSC"),
        ]:
            with self.subTest(field=field):
                obj = copy.deepcopy(self.fixture)
                obj["brand"][field] = value
                self.assert_invalid(obj)
        obj = copy.deepcopy(self.fixture)
        obj["profile"]["render_master"] = "pdf-drawing-engine"
        self.assert_invalid(obj)

    def test_missing_provenance_and_extra_authority_rejected(self):
        obj = copy.deepcopy(self.fixture)
        del obj["source"]["section"]
        self.assert_invalid(obj)
        obj = copy.deepcopy(self.fixture)
        obj["authorized_for_release"] = True
        self.assert_invalid(obj)

    def test_bad_path_or_unknown_extension_rejected(self):
        for path in ["../private.md", "diagrams/../../secret.mmd",
                     "https://example.com/diagram.svg", "diagrams/my.mjs"]:
            with self.subTest(path=path):
                obj = copy.deepcopy(self.fixture)
                obj["diagram_source"]["path"] = path
                self.assert_invalid(obj)

    def test_theme_is_white_ground_and_matches_repo_design_tokens(self):
        theme = load(MERMAID_THEME)
        tv = theme["themeVariables"]
        contract_tokens = TOKENS.read_text(encoding="utf-8")
        self.assertEqual(theme["theme"], "base")
        self.assertEqual(theme["securityLevel"], "strict")
        for value in ["#FFFFFF", "#000000", "#00BCEB", "#E30074"]:
            self.assertIn(value, contract_tokens)
        self.assertEqual(tv["background"], "#FFFFFF")
        self.assertEqual(tv["primaryColor"], "#FFFFFF")
        self.assertEqual(tv["primaryTextColor"], "#000000")
        self.assertEqual(tv["lineColor"], "#000000")

    def test_css_is_scoped_and_does_not_redraw_slide_or_logo(self):
        css = DIAGRAM_CSS.read_text(encoding="utf-8")
        self.assertIn(".boss-diagram", css)
        self.assertIn("var(--boss-color-ground", css)
        self.assertNotIn("dangerouslySetInnerHTML", css)


if __name__ == "__main__":
    unittest.main(verbosity=2)
