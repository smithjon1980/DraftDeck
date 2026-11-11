# 04 — Module 01 Visual & Infographic Brief

**Document role:** Brief for the Module 01 slide deck (16:9) and the Module 01 infographic family (square / portrait / landscape). Governs visual treatment only; content authority is `03_MODULE_01_PACKAGE_OPERATIONS_SOURCE` and doctrine.

---

## 1. Visual Job of These Artifacts

- **Deck:** *shows* the architecture — process flow, package anatomy, state boundaries, decision points.
- **Infographics:** *compress* — one concept per artifact, readable at a glance.
- Neither restates the podcast. The podcast explains; visuals show structure.

> **Representation ≠ learning.** A beautiful visual is not evidence of understanding — but a wrong visual is active contamination.

## 2. Composition Standard (verbatim from doctrine/composition-standard.md)

> **Editability is necessary but not sufficient.**

**Canvas:** exact 16:9; default 1920×1080. One top-level page section per slide; pages never nest.

**Token palette — pure-white core, one ground:**

| Token | Value | Use |
|---|---|---|
| Pure White Ground | #FFFFFF | The ground. No alternates in the core standard. |
| Near-Black Ink | #1A1A1A | Primary ink |
| Burnt Orange | #B34700 | Restricted accent (status, key marks, controlled emphasis) |
| Drafting Gray | #DEDEDE | Grid, construction lines, low-priority technical substrate |

**Typography:** heavy serif action titles (Georgia); uppercase monospace kickers and metadata (Courier New); sans body copy (Arial).

**Stroke hierarchy:** 1.0pt outer frames/major dividers · 0.5pt controls and connectors · 0.25pt grid/hatch/detail.

**Prohibited:** solid pictogram fills, UI red, gradients, glows, glossy 3D, soft pill shapes. State is communicated through architectural hatching and line texture, not color alone.

## 3. Module 01 Infographic Family — Package Anatomy

Produce three coordinated assets, same concept, three orientations:

### SQUARE (1:1) — "Package Anatomy — Quick Reference"
One bounded package drawn as a technical diagram: labeled callouts for PACKAGE_ID, CONTENTS, DESTINATION, ACCEPTANCE CONDITION, MINIMUM NECESSARY CARGO. Burnt-orange accent on the acceptance-condition callout only.

### PORTRAIT (vertical) — "Mission → Package → Acceptance" Training Poster
Top: MISSION (large, unbounded outline). Middle: decomposition into three bounded packages. Bottom: one package opened to show its required fields. Caption rule: "Mission governs destination; the package stays small."

### LANDSCAPE (16:9) — "Request → Bounded Package" Flow
Left-to-right transformation: vague request → alignment questions (destination? scope? inputs? acceptance?) → bounded package with declared fields. Show the alignment gate as a checkpoint, not a decorative arrow.

> **Alignment precedes packaging.** — must appear as the gate label.

## 4. Deck Guidance (Module 01)

Suggested slide arc (adapt, don't pad):

1. Title — Module 01: Package Operations
2. System question: What exactly is being moved?
3. The logistics frame: data is cargo (canonical identity line)
4. Mission ≠ package (contrast diagram)
5. Package anatomy (the required fields)
6. Alignment gate before packaging
7. Decomposition: scope reduction without destination reduction
8. Minimum necessary cargo
9. Block vs. package (unit of commitment vs. unit of accountability)
10. Failure modes: unbounded prompt / mission-as-package / scope stuffing / retrofitted acceptance / cargo dumping
11. Worked example walkthrough
12. Canonical rules recap
13. Bridge to Module 02: Route Operations

Every canonical statement on a slide must match the doctrine wording verbatim.
