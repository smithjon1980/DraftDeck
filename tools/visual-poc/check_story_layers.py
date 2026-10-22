#!/usr/bin/env python3
"""BOSS candidate story/art structural gate. Does NOT certify visual story or release.

Input is the actual single-slide rendered HTML and its separately authored
manifest. For this bounded offline route, source images must be inline data
URIs. External assets/CSS background artwork need different verified adapters.
"""
import argparse
import base64
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys

HASH = re.compile(r"^[0-9a-f]{64}$")
MODES = {"art-led", "narrative-led", "hybrid"}
# Recovered original supplied logo; update only through reviewed asset provenance.
EXPECTED_LOGO_SHA = "95f56729fe279a07b151ba5169a764a0aa387a1fac8cf283424ea783f950b146"
IMAGE = re.compile(r"^data:image/(?:png|jpeg|webp|svg\+xml);base64,(.+)$", re.S)


def seems_like_image(blob, mime):
    """Validate basic source file signatures only, not full decode or visual meaning."""
    if mime == "png":
        return (len(blob) >= 24 and blob.startswith(b"\x89PNG\r\n\x1a\n")
                and blob[12:16] == b"IHDR"
                and int.from_bytes(blob[16:20], "big") > 0
                and int.from_bytes(blob[20:24], "big") > 0)
    if mime == "jpeg":
        return len(blob) > 4 and blob.startswith(b"\xff\xd8\xff") and blob.endswith(b"\xff\xd9")
    if mime == "webp":
        return len(blob) > 20 and blob.startswith(b"RIFF") and blob[8:12] == b"WEBP"
    if mime == "svg+xml":
        import xml.etree.ElementTree as ET
        try:
            return ET.fromstring(blob).tag == "{http://www.w3.org/2000/svg}svg"
        except ET.ParseError:
            return False
    return False


class SlideHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.hidden = 0
        self.h1_depth = 0
        self.images = []
        self.headings = []
        self.body_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("script", "style"):
            self.hidden += 1
        if tag == "h1":
            self.h1_depth += 1
            self.headings.append("")
        if tag == "img":
            value = attrs.get("src", "")
            match = IMAGE.fullmatch(value)
            if match is None:
                self.images.append({"error": "non-inline or unsupported image source"})
            else:
                try:
                    mime, payload = match.groups()
                    blob = base64.b64decode(payload, validate=True)
                    if not seems_like_image(blob, mime):
                        self.images.append({"error": "image bytes do not match declared media type"})
                    else:
                        self.images.append({"sha256": hashlib.sha256(blob).hexdigest(), "bytes": len(blob)})
                except (ValueError, base64.binascii.Error):
                    self.images.append({"error": "invalid base64 image"})

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden = max(0, self.hidden - 1)
        if tag == "h1":
            self.h1_depth = max(0, self.h1_depth - 1)

    def handle_data(self, data):
        if not self.hidden:
            self.body_text.append(data)
            if self.h1_depth and self.headings:
                self.headings[-1] += data


def evaluate(html, manifest):
    errors = []
    if not isinstance(manifest, dict):
        return ["Manifest must be an object"], {}
    rendered = SlideHTML()
    rendered.feed(html)
    rendered.close()
    hashes = [v.get("sha256") for v in rendered.images]
    text = " ".join(" ".join(rendered.body_text).split())

    def require(where, key, label):
        value = where.get(key) if isinstance(where, dict) else None
        if not isinstance(value, str) or not value.strip():
            errors.append("missing " + label)
            return ""
        return value.strip()

    source = manifest.get("source", {})
    require(source, "source_id", "source.source_id")
    if source.get("status") not in ("CANDIDATE", "VERIFIED"):
        errors.append("invalid source.status")
    headline = require(source, "exact_headline", "source.exact_headline")
    if len(rendered.headings) != 1 or rendered.headings[0].strip() != headline:
        errors.append("exact native h1 heading missing or altered")
    bridge1 = manifest.get("bridge1", {})
    for field in ("teaching_assertion", "story_mechanism", "learner_observation"):
        require(bridge1, field, "bridge1." + field)
    bridge2 = manifest.get("bridge2", {})
    if bridge2.get("composition_mode") not in MODES:
        errors.append("invalid bridge2.composition_mode")
    for field in ("visual_relationship", "focal_art_description"):
        require(bridge2, field, "bridge2." + field)

    assets = manifest.get("assets", {})
    logo = require(assets, "logo_sha256", "assets.logo_sha256").lower()
    story = assets.get("story_art", {}) if isinstance(assets, dict) else {}
    story_sha = require(story, "sha256", "assets.story_art.sha256").lower()
    require(story, "source_id", "assets.story_art.source_id")
    require(story, "teaching_relationship", "assets.story_art.teaching_relationship")
    for label, value in (("logo", logo), ("story art", story_sha)):
        if not HASH.fullmatch(value):
            errors.append("invalid " + label + " SHA-256")
    if logo != EXPECTED_LOGO_SHA:
        errors.append("supplied logo SHA differs from recovered canonical asset")
    if logo not in hashes:
        errors.append("canonical logo image bytes absent from rendered HTML")
    if story_sha == logo:
        errors.append("story illustration cannot be the logo")
    if story_sha not in hashes:
        errors.append("separate manifested story illustration absent from rendered HTML")
    if any("error" in image for image in rendered.images):
        errors.append("non-inline, unsupported or invalid image; cannot verify its bytes")

    reflection = manifest.get("reflection", {})
    question = require(reflection, "question", "reflection.question")
    if reflection.get("status") not in ("AUTHOR_CANDIDATE", "AUTHOR_APPROVED"):
        errors.append("reflection is not a complete question candidate")
    if question and (not question.endswith("?") or question not in text):
        errors.append("reflection question not present as native rendered text")
    if "PENDING AUTHOR APPROVAL" in text.upper():
        errors.append("unresolved reflection placeholder in rendered HTML")
    return errors, {
        "image_count": len(rendered.images),
        "story_art_image_present": bool(story_sha in hashes and story_sha != logo),
        "native_h1_count": len(rendered.headings),
        "reference_visual_approved": False,
        "human_visual_approval": "NOT_TESTED",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("rendered_html", type=Path)
    parser.add_argument("manifest_json", type=Path)
    args = parser.parse_args()
    try:
        html = args.rendered_html.read_text(encoding="utf-8")
        manifest = json.loads(args.manifest_json.read_text(encoding="utf-8"))
        errors, observations = evaluate(html, manifest)
    except (OSError, ValueError) as exc:
        errors, observations = [str(exc)], {}
    status = "HOLD" if errors else "STRUCTURAL_READY_FOR_VISUAL_INSPECTION"
    print(json.dumps({"status": status, "errors": errors, "observations": observations,
                      "visual_story_quality_verified": False, "release_authorized": False}, indent=2))
    sys.exit(2 if errors else 0)


if __name__ == "__main__":
    main()
