#!/usr/bin/env python3
"""Offline regression: a logo-only slide cannot pass the story/art handoff."""
import base64
import copy
import hashlib
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "story_layers", ROOT / "tools" / "visual-poc" / "check_story_layers.py"
)
gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gate)
LOGO = (ROOT / "episode01" / "assets" / "brand" /
        "bioscillate-original-supplied.jpg").read_bytes()
# A deliberately minimal fixture, NOT proof of composition quality.
ART = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQIHWP4z8DwHwAFgAI/ScLttAAAAABJRU5ErkJggg=="
)  # Real 1px PNG format fixture; NOT meaningful teaching art

def uri(blob, mime):
    return "data:" + mime + ";base64," + base64.b64encode(blob).decode()

def make_html(art=True, reflection=True, headline=None):
    logo = uri(LOGO, "image/jpeg")
    story = '<img alt="synthetic art fixture" src="' + uri(ART, "image/png") + '">' if art else ""
    question = "<p>How does delivered capability create business value?</p>" if reflection else \
               "<p>[REFLECTION QUESTION PENDING AUTHOR APPROVAL]</p>"
    return ("<html><body><section class='slide'><img alt='logo' src='" + logo + "'>"
            + "<h1>" + (headline or "The Problem Isn't Networking") + "</h1>"
            + story + question + "</section></body></html>")

def make_manifest():
    return {
        "source": {
            "source_id": "episode01/reference/slide-copy.candidate.json#02",
            "status": "CANDIDATE",
            "exact_headline": "The Problem Isn't Networking",
        },
        "bridge1": {
            "teaching_assertion": "Delivery of capability differs from recruitment.",
            "story_mechanism": "A store operator receives an observable working result.",
            "learner_observation": "A service can be verified independently of recruiting."
        },
        "art_direction": {"medium": "EDITORIAL_ILLUSTRATION", "background": "WHITE", "photographic_reference": False},
        "bridge2": {
            "composition_mode": "art-led",
            "visual_relationship": "The store's working capability has a measurable outcome.",
            "focal_art_description": "Actual operational action, not a decorative logo"
        },
        "assets": {
            "logo_sha256": gate.EXPECTED_LOGO_SHA,
            "story_art": {
                "sha256": hashlib.sha256(ART).hexdigest(),
                "source_id": "SYNTHETIC-TEST-FIXTURE-NOT-APPROVED",
                "teaching_relationship": "Source-to-result relationship represented by a separate asset"
            }
        },
        "reflection": {
            "question": "How does delivered capability create business value?",
            "status": "AUTHOR_CANDIDATE"
        }
    }

class StoryArtTests(unittest.TestCase):
    def test_recovered_logo_hash(self):
        self.assertEqual(hashlib.sha256(LOGO).hexdigest(), gate.EXPECTED_LOGO_SHA)

    def test_synthetic_complete_metadata_passes_structure_only(self):
        errors, evidence = gate.evaluate(make_html(), make_manifest())
        self.assertEqual(errors, [])
        self.assertTrue(evidence["story_art_image_present"])
        self.assertFalse(evidence["reference_visual_approved"])
        self.assertEqual(evidence["human_visual_approval"], "NOT_TESTED")

    def test_logo_only_baseline_must_hold(self):
        errors, _ = gate.evaluate(make_html(art=False), make_manifest())
        self.assertTrue(any("separate manifested story illustration absent" in e for e in errors), errors)

    def test_reflection_placeholder_must_hold(self):
        errors, _ = gate.evaluate(make_html(reflection=False), make_manifest())
        self.assertTrue(any("reflection" in e for e in errors), errors)

    def test_story_art_cannot_be_relabelled_logo(self):
        m = make_manifest()
        m["assets"]["story_art"]["sha256"] = m["assets"]["logo_sha256"]
        errors, _ = gate.evaluate(make_html(art=False), m)
        self.assertTrue(any("cannot be the logo" in e for e in errors), errors)

    def test_untraceable_story_art_rejected(self):
        m = make_manifest()
        m["assets"]["story_art"]["source_id"] = ""
        errors, _ = gate.evaluate(make_html(), m)
        self.assertTrue(any("source_id" in e for e in errors), errors)

    def test_mismatch_between_art_bytes_and_manifest(self):
        m = make_manifest()
        m["assets"]["story_art"]["sha256"] = "0" * 64
        errors, _ = gate.evaluate(make_html(), m)
        self.assertTrue(any("separate manifested story illustration absent" in e for e in errors), errors)

    def test_wrong_headline_rejected(self):
        errors, _ = gate.evaluate(make_html(headline="The Problem Is Networking"), make_manifest())
        self.assertTrue(any("native h1" in e for e in errors), errors)

    def test_missing_story_mechanism_rejected(self):
        m = make_manifest()
        m["bridge1"]["story_mechanism"] = ""
        errors, _ = gate.evaluate(make_html(), m)
        self.assertTrue(any("story_mechanism" in e for e in errors), errors)

    def test_unverified_remote_image_rejected(self):
        source = make_html()
        source = source.replace(uri(ART, "image/png"), "https://untrusted.example/art.png")
        errors, _ = gate.evaluate(source, make_manifest())
        self.assertTrue(any("non-inline" in e for e in errors), errors)

    def test_invalid_image_signature_rejected(self):
        source = make_html().replace(uri(ART, "image/png"), uri(b"not a PNG", "image/png"))
        errors, _ = gate.evaluate(source, make_manifest())
        self.assertTrue(any("non-inline" in e or "invalid" in e for e in errors), errors)

    def test_photo_medium_declared_rejected(self):
        m = make_manifest()
        m["art_direction"]["medium"] = "PHOTOGRAPHY"
        m["art_direction"]["photographic_reference"] = True
        errors, _ = gate.evaluate(make_html(), m)
        self.assertTrue(any("EDITORIAL_ILLUSTRATION" in e for e in errors), errors)

    def test_dark_hud_declared_rejected(self):
        m = make_manifest()
        m["art_direction"]["medium"] = "DARK_HUD"
        m["art_direction"]["background"] = "DARK"
        errors, _ = gate.evaluate(make_html(), m)
        self.assertTrue(any("white ground" in e for e in errors), errors)

    def test_unverified_substituted_logo_rejected(self):
        m = make_manifest()
        m["assets"]["logo_sha256"] = hashlib.sha256(b"fake-logo").hexdigest()
        errors, _ = gate.evaluate(make_html(), m)
        self.assertTrue(any("supplied logo SHA differs" in e for e in errors), errors)

if __name__ == "__main__":
    unittest.main()
