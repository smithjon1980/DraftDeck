# Internal Slide Studio — working candidate 0.1

Slide Studio runs at `/tools/slides/` inside the existing BOSS OpenCode Railway service. It inherits the Google/Basic gateway; no additional service or public sharing is created. The internal-tools hub links to it.

## Working flow

1. Create a project and register exact source excerpts by pasting text or importing `.txt` / `.md` (60 KB per source, 20 sources). Record the file/page/timestamp alongside the excerpt. PDF extraction and remote Drive/GitHub discovery are not implemented.
2. Record Bridge 1 (source to reimagined story) and Bridge 2 (story to the existing visual system). Unknown source information remains explicit.
3. Enter exact title, supporting statement, body, evidence/limits, and reflective question for each slide; link source records. Up to 12 slides per project.
4. Compare A–D: editorial split, Evidence Window, Working Agreement reference layout, reflection rail. These are deterministic React compositions of the same supplied copy, not four model-generated concepts. Preview is a scaled 1920 × 1080 canvas. Bounds checks flag some overflow; NOT FLAGGED is not visual acceptance.
5. Search and select separate artwork from the existing atlas. Source and reuse information follows the selected artwork into the HTML and Markdown exports. The original supplied bioscillate image is embedded, not redrawn.
6. Save and record an explicit human review when the required fields are complete. Any content change clears that record; selecting a template is not approval. A recorded review does not establish factual verification or Canva editability.
7. Download a self-contained static HTML deck, Markdown companion, or JSON project backup. Restore a backup as a new project; review is not imported. Candidate exports remain marked CANDIDATE. HTML uses native text elements and separate embedded images, with no runtime React or external styles/assets. Source and reuse notes are appended. Browser print to PDF is available through the exported HTML's print stylesheet, but print fidelity must be inspected independently.

## Persistence and access

Projects are JSON records under `${BOSS_WORKSPACE}/slide-studio` (normally `/data/workspace/slide-studio`) on the existing Railway volume. Saves are explicit; the UI warns about unsaved navigation. Writes are serialized and atomically renamed. Revision matching rejects concurrent overwrites, and a content SHA-256 binds review to the saved content. Limit: 100 projects, 2 MB request bodies. No project deletion endpoint. This is a single-owner, single-replica tool, not multi-tenant storage. A backup is recommended before service changes; a volume is not an independent backup.

No model, NotebookLM, image-generation or audio calls are made by Slide Studio. It does not execute pasted source text or fetch supplied source URLs. Sources and projects are private to the existing authorized gateway. Existing OpenCode has its own provider/network behavior.

## Build and checks

React 19.3.1; Tailwind CSS / CLI 4.3.3; esbuild 0.28.2. `npm run build:studio` compiles local React/Tailwind sources to `public/studio`. Docker installs build dependencies, builds the UI, then prunes dev dependencies. The runtime still uses the existing Express gateway.

`node --test tests/slide-studio.mjs`: persistence/restart, stale saves, review invalidation, invalid references/oversize fields/forged review, and A–D native-text rendering with escaped untrusted text. These tests do not start OpenCode or call external providers.

The broader `npm test` run was blocked by automatic approval review because its OpenCode integration tests may contact `models.opencode.ai`; no claim is made that those tests passed for this change. The Google gateway test source now includes Slide Studio's page/list route and cross-origin POST rejection, but that expanded test has not been verified in this run.

Local browser QA was unavailable under the current managed Sites skill: the required control-browser skill is not installed. Build, route and text-layer checks do not establish mobile visual acceptance, browser export rendering, or PDF/Canva fidelity. Inspect the deployed page and exported deck before production use. This is infrastructure and an editing workflow; no new Episode 01 content or approved slide master is supplied.
