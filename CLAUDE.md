# CLAUDE.md

Las reglas de trabajo para agentes están en [AGENTS.md](AGENTS.md); el contexto de producto en
[PRODUCT.md](PRODUCT.md); la arquitectura en [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).
Leé esos tres antes de cambiar algo.

Resumen operativo:

- Contenido en `src/content/` (en y es); diseño en `src/variants/<variante>/`. Nunca mezclar.
- Verificar con `npm run check` y `npm run build` antes de proponer un PR. Nunca commitear en `master`.
- Servidor de desarrollo: `npx astro dev --background` (puerto 4321); `npx astro dev stop` para apagarlo.
- Capturas: `npx playwright screenshot --viewport-size=1440,900 --full-page <url> <png>`.
- Documentación de Astro 7: https://docs.astro.build (rutas, colecciones, i18n, fuentes).
