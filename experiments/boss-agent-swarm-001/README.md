# BOSS Swarm — Agent Routing and PDF Worker Trial
Status: CANDIDATE / SOURCE COMMITTED / CI OUTCOME UNVERIFIED.

The LangGraph routing graph remains a mock supervisor, with branched worker functions, bounded retry, independent VERIFY state and HOLD. The **separate PDF worker** now launches actual Playwright Chromium and writes a real PDF with SHA256 manifest. This worker is not yet wired as a node inside LangGraph; the separate CI job tests production of PDF bytes, rather than implying a fully connected agent swarm. The fixture page is an experiment, **not** an accepted design. CI attachments expire after 7 days and are **not persistent delivery**.

On GitHub Actions the `draftdeck-swarm-pdf-worker.yml` workflow runs node tests, installs Chromium, calls `src/build-demo.mjs`, verifies the PDF signature, and uploads a seven-day build artifact. We still require: successful CI log, actual PDF visual/text QA, source provenance checks, model worker integration, durable state and storage, human release authorization.
