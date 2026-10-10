---
title: RNDC integration for shippers and carriers
client: Grupo Nutresa, Rápido Ochoa and other carriers (independent)
period: 2020 – present
domain: Logistics / Government APIs
role: Software architect and developer
summary: Consignment notes, electronic cargo manifests and proof-of-delivery records filed with the Ministry of Transport's RNDC, with upfront data validation and full traceability of every submission.
stack: [Java, Kafka, Debezium, Confluent, Oracle, Keycloak, OpenTelemetry, Grafana]
metric: { value: "Every submission", label: "validated before filing and traceable end to end" }
featured: true
order: 2
---

The RNDC (National Cargo Dispatch Registry) is where every land freight dispatch in Colombia must be reported. For shippers and carriers I designed an event-driven lifecycle (order, consignment note, manifest, proof of delivery) with freight payment reconciliation on top, and modernized the surrounding Oracle/Java legacy with the Strangler Fig pattern and change data capture instead of a big-bang rewrite.
