# Composition Standard

> **Editability is necessary but not sufficient.**
> A technically editable slide that destroys the reference composition is a failed DraftDeck build.

An earlier run produced 99 verified live text elements and still failed, because it recreated a boxes-and-lines composition instead of the reference. Layer counts prove structure; they do not prove fidelity. Both are required.

## Canvas

- Exact 16:9 integer canvas; default 1920×1080.
- Pages never nest; one top-level page section per slide.

## Token palette

| Token | Value | Use |
|---|---|---|
| Pure White Ground | `#FFFFFF` | Infographic-branch ground |
| Near-Black Ink | `#1A1A1A` | Primary ink |
| Burnt Orange | `#B34700` | Restricted accent (stamps, key marks) |
| Parchment Ivory | `#FAF0EA` | Flight-manual branch only — never substituted silently for the infographic branch |

## Typography

- Heavy serif action titles (Georgia).
- Uppercase monospace kickers and metadata (Courier New).
- Sans body copy (Arial).

## Stroke hierarchy

- 1.0pt (≈3px) — outer frames and major dividers.
- 0.5pt (≈1.5–2px) — controls and connector housings.
- 0.25pt (≈0.75px) — grid, hatch, and detail lines.

## Prohibited

Solid pictogram fills, UI red, gradients, glows, ambient occlusion, glossy 3D, soft pill shapes. State is communicated through architectural hatching and line texture, not color alone.
