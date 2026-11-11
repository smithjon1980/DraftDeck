# Render Private SVG Worker Qualification — CANDIDATE

## Render networking constraint
Render private services lack a public endpoint but are normally reachable over the private network by other same-workspace, same-region services. A same-environment unauthorized service therefore MAY directly reach the worker's HTTP port even without using the intended OpenBot gateway. Render Pro+ environment isolation can restrict cross-environment private traffic, but not necessarily individual services within one environment.

Consequently public internet inaccessibility and denial of unauthorized internal SVG operations are **separate acceptance tests**. A mere private-service deployment cannot prove a non-bypassable OpenBot route.

## Components
* worker_server.py / Dockerfile: paid private service, runs REAL native Inkscape on a fixed synthetic six-frame SVG. No approved content, file paths, user payloads, original SVG import, SVG write, shell, or external URLs. Requires test-only HMAC key length >=32; short time validity; no replay inside one process. Ephemeral nonce tracking is NOT durable approval custody.
* canary_server.py / Dockerfile.canary: separate FREE web service in same workspace and region with NO gateway secret. The /probe endpoint attempts GET /healthz and then a well-formed unsigned POST to the worker. Expected network_reachable=true and protected_operation_refused=true with 403 MISSING_GATEWAY_PROOF.
* GitHub Actions: runs upstream Inkscape locally and Docker simulated shared network with both peers; verifies authorized fixed sample render and denial of unsigned traffic. This is NOT a Render network test.

## Manual Render admission (paid private service requires explicit action)
1. Preserve running public boss-openbot-gateway-test health probe and the main production stack, Auto-Deploy Off.
2. Create a NEW Render Private Service in same workspace and region; GitHub repo smithjon1980/DraftDeck; branch feature/render-private-svg-worker-qualification-20261025; Docker; root directory empty; build context .; Dockerfile path experiments/render-private-worker/Dockerfile; name boss-private-svg-qual-worker; Auto-Deploy Off.
3. Select paid compute knowingly; Render does not support Free private-service instances. Set BOSS_SYNTHETIC_GATEWAY_KEY to a unique random secret at least 32 characters DIRECTLY in Render. Do not share it in chat, GitHub or any other service.
4. Verify service has **no external/public domain**. Obtain its private hostname and port from Connect > Internal and construct an http:// internal address.
5. Create a separate Free Web Service for unauthorized canary on same branch and region, with Dockerfile experiments/render-private-worker/Dockerfile.canary and BOSS_PRIVATE_WORKER_URL set to the internal address. Do NOT assign the secret to canary. Auto-Deploy Off.
6. Visit canary public URL ending /probe. Expect HTTP 200 JSON containing network_reachable=true, protected_operation_refused=true, unsigned_svg_operation_http_status=403, denial_reason=MISSING_GATEWAY_PROOF.
7. Record a separate external public-Internet probe: no public domain is assigned to worker, and its internal hostname must not be publicly routeable.
8. Save redacted endpoint result, service types and region, deployed source SHA, health and error logs. No secrets; no user-approved source files.

## Promotion HOLD
The synthetic key proves only limited request authentication, not an authenticated OpenBot actor/dot/tenant, human approval, durable evidence before effect, tenant isolation, or non-bypassable route. A compromised peer that steals the test key can invoke the inert render; same-region peers can establish network connectivity. For production, require original OpenBot enforce mode, independently protected exact-digest human approval, pre-effect durable custody and recovery, server-to-server authorization, egress/firewall tests and explicit human release. Never point real BOSS production assets at this worker.

Render documentation: https://render.com/docs/private-network ; https://render.com/docs/private-services ; https://render.com/docs/free ; https://render.com/docs/projects
