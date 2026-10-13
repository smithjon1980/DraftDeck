# BOSS / DraftDeck Layered Swarm 001

**Candidate architecture; user-approved for prototyping, not implemented as operational agents.**

Layer responsibilities: Story = background narrative; Art = editable explanatory diagrams and structure; Text = exact authorized editable copy. Stack white base → Story → Art → Text.

LangGraph is the sole orchestration framework. Supervisor emits a common immutable scene contract and routes layer tasks with exact allowed file types and bounding regions. The Assembly Worker uses React/CSS and Chromium deterministically; independent QA checks each layer and final page.

Failure classes: L0_UNAUTHENTICATED, CONTRACT_INVALID, LAYER_SCOPE_VIOLATION, UNLICENSED_ASSET, PIXEL_TEXT, TEXT_DRIFT, ART_MISROUTED, ASSEMBLY_OVERFLOW, PDF_EXPORT_FAILURE, HASH_MISMATCH, VISUAL_FIDELITY_FAIL, STORAGE_NOT_VERIFIED, RELEASE_UNAUTHORIZED.

Per-layer rework with maximum two attempts; unknown provenance or side-effect state leads to HOLD. No release without human approval. GitHub Actions artifacts expire and do not meet durable storage acceptance.

Next task: wire the layer adapters into LangGraph, generate a three-layer test fixture, assemble, compare extracted PDF copy, inspect preview visually, and verify source and output hashes.