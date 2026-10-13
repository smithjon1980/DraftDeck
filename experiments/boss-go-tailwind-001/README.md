# BOSS Go + Tailwind + Chromium trial 001

Candidate-only standalone trial. GitHub Actions builds Tailwind CSS from a fixed input, runs Go's html/template renderer, invokes headless Chromium to create a real 16:9 PDF, checks the PDF signature, and writes a SHA-256 manifest. No React runtime and no SVG source or SVG intermediate stages.

This is a deterministic template trial, **not a live generative agent swarm**. Story, Art, and Text assignments remain an architecture for a later iteration; this trial establishes the renderer first. Passing CI does not establish visual fidelity, Canva text editability, or production approval. Main is not targeted.
