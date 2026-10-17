# OpenCode control plane candidate

OpenCode is a source dependency of the BOSS project. `upstream.json` identifies its repository, immutable commit, license, and build boundary. The checkout script places the source in `tools/opencode/upstream/`, excluded from DraftDeck commits; the upstream history and MIT notice remain intact.

## Acquire the source

From the DraftDeck root, run:

```sh
python3 tools/opencode/checkout.py
```

For a source build, follow `upstream/AGENTS.md` and `upstream/CONTRIBUTING.md`. The inspected snapshot declares Bun 1.4.2. Its `bun install` executes upstream installation hooks. Read those instructions before building; no source build was tested in the initial integration. Review and change the pinned commit explicitly for upgrades, then rerun the checkout script. Existing local edits stop checkout rather than being overwritten.

## Execution status

- OpenCode source cloned and its MIT notice inspected.
- The earlier installed runtime was `opencode-ai` 1.19.3. It reached Kaggle MCP and listed the server as connected; private notebook access returned a permission error.
- This source snapshot declares version 2.0.32. It has not inherited the earlier runtime's validation, and its configuration and commands must be checked against this snapshot before migration.
- Kaggle account authorization, model provider sign-in, source build, VPS hosting, and mobile web access remain unverified.
- No credentials, model weights, audio outputs, or upstream dependencies are committed here.

## First operational check

Connect the official Kaggle MCP endpoint `https://www.kaggle.com/mcp` using the installed version's supported authentication flow. Verify private access to `smithjon1980/boss-audio-003-kaggle-setup-repair`, retrieve its existing `BOSS_AUDIO_003_RESULTS.zip`, validate archive integrity and inventory the three WAV files. Do not regenerate the audio as part of retrieval. A discovery or generic OAuth success message alone does not prove private access.

BOSS instructions and integration code belong in DraftDeck. OpenCode provides execution tooling; Kaggle provides GPU compute; GitHub records source; persistent artifact storage retains outputs; Seven authorizes release. A repository stores the setup but still needs a running computer or VPS to execute it. Phone and computer access require an authenticated reachable web deployment, which this PR does not provision.

## License and attribution

OpenCode is copyright (c) 2025 opencode and distributed under the MIT license. The source checkout retains upstream `LICENSE`; retain its notice in copies and distributions. This integration does not change DraftDeck's own license or imply upstream endorsement.
