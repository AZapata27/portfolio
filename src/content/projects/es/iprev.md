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
---

Microservicios para el intercambio de listas de vehículos y pasos por peaje entre operadores e intermediadores. Optimicé el tráfico de mensajes en ActiveMQ Artemis (prefetch, concurrencia de consumidores y envío de pasos en lotes) para bajar la carga de red y la latencia, y propuse mejoras al diseño orientado a eventos, como centralizar las validaciones con Jakarta Bean Validation.
