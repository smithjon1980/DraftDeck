// BOSS 105 — read-only local source identity check; no network or archive writes.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { pathToFileURL } from "node:url";

const hex64=/^[a-f0-9]{64}$/;
const hex40=/^[a-f0-9]{40}$/;
function safeRel(p) {
  return typeof p==="string" && p.length>0 && !path.isAbsolute(p)
    && !/^[A-Za-z]:/.test(p) && !p.includes("\\") && !/[\0-\x1f]/.test(p)
    && p.split("/").every(x=>x!=="" && x!=="." && x!=="..");
}
export function verifyLocalReadback(root,relative,expectedRaw,expectedBlob) {
  const fail=(code)=>({status:"FAIL",code,scope:"LOCAL_ONLY"});
  if (!safeRel(relative)) return fail("PATH_UNSAFE");
  if (typeof expectedRaw!=="string" || !hex64.test(expectedRaw)
    || typeof expectedBlob!=="string" || !hex40.test(expectedBlob)) return fail("EXPECTED_DIGEST_INVALID");
  try {
    const rootReal=fs.realpathSync(root);
    const target=path.resolve(rootReal,...relative.split("/"));
    if (!target.startsWith(rootReal+path.sep)) return fail("ESCAPE_ROOT");
    const real=fs.realpathSync(target);
    if (!real.startsWith(rootReal+path.sep)) return fail("SYMLINK_ESCAPE");
    const stat=fs.statSync(real);
    if (!stat.isFile()) return fail("NOT_REGULAR_FILE");
    const bytes=fs.readFileSync(real);
    const raw=crypto.createHash("sha256").update(bytes).digest("hex");
    const prefix=Buffer.from("blob "+bytes.length+"\0","utf8");
    const gitBlob=crypto.createHash("sha1").update(prefix).update(bytes).digest("hex");
    if (raw!==expectedRaw) return fail("RAW_MISMATCH");
    if (gitBlob!==expectedBlob) return fail("GIT_BLOB_MISMATCH");
    return {status:"PASS",scope:"LOCAL_ONLY",bytes:bytes.length,raw_sha256:raw,git_blob_sha:gitBlob,
      note:"Local file identity matched; NOT remote GitHub readback, commit ancestry, or approval custody."};
  } catch(err) {
    return fail(err?.code==="ENOENT"?"MISSING_SOURCE":"READBACK_ERROR");
  }
}
if (process.argv[1] && import.meta.url===pathToFileURL(path.resolve(process.argv[1])).href) {
  if(process.argv.length!==6){console.error("Usage: node tools/boss105/readback.mjs ROOT RELATIVE_PATH RAW_SHA256 GIT_BLOB_SHA");process.exit(2);}
  const result=verifyLocalReadback(...process.argv.slice(2));console.log(JSON.stringify(result,null,2));
  process.exit(result.status==="PASS"?0:2);
}

