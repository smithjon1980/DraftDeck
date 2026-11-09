# Run isolated CE.SDK web harness

Requires Node.js 22+ and npm. From this folder:

```sh
npm install
npm run build
npm run dev
```

Open the local URL displayed by Vite. Requires browser access to IMG.LY CDN assets. No production license or secret is required for evaluation; output may be watermarked.

**What this proves:** If the browser initializes and creates a blank design scene, criterion C01 may be recorded as passed with console/screenshot evidence.

**What it does not prove:** CAD/Art/Story/Text fidelity, imported SVG editability, vector PDF fidelity, print PDF/X, security enforcement, or suitability for BOSS.

For manual test, open browser developer tools and inspect `window.bossCesdkTest`. Do not upload protected content. Never treat editor UI locks as a trusted authorization boundary.

Reference: https://img.ly/docs/cesdk/js/configuration-2c1c3d/
