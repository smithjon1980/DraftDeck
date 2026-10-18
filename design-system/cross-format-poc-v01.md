# BOSS Cross-Format Proof of Concept — v0.1

**Status:** NOT BUILT / PENDING REFERENCE AUTHORITY. **Purpose:** Test the library policy without confusing structural success with visually approved artwork or sellable print output.

## Source selection (blocking prerequisite)

Use one current, attributable BOSS editorial scene, tentatively the *The Interface Is the Agreement* revised two-column mechanical-connector concept. Identify the **original source artwork file and its hash**, approved/current copy, exact Bioscillate logo asset/hash, and the human-selected reference image. The example screenshot is **reference-only** until its source and human selection are recorded. If any is unavailable, label `REFERENCE_UNAPPROVED` and block visual-master/release claims. Do not recreate the connector as an SVG or generic wireframe.

## Outputs and tests

1. **Slide adapter:** A React/HTML + BOSS token implementation at exactly 1920 × 1080. Preserve the artwork, independent selectable editorial text, cyan/magenta/black identity, readable hierarchy, subtle CAD grid, drawing zones and title block. Test a simple keyboard-accessible slide-control primitive with **one** selected library (Radix, React Aria or Base UI) while leaving content untouched.
2. **Print adapter:** Independently typeset the **same source story** on an 11 × 17 in landscape sheet (792 × 1224 pt when oriented portrait; landscape is **1224 × 792 pt**), with physical units, legible magazine prose, visible drafting conventions, title plate, and margin/binding placeholders subject to printer review. Experiment with Paged.js or browser CSS paged media, without inferring press-readiness from a PDF export.
3. **Comparison bundle:** Capture real browser renders, side-by-side comparisons against selected reference, annotated deviations, DOM text selection proof, art/label layer separation, PDF MediaBox and selectable-text checks, and explicit `PASS` / `FAIL` / `NOT_TESTED` records.
4. **Release controls:** Document package versions and license notices. Any design changes require human concept review. Printer acceptance, Canva editability, physical proof and publication approval remain separate tasks.

## Entry criteria

- Source/reference provenance resolved or honestly marked unapproved.
- Library policy linked and one headless candidate chosen for the interactive experiment.
- Renderer can be run reproducibly and test logs/screenshots can be archived.

**Success condition:** Two actual independently composed output profiles retain the same approved content and brand while satisfying their own verified constraints. **Not success:** a screenshot, HTML page or generated PDF alone. No automated check can self-approve BOSS art.
