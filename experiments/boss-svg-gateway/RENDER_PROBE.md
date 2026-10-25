# Render configuration — test-only health probe

**This is NOT the OpenBot policy gateway.** The public web service supports /healthz solely to validate Docker startup, GitHub to Render build and network connectivity. It has NO approval service, custody service, decision engine, SVG worker, credentials, or operator access. All protected requests return 503 / DENIED.

Use the selected experimental branch `feature/boss-svg-openbot-gateway-contract-v1`. Root directory blank, Dockerfile path `./Dockerfile`, build context `.`, language Docker, Docker command empty. Select the smallest free option for health-only testing if supported. Region is not a security boundary. Auto-deploy MUST be Off. Set Render Health Check Path to `/healthz` (only confirms that the probe is running, NOT gateway readiness). /readyz intentionally returns HTTP 503. No approval or custody credentials should be set on this probe.

A live gateway must be a separate future deployment behind enforcement controls and restricted network paths. Never point an agent or OpenDots at this public test endpoint as a production gateway.

Acceptance requirements before real integration: actual independently authenticated principal/dot identity, real OpenBot enforce-mode CEL policy, separate human approval authority, durable pre-effect evidence custody, single-use binding, actual worker isolation, denied direct transport/network bypass, crash/restart and tenant isolation, hostile-input and egress testing. Preserve production HOLD and human release authority.
