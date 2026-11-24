import type { InboundOrder, MasterData } from "./types.js";

/** Returns actionable errors. Empty array = valid. Never calls SAP. */
export function validate(order: InboundOrder, md: MasterData): string[] {
  const errors: string[] = [];
  if (!order.externalOrderId) errors.push("externalOrderId is required");
  if (!md.customersByPhone[order.customerPhone]) errors.push(`Unknown customer phone ${order.customerPhone}: create the Business Partner first`);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(order.dueDate)) errors.push(`dueDate must be YYYY-MM-DD, got "${order.dueDate}"`);
  if (!order.lines?.length) errors.push("Order has no lines");
  order.lines?.forEach((l, i) => {
    const n = i + 1;
    if (!md.items[l.sku]) errors.push(`Line ${n}: unknown SKU "${l.sku}"`);
    if (!Number.isFinite(l.quantity) || l.quantity <= 0) errors.push(`Line ${n}: quantity must be > 0`);
    if (!Number.isFinite(l.unitPrice) || l.unitPrice < 0) errors.push(`Line ${n}: unitPrice must be >= 0`);
    if (!md.warehouses.includes(l.warehouse)) errors.push(`Line ${n}: unknown warehouse "${l.warehouse}"`);
  });
  return errors;
}
