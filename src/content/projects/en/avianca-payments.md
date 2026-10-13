---
title: "Payments core integration for an airline"
client: "Avianca (contractor)"
period: "2026 – present"
domain: "Enterprise integration"
role: "Senior Red Hat integration engineer"
summary: "Connecting the airline's payments core with Latin American payment gateways and methods such as DEUNA and Wompi, with Enterprise Integration Patterns on Quarkus and Apache Camel."
stack: [Quarkus, Apache Camel, Red Hat, Kafka]
featured: false
order: 13
schematic:
  columns:
    -
      - { id: core, label: "Payments core", sub: "airline" }
    -
      - { id: camel, label: "Camel on Quarkus", sub: "EIP · routes" }
      - { id: kafka, label: "Kafka", sub: "events", kind: bus }
    -
      - { id: deuna, label: "DEUNA", sub: "gateway", kind: cloud }
      - { id: wompi, label: "Wompi", sub: "gateway", kind: cloud }
      - { id: more, label: "More methods", sub: "one new route", kind: cloud }
  edges:
    - { from: core, to: camel }
    - { from: camel, to: deuna }
    - { from: camel, to: wompi }
    - { from: camel, to: more }
    - { from: camel, to: kafka, dashed: true }
---

Each payment provider speaks its own protocol. The integration layer on the Red Hat stack routes, transforms and reconciles messages between the core and every provider, so adding a new payment method is a new route, not a new project.
