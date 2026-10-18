# BOSS Composition Standard — coherent v0.1 candidate

Scope: current Episode 01 and Day Zero instructional visual production. Status: CANDIDATE_PENDING_HUMAN_REVIEW, not a released design-system version.

The authoritative machine-readable proposal is design-system/boss-design-contract.json. The original Bioscillate visual identity is preserved; the logo binary has not yet been hash-pinned and must not be replaced with a generated approximation.

## Visual constraints
- Primary slide profile: 1920 x 1080, exact 16:9 logical canvas. CSS-scaled viewing does not change the internal coordinate system.
- Ground: #FFFFFF. Core ink: black. Preserve approved cyan (#00BCEB) and magenta (#E30074) for the canonical logo and controlled emphasis.
- Tesla Model Y center touchscreen is a **layout influence** (controlled panels, information hierarchy), not a product skin or brand substitution.
- CAD/ISO drafting influence: measured edges, hairline geometry, explicit alignment. Project visual inspiration is not a claim of ISO compliance.
- Native selectable HTML text for headings, narrative, annotations, labels, and notes. Story art stays a separate asset. SVG may be used for art/geometry, not editorial text.
- Avoid gradients, glossy 3D, decorative shadows, thick frames, gratuitous rounded cards, and generic sparse marketing layouts.
- Use named shared design tokens and specify component state, accessibility, and content/visual source provenance.

## Output profiles
- Slides: fixed 1920 x 1080; art/text layered and independently inspectable.
- Responsive web and Academy lessons: semantic reflow across screen sizes, retaining design roles rather than literal slide dimensions.
- Print: independent profile pending explicit approval; do not reuse an incompatible slide canvas.

## Authority and migration
This rebuild supersedes contradictory prior core styling choices for new BOSS visual work **when approved**. Historical example decks and open feature branches may still contain older profiles; their code is not automatically migrated or verified. No current source may claim that an old accent or old instructional metaphor outranks the original Bioscillate identity.

Approval requires visual evaluation of a representative slide and the verified logo source. An accepted CSS stylesheet alone cannot establish design approval.
