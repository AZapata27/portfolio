---
title: "Agendamiento de citas de Tesorería"
client: "Banco de la República (con INDRA Colombia)"
period: "2022 – 2023"
domain: "Banca"
role: "Desarrollador full stack y revisor"
summary: "Plataforma con la que la ciudadanía agenda citas para los servicios del Departamento de Tesorería del banco central: alta transaccionalidad y tiempo real para el back office operativo."
stack: [Angular, Spring Boot, WebSockets, SSE]
featured: false
order: 11
schematic:
  columns:
    -
      - { id: cit, label: "Ciudadanía", sub: "agenda su cita", kind: channel }
    -
      - { id: web, label: "Angular", sub: "portal de citas" }
    -
      - { id: api, label: "Spring Boot", sub: "alta transaccionalidad" }
      - { id: rt, label: "WebSockets · SSE", sub: "tiempo real", kind: bus }
    -
      - { id: bo, label: "Back office", sub: "Tesorería" }
  edges:
    - { from: cit, to: web }
    - { from: web, to: api }
    - { from: api, to: rt, dashed: true }
    - { from: rt, to: bo }
    - { from: api, to: bo }
---

WebSockets y Server-Sent Events mantienen al back office sincronizado con cada cita; además hice las revisiones técnicas y la aprobación de pull requests del equipo.
