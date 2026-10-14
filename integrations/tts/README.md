# BOSS Kokoro TTS — Controlled Integration Candidate

**Status:** CANDIDATE / NOT HUMAN-APPROVED / NO RELEASE AUTHORITY.
**Source:** The exact 750-spoken-word, 15-turn Issue 001 mechanical fixture from 2026-10-13. This is not the later 752-word human-review editorial draft.
**Authority boundary:** Human-approved transcript -> Go supervisor REST adapter -> generated segments -> independent QA -> human release. MCP is editorial preview ONLY.

## Runtime

- `compose.yaml`: private-network Kokoro-FastAPI CPU image, configured `v0.9.0`; localhost-bound port 8880. A named release tag is not an immutable digest. The CI captures image digest(s); pin a reviewed digest before production.
- `go-transport/`: standard-library-only Go REST speech client. NEVER calls MCP.
- `audition.py`: Python **test harness** for 750-word baseline + exact one-sentence P12 edit; contacts only localhost REST or the private `kokoro:8880` Docker service. This is not the Go release supervisor.
- `mcp/`: BOSS restricted stdio editorial preview server, optional Docker Compose profile `editorial-preview`, no user-selected paths, voices whitelisted, one constrained backend address, output inside `/data/previews`. It does not run during manufacturing.
- `fixtures/pilot_turns.json`: 15 turns, 750 words, original candidate status preserved.
- `tests/`: mock REST harness tests; mock success does not establish neural model behavior.

## Run mechanically

```sh
cd integrations/tts
python -m unittest discover -s tests -v
(cd go-transport && go test ./...)
docker compose -f compose.yaml config
docker compose -f compose.yaml up -d kokoro
docker compose -f compose.yaml run --rm -T audition-runner audition.py --api-base http://kokoro:8880 --out output
```

The GitHub Actions file `.github/workflows/kokoro-tts-candidate.yml` runs Go, mock, Docker, and 750-word real model audition on push to the specified candidate branch. The job publishes non-release evidence artifacts for human review; it never commits generated media or releases it to the public.

Optional MCP previews can be started by a user-controlled stdio MCP client with `docker compose --profile editorial-preview run --rm -T mcp-preview` (client must explicitly support this command). Neither MCP nor its Docker profile is invoked by the audition script.

## Required checks

- REST-only request to `/v1/audio/speech`, WAV output recorded by voice + source text hash.
- Exact script word count 750 (15 turns); no claims of exact delivered speech without independent listening/transcript QA.
- Pause probe uses **`[pause:2s]`**, the supported Kokoro-FastAPI syntax, NOT `[pause 2s]`. Source text remains unchanged. The final assembled WAV inserts precisely 48,000 zero-valued 16-bit mono samples (2s at 24 kHz), independently of model syntax.
- English IPA transport check uses the known **Worcester** example `[/wˈʊstər/]` per upstream docs. **Bioscillate's intended IPA is not known; no human-approved override was supplied.** Brand pronunciation stays HOLD. Never invent it.
- Change only the designated sentence in turn P12; call synthesis once for P12; copy all 14 other WAV clips byte-for-byte; verify SHA-256 equal to originals. This proves **byte preservation by assembler**, not deterministic repeat synthesis.
- Independent human listening, word-fidelity comparison, naturalness, correct pronunciation, cost, join quality and public release are all HOLD until inspected.

## Security review of third-party MCP

Inspected `giannisanni/kokoro-tts-mcp` at commit `855b2af58b25154b840d2652cc774de8905896a2` on October 13, 2026. **Do not vendor without fixes:** `generate_speech(save_path)` creates arbitrary supplied directories; `voice` can be interpreted as an arbitrary local file for `torch.load` in local mode; optional host playback calls programs; a configured remote URL can send text outside a private environment. No explicit telemetry function was seen in inspected first-party Python source, but dependency egress has not been disproven. The constrained server here is a new, small BOSS wrapper; its transitive dependencies, container behavior and deployed runtime remain subject to further review.

## Release states

`LOCAL_MOCK_PASS` is not `KOKORO_AUDITION_PASS`. `KOKORO_AUDITION_PASS` is not `SPOKEN_FIDELITY_PASS`. `SPOKEN_FIDELITY_PASS` is not `HUMAN_RELEASE_APPROVED`. All output is candidate-only and transcript-first.

**Private-network test transport:** CI checks readiness from inside the Kokoro container, and the audition runner executes inside the private Docker bridge. Neither step depends on reaching an internal-network service from the GitHub runner host.
