---
title: RNDC integration for cargo companies
client: Grupo Nutresa, Rápido Ochoa and other carriers (independent)
period: 2020 – present
domain: Logistics / Government APIs
role: Architect and developer
summary: Consignments, electronic cargo manifests and completion reports filed with the Ministry of Transport's RNDC, with upfront validation and traceability of every report.
stack: [Java, Kafka, Debezium, Confluent, Oracle, Keycloak, OpenTelemetry, Grafana]
metric: { value: "Every report", label: "validated before filing and traceable end to end" }
featured: true
order: 2
---

The RNDC (Registro Nacional de Despachos de Carga) is where every land freight dispatch in Colombia must be reported. For cargo companies I designed an event-driven lifecycle (order, remesa, manifest, cumplido) with freight reconciliation on top, and modernized the surrounding Oracle/Java legacy with Strangler Fig and change data capture instead of a big-bang rewrite.
