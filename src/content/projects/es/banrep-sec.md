---
title: "SEC, nuevo Sistema de Información Cambiaria"
client: "Banco de la República (con INDRA Colombia)"
period: "2021 – 2022"
domain: "Banca"
role: "Ingeniero de software"
summary: "Modernización del Sistema Estadístico Cambiario, con el que se registran ante el banco central las operaciones de cambio del país. La primera fase, el módulo de inversiones internacionales, salió a producción en septiembre de 2021."
stack: [Java, Oracle, JBoss, WebLogic, Angular, Jenkins]
metric: { value: "Sept. 2021", label: "primera fase en producción" }
featured: true
order: 9
schematic:
  columns:
    -
      - { id: legacy, label: "Monolito SEC", sub: "Java 8 · JSP · Oracle", kind: store }
    -
      - { id: mig, label: "Migración", sub: "módulo por módulo" }
    -
      - { id: ms, label: "Microservicios", sub: "JBoss · WebLogic" }
      - { id: ci, label: "CI/CD", sub: "Docker · Jenkins · Git", kind: bus }
    -
      - { id: prod, label: "Inversiones intl.", sub: "producción · sept. 2021", kind: prod }
  edges:
    - { from: legacy, to: mig, dashed: true }
    - { from: mig, to: ms }
    - { from: ci, to: ms, dashed: true }
    - { from: ms, to: prod }
---

Migración del monolito en Java 8 y JSP sobre Oracle hacia el nuevo sistema, con microservicios desplegados en JBoss y WebLogic y CI/CD con Docker, Jenkins y Git.
