---
title: "Integración del core de pagos de una aerolínea"
client: "Avianca (contratista)"
period: "2026 – actual"
domain: "Integración empresarial"
role: "Senior Red Hat integration engineer"
summary: "Conexión del core de pagos de la aerolínea con pasarelas y medios de pago de Latam como DEUNA y Wompi, con Enterprise Integration Patterns sobre Quarkus y Apache Camel."
stack: [Quarkus, Apache Camel, Red Hat, Kafka]
featured: false
order: 13
schematic:
  columns:
    -
      - { id: core, label: "Core de pagos", sub: "aerolínea" }
    -
      - { id: camel, label: "Camel sobre Quarkus", sub: "EIP · rutas" }
      - { id: kafka, label: "Kafka", sub: "eventos", kind: bus }
    -
      - { id: deuna, label: "DEUNA", sub: "pasarela", kind: cloud }
      - { id: wompi, label: "Wompi", sub: "pasarela", kind: cloud }
      - { id: more, label: "Más medios", sub: "una ruta nueva", kind: cloud }
  edges:
    - { from: core, to: camel }
    - { from: camel, to: deuna }
    - { from: camel, to: wompi }
    - { from: camel, to: more }
    - { from: camel, to: kafka, dashed: true }
---

Cada proveedor de pagos habla su propio protocolo. La capa de integración sobre el stack de Red Hat enruta, transforma y concilia mensajes entre el core y cada proveedor, de modo que agregar un medio de pago es una ruta nueva, no un proyecto nuevo.
