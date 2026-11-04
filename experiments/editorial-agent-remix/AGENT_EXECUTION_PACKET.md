# BOSS Editorial Precision — isolated agent execution packet v1

Status: READY_FOR_INPUT_STAGING / AGENTS_NOT_EXECUTED
Authority: design-system/boss-editorial-precision-contract-v1.json (experimental replacement candidate)
Reference manifest: experiments/editorial-agent-remix/five-reference-run-manifest.json

## Runner prerequisites
- Stage five user-supplied references A-E in private, access-controlled runner storage. Never commit unpublished binaries to public repository. Record SHA-256, dimensions, provenance, permission to use and identical immutable paths for both runs.
- Obtain explicit qualified runner configuration, model name/version/license, runtime dependencies, network/egress policy and scoped read/write credentials. No production tokens or protected gateway routes.
- Before execution record an exact prompt digest and image digests; halt if any are missing.
- Do not assume a GitHub file, specification, or manifest means OpenHands or bolt.diy is installed or connected.

## Identical task for both candidates
Build THREE distinct 1920x1080 editorial slide variants using React and Tailwind, based on all five reference images. Use original design interpretation, not literal reproduction of third-party branding. Prioritize premium magazine hierarchy, photorealistic PNG art placement, pure-white ground, CMYK accent restraint, Tesla-like operator navigation, Apple-like typographic spacing and CAD technical rails. Use placeholders if the source PNGs cannot be safely staged; do not invent approved story artwork. All text must be editable HTML/CSS; SVG only for geometric technical elements. Keep artwork and text independently replaceable. Use fictional, clearly marked sample copy, not unpublished Episode Zero manuscript.

Variant 1: hero-dominant editorial spread.
Variant 2: chapter opener with operator navigation.
Variant 3: dense instructional page with modular learning panels.

## Required deliverables per candidate
- Source files and locked dependency manifest; reproducible setup instructions.
- Three exact 1920x1080 browser screenshots, and accessible Storybook or equivalent component review.
- Playwright clipping/geometry checks, Vitest contract checks, Sharp image metadata report.
- Side-by-side reference assessment A-E, deviation log and editable-text proof.
- PDF export inspection at declared physical size; separate raster art sharpness and text selection results.
- CPU/RAM/runtime metrics, egress/credential audit, and PASS/FAIL/NOT TESTED evidence ledger.

## Independent review gates
1. INPUT_READY: five image hashes and authorized private paths verified.
2. RUNNER_QUALIFIED: isolated execution and permissions verified.
3. IMPLEMENTED: actual source commits and screenshots exist.
4. QA_VERIFIED: automated and visual evidence inspected.
5. HUMAN_DECISION: owner accepts or rejects candidate; no automatic merge/deploy.

## Current facts
INPUT_READY=BLOCKED (image binaries not yet accessible as verified runner inputs)
RUNNER_QUALIFIED=NOT_TESTED
IMPLEMENTED=NOT_TESTED
QA_VERIFIED=NOT_TESTED
HUMAN_DECISION=PENDING

No deployment, production gateway reuse, image generation, or release is authorized by this packet.
