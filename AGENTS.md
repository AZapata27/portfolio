# Guía para agentes de IA

Este repositorio está pensado para que un agente (Claude Code u otro) lo mantenga sin romperlo.
Leé primero `PRODUCT.md` (qué es y para quién) y `docs/ARCHITECTURE.md` (cómo está armado).

## Reglas que no se negocian

1. **Contenido y diseño están separados.** Datos del CV: sólo en `src/content/` (JSON y Markdown,
   validados por `src/content.config.ts`). Identidad visual: sólo en `src/variants/<variante>/`.
   Un componente de variante nunca contiene texto del CV; un archivo de contenido nunca contiene
   decisiones visuales.
2. **Todo cambio de contenido va en los dos idiomas** (`en/` y `es/`). Si falta una traducción,
   agregala; no dejes un idioma desactualizado.
3. **No agregues dependencias** salvo necesidad clara. El sitio no envía JavaScript al cliente por
   defecto; si una interacción lo necesita, usá `<script>` de Astro con progresive enhancement y
   respetá `prefers-reduced-motion`.
4. **Accesibilidad mínima:** contraste AA (4.5:1 texto, 3:1 texto grande), foco visible, un solo
   `h1` por página, landmarks (`header`, `main`, `nav`, `footer`), `alt` en imágenes, iconos
   decorativos con `aria-hidden`.
5. **Nada de secretos ni datos de usuarios finales.** Los clientes se nombran sólo como ya aparecen
   en el CV público. El teléfono no se publica en HTML.
6. **Español en documentación y comentarios; inglés en identificadores de código.** Fechas absolutas.
7. **Git:** nunca commitear directo en `master`. Rama `feat/…`, `fix/…`, `docs/…` y PR hacia `master`.
   Antes de abrir el PR: `npm run check` y `npm run build` deben pasar.

## Cómo verificar lo que hiciste

```bash
npm run check          # tipos y esquemas de contenido
npm run build          # build completo (descarga fuentes; necesita red)
npx astro dev --background   # servidor en 4321; `npx astro dev stop` para apagarlo
```

Para capturar una página sin herramientas extra (Playwright CLI ya instalado en esta máquina):

```bash
npx playwright screenshot --viewport-size=1440,900 --full-page http://127.0.0.1:4321/blueprint/ screenshots/blueprint-desktop.png
npx playwright screenshot --viewport-size=390,844 --full-page http://127.0.0.1:4321/blueprint/ screenshots/blueprint-mobile.png
```

`screenshots/` está en `.gitignore`.

## Tareas típicas

| Quiero…                              | Tocar…                                                                 |
| ------------------------------------ | ---------------------------------------------------------------------- |
| Actualizar un puesto o agregar uno   | `src/content/experience/{en,es}/<slug>.md` (ver `docs/CONTENT.md`)     |
| Agregar un proyecto destacado        | `src/content/projects/{en,es}/<slug>.md`                               |
| Cambiar stack                        | `src/content/skills.json` (slugs de simple-icons en `icon`)            |
| Cambiar un texto de interfaz         | `src/lib/i18n.ts` (`ui.en` y `ui.es`)                                  |
| Cambiar colores / tipografía         | `src/variants/<variante>/tokens.css` y `astro.config.ts` (`fonts`)     |
| Agregar una sección                  | `src/variants/<variante>/sections/<Nombre>.astro` + incluirla en `Page.astro` |
| Agregar una ruta on-demand (API)     | `src/pages/api/<nombre>.ts` con `export const prerender = false`       |
| Promover la variante elegida         | `docs/ARCHITECTURE.md`, sección "Promover la variante ganadora"        |

## Lo que NO hay que hacer

- Duplicar contenido dentro de componentes "para ir más rápido".
- Añadir Tailwind, frameworks de UI o librerías de animación sin una razón documentada en
  `docs/ARCHITECTURE.md`.
- Tocar `src/layouts/Base.astro` para cosas visuales: ahí sólo va lo compartido (head, SEO, slots).
- Borrar la otra variante antes de que Andrés haya elegido.
