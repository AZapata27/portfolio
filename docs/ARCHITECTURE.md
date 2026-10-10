# Arquitectura

## Capas

```
src/content/*  ──►  src/lib/content.ts  ──►  src/variants/<v>/Page.astro  ──►  src/pages/**
(datos, zod)        (filtrado por idioma,     (layout + tokens + secciones)      (rutas; sólo
                     ordenado, tipado)                                            eligen variante
                                                                                  e idioma)
```

- **Contenido** (`src/content/`): colecciones de Astro con esquemas zod en `src/content.config.ts`.
  Cada colección localizada tiene carpetas `en/` y `es/`; el idioma se deriva del prefijo del `id`.
  `skills.json` es neutral al idioma (los nombres de grupo se traducen en `src/lib/i18n.ts`).
- **Acceso** (`src/lib/content.ts`): `getProfile(locale)`, `getExperience(locale)` (actuales primero,
  luego más recientes), `getProjects(locale)` (destacados primero), `getSkills()`.
- **i18n** (`src/lib/i18n.ts`): lista de idiomas, textos de UI (`t(locale)('clave')`), rutas
  localizadas (`localePath`), formato de fechas (`formatPeriod`, `formatDuration`). El enrutado lo
  hace Astro (`i18n` en `astro.config.ts`): inglés sin prefijo, español bajo `/es/`.
- **Base compartida**: `src/layouts/Base.astro` (head, `Seo.astro`, estilos globales, slot `head`
  para fuentes de la variante) y `src/styles/global.css` (reset y accesibilidad, sin identidad).
- **Variantes** (`src/variants/<v>/`): cada una es un mundo visual completo y autocontenido:
  - `Page.astro`: compone la página a partir del contenido.
  - `tokens.css`: colores, tipografías, espaciado, radios, sombras como custom properties bajo
    `html[data-variant="<v>"]`.
  - `sections/*.astro`: una sección por archivo (Hero, Capabilities, Experience, Work, Stack, Contact).
  - `README.md`: decisiones de diseño de la variante (dirección, tipografías, por qué).
- **Páginas** (`src/pages/`): sólo deciden variante e idioma. `/` y `/es/` son un selector temporal.
- **Iconos**: `src/components/Icon.astro`. Logos de marcas desde `simple-icons` (en build, sin coste
  en cliente) y un set propio de iconos de interfaz con un único grosor de trazo.
- **Fuentes**: Astro Fonts API (`fonts` en `astro.config.ts`, proveedor Fontsource). Se descargan
  en build y se sirven desde el propio sitio. Cada variante incluye `<Font cssVariable=… />` sólo
  para las familias que usa.
- **SEO**: `src/components/Seo.astro`: canonical, `hreflang`, Open Graph, Twitter, JSON-LD `Person`.
  Sitemap con `@astrojs/sitemap`.

## Build y despliegue

- `astro build` genera `.vercel/output/` (Build Output API) a través de `@astrojs/vercel`.
- Vercel despliega `master` a producción y cada rama/PR a una URL de vista previa.
- `output: 'static'`: todo se prerrenderiza. Una ruta puede volverse on-demand (serverless en
  Vercel) exportando `export const prerender = false`; para eso ya está el adaptador.
- Variables de entorno: ninguna hoy. `.env.example` reserva `ANTHROPIC_API_KEY` para el roadmap.

## Promover la variante ganadora

Cuando Andrés elija (por ejemplo `blueprint`):

1. `src/pages/index.astro` y `src/pages/es/index.astro`: renderizar `@/variants/blueprint/Page.astro`
   (con `path="/"` en el `Base`) en lugar de `Chooser.astro`.
2. Borrar `src/pages/blueprint/`, `src/pages/es/blueprint/`, `src/pages/script/`, `src/pages/es/script/`,
   `src/variants/script/` y `src/components/Chooser.astro`.
3. En `astro.config.ts`, quitar de `fonts` las familias que ya no se usen.
4. Actualizar `README.md`, `PRODUCT.md` (decisión cerrada) y escribir `DESIGN.md` a partir de
   `src/variants/blueprint/README.md` y `tokens.css`.
5. `npm run check && npm run build`, PR a `master`.

## Decisiones

- **Astro, sin framework de UI ni Tailwind.** Pedido explícito de simplicidad; CSS plano con tokens es
  lo más legible para un agente y no añade build steps.
- **Dos idiomas desde el día uno.** El CV está en español y el público objetivo es mixto; duplicar el
  contenido es barato comparado con migrar después.
- **Variantes como carpetas, no como ramas.** Una sola rama y una sola URL de vista previa permiten
  comparar en igualdad de condiciones; la descartada se borra con un commit.
- **Sin JavaScript en cliente por defecto.** Las variantes pueden añadir `<script>` pequeños para
  motion o navegación; siempre con fallback sin JS.
