---
title: "SARLAFT, control de lavado de activos"
client: "Banco de la República (con INDRA Colombia)"
period: "2022 – 2023"
domain: "Banca"
role: "Technical lead"
summary: "Sistema de prevención del lavado de activos y la financiación del terrorismo: procesos batch y ETL sobre archivos de 50.000 a 500.000 líneas y carga de listas restrictivas (OFAC, Consejo de Seguridad de la ONU, notificaciones rojas de Interpol)."
stack: [Java 11, Spring Batch, JBoss, SQL Server]
featured: false
order: 10
schematic:
  columns:
    -
      - { id: files, label: "Archivos planos", sub: "50.000–500.000 líneas", kind: channel }
      - { id: lists, label: "Listas restrictivas", sub: "OFAC · ONU · Interpol", kind: cloud }
    -
      - { id: batch, label: "Spring Batch", sub: "Java 11 · JBoss" }
    -
      - { id: db, label: "SQL Server", sub: "base de datos", kind: store }
    -
      - { id: ctrl, label: "Control de contrapartes", sub: "prevención LA/FT" }
  edges:
    - { from: files, to: batch }
    - { from: lists, to: batch }
    - { from: batch, to: db }
    - { from: db, to: ctrl }
---

Monolito en Java 11 con Spring Batch desplegado en JBoss sobre SQL Server, con el procesamiento por lotes como núcleo del control de contrapartes.
