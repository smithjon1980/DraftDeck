# DraftDeck production and source custody contract

For a given build, define and record:
1. Authoritative source: exact instructional copy, scene schema, validated reference, artwork identifiers and approved design-system version.
2. Compiler/renderer: deterministic transformations, supported output and environment versions.
3. Generated output: HTML/CSS, previews, PDFs, and adapter import payloads.
4. Evidence: content checks, layer/editability inspection, visual checks, destination tests and human decision.

Authoritative source -> compiler/renderer -> generated output. Generated files do not acquire authorship or approval authority. A rebuild can overwrite derivatives; changes intended to survive must be entered in source and rebuilt.

Current BOSS Episode 01/Day Zero builds use design-system/boss-design-contract.json as their **candidate** design profile until human acceptance. Earlier demonstration build scripts under examples/ retain their own recorded historical semantics and dimensions and must not be silently treated as evidence of current visual conformity.

No generation, import, or successful unit test upgrades NOT_TESTED to VERIFIED or authorizes release. Always record target, run identifier, relevant source hashes, environment, limitations, and approval status.
