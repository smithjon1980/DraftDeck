
/**
 * BOSS injected fault tests. The OpenBot production source stays pinned and unchanged.
 * These tests run inside a throwaway clone and use a fake computer only.
 */
test("BOSS fault: a failed audit insertion must stop an otherwise allowed click", async () => {
  const { provider, fetchImpl, calls } = fakeComputer();
  const gateway = createComputerGateway({
    provider,
    fetchImpl,
    policy: () => PERMISSIVE,
    auditStore: { insert: async () => {
      throw new Error("SYNTHETIC_AUDIT_DB_UNAVAILABLE");
    } },
  });
  await gateway.snapshot("bot-1");
  await expect(
    gateway.click("bot-1", ACTOR, { ref: "e9", snapshotId: 7 })
  ).rejects.toThrow("SYNTHETIC_AUDIT_DB_UNAVAILABLE");
  expect(calls).toEqual([]);
});

test("BOSS burst: 75 denied attempts make zero computer calls and 75 refusal records", async () => {
  const { gateway, calls, rows } = await gatewayWith({
    mode:"enforce",
    deny:['contains(element.name, "submit")'],
    allow:["true"],
  });
  const attempts = await Promise.allSettled(
    Array.from({length:75}, () =>
      gateway.click("bot-1", ACTOR, { ref:"e9", snapshotId:7 })
    )
  );
  expect(attempts).toHaveLength(75);
  expect(attempts.every(a => a.status === "rejected")).toBe(true);
  expect(calls).toHaveLength(0);
  expect(rows.filter(r=>r.eventType==="computer.action_refused")).toHaveLength(75);
});

test("BOSS burst: 75 permitted mock actions each produce a decision record", async () => {
  const { gateway, calls, rows } = await gatewayWith(PERMISSIVE);
  const attempts = await Promise.allSettled(
    Array.from({length:75}, () =>
      gateway.click("bot-1", ACTOR, {ref:"e9",snapshotId:7})
    )
  );
  expect(attempts.every(a=>a.status==="fulfilled")).toBe(true);
  expect(calls).toHaveLength(75);
  expect(rows.filter(r=>r.eventType==="computer.action_allowed")).toHaveLength(75);
});
