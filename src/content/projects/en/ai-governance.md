---
title: "AI governance and corporate agent harness"
client: "Quind"
period: "2025 – present"
domain: "Platform and AI"
role: "AI technical lead"
summary: "Claude Code integrated with Vertex AI, and a Google ADK harness carrying the company's guidelines, MCP servers, plugins and workflow agents."
stack: [Claude Code, Vertex AI, Google ADK, MCP, LangGraph, LangChain]
featured: false
order: 6
schematic:
  columns:
    -
      - { id: dev, label: "Claude Code", sub: "developer" }
    -
      - { id: harness, label: "ADK harness", sub: "guidelines · plugins" }
    -
      - { id: mcp, label: "MCP servers", sub: "tools" }
      - { id: agents, label: "Agents", sub: "LangGraph · LangChain" }
      - { id: gov, label: "Governance", sub: "policies · LLMOps", kind: bus }
    -
      - { id: vertex, label: "Vertex AI", sub: "models", kind: cloud }
  edges:
    - { from: dev, to: harness }
    - { from: harness, to: mcp }
    - { from: harness, to: agents }
    - { from: harness, to: gov, dashed: true }
    - { from: agents, to: vertex }
---

Agents, skills and MCP servers built with the Claude Agent SDK, Google ADK, LangGraph and LangChain, with LLMOps practices so the company can trust and operate them.
