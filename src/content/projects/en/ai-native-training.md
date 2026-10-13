---
title: "AI-native development and SDD training"
client: "Quind and its clients"
period: "2025 – present"
domain: "Platform and AI"
role: "Trainer and mentor"
summary: "A Spec-Driven Development and AI-native development program with Claude Code for five teams, plus technical training in Java, Spring WebFlux, Quarkus, testing and cloud."
stack: [Claude Code, SDD, Java, Spring WebFlux, Quarkus]
metric: { value: "80 people", label: "across 5 teams trained in AI-native development" }
featured: true
order: 8
schematic:
  columns:
    -
      - { id: teams, label: "5 teams", sub: "80 people" }
    -
      - { id: sdd, label: "SDD", sub: "spec first" }
      - { id: cc, label: "Claude Code", sub: "design · code · review" }
    -
      - { id: stack, label: "Java · Quarkus", sub: "WebFlux · testing · cloud" }
    -
      - { id: prod, label: "Delivery", sub: "the whole team", kind: prod }
  edges:
    - { from: teams, to: sdd }
    - { from: teams, to: cc }
    - { from: sdd, to: stack }
    - { from: cc, to: stack }
    - { from: stack, to: prod }
---

The goal is a whole team working with AI at every step, not one person: specification, design, code, review and delivery.
