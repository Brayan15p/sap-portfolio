# Int Outbox Event Hub

**Area:** Integration infrastructure · Transactional outbox (Docker)

## Real-life case

Real case: when SAP posts a delivery, the carrier, the e-commerce and the BI system must all be notified exactly once even if one of them is down. The hub writes the business change and the event in the same SQLite transaction (outbox), a relay delivers to each subscriber with retries and exponential backoff, keeps per-subscriber delivery state and moves poison messages to a dead-letter table. Ships with a stdlib HTTP API, Dockerfile and docker-compose.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates and thresholds are illustrative and must come from maintained tax configuration.

## Run the stack (Docker)

```bash
docker compose up --build
curl -X POST localhost:8080/deliveries -d '{"doc":"DN-1001","qty":5}'
curl localhost:8080/status        # {"DONE": 2}
docker compose logs carrier shop  # each received DN-1001 once
docker compose stop shop          # then post again: shop retries with backoff until it is back
```
