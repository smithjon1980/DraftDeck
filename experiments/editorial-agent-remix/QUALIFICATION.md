# BOSS Editorial Precision — two-reference React remix qualification

Status: EXPERIMENT / NOT APPROVED / NO RELEASE
Branch: experiment/editorial-agent-remix-qualification
Owner of final visual and release decisions: human

## Objective
Compare OpenHands and bolt.diy as candidate implementation agents for a 1920 × 1080 React/Tailwind editorial slide derived from the SAME two owner-approved reference images. Neither agent is admitted or connected merely by appearing here.

## Source and reference gates
- Require reference-A and reference-B image files with provenance and explicit human authorization. Until supplied: BLOCKED_REFERENCE_INPUT.
- Read AGENTS.md, design-system/README.md, and design-system/boss-design-contract.json before implementation.
- Episode Zero v0.19 is an unapproved candidate. Do not ingest its complete manuscript into public branches, generate release artwork from it, or imply editorial approval. A fictional placeholder headline may be used for layout-only qualification.
- The repository contract currently says no photorealistic imagery; the newer owner direction is PNG-first photographic editorial art. Record this as CONTRACT_CONFLICT and request a separate human-approved contract amendment before final art composition. Do not silently overwrite the contract.
- Keep private reference binaries and unpublished narration out of public PRs.

## Identical agent task
Given the two authorized references and a design brief, create three distinct candidate compositions, each:
- Fixed logical 1920 × 1080 slide; separate responsive web behavior if added.
- React + Tailwind; native editable HTML/CSS typography and annotations.
- White editorial ground, restrained cyan #00BCEB and magenta #E30074; controlled yellow only after separate brand approval.
- Tesla Model Y center-screen information hierarchy, Apple-like typography/spacing restraint, magazine-quality editorial storytelling, CAD/ISO-informed thin geometry.
- Placeholder for PNG artwork; do not generate or trace imagery in this qualification.
- SVG only for grids, lines, icons and geometric technical elements; no full-slide rasterized text.
- No gradients, heavy shadows, generic SaaS cards, stick figures, or borrowed brand logos.
- Clear source/status metadata rail and visibly marked candidate state.

## Tools to qualify, not auto-install
- OpenHands (candidate A) and bolt.diy (candidate B); compare licensing, permissions, dependency/runtime versions, network egress and credential exposure before execution.
- Vision-capable model (candidate; license and CPU feasibility not established).
- Storybook (component inspection), Playwright (1920x1080 screenshots and layout checks), Vitest (component/contract tests), Sharp (PNG metadata/size), existing VTracer/Inkscape (separate optional trace/PDF qualification).
- Run in isolated, least-privilege environments without production secrets or access to protected write routes.

## Evidence required from EACH candidate
1. Agent version, model/version/license, environment, exact input reference hashes and prompt hash.
2. Git commit/diff, package lockfile, dependency and security review.
3. Three browser screenshots at exactly 1920 × 1080; original source image dimensions and no upscaling claims.
4. Native text editability proof, art/text separation proof, geometry and no-clipping tests.
5. Side-by-side comparison with each input reference and a documented deviation log.
6. Storybook inspection, Playwright/Vitest output, CPU/RAM/runtime measurements.
7. PDF export inspected separately for image sharpness, font/text fidelity, clipping and intended print size.
8. PASS / FAIL / NOT TESTED for visual fidelity, editorial quality, accessibility, editability, security, reproducibility and PDF fidelity.

## Stop conditions
No images supplied -> do not claim a visual remix was tested.
No connected/qualified coding agent -> do not claim delegated execution.
No browser screenshots -> visual fidelity NOT TESTED.
No approved art/story -> no final composition.
No explicit human decision -> HOLD; no merge or publication.
No approved non-bypassable gateway and custody -> no production write or deployment.

## Immediate next step
Obtain the two exact reference images (or their approved repository paths) and qualify the agent runtimes in an isolated environment. This document is a test specification, not evidence of tool installation, benchmark completion, or approved visual output.
