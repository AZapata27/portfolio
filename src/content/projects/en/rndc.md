---
title: "RNDC integration for shippers and carriers"
client: "Grupo Nutresa, Rápido Ochoa and other carriers"
period: "2020 – present"
domain: "Transport and mobility"
role: "Software architect and developer · Independent contractor"
summary: "Consignment notes, electronic cargo manifests and proof-of-delivery records filed with the Ministry of Transport's RNDC, with upfront data validation and full traceability of every submission."
stack: [Java, Kafka, Debezium, Confluent, Oracle, Keycloak, OpenTelemetry, Grafana]
metric: { value: "Every submission", label: "validated before filing and traceable end to end" }
featured: true
order: 3
schematic:
  columns:
    -
      - { id: tms, label: "Carrier's system", sub: "order · consignment · manifest" }
    -
      - { id: events, label: "Event-driven cycle", sub: "Kafka · Debezium" }
      - { id: legacy, label: "Oracle/Java legacy", sub: "Strangler Fig", kind: store }
    -
      - { id: val, label: "Upfront validation", sub: "traceability" }
    -
      - { id: rndc, label: "RNDC", sub: "Ministry of Transport", kind: cloud }
  edges:
    - { from: tms, to: events }
    - { from: legacy, to: events, dashed: true, label: "CDC" }
    - { from: events, to: val }
    - { from: val, to: rndc }
---

The RNDC (National Cargo Dispatch Registry) is where every land freight dispatch in Colombia must be reported. For shippers and carriers I designed an event-driven lifecycle (order, consignment note, manifest, proof of delivery) with freight payment reconciliation on top, and modernized the surrounding Oracle/Java legacy with the Strangler Fig pattern and change data capture instead of a big-bang rewrite.
