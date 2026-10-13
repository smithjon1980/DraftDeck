# BOSS Swarm 001 — Execution Request

Authorized by user request: **run workflow**.

GitHub Actions workflow: `.github/workflows/draftdeck-swarm-trial.yml`.
Trigger: commit on candidate branch, limited to this experiment's path.

Expected checks: isolated dependency installation, LangGraph unit tests (instructional PDF/vector/research routing, invalid input HOLD, bounded repair), and mock demo.

This is **not** authorization to deploy, perform external side effects, use real model APIs, or claim persistent-file delivery. A passing graph test is not an end-to-end production test.

Evidence must be taken from the actual GitHub Actions run; if no run is visible, status remains **NOT VERIFIED**.
