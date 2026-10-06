# Canva layered CAD pipeline archive

This archive includes the existing Canva skill and the complete 15-slide experiment, with the original reference PDF.

## Contents

- `canva-layered-html-slides/`: skill instructions, agent metadata, builder, sample scene, icon, and verified pipeline notes.
- `experiment/`: complete and individual HTML slides, scene definitions, portable build script, original PNG and compressed WebP story artwork, SVG drafting backgrounds, previews, artwork subject notes, production notes, and Canva verification results.
- `reference/`: original retired aviation-era reference package.

## Rebuild

Keep the folders together. From the extracted archive run:

```sh
python3 experiment/Build_Deck.py
```

The rebuild uses only the Python standard library and bundled artwork. It requires no API key, PowerPoint, or image generation service. It regenerates the scene definitions, drafting frames, individual HTML slides, and combined HTML deck. The packaged rebuild was checked to reproduce the combined HTML byte for byte.

The builder contains the authored slide copy and geometry. Edit it to change most slides; slide 13 uses `Slide13_Seed.json`. Change assets to replace the story layer. Rebuilding overwrites generated HTML and `Scenes.json`; direct changes to those files should be retained separately or transferred into the builder.

## Layer contract and evidence

16:9 pages use a drafting background, a separate story image where applicable, and independent text elements. The successful Canva import had 15 pages, 707 rich-text records, and 24 image fills. Inspect `Canva_Verification.json` and `Production_Notes.md` for evidence and limits. Editable text presence was verified; a manual edit/save/reopen cycle and native SVG preservation were not independently verified.

HTML/CSS is the source; Canva import requires the connected Canva importer described in the skill. The archive can rebuild offline, but importing into Canva requires access to Canva. This is the Canva pipeline; Adobe Express is a separate workflow.

Artwork_Prompts.json preserves artwork subjects, not a complete provider-specific image generation replay. Saved artwork is included for faithful rebuilding.

The skill instructions are preserved as installed. The experiment build script was adjusted to use relative paths so the archive is portable. No credentials are included.
