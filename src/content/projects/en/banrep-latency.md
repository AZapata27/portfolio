---
title: "Low-latency microservices for Colombia's central bank"
client: "Banco de la República (with INDRA Colombia)"
period: "2021 – 2023"
domain: "Banking"
role: "Technical lead of two teams"
summary: "Mission-critical microservices went from 5 seconds to 100 milliseconds at 10,000 requests per second, with ACID guarantees that fixed data consistency."
stack: [Java, Spring Cloud, WebFlux, Redis, MongoDB, GCP Pub/Sub, Apigee, AWS, DynamoDB]
metric: { value: "−98%", label: "latency, 5 s to 100 ms at 10,000 req/s" }
featured: true
order: 12
schematic:
  columns:
    -
      - { id: clients, label: "Clients", sub: "10,000 req/s", kind: channel }
    -
      - { id: flux, label: "WebFlux", sub: "reactive · non-blocking" }
    -
      - { id: redis, label: "Redis", sub: "cache", kind: store }
      - { id: mongo, label: "MongoDB", sub: "reads", kind: store }
    -
      - { id: resp, label: "Response", sub: "5 s → 100 ms", kind: prod }
  edges:
    - { from: clients, to: flux }
    - { from: flux, to: redis }
    - { from: flux, to: mongo }
    - { from: redis, to: resp }
    - { from: mongo, to: resp }
---

Two teams of four developers, Java 8 to 17, and a set of services that had to answer fast under load. We rebuilt the hot paths on WebFlux with Redis and MongoDB, resolved transactional integrity issues by enforcing ACID guarantees (90% better data consistency) and launched a Coding Dojo with Jenkins, SonarQube and Kafka so the quality bar outlived the project.
