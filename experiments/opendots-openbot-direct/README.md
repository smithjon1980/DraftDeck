# OpenDots → OpenBot BOSS synthetic boundary trial

This is deliberately a **synthetic client simulation**, not a real deployment or integration of the OpenDots application and OpenBot gateway server.

The harness imports the **original pinned OpenBot CEL evaluator** and passes fake OpenDots-like requests to a small in-memory BOSS gateway. Its human-approval record is also a local *simulator*, **not** the production OpenBot approval service. No actual OpenDots code is imported.

Scope: allow/deny, protected manuscript, MCP write denial, unattended write denial, decision visibility, exact payload digest, human-only approval and duplicate replay rejection. Uses only fake strings, fake computer and no external accounts.

Original source: CopilotKit/OpenBot@bd4dc94943a9d62aefd05e5e99073ba58919c9c6, verified blob SHA 94bc46ad3a74bdb56ad84f86527057ecba6c735e.

Known **HOLD**: OpenDots authentic ComputerService, OpenBot real gateway, API authentication and network bypass tests, durable approval/restart, live tool side effects and credential egress. Success here proves only that a *proposed adapter design* can enforce these conditions with OpenBot's policy module. This does not close the source-level finding that OpenDots normally calls its own ComputerService outside OpenBot's policy gateway.
