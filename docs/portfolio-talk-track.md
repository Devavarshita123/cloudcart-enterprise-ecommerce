# Portfolio Walkthrough

## 60-second summary
“CloudCart is a local-first architecture portfolio project organized around the five AWS Well-Architected pillars. I built reusable Python modules and tests to demonstrate configuration validation, health aggregation, bounded retries, structured diagnostic events, caching, and transparent cost estimates. I kept the initial build local to avoid unplanned cloud charges and documented which parts are simulations versus future AWS implementation work.”

## Pillar-by-pillar
- **Security:** validate input at boundaries, reject control characters, and mask example PII in logs. A real deployment would still need IAM, encryption, network controls, and security testing.
- **Reliability:** aggregate dependency health and use bounded retries. A real deployment would need fault isolation, backups, recovery objectives, and failover validation.
- **Operational Excellence:** emit structured events and correlation IDs. A real deployment would need dashboards, alerts, runbooks, and incident exercises.
- **Performance Efficiency:** use a small local cache benchmark to illustrate measurement. Real decisions require representative load tests and workload-specific metrics.
- **Cost Optimization:** make assumptions visible and compare estimates to a budget threshold. Real costs require current regional pricing and actual billing data.

