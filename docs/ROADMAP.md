# Roadmap

Ideas para extender el portafolio después de elegir la variante. Ordenadas por relación
valor/esfuerzo; cada una cabe en un PR.

## Funcionalidades de IA (básicas primero)

1. **"Preguntale a mi CV"** (API on-demand). Ruta `src/pages/api/ask.ts` con
   `export const prerender = false`, que arma el contexto a partir de `src/content/` (ya tipado) y
   llama a la API de Anthropic (`claude-haiku-5-5` para costo bajo). Un cuadro de texto en la
   sección de contacto; respuestas en streaming; límite de peticiones por IP (Vercel KV o
   `@vercel/firewall`); el system prompt sólo responde sobre lo que está en el contenido.
   Variable: `ANTHROPIC_API_KEY` (ya reservada en `.env.example`).
2. **Servidor MCP del portafolio.** Un endpoint MCP (`/api/mcp`) que expone `get_profile`,
   `list_experience`, `list_projects`, `search_skills` leyendo las colecciones. Muy en línea con el
   posicionamiento AI-native: un reclutador con un agente puede "preguntarle" al sitio.
3. **CV en PDF generado desde el contenido.** Hoy el PDF es un archivo subido a mano. Generarlo en
   build (p. ej. con `@react-pdf/renderer` o Playwright `page.pdf()`) desde `src/content/` elimina la
   deriva entre sitio y CV, y permite una versión sin teléfono.
4. **Imagen Open Graph generada.** `src/pages/og.png.ts` con `satori` + `resvg` usando los tokens de
   la variante elegida; hoy `Seo.astro` apunta a `/og.png` que no existe (pendiente de la variante).

## Contenido y producto

5. **Notas / escritos** (`src/content/notes/`): colección Markdown con `render()`; RSS con
   `@astrojs/rss`. Buen lugar para ADRs públicos y aprendizajes de integración.
6. **Casos de estudio largos**: página por proyecto (`/work/<slug>/`) con `getStaticPaths` a partir
   de `projects`; hoy sólo hay resumen.
7. **Actividad de GitHub**: tarjeta con últimos repos/commits públicos vía API de GitHub en build.
8. **Analítica sin cookies**: Vercel Web Analytics (`vercel({ webAnalytics: { enabled: true } })`).

## Calidad e infraestructura

9. **Comprobación de paridad de idiomas** (`scripts/check-i18n.ts`): falla el build si un `slug`
   existe en `en/` y no en `es/` o viceversa.
10. **Pruebas visuales**: Playwright con capturas de referencia por sección y viewport, en GitHub
    Actions sobre cada PR.
11. **Lighthouse CI** en PR (rendimiento, accesibilidad, SEO).
12. **Tema oscuro** sólo si la variante elegida lo pide; hoy la escena de uso es clara.
