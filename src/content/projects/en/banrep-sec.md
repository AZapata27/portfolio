---
title: "SEC, the new Foreign Exchange Information System"
client: "Banco de la República (with INDRA Colombia)"
period: "2021 – 2022"
domain: "Banking"
role: "Software engineer"
summary: "Modernization of the Foreign Exchange Statistical System, where the country's foreign exchange operations are registered with the central bank. Its first phase, the international investments module, went live in September 2021."
stack: [Java, Oracle, JBoss, WebLogic, Angular, Jenkins]
metric: { value: "Sept 2021", label: "first phase in production" }
featured: true
order: 9
schematic:
  columns:
    -
      - { id: legacy, label: "SEC monolith", sub: "Java 8 · JSP · Oracle", kind: store }
    -
      - { id: mig, label: "Migration", sub: "module by module" }
    -
      - { id: ms, label: "Microservices", sub: "JBoss · WebLogic" }
      - { id: ci, label: "CI/CD", sub: "Docker · Jenkins · Git", kind: bus }
    -
      - { id: prod, label: "Intl. investments", sub: "production · Sept 2021", kind: prod }
  edges:
    - { from: legacy, to: mig, dashed: true }
    - { from: mig, to: ms }
    - { from: ci, to: ms, dashed: true }
    - { from: ms, to: prod }
---

Migration of the Java 8 and JSP monolith on Oracle to the new system, with microservices deployed on JBoss and WebLogic and CI/CD with Docker, Jenkins and Git.
