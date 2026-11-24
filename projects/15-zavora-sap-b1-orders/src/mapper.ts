import type { InboundOrder, MasterData } from "./types.js";

/**
 * Maps to the Service Layer `Orders` entity (Documents).
 * Fields used: CardCode, DocDueDate, DocCurrency, NumAtCard, DocumentLines[ItemCode, Quantity, UnitPrice, WarehouseCode].
 * NumAtCard carries a deterministic external reference so we can look the order up after a lost response.
 * Verify field names against $metadata of your B1 installation (requirement, not assumption).
 */
export function externalRef(order: InboundOrder): string {
  return `ZAV-${order.company}-${order.externalOrderId}`.slice(0, 100);
}

export function toB1Order(order: InboundOrder, md: MasterData) {
  return {
    CardCode: md.customersByPhone[order.customerPhone],
    DocDueDate: order.dueDate,
    DocCurrency: order.currency,
    NumAtCard: externalRef(order),
    DocumentLines: order.lines.map((l) => ({
      ItemCode: md.items[l.sku].itemCode,
      Quantity: l.quantity,
      UnitPrice: l.unitPrice,
      WarehouseCode: l.warehouse,
    })),
  };
}
