export interface OrderLine { sku: string; quantity: number; unitPrice: number; warehouse: string; }
export interface InboundOrder {
  company: string;            // tenant (distributor) id
  externalOrderId: string;    // id from the WhatsApp / Zavora flow
  customerPhone: string;
  currency: string;
  dueDate: string;            // YYYY-MM-DD
  lines: OrderLine[];
}
export interface MasterData {
  customersByPhone: Record<string, string>;            // phone -> B1 CardCode
  items: Record<string, { itemCode: string; uom: string }>; // sku -> B1 ItemCode
  warehouses: string[];
}
export type OrderState = "SENDING" | "CREATED" | "UNCERTAIN" | "REVIEW" | "REJECTED";
export interface ProcessResult { state: OrderState; docEntry?: number; errors?: string[]; postCalls: number; }
