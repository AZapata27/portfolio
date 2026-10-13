# Product

<!-- impeccable:product-schema 1 -->

> Contexto durable del producto para humanos y agentes. Lo visual NO vive aquí (ver `DESIGN.md`
> cuando exista y las notas de cada variante en `src/variants/*/README.md`).
> Los hechos marcados `[inferido]` se dedujeron del brief y del CV sin confirmación de Andrés;
> corregilos si no aplican.

## Platform

web

## Stack

Astro 7 (salida estática, adaptador de Vercel listo para rutas on-demand), TypeScript, CSS plano con
tokens por variante, sin framework de UI. Decisión del usuario: "debe ser con Astro para que sea lo
más fácil" y "mantenible fácilmente por una IA, extensible con funcionalidades".

## Users

- **Primario:** reclutadores, hiring managers, CTOs y clientes potenciales de freelance (Colombia,
  Latam y remoto internacional) que evalúan a Andrés para proyectos de arquitectura, integración o
  desarrollo AI-native. Llegan desde LinkedIn, GitHub o un enlace en el CV. `[inferido]` Suelen
  mirar en escritorio, en horario laboral; a veces desde el teléfono dentro de un chat.
  Su trabajo: decidir en menos de un minuto si vale la pena una conversación, luego encontrar
  pruebas (experiencia, casos, stack) y una forma de contacto.
- **Secundario:** el propio Andrés manteniéndolo, casi siempre a través de agentes de IA.

## Product Purpose

Portafolio personal en https://www.andres-zapata.dev. Muestra quién es (arquitecto de software:
integración, event streaming, AI-native), pruebas (10+ años, cifras, casos), stack y contacto, en
inglés (por defecto) y español. Éxito: el visitante escribe o conecta por LinkedIn; un reclutador
entiende el posicionamiento en el primer viewport.

## Positioning

"Mi oficio es hacer que los sistemas se hablen entre sí": un arquitecto de integración (EIP, Apache
Camel sobre Quarkus, Kafka con Debezium y Streams) que además construye el lado de la IA (harnesses
de agentes, servidores MCP, skills, gobernanza) y lidera equipos (200+ personas en cinco años). No es
un portafolio genérico de full stack. Dominio probado: fintech, banca, transporte y movilidad,
logística; conocimiento de RNDC, IP/REV, RUNT, peajes electrónicos y facturación electrónica.

## Capabilities

Una sola página por idioma con: identidad y propuesta, capacidades (arquitectura, integración,
AI-native, liderazgo) con la tabla de logros, la trayectoria como línea de tiempo (empresa, cargo,
una línea y stack superficial; el detalle queda en el CV), los proyectos tangibles como galería de láminas agrupada por
dominio (la sección con más peso), con una página por proyecto (`/proyectos/<slug>/`) que lleva la
captura real del sitio público o un esquema de arquitectura, stack, idiomas, contacto, descarga del CV (PDF en el idioma de
la página) y cambio de idioma. Hoy no hay blog, formularios ni
analítica.

## Constraints

- El contenido es la única fuente de verdad y vive en `src/content/` (en y es). Los datos de
  clientes se limitan a lo que ya es público en el CV; nunca datos de usuarios finales.
- Salida estática en Vercel; sin dependencias en tiempo de ejecución. Las rutas on-demand quedan
  reservadas para funcionalidades de IA futuras (`docs/ROADMAP.md`).
- Mundo visual único: `blueprint` (plano de ingeniería / ruta EIP), elegido el 2026-10-10 entre dos
  variantes. Español por defecto en `/`, inglés en `/en/`.
- La consultora intermediaria de un contrato no se nombra: se dice "Contratista" a secas.
- Accesibilidad: contraste AA, navegación por teclado, `prefers-reduced-motion` respetado.
- El teléfono no se publica en HTML (el PDF del CV sí lo contiene; decisión pendiente de Andrés).
- Idioma de la documentación y del código: español en comentarios y docs, inglés en identificadores.

## Terminology

EIP (Enterprise Integration Patterns), Camel, Quarkus, Kafka, CDC (Debezium), CQRS, DDD, ADR,
Strangler Fig, MCP (Model Context Protocol), harness de agentes, skills; RNDC, remesa, manifiesto
electrónico de carga, cumplido, SICE-TAC, IP/REV, RUNT, TAG (peaje electrónico), facturación
electrónica.

## Evidence

Cifras del CV: 700.000+ usuarios servidos; −98 % de latencia (5 s → 100 ms a 10.000 req/s) en Banco
de la República; −40 % de time-to-market con la plataforma de Developer Experience; 200+ personas
lideradas en cinco años; 10+ años de experiencia. Clientes y proyectos públicos: Flypass (vía Quind),
Avianca (como contratista; no se nombra a la consultora intermediaria), Fiscalía General de la
Nación, Celsia, Ministerio de Transporte (IP/REV, RUNT vía OLJ Solutions), Banco de la República
(vía INDRA), Grupo Nutresa y Rápido Ochoa (RNDC).

## Voice

Directa, en primera persona, concreta, sin hype. Marco narrativo heredado de los borradores del
README de GitHub: tres voces de un mismo ingeniero (el arquitecto, el constructor, el líder) y la
trayectoria como una ruta de integración (canal de entrada, router, ramas, agregador, producción).

## Assets

- Monograma AZ como favicon (`public/favicon.svg`) e imagen Open Graph (`public/og.png`, generada
  desde `docs/og-card.html`).
- CV en PDF en español e inglés (`public/cv/Andres-Zapata-CV-es.pdf`, `-en.pdf`), ambos con el
  teléfono.
- SVG de los cuatro conceptos de README (`conciso`, `ruta-eip`, `git-log`, `autopista`) en las ramas
  `docs/readme-*` del repo `AZapata27/AZapata27`: referencia visual, no se publican.

## Accessibility

Escena de uso: escritorio en jornada laboral, luz de día; tema claro. Contraste AA mínimo,
foco visible, estructura semántica (landmarks, encabezados), textos alternativos en imágenes,
animaciones desactivables.

## Open decisions

- Si el PDF del CV se publica con el teléfono o se genera una versión sin él.
- Nombre público: "Andrés Zapata" (corto) en la interfaz; "Andrés Felipe Zapata" en metadatos.
