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
  luego más recientes), `getProjects(locale)` (por `order`), `groupProjects()` (agrupa por `domain`), `getSkills()`.
- **i18n** (`src/lib/i18n.ts`): lista de idiomas, textos de UI (`t(locale)('clave')`), rutas
  localizadas (`localePath`), formato de fechas (`formatPeriod`, `formatDuration`). El enrutado lo
  hace Astro (`i18n` en `astro.config.ts`): español sin prefijo, inglés bajo `/en/`.
- **Base compartida**: `src/layouts/Base.astro` (head, `Seo.astro`, estilos globales, slot `head`
  para fuentes de la variante) y `src/styles/global.css` (reset y accesibilidad, sin identidad).
- **Mundo visual** (`src/variants/blueprint/`): autocontenido. Se conserva la carpeta `variants/`
  porque permite construir y comparar alternativas sin tocar el contenido (así se eligió esta).
  - `Page.astro`: compone la página a partir del contenido; recibe `locale`.
  - `tokens.css`: colores, tipografías, espaciado, grosores de línea y motion como custom properties
    bajo `html[data-variant="blueprint"]`, más las clases base de las hojas.
  - `sections/*.astro`: una hoja por archivo (Hero, Capabilities, Experience, Work, Stack, Contact)
    más Topbar y Footer. `components/`: Sheet, RouteDiagram, RouteFlow, EipSprite, DetailA, TitleBlock.
  - `labels.ts`: vocabulario del plano (SHEET, REV, PARTS LIST…) en en/es.
  - `README.md`: decisiones de diseño; `DESIGN.md` en la raíz las resume en formato de tokens.
- **Páginas** (`src/pages/`): sólo deciden idioma: `index.astro` (es) y `en/index.astro` (en), más
  las páginas de proyecto `proyectos/[slug].astro` y `en/work/[slug].astro` (estáticas, una por
  entrada de `projects`; `projectPath()` en `i18n.ts` da la ruta por idioma).
- **Iconos**: `src/components/Icon.astro`. Logos de marcas desde `simple-icons` (en build, sin coste
  en cliente) y un set propio de iconos de interfaz con un único grosor de trazo.
- **Fuentes**: Astro Fonts API (`fonts` en `astro.config.ts`, proveedor Fontsource). Se descargan
  en build y se sirven desde el propio sitio. Cada variante incluye `<Font cssVariable=… />` sólo
  para las familias que usa.
- **SEO**: `src/components/Seo.astro`: canonical, `hreflang`, Open Graph, Twitter, JSON-LD `Person`.
  Acepta `paths` (rutas ya localizadas) para las páginas cuyo segmento cambia por idioma, e `image`.
- **Imágenes**: capturas de proyectos en `src/assets/work/`, servidas por `astro:assets` (`<Image>`,
  sharp en build) desde `components/Plate.astro`.
  Sitemap con `@astrojs/sitemap`.

## Build y despliegue

- `astro build` genera `.vercel/output/` (Build Output API) a través de `@astrojs/vercel`.
- Vercel despliega `master` a producción y cada rama/PR a una URL de vista previa.
- `output: 'static'`: todo se prerrenderiza. Una ruta puede volverse on-demand (serverless en
  Vercel) exportando `export const prerender = false`; para eso ya está el adaptador.
- Variables de entorno: ninguna hoy. `.env.example` reserva `ANTHROPIC_API_KEY` para el roadmap.

## Rendimiento y SEO técnico

Línea base medida con Lighthouse 12 el 2026-10-13 sobre producción (móvil simulado, CPU ×4):
portada 72 → tras los ajustes de abajo 87 en local sin compresión (el bloqueo del hilo principal pasó de
1.000 ms a 60 ms); escritorio 99; página de proyecto en móvil 97; accesibilidad, buenas prácticas y SEO 100.
Reglas que mantienen esos números:

- **Fuentes**: sólo los pesos y estilos que se usan (`fonts` en `astro.config.ts`: Barlow Condensed 700/800,
  Barlow 400/500/600 sin itálica, JetBrains Mono 400/500/700). Se precargan display y cuerpo; la mono no.
  Cada archivo extra es una precarga más y un relayout de toda la página cuando llega.
- **CSS en línea** (`build.inlineStylesheets: 'always'`): sin hoja externa bloqueante antes del primer render.
- **Sin `text-wrap: pretty` global**: en una página de ~1.500 elementos encarece cada relayout; `balance` sólo en
  encabezados.
- **Sitemap**: `lastmod` real por URL (último commit que tocó su contenido; en un clon superficial, la fecha del
  commit desplegado) y alternates es/en también en las páginas de proyecto. JSON-LD `Person` en todas las
  páginas y `BreadcrumbList` en las de proyecto.
- Para volver a medir: `npx lighthouse@12 https://www.andres-zapata.dev/ --output=json` (con Playwright, `CHROME_PATH`
  apuntando a su Chromium); los números de un servidor local sin compresión no son comparables en LCP.

## Probar una alternativa visual

Si algún día se quiere ensayar otro mundo visual sin tocar el contenido: crear
`src/variants/<nueva>/` con su `Page.astro`, montarla en una ruta temporal (`src/pages/<nueva>/index.astro`
y `src/pages/en/<nueva>/index.astro`), comparar, y al decidir dejar una sola en `/` y `/en/` y borrar
la otra. Así se hizo el 2026-10-10 entre `blueprint` (elegida) y `script`.

## Decisiones

- **Astro, sin framework de UI ni Tailwind.** Pedido explícito de simplicidad; CSS plano con tokens es
  lo más legible para un agente y no añade build steps.
- **Dos idiomas desde el día uno, español por defecto.** Decisión de Andrés (2026-10-10): el CV y el
  mercado principal son en español; el inglés vive en `/en/` con `hreflang` y `x-default` al español.
- **Variantes como carpetas, no como ramas.** Una sola rama y una sola URL de vista previa permitieron
  comparar en igualdad de condiciones; la descartada se borró con un commit.
- **Analítica**: `@vercel/analytics` y `@vercel/speed-insights` montados una vez en `Base.astro`
  (componentes Astro oficiales). Sin cookies ni datos personales; límites y lectura en `docs/ANALITICA.md`.
- **Sin JavaScript en cliente por defecto.** La única excepción es el script de analítica. Las variantes pueden añadir `<script>` pequeños para
  motion o navegación; siempre con fallback sin JS.
