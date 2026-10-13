---
title: "IP/REV, nationwide electronic toll interoperability"
client: "Colombia's Ministry of Transport (with OLJ Solutions)"
period: "2023 – 2024"
domain: "Transport and mobility"
role: "Senior developer on the core team"
summary: "The official system for paying tolls on national roads with a single TAG: it connects toll operators with the intermediaries that issue TAGs and keeps vehicle lists and toll passes in sync."
stack: [Java 17, Spring Boot, ActiveMQ Artemis, Docker, AWS]
metric: { value: "One TAG", label: "for every national road" }
featured: true
order: 1
plate:
  src: ../../../assets/work/iprev.png
  alt: "Home page of Colpass, the Ministry of Transport's IP/REV electronic toll collection portal"
  source: colpass.mintransporte.gov.co
  captured: "2026-10"
schematic:
  columns:
    -
      - { id: ops, label: "Toll operators", sub: "toll passes", kind: channel }
    -
      - { id: core, label: "IP/REV core", sub: "Java 17 · Spring Boot" }
      - { id: mq, label: "ActiveMQ Artemis", sub: "batches · prefetch", kind: bus }
    -
      - { id: inter, label: "Intermediaries", sub: "issue the TAGs", kind: channel }
  edges:
    - { from: ops, to: core, label: "passes" }
    - { from: core, to: inter, label: "lists" }
    - { from: core, to: mq, dashed: true }
---

Microservices for exchanging vehicle lists and toll passes between operators and intermediaries. I tuned message traffic on ActiveMQ Artemis (prefetch, consumer concurrency and batched toll passes) to cut network load and latency, and proposed improvements to the event-driven design such as centralizing validations with Jakarta Bean Validation.
