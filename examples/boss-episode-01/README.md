# BOSS Episode 01 — composition candidate

Separate React/Tailwind preview for Slides 01, 02, 06. Inputs: textual
Visual Authority Spec v1.0 and exact candidate JSON at main b96b358,
read after GEMINI_RECONCILIATION.md. No approved rendered reference was
supplied. Jonathan Smith's visual approval remains pending.

Run npm install, npm run dev; npm run build compiles preview assets.
Run npx playwright install chromium, then npm run check:browser.
CI checks all three slides at four viewport widths and captures screenshots.

## Layer plan and proposed measurements

All slides: fixed 1920×1080 native DOM, proportional CSS transform,
white ground, black text, 1px rules. Fonts: proposed Arial and
Consolas/Courier New. Preview controls and missing-field notes stay outside pages.

01: separate original logo image, 1240px wide at x340/y28; exact native
headline in a 1472×222px hairline frame at x224/y746. Title 64px centered.
Unknown footer omitted and flagged in preview UI.

02: 144px metadata rail; full original image scaled to 256px width;
160px title band; 662px main/sidebar region at 67%/33%; 112px exact-copy
footer. Main inset 64px, comparison gutter 40px. Left column heading is
#646464 as requested by supplied candidate; other text is #000000.
Native body 28–32px, headings 34–52px. Comparison labels and sidebar
copy are read directly from the supplied JSON.

06: same rail/title/footer regions; five exact ordered labels in independent
native boxes, 248px high, 28px gaps. No arrows, participants, messages,
or decision gates invented. This is an ordered-step composition, not a
participant/message protocol.

## Logo and unresolved fields

The recovered JPEG is used unchanged: no crop, recoloring, signature
removal, or replacement wordmark. Git blob hash:
ab4d85210dd410757d6542b286b15b65d4c7b774.
Its cyan/black/magenta identity was visually inspected. Byte equivalence
to Gemini's differently named asset remains unknown.

Reduced lockup unavailable: internal rails use the scaled full original
as a candidate treatment. Internal metadata, Slide 01 footer, and Slide 06
protocol fields remain unresolved. No additional illustration was supplied.
CSS rules, panels, and sequence boxes supply the proposed composition.

The original orientation ZIP and Logistics Framework are preserved.
Rejected first screenshot is not visual authority. Passing checks establish
rendering behavior, not creative approval. Discrete static HTML and Canva
import verification remain pending author approval.
