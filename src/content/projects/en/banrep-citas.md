---
title: "Treasury appointment scheduling"
client: "Banco de la República (with INDRA Colombia)"
period: "2022 – 2023"
domain: "Banking"
role: "Full stack developer and reviewer"
summary: "The platform citizens use to book appointments for the central bank's Treasury Department services: high transaction volume with real-time updates for the operations back office."
stack: [Angular, Spring Boot, WebSockets, SSE]
featured: false
order: 11
schematic:
  columns:
    -
      - { id: cit, label: "Citizens", sub: "book an appointment", kind: channel }
    -
      - { id: web, label: "Angular", sub: "appointments portal" }
    -
      - { id: api, label: "Spring Boot", sub: "high transaction volume" }
      - { id: rt, label: "WebSockets · SSE", sub: "real time", kind: bus }
    -
      - { id: bo, label: "Back office", sub: "Treasury" }
  edges:
    - { from: cit, to: web }
    - { from: web, to: api }
    - { from: api, to: rt, dashed: true }
    - { from: rt, to: bo }
    - { from: api, to: bo }
---

WebSockets and Server-Sent Events keep the back office in sync with every appointment; I also ran technical peer reviews and pull request approvals for the team.
