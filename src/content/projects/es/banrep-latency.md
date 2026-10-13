---
title: "Microservicios de baja latencia para el banco central"
client: "Banco de la República (con INDRA Colombia)"
period: "2021 – 2023"
domain: "Banca"
role: "Technical lead de dos equipos"
summary: "Microservicios críticos que pasaron de 5 segundos a 100 milisegundos a 10.000 peticiones por segundo, con un modelo ACID que arregló la consistencia de datos."
stack: [Java, Spring Cloud, WebFlux, Redis, MongoDB, GCP Pub/Sub, Apigee, AWS, DynamoDB]
metric: { value: "−98 %", label: "de latencia, de 5 s a 100 ms a 10.000 req/s" }
featured: true
order: 12
---

Dos equipos de cuatro desarrolladores, Java 8 a 17 y un conjunto de servicios que tenían que responder rápido bajo carga. Reconstruimos los caminos críticos sobre WebFlux con Redis y MongoDB, resolvimos la transaccionalidad con un modelo ACID (más de 90 % de consistencia de datos) y montamos un Coding Dojo con Jenkins, SonarQube y Kafka para que el estándar de calidad sobreviviera al proyecto.
