# Verified HTML → Canva pipeline

## Successful run: 2026-10-05

Reference: page 1 of AI_Pilot_Interface_QA_Specification.pdf, a raster 15-page document supplied by the user. First page: large male connector at left, socket cutaway at right, enlarged pin cutaway below, bold two-line serif title, dimension callouts, drafting frame, angled orange approval stamp, lower-right title block.

1. Render the PDF page with Poppler and inspect it visually.
2. Use image editing to remove every title, dimension label, margin coordinate, stamp, and title-block word. Preserve connector/cutaway artwork and drafting linework. Use pure white ground for the infographic branch.
3. Save that output as a separate PNG artwork asset. It is a generated reference-derived raster reconstruction, not an exact trace or engineering drawing.
4. Compose the page in HTML/CSS: separate text divs, embedded PNG, CSS-bordered rotated stamp with live wording, explicit page dimensions and `data-document-role="page"`.
5. Import the local HTML directly through Canva's `design_file` route with intended type `presentation`.
6. Inspect Canva's imported page and layer records and its rendered thumbnail.

## Evidence

Final Canva design ID: `DAHXHgS0qB0`.
Edit link: https://www.canva.com/d/lIp8Rg_NsECfxTA
Verified page dimensions: 1920 × 1080.
Verified richtext elements: 36.
Verified image assets on the page: 1.
Page reported editable. Titles, dimension annotations, margin coordinates, stamp words and title-block metadata appeared as separate text elements. CSS stamp rotation and border appeared in the preview. Connector/cutaway asset remained separate.

User-facing saved artifacts:
- AI_Pilot_Interface_QA_Layered.html
- AI_Pilot_Connector_Artwork.png
- AI_Pilot_Interface_QA_Canva_Final_Preview.png

Resolve these by filename through Library if needed; do not assume original scratch paths persist.

## Boundaries of verification

The run verified the native layer records and rendered composition. It did not perform a saved text-edit round trip or establish font-perfect equivalence. The user said the result was very close; it was not approved as exact or canonical. Artwork remained raster and its internal content was not independently editable. No SVG preservation test or Adobe Express import test was completed.

An earlier 2400 × 1350 run verified 99 live text elements but merely repeated a boxes-and-lines SVG composition. It passed layer inspection and failed the user's visual intent. Do not repeat that as the default design method.

## Stable import pattern

```html
<section data-document-role="page" data-label="Slide title"
         style="position:relative;width:1920px;height:1080px;overflow:hidden;background:#FFFFFF">
  <img src="data:image/png;base64,..." alt="Text-free artwork"
       style="position:absolute;left:0;top:0;width:1920px;height:1080px">
  <div style="position:absolute;left:80px;top:110px;font-family:Georgia;font-size:56px;font-weight:bold">
    Editable action title
  </div>
</section>
```

Discover tool names and schemas at execution time. The demonstrated sequence was import → start editing transaction → inspect richtexts/fills/pages → get thumbnail → show and inspect preview → cancel inspection transaction. Do not retain transaction IDs or expiring image URLs for reuse.

## AI Pilot style route

Follow the selected reference and current project standard together. Infographic branch: pure white #FFFFFF; near-black technical ink; burnt orange #B34700; heavy serif action title; uppercase monospace kicker; line-built diagrams/hatching and drafting rails. The distinct flight-manual branch uses parchment. Do not silently substitute one branch for the other. Use the actual source copy and record ambiguities; illustrations do not substantiate engineering dimensions or an approval state.
