# Verified HTML → Canva pipeline

## Demonstrated route: 2026-10-05

A 15-page raster reference document was used to validate the layered import method. The test established a stable workflow for converting a visual reference into static HTML/CSS with live text and separate artwork layers.

1. Render the source page and inspect it visually.
2. Separate artwork from titles, dimensions, annotations, stamps, and title-block wording.
3. Save the artwork as an independent asset.
4. Compose the page in HTML/CSS with separate live text elements and explicit page dimensions.
5. Import the local HTML through Canva's file-import route.
6. Inspect the imported page, layer records, and rendered thumbnail.

## Evidence

The demonstrated route verified:
- 1920 × 1080 page dimensions;
- independent rich-text elements;
- separate image assets;
- adapter-side editability flags;
- preserved rotation/border behavior in the rendered preview.

The current Logistics Framework flagship is a semantic and artwork migration of the reference implementation and must be re-verified in Canva before its own adapter status is marked current.

## Boundaries of verification

The earlier route did not establish font-perfect equivalence, native SVG preservation, or a full edit/save/reopen round trip. A technically editable import can still fail visual intent.

An earlier test with many live text elements failed because the design became a generic boxes-and-lines composition. Do not treat layer count as proof of fidelity.

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

## Logistics Framework style route

Follow the selected reference together with the current project standard: pure white `#FFFFFF`, near-black technical ink, burnt orange `#B34700`, heavy serif action titles, uppercase monospace metadata, line-built diagrams/hatching, and logistics-native component semantics.

The active semantic model is documented in `doctrine/logistics-framework.md`. Do not reintroduce predecessor travel/aviation metaphors.
