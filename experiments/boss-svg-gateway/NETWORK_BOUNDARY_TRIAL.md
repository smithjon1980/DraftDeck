# BOSS disposable network-boundary trial

Status: test-only network experiment; production and Render probe remain unchanged.

This workflow runs unmodified Docker Engine containers on GitHub Actions. A synthetic worker HTTP server has NO application authorization, deliberately making any network bypass observable. The simulated gateway container belongs to both ingress and private networks; the attacker belongs only to ingress.

Expected:
- Gateway-simulation container can contact private worker.
- Untrusted ingress cannot resolve worker or access its private IP.
- No worker port is published.
- NEGATIVE CONTROL: attacker granted membership of worker's private Docker network reaches worker directly without a policy check.
- Removing the attacker from the network reestablishes inaccessibility.

**Important**: Passing this trial proves Docker bridge topology on an ephemeral GitHub runner, NOT Render network isolation, NOT OpenBot gateway enforcement and NOT real workload identity. The negative control demonstrates that **network membership is a protected authorization surface**. Render Free web service is public and does not validate private-worker enforcement.

Never reuse this synthetic unprotected worker in production. Must still demonstrate actual authenticated identity, production-grade independent approval, durable pre-effect custody, real OpenBot CEL policy enforced at the dispatch point, worker rejection of all direct requests, managed tenancy separation and malicious browser/egress controls.
