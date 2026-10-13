---
title: "Memoria corporativa con MCP y RAG"
client: "Quind"
period: "2025 – actual"
domain: "Plataforma e IA"
role: "Arquitecto de la solución"
summary: "Un servidor MCP con generación aumentada por recuperación (RAG) sobre más de 7.000 recursos internos, para que agentes y personas respondan con el conocimiento de la empresa."
stack: [MCP, RAG, LangChain, Vertex AI]
metric: { value: "7.000+", label: "recursos internos consultables por los agentes" }
featured: true
order: 7
schematic:
  columns:
    -
      - { id: docs, label: "Documentos", sub: "7.000+ recursos", kind: store }
      - { id: code, label: "Código y decisiones", sub: "repos · ADRs", kind: store }
    -
      - { id: rag, label: "Ingesta + índice", sub: "RAG" }
    -
      - { id: mcp, label: "Servidor MCP", sub: "herramientas" }
    -
      - { id: agents, label: "Agentes", sub: "del flujo de trabajo" }
      - { id: people, label: "Personas", sub: "respuestas con fuente" }
  edges:
    - { from: docs, to: rag }
    - { from: code, to: rag }
    - { from: rag, to: mcp }
    - { from: mcp, to: agents }
    - { from: mcp, to: people }
---

Expuesta como herramientas MCP, de modo que cualquier agente del flujo de trabajo de la empresa consulta la misma base de conocimiento.
