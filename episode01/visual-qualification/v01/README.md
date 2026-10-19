# Episode 01 — BOSS Visual Qualification v0.1

**Status: CANDIDATE, NOT VISUALLY APPROVED OR RELEASED.** 2026-10-18.

This scoped visual qualification implements candidate Slides 01, 02, and 06 using React DOM components and compiled Tailwind CSS utility output plus project-specific CAD layout CSS. Native HTML editorial text and the original verified JPEG artwork remain separate.

## Materials
- `BOSS_Visual_Qualification_Standalone.html` is a standalone offline interactive three-slide browser reviewer, bundling React and the **unaltered original-supplied JPEG** as a data URL. It is a convenient preview, not the approved visual master.
- `src/app.js` is the React component source with a repo-relative reference to the original JPEG.
- `src/build.css` contains the offline compiled Tailwind utility layer followed by explicit composition styles.
- `qualification-manifest.json` records independently observed checks, unknowns and Canva evidence.

The original brand asset is **`episode01/assets/brand/bioscillate-original-supplied.jpg`**. Verified SHA-256: `95f56729fe279a07b151ba5169a764a0aa387a1fac8cf283424ea783f950b146`. This is JPEG source fidelity, not a verified editable vector master.

Source text: `episode01/reference/slide-copy.candidate.json` (candidate; exact teaching approval not presumed). Visual influence: Tesla center touchscreen hierarchy plus CAD/ISO-informed hairline geometry. All HTML headings, labels, notes, and diagrams are native DOM text. The Slide 06 diagram shows ordered source labels, **not invented decision gates or participants**.

## Evidence
- Browser visual inspection completed using a headless Chromium render, followed by two fixes for reflection-footer overlap.
- Three slides, 1920×1080; PDF text selectable; no SVG editorial text; 11, 33 and 28 native text leaf elements respectively; no canvas overflow observed.
- Canva import created 3 editable 1920×1080 pages, 72 independent TEXT elements and 3 image fills. Temporary replacement of the Slide 01 headline succeeded but was cancelled; original text verified restored.
- Canva design: https://www.canva.com/d/IeOVTDsYtwdhKP0

## HOLD before approval
Obtain human inspection of final Canva visual composition, image manipulation test, approved Slide 01/02/06 reference compositions, source status of teaching copy, and explicit authorization. Do not convert this technical import success into a claim that the design itself was approved.
