---
title: "Plataforma de Developer Experience"
client: "Flypass (con Quind)"
period: "2024 – actual"
domain: "Plataforma e IA"
role: "Technical lead"
summary: "Backstage, AWS Service Catalog y arquetipos de proyecto para que un servicio nuevo arranque sobre rieles. Presentada al C-Level con una reducción medida del 40 % en time-to-market."
stack: [Backstage, AWS Service Catalog, GitHub Actions, Terraform, Quarkus, Spring Boot]
metric: { value: "−40 %", label: "de time-to-market para servicios nuevos" }
featured: true
order: 5
schematic:
  columns:
    -
      - { id: team, label: "Equipo", sub: "servicio nuevo" }
    -
      - { id: backstage, label: "Backstage", sub: "catálogo · TechDocs" }
      - { id: catalog, label: "Service Catalog", sub: "productos AWS" }
      - { id: arch, label: "Arquetipos", sub: "Quarkus · Spring Boot" }
    -
      - { id: ci, label: "GitHub Actions", sub: "CI/CD" }
      - { id: tf, label: "Terraform", sub: "infraestructura" }
    -
      - { id: prod, label: "PROD", sub: "−40 % time-to-market", kind: prod }
  edges:
    - { from: team, to: backstage }
    - { from: team, to: catalog }
    - { from: team, to: arch }
    - { from: arch, to: ci }
    - { from: catalog, to: tf }
    - { from: ci, to: prod }
    - { from: tf, to: prod }
---

Junto con la arquitectura de microservicios y streaming con Kafka de la plataforma de pagos y movilidad, lideré una iniciativa de Developer Experience: catálogo de servicios en Backstage, productos de AWS Service Catalog y arquetipos que llevan los estándares del equipo (observabilidad, seguridad, pruebas) desde el primer commit.
