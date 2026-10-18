# Episode 01 print: canonical logo placement

**Owner direction (2026-10-18):** The authentic Bioscillate Operating System by Seven logo belongs in the **bottom-right corner** of each Episode 01 print page, NOT top-right. This is distinct from selecting a text-led (A) or art-led (B) composition: the logo location must not change between those patterns.

## Approved boundaries to preserve

- Original source logo asset, without regenerating a substitute. Verify against the recorded unmodified asset SHA-256 `95f56729fe279a07b151ba5169a764a0aa387a1fac8cf283424ea783f950b146`.
- White `#FFFFFF` ground, black `#000000` type, cyan `#00BCEB` and magenta `#E30074` accents.
- Keep the logo visually inside the lower-right trim-safe area, not top-right and not in the body-text region. Reserve footer/white-space clearance instead of overlaying words, technical drawings, figure captions or page numbering.
- Native selectable editorial text and real source artwork remain independent. Reflow the text to maintain the *exact same* spoken paragraphs.
- A/B/hybrid composition is still decided by the teaching beat, not by a universal text-image grid. This logo rule applies only to the independent 17x11 **print** profile, and does not implicitly change the separate 1920x1080 teaching-slide UI or responsive web identity.

## Private proof and tests

After PR #70's palette change was merged, the four-page owner review proof was rebuilt from the existing private candidate A/B HTML and original logo asset, changing only the placement and necessary footer/narrative clearance. Actual Chromium renders and exported PDFs confirm:

- Four landscape 1224x792-point pages, with selectable, exact manuscript paragraphs (8 source paragraphs preserved across each two-page candidate).
- Visible original logo anchored bottom-right on each page, verified image loading and no detected logo-versus-narration, caption, figure, footer, or masthead collisions.
- The original cyan/magenta identity maintained; A and B preserved as separate composition patterns. No visual-master or print-release approval is inferred.
- No confidential manuscript, artwork bytes, PDF or screenshot is committed to the public repository.

**Automated fail-before/pass-after regression:** `tools/visual-poc/check_print_logo_placement.py` inspects actual rendered screenshots for both brand accent colors in the lower-right region. The earlier top-right logo screenshots failed this gate; all four corrected bottom-right screenshots passed. Run with the existing `check_brand_proof.py` source-SHA and palette checks. Color-region matching alone is insufficient to authenticate the real logo or guarantee physical trim safety: human inspection and printer specifications are still separate requirements.

This is a brand placement *rule and candidate visual proof*, not authorization to publish or merge automatically.
