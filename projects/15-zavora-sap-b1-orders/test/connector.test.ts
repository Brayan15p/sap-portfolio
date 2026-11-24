import { describe, it, expect, beforeEach, afterEach } from "vitest";
import { readFileSync, rmSync } from "node:fs";
import { startSimulator } from "../src/simulator.js";
import { Store } from "../src/store.js";
import { B1Client } from "../src/b1client.js";
import { Connector } from "../src/connector.js";
import { toB1Order } from "../src/mapper.js";

const md = JSON.parse(readFileSync("examples/master-data.json", "utf8"));
const base = JSON.parse(readFileSync("examples/order.json", "utf8"));
let sim: Awaited<ReturnType<typeof startSimulator>>;
let c: Connector;
beforeEach(async () => { sim = await startSimulator(); c = new Connector(new Store(), new B1Client(sim.url, "", 300), md); });
afterEach(() => sim.close());

describe("validation (no SAP call)", () => {
  it("unknown SKU -> actionable error, zero POSTs", async () => {
    const r = await c.process({ ...base, lines: [{ ...base.lines[0], sku: "NOPE" }] });
    expect(r.state).toBe("REJECTED");
    expect(r.errors?.[0]).toMatch(/Line 1: unknown SKU "NOPE"/);
    expect(sim.state.posts).toBe(0);
  });
  it("invalid quantity is rejected", async () => {
    const r = await c.process({ ...base, lines: [{ ...base.lines[0], quantity: 0 }] });
    expect(r.errors).toContain("Line 1: quantity must be > 0");
  });
});

describe("mapping to Service Layer Orders", () => {
  it("builds the expected body", () => {
    const b = toB1Order(base, md);
    expect(b).toMatchObject({ CardCode: "C0001", DocDueDate: "2026-12-01", NumAtCard: "ZAV-distribuidora-demo-WA-2001" });
    expect(b.DocumentLines).toEqual([
      { ItemCode: "A1001", Quantity: 10, UnitPrice: 98000, WarehouseCode: "BOG01" },
      { ItemCode: "A2002", Quantity: 24, UnitPrice: 31500, WarehouseCode: "BOG02" },
    ]);
  });
});

describe("idempotency", () => {
  it("valid order creates exactly one SAP order", async () => {
    const r = await c.process(base);
    expect(r).toMatchObject({ state: "CREATED", docEntry: 1001 });
  });
  it("same WhatsApp event twice -> one order", async () => {
    await c.process(base); const r2 = await c.process(base);
    expect(r2.postCalls).toBe(0); expect(sim.orders).toHaveLength(1);
  });
  it("two concurrent deliveries -> one POST", async () => {
    const [a, b] = await Promise.all([c.process(base), c.process(base)]);
    expect(sim.state.posts).toBe(1);
    expect([a.state, b.state].sort()).toEqual(["CREATED", "SENDING"]);
  });
  it("same external id in two companies -> two orders", async () => {
    await c.process(base); await c.process({ ...base, company: "otra-distribuidora" });
    expect(sim.orders).toHaveLength(2);
  });
});

describe("crashed worker", () => {
  it("a SENDING row older than the lease is reconciled, not left stuck", async () => {
    const store = new Store(); store.claim(base.company, base.externalOrderId);
    const r = await new Connector(store, new B1Client(sim.url, "", 300), md, -1).process(base);
    expect(r).toMatchObject({ state: "CREATED", postCalls: 1 });
  });
});

describe("lost response recovery", () => {
  it("SAP creates but response is lost -> UNCERTAIN, then reconciled without a second POST", async () => {
    sim.state.mode = "drop-after-create";
    expect((await c.process(base)).state).toBe("UNCERTAIN");
    sim.state.mode = "ok";
    const r = await c.process(base);
    expect(r).toMatchObject({ state: "CREATED", docEntry: 1001, postCalls: 0 });
    expect(sim.state.posts).toBe(1);
  });
  it("survives a process restart (persistent ledger)", async () => {
    const db = "/tmp/ledger-test.db"; rmSync(db, { force: true });
    sim.state.mode = "drop-after-create";
    await new Connector(new Store(db), new B1Client(sim.url, "", 300), md).process(base);
    sim.state.mode = "ok";
    const r = await new Connector(new Store(db), new B1Client(sim.url, "", 300), md).process(base);
    expect(r.state).toBe("CREATED"); expect(sim.orders).toHaveLength(1);
  });
  it("SAP down before send -> UNCERTAIN; lookup confirms absence; then creates once", async () => {
    sim.state.mode = "down";
    expect((await c.process(base)).state).toBe("UNCERTAIN");
    sim.state.mode = "ok";
    const r = await c.process(base);
    expect(r).toMatchObject({ state: "CREATED", postCalls: 1 });
    expect(sim.orders).toHaveLength(1);
  });
  it("while SAP is still unreachable, never re-POSTs blindly", async () => {
    sim.state.mode = "drop-after-create"; await c.process(base);
    sim.state.mode = "down"; const r = await c.process(base);
    expect(r.state).toBe("UNCERTAIN"); expect(sim.state.posts).toBe(1);
  });
});
