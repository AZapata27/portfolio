// @ts-check
import { defineConfig, fontProviders } from 'astro/config';
import vercel from '@astrojs/vercel';
import sitemap from '@astrojs/sitemap';

/**
 * Configuración de Astro.
 *
 * - `site`: URL canónica (se usa para sitemap, canonical y Open Graph).
 * - `i18n`: español sin prefijo (`/`), inglés bajo `/en/`.
 * - `adapter`: Vercel. El sitio es estático; el adaptador queda listo para
 *   rutas on-demand (p. ej. `src/pages/api/*.ts` con `export const prerender = false`).
 * - `fonts`: tipografías autoalojadas en build (Astro Fonts API). Cada variante
 *   visual declara cuáles usa con `<Font cssVariable=... />` en su layout.
 */
export default defineConfig({
  site: 'https://www.andres-zapata.dev',
  output: 'static',
  adapter: vercel(),
  trailingSlash: 'ignore',
  integrations: [
    sitemap({
      i18n: { defaultLocale: 'es', locales: { es: 'es', en: 'en' } },
    }),
  ],
  i18n: {
    defaultLocale: 'es',
    locales: ['es', 'en'],
    routing: { prefixDefaultLocale: false },
  },
  fonts: [
    // Plano técnico (variante "blueprint"): display, cuerpo y mono
    {
      provider: fontProviders.fontsource(),
      name: 'Barlow Condensed',
      cssVariable: '--font-barlow-condensed',
      weights: [600, 700, 800],
      styles: ['normal'],
      subsets: ['latin'],
      fallbacks: ['Arial Narrow', 'sans-serif'],
    },
    {
      provider: fontProviders.fontsource(),
      name: 'Barlow',
      cssVariable: '--font-barlow',
      weights: [400, 500, 600],
      styles: ['normal', 'italic'],
      subsets: ['latin'],
      fallbacks: ['Arial', 'sans-serif'],
    },
    {
      provider: fontProviders.fontsource(),
      name: 'JetBrains Mono',
      cssVariable: '--font-jetbrains-mono',
      weights: [400, 500, 700],
      styles: ['normal'],
      subsets: ['latin'],
      fallbacks: ['Consolas', 'monospace'],
    },
  ],
});
