---
title: "Integration bus migration off IBM App Connect"
client: "Celsia"
period: "2025 – 2026"
domain: "Enterprise integration"
role: "Senior integration developer"
summary: "Led the move of the integration bus from IBM App Connect to on-premise Kubernetes using Quarkus, Apache Camel and Kafka, including the migration strategy for mission-critical metering systems."
stack: [Quarkus, Apache Camel, Kafka, Kubernetes, Grafana, Loki, Tempo]
featured: false
order: 14
schematic:
  columns:
    -
      - { id: ibm, label: "IBM App Connect", sub: "legacy", kind: cloud }
    -
      - { id: bus, label: "Quarkus + Camel", sub: "on-prem Kubernetes" }
      - { id: kafka, label: "Kafka", sub: "events", kind: bus }
    -
      - { id: meter, label: "Metering", sub: "critical systems" }
      - { id: obs, label: "Grafana · Loki · Tempo", sub: "observability", kind: bus }
  edges:
    - { from: ibm, to: bus, dashed: true, label: "migration" }
    - { from: bus, to: meter }
    - { from: bus, to: kafka }
    - { from: bus, to: obs, dashed: true }
---

The mission-critical power distribution metering systems could not stop while the bus moved. I designed and documented the migration strategy, led the implementation and wired end-to-end observability with Grafana, Loki and Tempo so every route could be watched during the cut-over.
