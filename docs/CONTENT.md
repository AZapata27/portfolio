# Contenido

Toda la información del CV vive en `src/content/`. Los esquemas están en `src/content.config.ts` y
`npm run check` los valida. Cada cambio se hace en inglés **y** en español.

## Perfil (`src/content/profile/{en,es}.json`)

Identidad, resumen, enlaces, dominios, cifras (`metrics`), capacidades (`capabilities`: cuatro,
con `id` fijo: `architecture`, `integration`, `ai-native`, `leadership`), voces (`voices`: tres, con
`id` fijo: `architect`, `builder`, `leader`), formación, extras. Los `id` son fijos porque las
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
---
- Logro uno, con cifra si la hay.
- Logro dos.
```

El cuerpo es Markdown: una lista de logros. Para los primeros años (`type: early`) un solo archivo
agrupa varios roles cortos.

## Proyectos (`src/content/projects/{en,es}/<slug>.md`)

```yaml
---
title: IP/REV, interoperabilidad de peajes electrónicos
client: Ministerio de Transporte (con OLJ Solutions)
period: 2023 – 2024
domain: Transporte / Pagos
role: Senior software developer
summary: Una o dos líneas.
stack: [Java, Kafka]
metric: { value: "−98 %", label: "de latencia" }   # opcional
featured: true        # los destacados van primero
order: 1
url: https://…        # opcional, enlace público
---
Uno o dos párrafos de contexto. Sin datos confidenciales del cliente.
```

## Stack (`src/content/skills.json`)

Lista de grupos `{ id, order, items: [{ name, icon? }] }`. `id` debe tener su etiqueta en
`src/lib/i18n.ts` (`skills.<id>`). `icon` es un slug de [simple-icons](https://simpleicons.org)
(`apachekafka`, `quarkus`…); si no hay logo se omite y la variante muestra sólo el nombre.

## Textos de interfaz (`src/lib/i18n.ts`)

Etiquetas cortas (navegación, títulos de sección, botones). Agregar la clave en `ui.en` y `ui.es`.

## Archivos estáticos

- `public/cv/Andres-Zapata-CV.pdf`: el CV descargable. Reemplazar el archivo para actualizarlo.
- `src/assets/portrait.svg`: retrato vectorial (posterizado, tres capas). Las variantes lo importan
  y lo colorean con `fill` sobre cada capa si lo necesitan.
