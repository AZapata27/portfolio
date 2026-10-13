---
title: "IP/REV, interoperabilidad de peajes electrónicos"
client: "Ministerio de Transporte (con OLJ Solutions)"
period: "2023 – 2024"
domain: "Transporte y movilidad"
role: "Desarrollador senior en el equipo core"
summary: "El sistema oficial para pagar los peajes de las vías nacionales con un único TAG: conecta a los operadores de peaje con los intermediadores que emiten los TAG y sincroniza las listas de vehículos y sus pasos por peaje."
stack: [Java 17, Spring Boot, ActiveMQ Artemis, Docker, AWS]
metric: { value: "Un solo TAG", label: "para todas las vías del país" }
featured: true
order: 1
plate:
  src: ../../../assets/work/iprev.png
  alt: "Portada del portal Colpass del Ministerio de Transporte, el sistema IP/REV de recaudo electrónico de peajes"
  source: colpass.mintransporte.gov.co
  captured: "2026-10"
schematic:
  columns:
    -
      - { id: ops, label: "Operadores de peaje", sub: "pasos por peaje", kind: channel }
    -
      - { id: core, label: "IP/REV core", sub: "Java 17 · Spring Boot" }
      - { id: mq, label: "ActiveMQ Artemis", sub: "lotes · prefetch", kind: bus }
    -
      - { id: inter, label: "Intermediadores", sub: "emiten los TAG", kind: channel }
  edges:
    - { from: ops, to: core, label: "pasos" }
    - { from: core, to: inter, label: "listas" }
    - { from: core, to: mq, dashed: true }
---

Microservicios para el intercambio de listas de vehículos y pasos por peaje entre operadores e intermediadores. Optimicé el tráfico de mensajes en ActiveMQ Artemis (prefetch, concurrencia de consumidores y envío de pasos en lotes) para bajar la carga de red y la latencia, y propuse mejoras al diseño orientado a eventos, como centralizar las validaciones con Jakarta Bean Validation.
