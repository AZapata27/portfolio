---
title: "SARLAFT, anti-money-laundering control"
client: "Banco de la República (with INDRA Colombia)"
period: "2022 – 2023"
domain: "Banking"
role: "Technical lead"
summary: "The central bank's system for preventing money laundering and terrorism financing: batch and ETL processes over files of 50,000 to 500,000 lines, and loading of restrictive lists (OFAC, UN Security Council, Interpol red notices)."
stack: [Java 11, Spring Batch, JBoss, SQL Server]
featured: false
order: 10
schematic:
  columns:
    -
      - { id: files, label: "Flat files", sub: "50k–500k lines", kind: channel }
      - { id: lists, label: "Restrictive lists", sub: "OFAC · UN · Interpol", kind: cloud }
    -
      - { id: batch, label: "Spring Batch", sub: "Java 11 · JBoss" }
    -
      - { id: db, label: "SQL Server", sub: "database", kind: store }
    -
      - { id: ctrl, label: "Counterparty screening", sub: "AML/CFT" }
  edges:
    - { from: files, to: batch }
    - { from: lists, to: batch }
    - { from: batch, to: db }
    - { from: db, to: ctrl }
---

A Java 11 monolith with Spring Batch deployed on JBoss over SQL Server, with batch processing at the core of counterparty screening.
