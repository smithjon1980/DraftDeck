# Composition Standard

> **Editability is necessary but not sufficient.**
> A technically editable slide that destroys the reference composition is a failed DraftDeck build.

An earlier run produced verified live text elements and still failed because it recreated a generic boxes-and-lines composition instead of the reference. Layer counts prove structure; they do not prove fidelity. Both are required.

## Canvas

- Exact 16:9 integer canvas; default 1920×1080.
- Pages never nest; one top-level page section per slide.

## Token palette

The core standard is pure-white-only. There is one ground.

| Token | Value | Use |
|---|---|---|
| Pure White Ground | `#FFFFFF` | The ground. No alternates in the core standard. |
| Near-Black Ink | `#1A1A1A` | Primary ink |
| Burnt Orange | `#B34700` | Restricted accent (status, key marks, controlled emphasis) |
| Drafting Gray | `#DEDEDE` | Grid, construction lines, low-priority technical substrate |

**Visual profiles.** DraftDeck can host named optional profiles, but a profile is valid only when explicitly declared for a build and documented under `design-system/`. The core profile remains pure white.

## Typography

- Heavy serif action titles (Georgia).
- Uppercase monospace kickers and metadata (Courier New).
- Sans body copy (Arial).

## Stroke hierarchy

- 1.0pt (≈3px) — outer frames and major dividers.
- 0.5pt (≈1.5–2px) — controls and connector housings.
- 0.25pt (≈0.75px) — grid, hatch, and detail lines.

## Semantic constraint

The flagship Logistics Framework uses shipping, receiving, cargo, routing, proof-of-delivery, consignee, dispatch, handling, and release language. Deprecated travel/aviation metaphors are prohibited in current source, generated output, component names, and user-facing documentation.

## Prohibited

Solid pictogram fills, UI red, gradients, glows, ambient occlusion, glossy 3D, soft pill shapes, and silent substitution of a non-core visual profile. State is communicated through architectural hatching and line texture, not color alone.
