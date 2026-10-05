# Release QA

A DraftDeck build is not done when the HTML renders locally. It is done when the target adapter has been inspected and the evidence is recorded.

## Three distinct levels of verification

1. **Import / layer inspection** — exact page dimensions, `is_editable`, separate richtext records with preserved wording and positions, separate image/fill records.
2. **Visual review of the adapter render** — retrieve the rendered thumbnail or preview and inspect for font substitution, missing images, clipping, overlaps, rotation loss, text drift, and semantic drift.
3. **Hands-on edit test** — the user edits, saves, and reopens in the target tool.

Never report a lower level as if it were a higher one. The HTML → Canva route has prior levels-1-and-2 evidence; the logistics-migrated flagship requires a fresh adapter review before its own verification record is marked current.

## Release checklist

- Exact 16:9 integer canvas (default 1920×1080).
- Reference composition visibly retained — no generic redesign.
- Required copy exists as separate editable text, not baked into artwork.
- Artwork exists as separately movable assets; no unverified claims of native vector preservation.
- No missing artwork, clipping, collisions, or unreadable required text.
- No deprecated travel/aviation terminology or imagery in current source, output, previews, or component labels.
- Logistics doctrine matches `doctrine/logistics-framework.md`.
- No PowerPoint intermediate; no per-slide reconstruction service required.
- Verification record saved with the build under `examples/logistics-framework/verification/`.
- Remaining limitations stated explicitly.

## Adapter claims

An adapter may be claimed as supported only after a recorded verification run against the current pipeline. Canva's import route is verified historically, but the current logistics flagship remains pending re-verification. Adobe Express, Figma, and Floot are not verified.
