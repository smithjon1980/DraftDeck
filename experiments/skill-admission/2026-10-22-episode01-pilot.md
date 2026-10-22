# BOSS external skills — Pilot 04: admission and baseline evaluation
Date: 2026-10-22
Status: **CANDIDATE — NOT APPROVED FOR MAIN OR RELEASE**

## Source and scope
The installed \`find-skills\` discovery process shortlisted three candidates against Episode 01 Slide 02's known defects. This PR stages exactly two **project-scoped** skills, without executing their upstream helpers or granting any new release authority:

| Skill | Upstream pinned commit | License | Candidate verdict |
| --- | --- | --- | --- |
| \`webapp-testing\` | \`anthropics/skills@dbd4588f9e1033efb41dad4bef2f7947c8993d44\` | Apache-2.0 | CANDIDATE: Python Playwright compatible with system Chromium |
| \`diagnosing-bugs\` | \`mattpocock/skills@5beb35b040e3de97e54fa9e386d7e42d15c295c2\` | MIT | CANDIDATE: reproducible negative-case technique; no agent outcome A/B benchmark yet |
| \`skill-creator\` | \`anthropics/skills@dbd4588f9e1033efb41dad4bef2f7947c8993d44\` | Apache-2.0 | HOLD: upstream \`run_eval.py\` invokes \`claude -p\`, unavailable in this environment. Not installed. |

Pinned upstream skill source and helper blobs are guarded by \`tests/test_external_skill_admission.py\`. No transitive installer, global skill installation, remote script execution, or automatic update has been authorized.

## Executed local regression (private evidence)
Source: owner-provided \`BOSS_Episode01_3Slide_Interactive_Candidate.html\`, used only in an isolated Chromium/Python environment; no source assets or screenshots committed here.

- Browser navigation to Slide 02: **PASS**
- Logical canvas 1920x1080: **PASS**
- Exact recovered candidate headline / list copy: **PASS**
- Canonical supplied logo embedded image SHA256 match: **PASS**
- Native HTML headline and PDF-selectable text: **PASS**
- PDF 1440x810 pt / 828 selectable characters / one image: **PASS**
- Controlled failure injection: replace required headline → copy validation fails: **PASS**
- Controlled failure injection: remove logo element → logo identity validation fails: **PASS**
- Browser-to-PDF raster pixel comparison: mean absolute RGB channel difference **6.753/255**, **5.455%** of pixels have at least one channel difference >20 after 1920x1080 alignment. **Numerical evidence, not a subjective quality pass.**
- Distinct story illustration: **FAIL** (only the logo image is present)
- Author-approved reflection question: **FAIL** (placeholder remains)
- Approved reference, actual human visual acceptance, adapter import/edit/save/reopen: **HOLD / NOT_TESTED**

**Interpretation:** Browser and diagnostic workflow are reproducible. The image shows a comparison table, not the original rich story artwork. Export fidelity does not repair source-composition gaps.

## Dependencies, risks and non-claims
- Python Playwright imports; default Playwright-managed Chromium binary is missing. The local system Chromium executable \`/usr/bin/chromium\` works, and \`page.set_content\` bypasses blocked \`file://\` navigation. These adaptations are **environment-specific**, not portability guarantees.
- Upstream \`webapp-testing/scripts/with_server.py\` uses \`subprocess.Popen(... shell=True)\` for the user-supplied server command. **Do not execute it on untrusted command strings.** Not run in this pilot. Use the direct offline Playwright harness for private slides.
- Upstream \`diagnosing-bugs\` references adjacent optional skills (e.g., codebase-design). These are not imported or implicitly authorized.
- Node v22.16.0 in the local runtime is below the Skills CLI documented Node >=22.20.0 requirement; \`npx skills add\` completion is **not** claimed.
- No model A/B comparison establishes that adopting either skill improves the *quality of a newly composed* slide. These are admission and technical-feasibility tests only.
- Existing \`AGENTS.md\`, \`skills/draftdeck/SKILL.md\`, original brand/design contract and visual-evidence gate override all imported advice. A third-party skill cannot authorize asset substitutions or release.

## Next authorized gate
1. Check PR CI and independently review exact imported source files, license and helper security.
2. Confirm actual agent use in an isolated DraftDeck test (not production) with the same source, prompt, model, browser and acceptance rubric, measuring before-vs-after.
3. Build one *new* source-grounded story composition only after reference and artwork admission. Collect actual browser render, PDF parity, separate story-art evidence and a reviewer decision.
4. Keep Episode 01 publication on **HOLD** until human visual approval.
