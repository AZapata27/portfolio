# Contenido

Toda la información del CV vive en `src/content/`. Los esquemas están en `src/content.config.ts` y
`npm run check` los valida. Cada cambio se hace en inglés **y** en español.

## Perfil (`src/content/profile/{en,es}.json`)

Identidad, resumen, enlaces, ruta del CV (`cv`), dominios, cifras (`metrics`), logros clave del CV
(`achievements`: cuatro, con `value` para la cifra o etiqueta corta, `title` y `body`), capacidades (`capabilities`: cuatro,
con `id` fijo: `architecture`, `integration`, `ai-native`, `leadership`), voces (`voices`: tres, con
`id` fijo: `architect`, `builder`, `leader`), idiomas, extras. Los `id` son fijos porque las
variantes los usan para ubicar cada bloque en su composición; el texto es libre.

## Experiencia (`src/content/experience/{en,es}/<slug>.md`)

Mismo `slug` en los dos idiomas. Frontmatter:

```yaml
---
company: Quind
role: Technical Lead
client: Flypass (peajes y parqueaderos electrónicos)   # opcional
sector: Fintech / Transporte
location: Remoto
start: 2024-03        # AAAA-MM
end: null             # AAAA-MM o null si es el puesto actual
type: employment      # employment | contract | freelance | early
order: 1              # desempate al ordenar (menor primero)
summary: Una línea que resume el puesto.
stack: [Spring Boot, Kafka, AWS]
short: Resumen de una línea para la línea de tiempo (opcional; si falta se usa summary).
tags: [Spring Boot, Kafka, AWS, Claude Code]   # stack superficial, máximo 4 (si falta, los primeros de stack)
---
- Logro uno, con cifra si la hay.
- Logro dos.
```

El cuerpo es Markdown: una lista de logros. Hoy el sitio no lo muestra (la hoja de trayectoria es
una línea de tiempo y el detalle vive en el CV), pero se mantiene como fuente para futuras
funcionalidades (p. ej. "Preguntale a mi CV"). Para los primeros años (`type: early`) un solo
archivo agrupa varios roles cortos. `type: freelance` se dibuja como vía paralela, no como estación.

## Proyectos (`src/content/projects/{en,es}/<slug>.md`)

```yaml
---
title: IP/REV, interoperabilidad de peajes electrónicos
client: Ministerio de Transporte (con OLJ Solutions)
period: 2023 – 2024
domain: Transporte y movilidad   # la hoja agrupa por este texto exacto
role: Senior software developer
summary: Una o dos líneas.
stack: [Java, Kafka]
metric: { value: "−98 %", label: "de latencia" }   # opcional
featured: true        # reservado; hoy la cota la decide `metric`
order: 1              # los del mismo domain deben ir contiguos
url: https://…        # opcional, enlace público
---
Uno o dos párrafos de contexto. Sin datos confidenciales del cliente.

Dominios en uso (mismo nombre en todos los proyectos del grupo): `Transporte y movilidad` /
`Transport and mobility`, `Plataforma e IA` / `Platform and AI`, `Banca` / `Banking`,
`Integración empresarial` / `Enterprise integration`, `Sector público` / `Public sector`,
`Datos y telecomunicaciones` / `Data and telecommunications`. Las letras de los detalles (B, C, D…)
se asignan solas por `order`.
```

## Stack (`src/content/skills.json`)

Lista de grupos `{ id, order, items: [{ name, icon? }] }`. `id` debe tener su etiqueta en
`src/lib/i18n.ts` (`skills.<id>`). `icon` es un slug de [simple-icons](https://simpleicons.org)
(`apachekafka`, `quarkus`…); si no hay logo se omite y la variante muestra sólo el nombre.

## Textos de interfaz (`src/lib/i18n.ts`)

Etiquetas cortas (navegación, títulos de sección, botones). Agregar la clave en `ui.en` y `ui.es`.

## Archivos estáticos

- `public/cv/Andres-Zapata-CV-es.pdf` y `public/cv/Andres-Zapata-CV-en.pdf`: el CV descargable en cada
  idioma. La ruta se declara en `profile.cv` de cada `profile/<idioma>.json`; reemplazar el archivo
  para actualizarlo.
- `public/og.png`: imagen para redes (1200×630). Se regenera desde `docs/og-card.html` con
  `npx playwright screenshot --viewport-size=1200,630 docs/og-card.html public/og.png`.
