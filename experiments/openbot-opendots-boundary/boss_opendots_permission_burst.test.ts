/**
 * Supplemental adversarial cases run inside disposable pinned OpenDots checkout.
 * No real computer, browser, model, production account or HTTP call.
 */
import { expect, it } from "vitest";
import { DatabaseSync } from "node:sqlite";
import { mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
function readPersistedAudit(path:string, dotId:string) {
 const db=new DatabaseSync(path);
 try {const row=db.prepare("SELECT count(*) AS n FROM computer_audit WHERE dotId=?").get(dotId);return Number(row?.n ?? 0);} finally{db.close()}
}
import { WorkspaceStore } from "../src/server/workspace.js";
import { ComputerService } from "../src/server/computer-service.js";

it("BOSS: 75 concurrent disabled-shell requests never forward and are recorded as failures", async () => {
  const temp=mkdtempSync(join(tmpdir(),"boss-dots-audit-"));
  const path=join(temp,"workspace.sqlite");
  const w = new WorkspaceStore(path, "owner");
  let dotId="";
  try {
    const id = w.dots()[0].id;
    dotId=id;
    let forwarded = 0;
    const transport: typeof fetch = async () => {
      forwarded++;
      return Response.json({ text:"unexpected dispatch" });
    };
    const service = new ComputerService(w,{
      baseUrl:"http://127.0.0.1",
      voiceName:"voice",
      slackUsers:[],
      runtimeUrl:"http://127.0.0.1",
      computerSupervisorUrl:"http://127.0.0.1:4312",
      computerSupervisorToken:"TEST-ONLY-NOT-A-SECRET",
      computerToken:"TEST-ONLY-NOT-A-SECRET"
    },()=>false,transport);
    const results = await Promise.allSettled(
      Array.from({length:75},() => service.action(id,"exec",{command:"echo synthetic"},"agent"))
    );
    expect(results).toHaveLength(75);
    expect(results.every(r=>r.status==="rejected")).toBe(true);
    expect(forwarded).toBe(0);
    expect(w.computers.audit(id)).toHaveLength(50);
    expect(w.computers.audit(id).every(row=>row.outcome==="failed")).toBe(true);
  } finally {
    w.close();
    try {expect(readPersistedAudit(path,dotId)).toBe(75);} finally {rmSync(temp,{recursive:true,force:true});}
  }
});

it("BOSS: 75 concurrent globally paused shell requests never forward and remain auditable", async () => {
  const temp=mkdtempSync(join(tmpdir(),"boss-dots-audit-"));
  const path=join(temp,"workspace.sqlite");
  const w = new WorkspaceStore(path,"owner");
  let dotId="";
  try {
    const id=w.dots()[0].id;
    dotId=id;
    w.computers.patch(id,{enabled:true,shell:true});
    let forwarded=0;
    const service=new ComputerService(w,{
      baseUrl:"http://127.0.0.1",
      voiceName:"voice",slackUsers:[],
      runtimeUrl:"http://127.0.0.1",
      computerSupervisorUrl:"http://127.0.0.1:4312",
      computerSupervisorToken:"TEST-ONLY-NOT-A-SECRET",
      computerToken:"TEST-ONLY-NOT-A-SECRET"
    },()=>true,async()=>{forwarded++;return Response.json({text:"unexpected dispatch"})});
    const outcomes=await Promise.allSettled(
      Array.from({length:75},()=>service.action(id,"exec",{command:"echo synthetic"},"agent"))
    );
    expect(outcomes.every(r=>r.status==="rejected")).toBe(true);
    expect(forwarded).toBe(0);
    expect(w.computers.audit(id)).toHaveLength(50);
  } finally {
    w.close();
    try {expect(readPersistedAudit(path,dotId)).toBe(75);} finally {rmSync(temp,{recursive:true,force:true});}
  }
});
