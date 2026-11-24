import type { InboundOrder, MasterData, ProcessResult } from "./types.js";
import { validate } from "./validate.js";
import { toB1Order, externalRef } from "./mapper.js";
import { Store } from "./store.js";
import { B1Client, B1HttpError } from "./b1client.js";

/**
 * Exactly-once intent over an at-least-once channel:
 * 1. validate (no SAP call on bad data)  2. atomic claim in ledger
 * 3. POST Orders  4. on timeout/network loss -> UNCERTAIN, never blind re-POST
 * 5. reconcile UNCERTAIN by looking up NumAtCard before any retry.
 */
export class Connector {
  /** A SENDING row younger than this belongs to a live worker; older means it crashed mid-send. */
  constructor(private store: Store, private b1: B1Client, private md: MasterData, private leaseMs = 60_000) {}

  async process(order: InboundOrder): Promise<ProcessResult> {
    const errors = validate(order, this.md);
    if (errors.length) return { state: "REJECTED", errors, postCalls: 0 };

    if (!this.store.claim(order.company, order.externalOrderId)) {
      const row = this.store.get(order.company, order.externalOrderId)!;
      if (row.state === "SENDING" && this.store.ageMs(row) < this.leaseMs)
        return { state: "SENDING", postCalls: 0 }; // another worker is posting right now: do nothing
      if (row.state === "UNCERTAIN" || row.state === "SENDING") return this.reconcile(order);
      return { state: row.state, docEntry: row.doc_entry ?? undefined, postCalls: 0 };
    }
    return this.send(order);
  }

  private async send(order: InboundOrder): Promise<ProcessResult> {
    const { company, externalOrderId: id } = order;
    try {
      const { DocEntry } = await this.b1.createOrder(toB1Order(order, this.md));
      this.store.set(company, id, "CREATED", DocEntry);
      return { state: "CREATED", docEntry: DocEntry, postCalls: 1 };
    } catch (e) {
      if (e instanceof B1HttpError && e.status >= 400 && e.status < 500) {
        this.store.set(company, id, "REVIEW", null, e.message);   // business error: human fixes data
        return { state: "REVIEW", errors: [e.message], postCalls: 1 };
      }
      this.store.set(company, id, "UNCERTAIN", null, String(e)); // may or may not exist in SAP
      return { state: "UNCERTAIN", postCalls: 1 };
    }
  }

  /** Called on redelivery or by a recovery job after restart. */
  async reconcile(order: InboundOrder): Promise<ProcessResult> {
    const { company, externalOrderId: id } = order;
    let found: number | null;
    try { found = await this.b1.findByRef(externalRef(order)); }
    catch (e) { return { state: "UNCERTAIN", errors: [String(e)], postCalls: 0 }; } // still unknown: do NOT post
    if (found !== null) {
      this.store.set(company, id, "CREATED", found);
      return { state: "CREATED", docEntry: found, postCalls: 0 };
    }
    return this.send(order); // confirmed absent in SAP -> safe to create
  }
}
