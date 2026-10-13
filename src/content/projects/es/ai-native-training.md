---
title: "Formación en desarrollo AI-native y SDD"
client: "Quind y sus clientes"
period: "2025 – actual"
domain: "Plataforma e IA"
role: "Formador y mentor"
summary: "Programa de capacitación en Spec-Driven Development y desarrollo AI-native con Claude Code para cinco equipos, además de formación técnica en Java, Spring WebFlux, Quarkus, testing y cloud."
stack: [Claude Code, SDD, Java, Spring WebFlux, Quarkus]
metric: { value: "80 personas", label: "en 5 equipos formados en desarrollo AI-native" }
featured: true
order: 8
schematic:
  columns:
    -
      - { id: teams, label: "5 equipos", sub: "80 personas" }
    -
      - { id: sdd, label: "SDD", sub: "especificación primero" }
      - { id: cc, label: "Claude Code", sub: "diseño · código · revisión" }
    -
      - { id: stack, label: "Java · Quarkus", sub: "WebFlux · testing · cloud" }
    -
      - { id: prod, label: "Entrega", sub: "todo el equipo", kind: prod }
  edges:
    - { from: teams, to: sdd }
    - { from: teams, to: cc }
    - { from: sdd, to: stack }
    - { from: cc, to: stack }
    - { from: stack, to: prod }
---

El objetivo es que un equipo completo trabaje con IA en cada paso, no una sola persona: especificación, diseño, código, revisión y entrega.
