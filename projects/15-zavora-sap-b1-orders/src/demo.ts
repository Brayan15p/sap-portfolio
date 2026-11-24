import { readFileSync } from "node:fs";
import { startSimulator } from "./simulator.js";
import { Store } from "./store.js";
import { B1Client } from "./b1client.js";
import { Connector } from "./connector.js";

const md = JSON.parse(readFileSync("examples/master-data.json", "utf8"));
const order = JSON.parse(readFileSync("examples/order.json", "utf8"));
const sim = await startSimulator();
const c = new Connector(new Store(), new B1Client(sim.url, "", 500), md);

console.log("1) Valid order          ->", await c.process(order));
console.log("2) Same WhatsApp event  ->", await c.process(order));
sim.state.mode = "drop-after-create";
const o2 = { ...order, externalOrderId: "WA-2002" };
console.log("3) SAP creates, response lost ->", await c.process(o2));
sim.state.mode = "ok";
console.log("4) Redelivery reconciles      ->", await c.process(o2));
console.log(`SAP orders: ${sim.orders.length} (expected 2), POSTs received: ${sim.state.posts}`);
sim.close();
