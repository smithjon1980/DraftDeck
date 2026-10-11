import express from "express";
import crypto from "node:crypto";

const app = express();
app.disable("x-powered-by");
app.use(express.json({ limit: "8kb" }));
const path = "/api/v1/diagnostic/synthetic-run";
const token = process.env.ENVSCAN_WINDMILL_SECRET;
if (!token) throw new Error("ENVSCAN_WINDMILL_SECRET must be configured");

function authorized(header) {
  if (!header?.startsWith("Bearer ")) return false;
  const supplied = Buffer.from(header.slice(7));
  const expected = Buffer.from(token);
  return supplied.length === expected.length && crypto.timingSafeEqual(supplied, expected);
}
app.post(path, async (req, res) => {
  res.setHeader("Cache-Control", "no-store");
  if (!authorized(req.get("authorization"))) return res.status(401).json({ error: "AUTHENTICATION_REJECTED" });
  const { correlation_id, mission_profile } = req.body ?? {};
  const valid = typeof correlation_id === "string" && /^[A-Za-z0-9_-]{8,100}$/.test(correlation_id) &&
    mission_profile === "HANDSHAKE_TEST";
  if (!valid) return res.status(400).json({ error: "CONTRACT_VIOLATION" });
  const started_at = new Date().toISOString();
  await new Promise(r => setTimeout(r, 1500));
  const receipt = { schema_version: "0.1.0", correlation_id, mission_profile, diagnostic_code: "E9999_SYNTHETIC",
    outcome: "EXPECTED_SYNTHETIC_FAILURE", started_at, completed_at: new Date().toISOString(),
    executor: "railway-wr001", synthetic: true };
  console.log(JSON.stringify({ event: "synthetic_execution", correlation_id, outcome: receipt.outcome, completed_at: receipt.completed_at }));
  return res.status(200).json(receipt);
});
app.use((err, req, res, next) => {
  if (err instanceof SyntaxError && "body" in err) return res.status(400).json({ error: "CONTRACT_VIOLATION" });
  if (err?.status === 413) return res.status(413).json({ error: "PAYLOAD_TOO_LARGE" });
  return res.status(500).json({ error: "EXECUTION_ERROR" });
});
const port = Number(process.env.PORT || 3000);
app.listen(port, "0.0.0.0", () => console.log(JSON.stringify({ event: "listening", port })));
