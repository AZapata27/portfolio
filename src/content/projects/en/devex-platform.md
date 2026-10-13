---
title: "Developer Experience platform"
client: "Flypass (with Quind)"
period: "2024 – present"
domain: "Platform and AI"
role: "Technical lead"
summary: "Backstage, AWS Service Catalog and service archetypes so a new service starts on rails. Presented to the C-suite with a measured 40% cut in time-to-market."
stack: [Backstage, AWS Service Catalog, GitHub Actions, Terraform, Quarkus, Spring Boot]
metric: { value: "−40%", label: "time-to-market for new services" }
featured: true
order: 5
schematic:
  columns:
    -
      - { id: team, label: "Team", sub: "new service" }
    -
      - { id: backstage, label: "Backstage", sub: "catalog · TechDocs" }
      - { id: catalog, label: "Service Catalog", sub: "AWS products" }
      - { id: arch, label: "Archetypes", sub: "Quarkus · Spring Boot" }
    -
      - { id: ci, label: "GitHub Actions", sub: "CI/CD" }
      - { id: tf, label: "Terraform", sub: "infrastructure" }
    -
      - { id: prod, label: "PROD", sub: "−40% time-to-market", kind: prod }
  edges:
    - { from: team, to: backstage }
    - { from: team, to: catalog }
    - { from: team, to: arch }
    - { from: arch, to: ci }
    - { from: catalog, to: tf }
    - { from: ci, to: prod }
    - { from: tf, to: prod }
---

Alongside the microservice and Kafka streaming architecture for the payments and mobility platform, I led a Developer Experience initiative: a service catalog in Backstage, AWS Service Catalog products and archetypes that encode the team's standards (observability, security, testing) from the first commit.
