# BOSS Governed Agent Swarm — Trial 001
Status: SPECIFIED / CI TEST REQUESTED / NOT DEPLOYED.
Orchestration choice: open-source LangGraph.js. This first executable experiment is a **deterministic agent-shaped graph**, not yet an LLM-powered swarm. It tests the routing and authority contract before connecting model agents.
User request → Supervisor → Requirements → Design → Artwork → Verification → HUMAN_REVIEW/HOLD. The role nodes return structured stubs, not produced designs, PDF files or storage links.
A later authorized phase can replace each specialist node with a bounded LLM agent or a deterministic tool, retaining the same state transitions and checks. Dynamic supervisor selection should be restricted to an enumerated set of approved worker identities.
Human approves any external side effect, repository mutation, generation cost, permanent storage upload, and release. No unbounded loops or blind retries. GitHub Actions CI is a build/test environment, **not persistent storage**.
Run: `npm install --ignore-scripts && npm test`. No secrets required.
Do not claim the model has already created a PDF or generated a persistent link.
