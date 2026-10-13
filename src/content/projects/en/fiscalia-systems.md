---
title: "Three core systems for the Attorney General's Office"
client: "Fiscalía General de la Nación (contractor)"
period: "2025 – 2026"
domain: "Public sector"
role: "Full stack developer and tech lead"
summary: "Extradition & Capture, Victim & Witness Protection and Private Prosecution, built full stack on NestJS, React and Oracle and deployed to OpenShift through GitHub Actions pipelines."
stack: [Node.js, TypeScript, NestJS, React, Oracle PL/SQL, OpenShift, GitHub Actions]
featured: false
order: 15
schematic:
  columns:
    -
      - { id: ext, label: "Extradition & Capture", sub: "international affairs" }
      - { id: vict, label: "Victims & Witnesses", sub: "protection" }
      - { id: acus, label: "Private Prosecution", sub: "criminal justice" }
    -
      - { id: stack, label: "NestJS + React", sub: "one stack" }
      - { id: ora, label: "Oracle", sub: "PL/SQL", kind: store }
    -
      - { id: ci, label: "GitHub Actions", sub: "one pipeline" }
    -
      - { id: os, label: "OpenShift", sub: "deployment", kind: prod }
  edges:
    - { from: ext, to: stack }
    - { from: vict, to: stack }
    - { from: acus, to: stack }
    - { from: stack, to: ora }
    - { from: stack, to: ci }
    - { from: ci, to: os }
---

Three systems with legal weight, each with its own workflow and data model, delivered with one stack and one deployment pipeline.
