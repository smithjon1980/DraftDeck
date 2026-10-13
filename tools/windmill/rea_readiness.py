# Windmill Python script: BOSS Tool Readiness Gateway
# Deploy to Windmill as a Python script; call main(). All checks are non-destructive.
# No install and no tool execution unless explicitly enabled.
import datetime as dt
import hashlib
import json
import os
import pathlib
import shutil
import subprocess
import time
import uuid

def _run(argv, cwd, timeout=25):
    started=time.monotonic()
    try:
        p=subprocess.run(argv,cwd=cwd,timeout=timeout,capture_output=True,text=True,
                         check=False,stdin=subprocess.DEVNULL)
        return {"status":"OK" if p.returncode==0 else "COMMAND_FAILED",
                "exit_code":p.returncode,"stdout":p.stdout[-12000:],
                "stderr":p.stderr[-6000:],"duration_ms":round((time.monotonic()-started)*1000)}
    except FileNotFoundError as e:
        return {"status":"BINARY_MISSING","error":str(e)}
    except subprocess.TimeoutExpired:
        return {"status":"TIMEOUT","timeout_s":timeout}
    except Exception as e:
        return {"status":"ERROR","error":type(e).__name__+": "+str(e)}

def _sha(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for block in iter(lambda:f.read(1048576),b""): h.update(block)
    return h.hexdigest()

def main(repository_root: str = "/workspace/DraftDeck",
         execute_cli: bool = False,
         execute_mcp_probe: bool = False,
         expected_version: str = "6.3.0") -> dict:
    root=pathlib.Path(repository_root).resolve()
    experiment_id="BOSS-D0-REA-"+str(uuid.uuid4())
    result={"experiment_id":experiment_id,"timestamp_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
            "repository_root":str(root),"expected_rea_version":expected_version,
            "steps":{},"claim_boundary":"A repository config is not a verified execution."}
    result["steps"]["host"]={"platform":os.name,"python":os.sys.version.split()[0],
                              "cwd":os.getcwd(),"root_exists":root.is_dir(),
                              "executables":{k:shutil.which(k) for k in ["git","node","npm","npx"]}}
    if not root.is_dir():
        result["disposition"]="ENVIRONMENT_BLOCKED"
        result["next_action"]="Mount/clone the approved DraftDeck repository into the worker."
        return result
    src=root/"examples/interactive-checklist/index.html"
    pkg=root/"tools/rea/package.json"
    config=root/".mcp.json"
    result["steps"]["inputs"]={"sample_exists":src.is_file(),
        "sample_sha256":_sha(src) if src.is_file() else None,
        "package_exists":pkg.is_file(),"package_sha256":_sha(pkg) if pkg.is_file() else None,
        "mcp_config_exists":config.is_file()}
    result["steps"]["git_commit"]=_run(["git","rev-parse","HEAD"],str(root)) if shutil.which("git") else {"status":"NOT_EXECUTED"}
    for name in ("node","npm"):
        result["steps"][name]=_run([name,"--version"],str(root)) if shutil.which(name) else {"status":"BINARY_MISSING"}
    if not execute_cli:
        result["steps"]["cli"]={"status":"NOT_EXECUTED","reason":"execute_cli=false"}
    elif not src.is_file() or not shutil.which("npm"):
        result["steps"]["cli"]={"status":"ENVIRONMENT_BLOCKED","reason":"sample or npm missing"}
    elif not (root/"tools/rea/node_modules/.bin/rea").exists():
        result["steps"]["cli"]={"status":"DEPENDENCY_BLOCKED","reason":"Pin rea-agents in tools/rea; install using a reviewed worker provisioning step before running."}
    else:
        result["steps"]["cli_help"]=_run(["npm","run","rea:help"],str(root/"tools/rea"),30)
        result["steps"]["cli"]=_run(["npm","run","rea:static","--",str(src.parent),"--json"],str(root/"tools/rea"),90)
    # MCP discovery is deliberately not equated with a successful tool call.
    if execute_mcp_probe:
        result["steps"]["mcp"]={"status":"NOT_IMPLEMENTED","reason":"A real MCP JSON-RPC client handshake, tools/list, and approved tool invocation must be separately implemented and verified."}
    else:
        result["steps"]["mcp"]={"status":"NOT_EXECUTED","reason":"execute_mcp_probe=false"}
    st=result["steps"]["cli"]["status"]
    result["disposition"]="CLI_ONLY_VERIFIED" if st=="OK" else ("CONFIG_ONLY_VERIFIED" if config.is_file() else "ENVIRONMENT_BLOCKED")
    result["mcp_verified"]=False
    result["learner_audit_score"]=None
    result["human_review"]="PENDING"
    return result
