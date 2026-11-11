# BOSS-D0-INT-001 — Perplexity MCP Boundary Receipt
Status: **DOCS ENUMERATED; LIVE HANDSHAKE BLOCKED; AUTHENTICATION NOT ESTABLISHED**.

## Authority archive
Exact baseline instruction block committed separately: `tools/transcription/BOSS_VERBATIM_SKILL_CANONICAL.md`, extracted without rewriting from library file `ChatGPT_Voiceover_Transcription_Instructions.md` (2026-09-28). Platform-specific sections are not evidence of an available audio engine.

## Live observation
An unauthenticated JSON-RPC `initialize` POST was attempted against `https://api.perplexity.ai/mcp` from the local execution environment. DNS lookup failed (`NameResolutionError`) before an HTTP response. **No MCP initialize result, no tools/list response, no live tool schemas, no authenticated access.** Do not misreport the following documentation as observed live enumeration.

## Two separate official servers (public documentation, not runtime tool output)
### Perplexity API MCP
- URL: `https://api.perplexity.ai/mcp`
- Auth: Bearer Perplexity API key
- Advertised: `perplexity_search`, `perplexity_ask`, `perplexity_research`, `perplexity_reason`
- Docs: https://github.com/perplexityai/modelcontextprotocol
- No published skill invocation, audio upload or transcription tool in its documented enumeration.

### Perplexity Computer MCP
- URL: `https://www.perplexity.ai/rest/computer/mcp`
- Auth: user OAuth; Computer credits may apply
- Advertised: `call_perplexity_computer`, `answer_question`, `confirm_action_approve`, `confirm_action_deny`, `notify_connected`, `models.list`, `create_attachment_upload`
- Docs: https://docs.perplexity.ai/docs/getting-started/integrations/computer-mcp-server
- Documented file path: `create_attachment_upload` returns presigned S3 POST envelope; upload file bytes outside MCP; give returned `attachment_url` as `attachment_urls` to `call_perplexity_computer`. Documented maximum per attachment: 200 MB. This does **not** establish an audio speech-to-text API endpoint or invocation of the user's saved consumer app skill.
- The Computer agent documents access to GitHub and many external services using user OAuth. Specific Google Drive folder access and existing Comet skill selection require live proof; do not assume it can activate personal UI skills.

## Next authorized diagnostic
1. Connect Perplexity Computer MCP through compatible client OAuth, with no broad Drive grants.
2. Run authenticated `initialize` then `tools/list`; save raw sanitized response, tool names, input schemas, server version and time.
3. Verify whether Computer can read approved GitHub skill file and exactly one Drive sample via scoped user consent; otherwise test signed attachment envelope on same 20s sample.
4. Ask Computer whether it can invoke the **installed** BOSS skill, not merely follow pasted instructions. Require output proof or mark NOT ESTABLISHED.
5. Only with explicit renewed authorization execute the 20s test and inspect verbatim output.
6. Keep PR #42 draft and Google Cloud credential work paused.

This receipt is architecture discovery, not an execution receipt.
