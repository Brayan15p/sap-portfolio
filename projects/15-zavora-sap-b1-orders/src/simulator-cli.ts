import { startSimulator } from "./simulator.js";
const s = await startSimulator(Number(process.env.PORT ?? 50000));
console.log(`Service Layer simulator on ${s.url}/b1s/v2`);
