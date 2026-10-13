// @ts-check
import { execSync } from 'node:child_process';
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
 *   visual declara cuáles usa con `<Font cssVariable=... />` en su layout. Sólo los
 *   pesos y estilos que se usan: cada archivo extra es una precarga y un relayout en móvil.
 * - `sitemap`: cada URL lleva `lastmod` real (fecha del último commit que tocó su
 *   contenido) y las páginas de proyecto declaran sus alternates es/en, que el
 *   segmento distinto por idioma (`proyectos` / `work`) impide derivar solo.
 */

/** Segmento de las páginas de proyecto por idioma; debe coincidir con `projectSegment` en `src/lib/i18n.ts`. */
const projectSegment = { es: 'proyectos', en: 'work' } as const;

/** Fecha ISO del último commit que tocó las rutas dadas; `undefined` si git no está disponible. */
function lastCommitDate(paths: string[]): Date | undefined {
  try {
    const out = execSync(`git log -1 --format=%cI -- ${paths.map((p) => JSON.stringify(p)).join(' ')}`, {
      encoding: 'utf8',
      stdio: ['ignore', 'pipe', 'ignore'],
    }).trim();
    return out ? new Date(out) : undefined;
  } catch {
    return undefined;
  }
}

/** Clon superficial (Vercel): las fechas por archivo no son fiables, se usa la del commit desplegado. */
const shallow = (() => {
  try {
    return execSync('git rev-parse --is-shallow-repository', { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).trim() === 'true';
  } catch {
    return true;
  }
})();
const deployDate = lastCommitDate([]) ?? new Date();

/** `https://…/proyectos/iprev/` da `{ locale: 'es', slug: 'iprev' }`; otras URL dan `undefined`. */
function projectOf(url: string): { locale: keyof typeof projectSegment; slug: string } | undefined {
  const path = new URL(url).pathname;
  const es = path.match(/^\/proyectos\/([^/]+)\/?$/);
  if (es) return { locale: 'es', slug: es[1]! };
  const en = path.match(/^\/en\/work\/([^/]+)\/?$/);
  if (en) return { locale: 'en', slug: en[1]! };
  return undefined;
}
export default defineConfig({
  site: 'https://www.andres-zapata.dev',
  output: 'static',
  adapter: vercel(),
  build: {
    /* Todo el CSS va en línea en cada HTML: una petición bloqueante menos antes del primer render (LCP en móvil). */
    inlineStylesheets: 'always',
  },
  trailingSlash: 'ignore',
  integrations: [
    sitemap({
      i18n: { defaultLocale: 'es', locales: { es: 'es', en: 'en' } },
      serialize(item) {
        const project = projectOf(item.url);
        const site = new URL(item.url).origin;
        if (project) {
          const content = [`src/content/projects/es/${project.slug}.md`, `src/content/projects/en/${project.slug}.md`];
          item.lastmod = (shallow ? undefined : lastCommitDate(content)) ?? deployDate;
          item.links = [
            { lang: 'es', url: `${site}/${projectSegment.es}/${project.slug}/` },
            { lang: 'en', url: `${site}/en/${projectSegment.en}/${project.slug}/` },
          ];
        } else {
          // Portadas: cambian cuando cambia cualquier contenido o la variante visual
          item.lastmod = (shallow ? undefined : lastCommitDate(['src/content', 'src/variants', 'src/lib'])) ?? deployDate;
        }
        return item;
      },
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
      weights: [700, 800],
      styles: ['normal'],
      subsets: ['latin'],
      fallbacks: ['Arial Narrow', 'sans-serif'],
    },
    {
      provider: fontProviders.fontsource(),
      name: 'Barlow',
      cssVariable: '--font-barlow',
      weights: [400, 500, 600],
      styles: ['normal'],
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
