# Layered Swarm Executable Trial 001
Status: CANDIDATE / MOCK LAYER WORKERS / CHROMIUM REAL / VISUAL QA NOT ESTABLISHED.

LangGraph routes to three distinct mock layer workers using immutable JSON files with SHA256 outputs. Story emits a **white placeholder** (not a generated image), Art emits editable diagram instructions, Text emits structured wording. Deterministic assembler creates standalone HTML; actual Chromium exports PDF. Structural QA checks output signature and hash and returns AWAITING_HUMAN_VISUAL_REVIEW, never production PASS.

The initial graph executes layer workers sequentially to avoid shared-state collision. This demonstrates separation and isolation, not parallel execution or cooperation between LLMs. Files are a CI artifact for seven days only.

Success criteria for next iteration: authenticated approved source, story illustration model/tool, art geometry component renderer, exact PDF text extraction against source, clipping QA, richer reference fidelity, persistent file link with read-back, and human release.