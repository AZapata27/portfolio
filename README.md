# andres-zapata.dev

Portafolio de Andrés Zapata, arquitecto de software. Sitio estático construido con
[Astro 7](https://docs.astro.build), bilingüe (inglés por defecto, español en `/es/`), desplegado en
Vercel desde este repositorio.

## Requisitos

- Node.js 22.12 o superior (`.nvmrc` fija 22.16.0; en Vercel `engines.node` pide 22.x).
- npm 10.

## Comandos

| Comando           | Qué hace                                                              |
| ----------------- | --------------------------------------------------------------------- |
| `npm install`     | Instala dependencias.                                                 |
| `npm run dev`     | Servidor de desarrollo en http://localhost:4321 (`astro dev`).        |
| `npm run check`   | Chequeo de tipos y de componentes Astro (`astro check`).              |
| `npm run build`   | Build de producción (`.vercel/output/`, Build Output API de Vercel).  |
| `npm run preview` | Sirve el build localmente.                                            |

## Estructura

```
src/
  content/            # ÚNICA fuente de verdad del contenido (CV)
    profile/{en,es}.json
    experience/{en,es}/*.md
    projects/{en,es}/*.md
    skills.json
  content.config.ts   # esquemas (zod) de las colecciones
  lib/                # i18n.ts (idiomas, textos de UI), content.ts (acceso tipado)
  components/         # Icon.astro, Seo.astro, Chooser.astro (temporal)
  layouts/Base.astro  # esqueleto HTML común; sin identidad visual
  styles/global.css   # reset y accesibilidad; sin colores ni fuentes
  variants/           # una carpeta por variante visual (layout, tokens, secciones)
    blueprint/
    script/
  pages/              # rutas: /, /es/, /blueprint/, /es/blueprint/, /script/, /es/script/
public/               # favicon, robots.txt, cv/Andres-Zapata-CV.pdf
docs/                 # ARCHITECTURE.md, CONTENT.md, ROADMAP.md
PRODUCT.md            # contexto de producto (para humanos y agentes)
AGENTS.md / CLAUDE.md # reglas para agentes de IA que mantienen el repo
```

Regla central: **las variantes sólo leen contenido; el contenido nunca sabe de diseño.** Cambiar un
dato del CV es editar un archivo en `src/content/` en los dos idiomas.

## Variantes visuales

Hay dos variantes en evaluación, ambas construidas sobre el mismo contenido:

- **Blueprint** (`/blueprint/`): plano técnico; la trayectoria dibujada como una ruta de
  integración (Enterprise Integration Patterns).
- **Script** (`/script/`): guion a tres voces (el arquitecto, el constructor, el líder).

La raíz `/` es una página temporal para compararlas. Cuando se elija una, ver
[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md#promover-la-variante-ganadora) para promoverla a `/` y
borrar la otra.

## Despliegue

Vercel está conectado al repo (`AZapata27/portfolio`): cada push a `master` despliega a producción
(https://www.andres-zapata.dev) y cada PR genera una vista previa. La configuración vive en
`vercel.json` y `astro.config.ts` (adaptador `@astrojs/vercel`).

## Cómo agregar o cambiar contenido

Ver [docs/CONTENT.md](docs/CONTENT.md). Resumen:

1. Editar o crear el archivo en `src/content/<colección>/en/` **y** `src/content/<colección>/es/`.
2. `npm run check` valida el esquema; `npm run dev` para verlo.
3. Abrir PR hacia `master`.
