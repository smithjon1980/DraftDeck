"""One-shot Railway evaluation. Full synthetic report emitted to runtime logs."""
import hashlib,json,os,pathlib,subprocess,time,urllib.request
import evaluate
REV="1336c0b5d74dfe6ad7f793577092f5effd9f97c6"
FILE="Underdog-Saluki-27B-1.0-IQ2-mix.gguf"
def emit(event,**data):
    print(json.dumps(dict(event=event,**data)),flush=True)
def main():
    model=pathlib.Path("/tmp/"+FILE)
    url="https://huggingface.co/ConwayResearch/Underdog-Saluki-27B-1.0/resolve/"+REV+"/"+FILE
    emit("DOWNLOAD_START",revision=REV)
    urllib.request.urlretrieve(url,model)
    h=hashlib.sha256()
    with model.open("rb") as f:
        for block in iter(lambda:f.read(8*1024*1024),b""): h.update(block)
    sha=h.hexdigest()
    emit("MODEL_READY",bytes=model.stat().st_size,sha256=sha,revision=REV)
    server=subprocess.Popen(["/opt/llama/llama-server","-m",str(model),"--host","127.0.0.1",
        "--port","8080","-c","4096","-t","4","-ngl","0","--jinja","--alias","saluki"])
    try:
        ready=False
        for _ in range(180):
            if server.poll() is not None: raise RuntimeError("Model server exited")
            try:
                with urllib.request.urlopen("http://127.0.0.1:8080/health",timeout=2) as r:
                    if r.status==200: ready=True; break
            except Exception: pass
            time.sleep(2)
        if not ready: raise TimeoutError("Model readiness timeout")
        warm={"model":"saluki","messages":[{"role":"user","content":"Reply OK."}],
              "temperature":0,"max_tokens":16,"chat_template_kwargs":{"enable_thinking":False}}
        start=time.perf_counter()
        req=urllib.request.Request("http://127.0.0.1:8080/v1/chat/completions",
            data=json.dumps(warm).encode(),headers={"Content-Type":"application/json"})
        with urllib.request.urlopen(req,timeout=180) as r: warm_result=json.load(r)
        emit("WARMUP",elapsed_seconds=time.perf_counter()-start,response=warm_result)
        cmd=["python","evaluate.py","--model","saluki","--model-revision",REV+":"+sha,
             "--runtime-version","llama.cpp ead9f3205848f81ca079b4e760b76a01a6359f4b",
             "--source-revision",os.environ.get("RAILWAY_GIT_COMMIT_SHA","UNKNOWN"),
             "--device","Railway CPU container; configured 16GB RAM/4vCPU; context4096; GPU0",
             "--output","/tmp/saluki-results.json"]
        result=subprocess.run(cmd,timeout=3000)
        report=pathlib.Path("/tmp/saluki-results.json")
        if report.exists():
            data=json.loads(report.read_text())
            for record in data.pop("results"): emit("CASE_RESULT",record=record)
            emit("RUN_REPORT",report=data)
        if result.returncode: raise RuntimeError("Evaluator returned "+str(result.returncode))
        # Linux process evidence: VmHWM is server RSS high-water, not total container memory.
        try:
            status=pathlib.Path(f"/proc/{server.pid}/status").read_text()
            emit("SERVER_MEMORY",fields=[line for line in status.splitlines() if line.startswith(("VmHWM:","VmRSS:"))])
        except OSError: emit("SERVER_MEMORY",status="UNAVAILABLE")
        try:
            emit("CGROUP_MEMORY",peak_bytes=pathlib.Path("/sys/fs/cgroup/memory.peak").read_text().strip())
        except OSError: pass
        emit("EVALUATION_COMPLETED",human_review="PENDING",repetitions=1)
    finally:
        server.terminate()
        try: server.wait(timeout=15)
        except subprocess.TimeoutExpired: server.kill(); server.wait()
if __name__=="__main__":
    main()
