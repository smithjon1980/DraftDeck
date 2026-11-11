/**
 * BOSS synthetic governance evaluation against CopilotKit/OpenBot's actual policy.ts.
 *
 * This file is copied INTO a pinned clean checkout of upstream OpenBot server/tests
 * before bun test; it imports the ORIGINAL OpenBot module. No policy engine is mocked.
 * Synthetic names only: no private manuscript, BOSS credentials, or write tooling.
 *
 * A successful policy decision is NOT an end-to-end gateway/audit proof:
 * existing upstream computer-gateway.test.ts verifies forwarding and audit.
 */
import {describe, expect, test} from "bun:test";
import {
  type ActionPolicy,
  type PolicyContext,
  evaluateActionPolicy,
} from "../src/computer/policy";

const POLICY: ActionPolicy = {
  mode: "enforce",
  // These "hard denies" override any generic allow below.
  deny: [
    'intent == "run_command"',
    'mcp.effect == "write"',
    'intent == "write_file" && (contains(file.path, "approved/") || contains(file.path, "release/"))',
    'initiator.kind == "routine" && intent != "read" && intent != "read_file"',
  ],
  allow: [
    'intent == "read_file" && contains(file.path, "source/")',
    'intent == "write_file" && contains(file.path, "candidates/")',
    'intent == "read"',
  ],
};

function context(partial: Partial<PolicyContext>):PolicyContext {
  return {
    tool: {name: "computer_read_file"},
    bot: {id: "boss-art-producer"},
    actor: {id: "synthetic-human"},
    page: {url: "",host: ""},
    element: {ref:"",role:"",name:""},
    file: {path:"",name:"",extension:""},
    mcp: {server:"",tool:"",effect:""},
    command:"",
    key:"",
    intent:"read_file",
    initiator:{kind:"person",id:""},
    ...partial,
  };
}

function decision(c:PolicyContext, p=POLICY){return evaluateActionPolicy(p,c);}

describe("BOSS isolated OpenBot policy contract",()=>{
  test("reads approved source location only, without exposing its contents",()=>{
    const d=decision(context({intent:"read_file",file:{path:"source/synthetic-case.txt",name:"synthetic-case.txt",extension:"txt"}}));
    expect(d.forward).toBe(true);
    expect(d.source).toBe("allow");
  });
  test("permits proposed candidate slide output",()=>{
    const d=decision(context({intent:"write_file",tool:{name:"computer_write_file"},file:{path:"candidates/slide-02.html",name:"slide-02.html",extension:"html"}}));
    expect(d.forward).toBe(true);
    expect(d.allowed).toBe(true);
  });
  test("refuses modification of an approved manuscript path",()=>{
    const d=decision(context({intent:"write_file",tool:{name:"computer_write_file"},file:{path:"approved/ep01.txt",name:"ep01.txt",extension:"txt"}}));
    expect(d.forward).toBe(false);
    expect(d.source).toBe("deny");
  });
  test("refuses write to release folder under otherwise permissive policy",()=>{
    const d=decision(context({intent:"write_file",tool:{name:"computer_write_file"},file:{path:"release/episode01.html",name:"episode01.html",extension:"html"}}));
    expect(d.forward).toBe(false);
  });
  test("unrecognized storage path refuses by default",()=>{
    const d=decision(context({intent:"write_file",file:{path:"misc/unknown.txt",name:"unknown.txt",extension:"txt"}}));
    expect(d.allowed).toBe(false);
    expect(d.source).toBe("default");
  });
  test("no shell execution even with human initiator",()=>{
    const d=decision(context({intent:"run_command",tool:{name:"computer_exec"},command:"echo synthetic"}));
    expect(d.forward).toBe(false);
    expect(d.source).toBe("deny");
  });
  test("refuses external write-capable MCP tool",()=>{
    const d=decision(context({intent:"write_tool",tool:{name:"mcp__github__merge_pull_request"},mcp:{server:"github",tool:"merge_pull_request",effect:"write"}}));
    expect(d.forward).toBe(false);
  });
  test("scheduled routine cannot produce candidate write without person",()=>{
    const d=decision(context({
      intent:"write_file",
      tool:{name:"computer_write_file"},
      file:{path:"candidates/slide02.html",name:"slide02.html",extension:"html"},
      initiator:{kind:"routine",id:"synthetic-nightly"},
    }));
    expect(d.forward).toBe(false);
  });
  test("missing policy refuses by default",()=>{
    const d=evaluateActionPolicy(null,context({intent:"read"}));
    expect(d.allowed).toBe(false);
    expect(d.forward).toBe(false);
  });
  test("malformed deny condition still blocks even with allow-all",()=>{
    const d=decision(context({intent:"read"}),{mode:"enforce",deny:["bad ( CEL"],allow:["true"]});
    expect(d.forward).toBe(false);
    expect(d.source).toBe("deny");
  });
  test("deny overrides broad permission",()=>{
    const d=decision(context({intent:"run_command",command:"echo private"}),{mode:"enforce",deny:['intent == "run_command"'],allow:["true"]});
    expect(d.forward).toBe(false);
    expect(d.source).toBe("deny");
  });
  test("dry-run is NOT enforce: a denied action is still forwarded",()=>{
    const d=decision(context({intent:"run_command",command:"echo synthetic"}),{mode:"dry-run",deny:['intent == "run_command"'],allow:["true"]});
    expect(d.allowed).toBe(false);
    expect(d.forward).toBe(true); // an explicit trap to prevent BOSS from deploying dry-run as an access boundary
  });
  test("synthetic action cannot self-assert permission by changing actor",()=>{
    const d=decision(context({intent:"write_file",file:{path:"approved/ep01.txt",name:"ep01.txt",extension:"txt"},actor:{id:"synthetic-admin"}}));
    expect(d.forward).toBe(false);
  });
});
