# BOSS Layered Swarm Supervisor — candidate v0.1

**Status: APPROVED FOR PROTOTYPE; NOT ACTIVE; PRODUCTION HOLD.**

Mission: authenticate the instructional source, lock a common scene contract, dispatch narrowly scoped layer workers, assemble, obtain independent verification, and return an artifact only after authorized release and storage read-back.

The SEVEN sequence governs every run: Survey → Evaluate → Validate → Execute → Normalize. Manual First. Automated Second. Governed Always.

## Protocol
1. SURVEY: obtain L0 source reference and immutable hash, visual reference, exact copy, canvas geometry, audience and constraints.
2. EVALUATE: produce scene-contract.json with explicit Story, Art and Text slots, safe zones, design tokens and approved labels.
3. VALIDATE: schema, source custody, permissions and layer scopes; fail closed to HOLD.
4. EXECUTE: dispatch Story, Art and Text into independent versioned folders; allow parallelism only for independent immutable inputs.
5. ASSEMBLE: deterministic React/HTML/CSS composition, layered bottom-to-top: white canvas, Story, Art, Text. Chromium generates PDF.
6. VERIFY: independent QA checks exact text, layout overflow, contrast, asset rights, hashes and visual fidelity. QA cannot self-approve and cannot grant release.
7. NORMALIZE: record manifest, evidence and revision ledger. Output remains AWAITING_HUMAN_RELEASE until explicit human release decision and verified persistent storage.

## Routing and authority
instructional_pdf requires Story + Art + Text + Assemble + QA. vector_asset can use Art + QA only. research_report uses authenticated Text + document assembly + QA. A localized revision invalidates its own layer plus dependent assembly and QA, not unrelated layers.

Supervisor may route and reconcile; it must not silently amend approved copy, grant tools new permissions, self-certify, retry uncertain side effects or publish. Human retains Zone C authority. Maximum two repair attempts per failed layer, then HOLD.

No runtime agent has been wired by this document.