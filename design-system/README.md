# BOSS / DraftDeck design system

CURRENT CANDIDATE. This directory is the entry point for the contemporary Bioscillate visual contract for Episode 01, Day Zero, and related instructional web surfaces.

Source files:
- boss-design-contract.json — bounded machine-readable rules, status, known unknowns, and separate output profiles.
- tokens/tokens.css — named color, typography, spacing, and slide-size variables, subject to contract validation.
- components.md — bounded semantic component registry; specification does not imply implementation.
- validation/check_contract.py — structural contract checks and negative fixtures.
- library-policy.md — third-party React/print tooling admission policy; candidates not installed.
- cross-format-poc-v01.md — bounded 16:9 slide to 11 × 17 in print experiment, pending source selection.
- episode-manifest-template-v01.json — per-episode source/manuscript/page coverage and review-state template.
- ../doctrine/episode-production-protocol-v01.md — proposed repeatable art-first editorial production gates with verbatim reading tracks.

Read AGENTS.md for the two-bridge editorial workflow, four-candidate comparison, rendering, and approval boundaries. The project must validate source provenance, reference composition, editability, and actual target rendering separately.

Do not silently import older palettes, themes, or metaphor-based components from prior work. Older experimental branches and examples remain available as history, not as approval of their visual decisions. This new contract is a candidate until the human reviewer selects a representative visual master and approves its authority.

A slide profile is not a web breakpoint. A print page is not a 16:9 slide. Do not assume Canva, Figma, or another target is editable or visually faithful without a current adapter-specific test.
