---
title: "Gobierno de IA y harness corporativo de agentes"
client: "Quind"
period: "2025 – actual"
domain: "Plataforma e IA"
role: "Líder técnico de IA"
summary: "Integración de Claude Code con Vertex AI y un harness en Google ADK con los lineamientos, MCPs, plugins y agentes propios del flujo de trabajo de la empresa."
stack: [Claude Code, Vertex AI, Google ADK, MCP, LangGraph, LangChain]
featured: false
order: 6
schematic:
  columns:
    -
      - { id: dev, label: "Claude Code", sub: "desarrollador" }
    -
      - { id: harness, label: "Harness ADK", sub: "lineamientos · plugins" }
    -
      - { id: mcp, label: "MCPs", sub: "herramientas" }
      - { id: agents, label: "Agentes", sub: "LangGraph · LangChain" }
      - { id: gov, label: "Gobernanza", sub: "políticas · LLMOps", kind: bus }
    -
      - { id: vertex, label: "Vertex AI", sub: "modelos", kind: cloud }
  edges:
    - { from: dev, to: harness }
    - { from: harness, to: mcp }
    - { from: harness, to: agents }
    - { from: harness, to: gov, dashed: true }
    - { from: agents, to: vertex }
---

Agentes, skills y servidores MCP construidos con Claude Agent SDK, Google ADK, LangGraph y LangChain, con prácticas de LLMOps para que la empresa pueda confiar en ellos y operarlos.
