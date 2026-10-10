-- BOSS Tool Observatory v0.1 · migration proposal (PostgreSQL)
CREATE TABLE IF NOT EXISTS boss_tool_run (
 run_id TEXT PRIMARY KEY, tool_id TEXT NOT NULL, tool_version TEXT,
 environment_id TEXT NOT NULL, repository_commit TEXT, input_sha256 TEXT,
 recorded_at TIMESTAMPTZ NOT NULL DEFAULT now(), status TEXT NOT NULL,
 cli_status TEXT NOT NULL, mcp_status TEXT NOT NULL,
 raw_evidence JSONB NOT NULL, evidence_sha256 TEXT NOT NULL,
 CHECK (status IN ('ENVIRONMENT_BLOCKED','CONFIG_ONLY_VERIFIED','CLI_ONLY_VERIFIED','VERIFIED_MCP_CALL','FAILED_WITH_EVIDENCE'))
);
CREATE TABLE IF NOT EXISTS boss_model_response (
 response_id TEXT PRIMARY KEY, run_id TEXT NOT NULL REFERENCES boss_tool_run(run_id),
 provider TEXT NOT NULL, displayed_model TEXT NOT NULL, prompt_version TEXT NOT NULL,
 prompt_sha256 TEXT NOT NULL, packet_sha256 TEXT NOT NULL,
 repeat_index INT NOT NULL, settings JSONB NOT NULL DEFAULT '{}'::jsonb,
 raw_response TEXT, error TEXT, recorded_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 UNIQUE(run_id,provider,displayed_model,prompt_sha256,repeat_index)
);
CREATE TABLE IF NOT EXISTS boss_review (
 review_id TEXT PRIMARY KEY, response_id TEXT NOT NULL REFERENCES boss_model_response(response_id),
 reviewer_id TEXT NOT NULL, diagnostic_quality INT, evidence_discipline INT,
 instruction_fidelity INT, actionability INT, rationale TEXT, adjudicated BOOLEAN NOT NULL DEFAULT false,
 CHECK (diagnostic_quality BETWEEN 0 AND 3), CHECK (evidence_discipline BETWEEN 0 AND 3),
 CHECK (instruction_fidelity BETWEEN 0 AND 3), CHECK (actionability BETWEEN 0 AND 3)
);
