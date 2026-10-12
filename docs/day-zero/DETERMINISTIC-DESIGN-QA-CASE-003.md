# Day Zero Case — Taste as a Testable Constraint
Status: INSTRUCTIONAL_CANDIDATE / NOT_TESTED
Why: A transcript about Paul Bakaus's Impeccable describes committing product context and visual rules rather than repeatedly asking a frontier model to 'make it more premium.'
Do not treat promotional statements about quality or 'zero cost' as measured DraftDeck outcomes. Offline detector runs may have setup and maintenance cost even if no API tokens are consumed.

Learner question: If a slide uses the wrong font, do we need a general AI model to discover it?
Manual demonstration: compare reference font/color specification against an HTML file; identify a mismatch and quote the authoritative design token. Contrast deterministic font check (script/program) with subjective composition fidelity evaluation (human and optionally model).
Three quadrants:
A: human reviewer, agent assistant, DraftDeck QA skill, HTML/CSS parser as tool.
B: manual inspection → deterministic program → optional model critique if uncertainty remains.
C: SOP layout QA; KPI reproducible rule failures; OKR optional; CAPA update source, rebuild and retest.
Counterexample: third-party linter rejects Arial while DraftDeck requires Arial. Correct resolution: record reviewed exception, preserve governing source, not override doctrine to make the linter green.
Assessment: learner explains false positive, versioned design truth, why source files outrank generated output, and how automated checks differ from visual fidelity.
No aviation metaphors. No new architectural layer.
