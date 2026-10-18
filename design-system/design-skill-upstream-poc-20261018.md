# Design skills / Episode 01 print proof — upstream review and adoption gate

**Status:** REVIEW CANDIDATE — original BOSS source remains authoritative. No third-party skill installed in the DraftDeck repository, no changes to the 1920x1080 slide contract, no public upload of the 3,578-word script, and no authorized publication or merge.

## Intent

Test whether selected open-source design instructions can reduce boxy SVG-like layouts while preserving original BOSS typography, black/cyan/magenta brand, narrative fidelity, and required visual evidence. Reuse existing technical artwork for an **independently composed** 17x11 landscape proof. Record separate structural, aesthetic and print gates. This is not a request to clone any upstream brand.

## Upstream revision inventory (reviewed 2026-10-18)

| Source | Revision pinned for audit | Declared license | Admission |
|---|---|---|---|
| [Taste Skill](https://github.com/Leonxlnx/taste-skill) | `f624f37a8c650b9cc550253104925efe4c8de246` | MIT | Reference only. No `npx skills add` until full file, asset-credit, executable and dependency review. |
| [Impeccable](https://github.com/pbakaus/impeccable) | `2f46b7a8b059af00d20dd13b64dbe165e7c6a742` | Apache-2.0 | Reference only. Its installer may provision binaries and provider hooks: no unattended install. |
| [Microsoft Playwright CLI](https://github.com/microsoft/playwright-cli) | `b85c7a736bb473bf55b584e54a09ffa698d6d871` | Apache-2.0 | Candidate for sandboxed, purpose-limited browser tests; do not run untrusted pages with credentials. |
| [VoltAgent Awesome DESIGN.md](https://github.com/VoltAgent/awesome-design-md) | `3b605329240ce735b510037cca322f1831fdd7f8` | MIT | Read-only design-analysis inspiration. Do **not** import a Tesla or third-party theme as BOSS identity. |
| [img2threejs](https://github.com/img2threejs/img2threejs) | `d508b596cb221f1509f6e50ab68fce275a5cfb44` | Apache-2.0 | Deferred. No 3D requirement or fidelity evidence for current 11x17 editorial print. |

A repository's license alone does not establish that bundled photos, assets, dependencies, or optional cloud services are free to reuse. Check license notices, transitive packages, recent security advisories, untrusted scripts and maintenance before any install.

## Evidence from private prototype (not committed here)

A local, unpublished experiment composed two 17x11 landscape pages from full, consecutive paragraphs of the candidate Episode 01 script (section 01, paragraphs 1-5; section 02, paragraphs 1-3). It used existing BOSS art from the owner's local assets rather than external example imagery. Candidate titles/captions are separately labeled non-spoken editorial material. Print profiles were authored independently of the 1920x1080 slide renderer.

- Browser testing ran with an already available **Python Playwright package and local Chromium**, not with upstream Playwright CLI installed in DraftDeck.
- A private exact-copy manifest validated all eight source paragraphs in the HTML; the PDF extractor independently found all eight paragraphs with whitespace-only normalization.
- A two-page PDF was rendered and verified: both MediaBoxes measured 1224x792 points, both contained selectable text, page 1 had no images and page 2 contained an independent image.
- Screenshots were visually inspected locally; no design candidate is marked human-approved or printer-certified. The complete original manuscript and art evidence were **not** copied into this public branch.
- The Taste and Impeccable agents were **not installed or executed**; no claim of benchmarked upstream improvement is made.

## Public reproducible verification utility

Run `python tools/visual-poc/check_print_pdf.py path/to/PRIVATE_proof.pdf --expected-pages 2 --private-manifest path/to/PRIVATE_manifest.json` in a bounded local environment after installing and recording an approved PyMuPDF revision. The optional private manifest has `exact_text_segments` mapping page numbers `"1"`, `"2"` to ordered arrays of complete source paragraphs. Without a manifest, the copy gate remains `NOT_TESTED`. **Do not push the manifest, unreleased narration, screenshot, or original artwork to public GitHub.**

## Approval matrix

| Gate | State now | Remaining operation |
|---|---|---|
| Upstream identity/license declared | VERIFIED AS DECLARED | Review complete dependency, executable/hook and bundled asset licenses before installing |
| Contract separation: slide / print | PRESERVED | Confirm at PR inspection |
| Source-to-DOM copy exactness | PASS (private two-page proof only) | Repeat for approved full manuscript |
| Browser render | PASS (local structural proof only) | Run controlled responsive/browser versions with captured evidence |
| Print geometry and extractable text | PASS (local two-page proof only) | Repeat on all pages with physical printer requirements |
| Taste and Impeccable command audit | NOT_TESTED | Sandbox each separately; compare before/after against an approved reference |
| Human visual selection | PENDING | Review competing editorial designs, especially art-text integration |
| 48-page issue and publication | NOT BUILT / HOLD | Approve script, source art and full print profile first |

**Gate rule:** a skill suggestion, passing browser test or valid PDF is never equivalent to an approved BOSS visual master, source manuscript, print publication, or Canva editable design.
