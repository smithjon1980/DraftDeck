import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "story_resolution", ROOT / "tools/visual-poc/check_story_art_resolution.py")
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

def specimen(nw=1400, nh=700, dw=950, dh=330, fit="cover"):
    return {"profile": "slide", "viewport": [1920, 1080],
            "images": [
                {"role": "original-logo", "natural_width": 1536, "natural_height": 857,
                 "display_width": 220, "display_height": 123, "object_fit": "contain"},
                {"role": "story-art", "natural_width": nw, "natural_height": nh,
                 "display_width": dw, "display_height": dh, "object_fit": fit}
            ]}

class StoryArtResolutionTests(unittest.TestCase):
    def test_resolution_ready_not_story_approval(self):
        errors, rows = gate.evaluate(specimen())
        self.assertEqual(errors, [])
        self.assertGreaterEqual(rows[0]["source_pixels_per_css_pixel"], 1.0)

    def test_small_cropped_art_rejected(self):
        errors, _ = gate.evaluate(specimen(nw=473, nh=289, dw=945, dh=333))
        self.assertTrue(any("upscaled" in x for x in errors))

    def test_logo_alone_rejected(self):
        data = specimen()
        data["images"] = [data["images"][0]]
        errors, _ = gate.evaluate(data)
        self.assertIn("no measured story-art image", errors)

    def test_wrong_render_viewport_rejected(self):
        data = specimen()
        data["viewport"] = [1280, 720]
        errors, _ = gate.evaluate(data)
        self.assertTrue(any("1920x1080" in x for x in errors))

    def test_invalid_zero_dimensions_rejected(self):
        errors, _ = gate.evaluate(specimen(nw=0))
        self.assertTrue(any("invalid" in x for x in errors))

    def test_boolean_size_rejected(self):
        errors, _ = gate.evaluate(specimen(nw=True))
        self.assertTrue(any("invalid" in x for x in errors))

    def test_fit_stretch_uses_worst_axis(self):
        errors, _ = gate.evaluate(specimen(nw=1400, nh=200, fit="fill"))
        self.assertTrue(any("upscaled" in x for x in errors))

    def test_cover_uses_worst_axis(self):
        errors, _ = gate.evaluate(specimen(nw=1200, nh=100))
        self.assertTrue(any("upscaled" in x for x in errors))

    def test_unknown_fit_rejected(self):
        errors, _ = gate.evaluate(specimen(fit="mystery"))
        self.assertTrue(any("object-fit" in x for x in errors))

    def test_unapproved_story_can_pass_density_only(self):
        errors, _ = gate.evaluate(specimen())
        self.assertEqual(errors, []) # Explicitly does not prove art semantics.

if __name__ == "__main__":
    unittest.main()
