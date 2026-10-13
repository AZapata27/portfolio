---
title: "RUNT citizen portal"
client: "RUNT, Colombia's National Transit Registry (with OLJ Solutions)"
period: "2023 – 2024"
domain: "Transport and mobility"
role: "Full stack developer"
summary: "Modules of RUNT's nationwide public portal: vehicle lookup by plate, citizen data updates and vehicle history."
stack: [Angular, Node.js, Webpack Module Federation, Bootstrap, Azure]
metric: { value: "Millions", label: "of citizens use the portal" }
featured: true
order: 2
url: https://www.runt.gov.co/
plate:
  src: ../../../assets/work/runt-portal.png
  alt: "Vehicle lookup by plate module on the RUNT citizen portal"
  source: runt.gov.co
  captured: "2026-10"
---

Each module is a micro-frontend built with Webpack Module Federation, deployed to Azure and integrated independently into the main portal, so it ships without touching the rest of the site.
