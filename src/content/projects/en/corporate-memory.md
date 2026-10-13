---
title: "Corporate memory with MCP and RAG"
client: "Quind"
period: "2025 – present"
domain: "Platform and AI"
role: "Solution architect"
summary: "An MCP server with retrieval-augmented generation (RAG) over 7,000+ internal resources, so agents and people answer with the company's own knowledge."
stack: [MCP, RAG, LangChain, Vertex AI]
metric: { value: "7,000+", label: "internal resources queryable by agents" }
featured: true
order: 7
schematic:
  columns:
    -
      - { id: docs, label: "Documents", sub: "7,000+ resources", kind: store }
      - { id: code, label: "Code and decisions", sub: "repos · ADRs", kind: store }
    -
      - { id: rag, label: "Ingest + index", sub: "RAG" }
    -
      - { id: mcp, label: "MCP server", sub: "tools" }
    -
      - { id: agents, label: "Agents", sub: "in the workflow" }
      - { id: people, label: "People", sub: "sourced answers" }
  edges:
    - { from: docs, to: rag }
    - { from: code, to: rag }
    - { from: rag, to: mcp }
    - { from: mcp, to: agents }
    - { from: mcp, to: people }
---

Exposed as MCP tools, so every agent in the company's workflow draws on the same knowledge base.
