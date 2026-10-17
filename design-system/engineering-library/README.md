# Engineering graphics library — candidate 0.2

An actual engineering asset collection for DraftDeck figures, with original sources vendored in `vendor/source-pack.zip`, pinned revisions and hashes, and reusable React adapters. This replaces the rejected layout-container kit. It is not an approved slide master.

## Available components

| Collection | Imported assets | Examples |
| --- | ---: | --- |
| ISO-referenced process drawings | 286 | Heat exchangers with internals, vessels and tanks, columns, pumps, compressors, valves, drives and apparatus |
| Mechanical drafting | 75 | GD&T symbols and frames, datum/feature markers, section/break marks, callout/arrow geometry, first/third-angle projection, surface roughness |
| ANSI/IEEE logic | 7 | AND, NAND, OR, NOR, NOT, XOR, XNOR; original terminal coordinates retained |
| Composition adapters | 3 | TechnicalSymbol, LeaderCallout, DimensionLine; native HTML labels over separate vector geometry |

368 assets have rendered nonempty geometry bounds. Eight additional source elements are retained in the archive but omitted from the atlas because they need editable-label adapters. The build reports them explicitly; it does not silently strip visible wording from a symbol and call it complete.

## Build and inspect

Requires Node 24 and Python 3. No CAD application or browser download is needed to build.

```sh
cd design-system/engineering-library
npm ci
npm run package
```

Extract `dist/DraftDeck_Engineering_Atlas_Complete.zip` in full, then open `index.html`. Keep `assets.js` and the `assets/` directory beside it. The offline React-rendered atlas has search, collection filters, enlarged inspection, source/license metadata and per-component SVG download. `dist/assets.json` is the reusable component data. Source geometry is kept separate from live HTML titles, captions and annotations. Tailwind is compiled locally; no CDN or web server is required. The 13.8 KB HTML shell contains no base64 images. Geometry files and catalogue data are separate, avoiding the former 2.87 MB single-file handoff. `npm run build` creates the folder; `npm run package` also creates and verifies the ZIP and per-file SHA-256 packing list.

`src/components.tsx` exports `TechnicalSymbol`, `LeaderCallout`, `DimensionLine`, and `EngineeringAtlas`. `TechnicalSymbol` takes an `EngineeringAsset` and uses its `assetUrl` when present. Its optional embedded-SVG fallback uses Node Buffer during server rendering. Reuse the content records independently of the atlas UI. Dimension labels describe the supplied content; never invent measurements or tolerances.

To regenerate the source pack from checked-out upstream repositories at the recorded commits:

```sh
python3 scripts/import_assets.py --iso /path/to/BK-2020-04 --freecad /path/to/FreeCAD --qet /path/to/qelectrotech-elements
```

The normal build verifies every original file against its recorded SHA-256. `vendor/viewboxes.json` stores measured browser geometry bounds for the imported IDs. If an asset changes, regenerate and visually inspect its crop rather than guessing a bounding box. The build fails when a crop record is missing.

## Sources and licensing

| Source | Pinned revision | Terms / adaptations |
| --- | --- | --- |
| [Steven Baltakatei Sandoval — BK-2020-04](https://gitlab.com/baltakatei/BK-2020-04) | `105ff030f6d8a9a335b6b94fc8eda7f6d0f07d3b` | CC BY-SA 4.0. Seven original drawing sheets and README retained. Derivatives extract individual symbol groups with needed definitions; labels are separated and bounds cropped. Derivative geometry remains CC BY-SA 4.0. |
| [FreeCAD TechDraw](https://github.com/FreeCAD/FreeCAD/tree/e95a31c3119f09a5b185c0b9c901a91384961cc0/src/Mod/TechDraw/Symbols) | `e95a31c3119f09a5b185c0b9c901a91384961cc0` | Root LGPL 2.1 license and selected original SVGs retained, including per-file metadata. Cropped bounds for atlas display; text-bearing sources await adapters. Individual standards equivalence not verified. |
| [QElectroTech elements](https://github.com/qelectrotech/qelectrotech-elements) | `73cbffb86d29590ad0fa63508afdc41163fff975` | CC BY 3.0 plus upstream restriction against use as sample data for building machine-learning models. Full ELEMENTS.LICENSE retained. ANSI/IEEE folder elements converted from ELMT to SVG, including Qt arc geometry; terminal coordinates retained. |

Attribution, original source URL pinned to revision, license and adaptation notice are embedded in every exported SVG's metadata and visible in the inspector. Original source files and full upstream notices remain in the archive. The repository's MIT license does not override third-party asset terms. This is a graphics reuse/import workflow, not model training.

## Standards scope

These are reusable engineering graphics and documented reference families, not a certified implementation or a downloaded collection of proprietary standards documents.

| Family | Relevant authority | What is established here |
| --- | --- | --- |
| Process and apparatus symbols | ISO 10628-2:2012; cross-references to ISO 14617 | The independent author's drawing set identifies these references and registration/example numbers. Artwork provenance is recorded; individual conformance is not independently certified. |
| General diagram symbols | [ISO 14617-2:2025](https://www.iso.org/standard/83364.html) | Current general-symbol standard identified for future validation. Do not relabel this 2012 drawing collection as the 2025 edition. |
| Engineering line conventions | [ASME Y14.2](https://www.asme.org/codes-standards/find-codes-standards/y14-2-line-conventions-lettering) | Scope identified for line/lettering practices; original DraftDeck leaders and dimension adapters are candidates, not a conformance claim. |
| GD&T | [ASME Y14.5](https://www.asme.org/codes-standards/find-codes-standards/y14-5-dimensioning-tolerancing) / ISO 1101 family | TechDraw assets downloaded; individual edition and geometry matching remain to be checked before claiming a specific standard. |
| ANSI/IEEE logic | QElectroTech's explicitly named ANSI/IEEE collection | Actual upstream source family and seven rendered gates established; no invented standards-edition claim. |

## NotebookLM reference relationship

The inspected connector illustration on page 12 of `Enterprise_AI_Operations_Manual (1).pdf` uses detailed mechanical assembly artwork, keyed interfaces, hatched surfaces, centerlines, and callout leaders. Those are materially richer than generic comparison boxes. The library supplies technical symbols and drafting grammar for that visual language.

Detailed mechanical cutaways, exploded connectors, and perspective assemblies still need a dedicated CAD/illustration asset layer. The atlas does not pretend its two-dimensional schematic symbols reproduce that artwork. Preserve the real engineering meaning of symbols when used literally; label any explanatory analogy explicitly.

No teaching copy, retired aviation language, or orange identity is adopted from the PDF. Lesson composition still requires its source page, exact-copy record, story/visual bridges and A–D review. Keep original bioscillate artwork, live editorial text and technical geometry separate. SVG is used for individual geometry assets, never to flatten an entire production slide or its editorial text.

## Verification

Build/import, geometry checks, browser interaction checks and visual findings are in [verification.md](verification.md). Human visual approval and Canva import/editability remain pending.
