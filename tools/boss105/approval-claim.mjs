// BOSS-105: cryptographic scope check for signed human-decision CLAIMS.
// A valid signature is NOT human-authenticated approval or durable ledger custody.
import crypto from "node:crypto";
const HASH=/^[a-f0-9]{64}$/;
const ORDER=["schema","gate","actor_id","event_id","nonce","issued_at","expires_at",
  "source_digest","candidate_id","candidate_sha256","preview_sha256",
  "target_id","profile","composition_id","ledger_ref"];
export function canonicalApprovalClaim(record) {
  const payload={};
  for (const k of ORDER) payload[k]=record[k];
  return Buffer.from(JSON.stringify(payload),"utf8");
}
export function verifySignedClaim(record,signatureBase64,trustedKeyPem,expected,seenEvents=new Set(),now=Date.now()) {
  const fail=(code)=>({status:"FAIL",code,cryptographic:"FAIL",authority:"HOLD"});
  if(!record || typeof record!=="object" || !expected) return fail("MISSING_INPUT");
  if(record.schema!=="BOSS-APPROVAL-CLAIM/1.0") return fail("CLAIM_SCHEMA");
  if(!["ART","STORY","OPENER","CLOSER","EDITORIAL","NARRATIVE","LAYOUT","RELEASE"].includes(record.gate)) return fail("GATE_INVALID");
  for(const k of ORDER) if(typeof record[k]!=="string" || !record[k].trim()) return fail("MISSING_FIELD_"+k);
  for(const k of ["source_digest","candidate_sha256","preview_sha256"])
    if(!HASH.test(record[k])) return fail("DIGEST_INVALID_"+k);
  if(!record.actor_id.startsWith("human:")) return fail("ACTOR_NOT_HUMAN_CLAIM");
  if(record.nonce.length<16) return fail("NONCE_TOO_SHORT");
  const issued=Date.parse(record.issued_at), expiry=Date.parse(record.expires_at);
  if(!Number.isFinite(issued) || !Number.isFinite(expiry) || issued>now || expiry<=now || expiry<=issued) return fail("EXPIRED_OR_INVALID_WINDOW");
  if(seenEvents.has(record.event_id)) return fail("REPLAY_EVENT_IN_PROCESS");
  for(const k of ["gate","source_digest","candidate_id","candidate_sha256",
    "preview_sha256","target_id","profile","composition_id"])
    if(record[k]!==expected[k]) return fail("APPROVAL_SCOPE_MISMATCH_"+k);
  if(typeof signatureBase64!=="string" || typeof trustedKeyPem!=="string") return fail("MISSING_SIGNATURE_OR_TRUST_ANCHOR");
  try {
    const key=crypto.createPublicKey(trustedKeyPem);
    if(key.asymmetricKeyType!=="ed25519") return fail("UNSUPPORTED_KEY");
    const ok=crypto.verify(null,canonicalApprovalClaim(record),key,Buffer.from(signatureBase64,"base64"));
    if(!ok) return fail("SIGNATURE_MISMATCH");
  } catch {
    return fail("SIGNATURE_INVALID");
  }
  seenEvents.add(record.event_id);
  return {status:"HOLD",cryptographic:"PASS",scope:"PASS",authority:"HOLD",
    code:"INDEPENDENT_LEDGER_ACTOR_CUSTODY_AND_DURABLE_REPLAY_REQUIRED",
    note:"Signature proves only a trusted-key cryptographic claim. Key-to-human attribution, independent ledger readback and replay resistance remain external."};
}

