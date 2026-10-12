# Design Tokens

Named, bounded style choices governing DraftDeck and BOSS editorial output.
Practice adopted from USWDS token discipline: name the choice once, reuse the
name everywhere, forbid scattered literal overrides.

- `tokens.css` — canonical CSS custom properties for web and HTML slide output.
- Values implement `doctrine/composition-standard.md` and
  `design-system/editorial-components.md` (Foundations section).

Rules:

1. Components and slides reference token names (`var(--boss-*)`), never raw
   values. A raw hex or pixel value in generated HTML is a contract violation.
2. Adding or changing a token requires updating this file and noting the
   change in the acceptance record of the next build that uses it.
3. The core profile stays pure white. Optional visual profiles must be
   declared here before use.
