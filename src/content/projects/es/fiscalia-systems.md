---
title: "Tres sistemas misionales para la Fiscalía"
client: "Fiscalía General de la Nación (contratista)"
period: "2025 – 2026"
domain: "Sector público"
role: "Full stack y tech lead"
summary: "Extradición y Captura, Protección de Víctimas y Testigos, y Acusadores Privados, construidos full stack sobre NestJS, React y Oracle y desplegados en OpenShift con GitHub Actions."
stack: [Node.js, TypeScript, NestJS, React, Oracle PL/SQL, OpenShift, GitHub Actions]
featured: false
order: 15
schematic:
  columns:
    -
      - { id: ext, label: "Extradición y Captura", sub: "asuntos internacionales" }
      - { id: vict, label: "Víctimas y Testigos", sub: "protección" }
      - { id: acus, label: "Acusadores Privados", sub: "penal acusatorio" }
    -
      - { id: stack, label: "NestJS + React", sub: "un solo stack" }
      - { id: ora, label: "Oracle", sub: "PL/SQL", kind: store }
    -
      - { id: ci, label: "GitHub Actions", sub: "un solo pipeline" }
    -
      - { id: os, label: "OpenShift", sub: "despliegue", kind: prod }
  edges:
    - { from: ext, to: stack }
    - { from: vict, to: stack }
    - { from: acus, to: stack }
    - { from: stack, to: ora }
    - { from: stack, to: ci }
    - { from: ci, to: os }
---

Tres sistemas con peso legal, cada uno con su propio flujo y modelo de datos, entregados con un solo stack y un solo pipeline de despliegue.
