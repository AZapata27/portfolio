---
title: "Migración del bus de integración fuera de IBM App Connect"
client: "Celsia"
period: "2025 – 2026"
domain: "Integración empresarial"
role: "Senior integration developer"
summary: "Lideré el paso del bus de integración de IBM App Connect a Kubernetes on-premise con Quarkus, Apache Camel y Kafka, incluida la estrategia de migración de los sistemas críticos de medición."
stack: [Quarkus, Apache Camel, Kafka, Kubernetes, Grafana, Loki, Tempo]
featured: false
order: 14
schematic:
  columns:
    -
      - { id: ibm, label: "IBM App Connect", sub: "legado", kind: cloud }
    -
      - { id: bus, label: "Quarkus + Camel", sub: "Kubernetes on-prem" }
      - { id: kafka, label: "Kafka", sub: "eventos", kind: bus }
    -
      - { id: meter, label: "Medición", sub: "sistemas críticos" }
      - { id: obs, label: "Grafana · Loki · Tempo", sub: "observabilidad", kind: bus }
  edges:
    - { from: ibm, to: bus, dashed: true, label: "migración" }
    - { from: bus, to: meter }
    - { from: bus, to: kafka }
    - { from: bus, to: obs, dashed: true }
---

Los sistemas críticos de medición de distribución eléctrica no podían detenerse mientras el bus se movía. Diseñé y documenté la estrategia de migración, lideré la implementación y conecté observabilidad end-to-end con Grafana, Loki y Tempo para vigilar cada ruta durante el cambio.
