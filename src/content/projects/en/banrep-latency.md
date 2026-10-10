---
title: Low-latency microservices for the central bank
client: Banco de la República (with INDRA Colombia)
period: 2021 – 2023
domain: Banking
role: Technical lead of two teams
summary: Critical microservices went from 5 seconds to 100 milliseconds at 10,000 requests per second, with an ACID model that fixed data consistency.
stack: [Java, Spring Cloud, WebFlux, Redis, MongoDB, GCP Pub/Sub, Apigee, AWS, DynamoDB]
metric: { value: "−98%", label: "latency, 5 s to 100 ms at 10,000 req/s" }
featured: true
order: 3
---

Two teams of four developers, Java 8 to 17, and a set of services that had to answer fast under load. We rebuilt the hot paths on WebFlux with Redis and MongoDB, solved transactionality with a proper ACID model (over 90 % data consistency) and set up a Coding Dojo with Jenkins, SonarQube and Kafka so the quality bar outlived the project.
