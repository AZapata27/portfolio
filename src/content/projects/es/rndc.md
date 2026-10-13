---
title: "Integración con el RNDC para empresas de carga"
client: "Grupo Nutresa, Rápido Ochoa y otros transportadores"
period: "2020 – actual"
domain: "Transporte y movilidad"
role: "Arquitecto y desarrollador · Contratista independiente"
summary: "Remesas, manifiestos electrónicos de carga y cumplidos reportados al RNDC del Ministerio de Transporte, con validación previa y trazabilidad de cada reporte."
stack: [Java, Kafka, Debezium, Confluent, Oracle, Keycloak, OpenTelemetry, Grafana]
metric: { value: "Cada reporte", label: "validado antes de enviarse y trazable de punta a punta" }
featured: true
order: 3
schematic:
  columns:
    -
      - { id: tms, label: "Sistema del transportador", sub: "orden · remesa · manifiesto" }
    -
      - { id: events, label: "Ciclo por eventos", sub: "Kafka · Debezium" }
      - { id: legacy, label: "Legado Oracle/Java", sub: "Strangler Fig", kind: store }
    -
      - { id: val, label: "Validación previa", sub: "trazabilidad" }
    -
      - { id: rndc, label: "RNDC", sub: "Ministerio de Transporte", kind: cloud }
  edges:
    - { from: tms, to: events }
    - { from: legacy, to: events, dashed: true, label: "CDC" }
    - { from: events, to: val }
    - { from: val, to: rndc }
---

El RNDC (Registro Nacional de Despachos de Carga) es donde debe reportarse cada despacho de carga terrestre en Colombia. Para empresas de carga diseñé un ciclo de vida orientado a eventos (orden, remesa, manifiesto, cumplido) con conciliación de fletes encima, y modernicé el legado Oracle/Java alrededor con Strangler Fig y captura de cambios (CDC) en lugar de una reescritura big-bang.
