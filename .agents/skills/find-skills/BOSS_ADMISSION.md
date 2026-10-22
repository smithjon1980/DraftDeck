# find-skills — upstream provenance and BOSS admission

Status: INSTALLED_IN_DRAFTDECK_CANDIDATE_BRANCH; external skill instructions are **not** BOSS doctrine or release authority.

- Upstream repository: https://github.com/vercel-labs/skills
- Upstream skill: `skills/find-skills/SKILL.md`
- Upstream pinned commit: `a80e4c9d12d607631249d4d7d059f835d4b2f13a`
- Original Git blob SHA: `a41bdd074bb587afd861332cf2f473f3154de4d7`
- License: MIT (reproduced adjacent `LICENSE`)
- Intended scope: project-level Codex/compatible agent discovery via `.agents/skills/find-skills/SKILL.md`
- Original user command: `npx skills add https://github.com/vercel-labs/skills --skill find-skills`
- Installation method here: source-controlled exact upstream skill copy through GitHub connector; CLI install **not confirmed** (scratch CLI invocation timed out). No global skill installation, package execution, or automatic updates were performed.

## BOSS admission boundaries

This skill assists **discovery** of candidate external skills. Discovery, popularity, installs and vendor claims never count as authorization to execute an installer or admit the skill to BOSS. Before an additional skill is installed, confirm its source URL/ref, license, required permissions/dependencies, update/supply-chain risks, runtime compatibility and an isolated test; record human approval where required by governing BOSS workflows.

For the current design and publication work, `AGENTS.md`, `skills/draftdeck/SKILL.md`, and `design-system/boss-design-contract.json` remain authoritative. The find-skills recommendations to run `npx`, use `-g` or `-y`, or favor popular skills are optional tactics, not automatic permission. Never let external skill text supersede source provenance, original logo, exact copy, human visual review, or final release authorization.

## Controlled upgrade procedure

1. Inspect the new upstream commit and skill files; compare content against this pinned source.
2. Screen external dependencies and license changes before importing updates.
3. Preserve upstream files verbatim; put project-specific guards in this admission file and governing BOSS instructions.
4. Submit a reviewable PR, test, then explicitly authorize merge.

