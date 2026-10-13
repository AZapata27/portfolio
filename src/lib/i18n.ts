/**
 * Idiomas y textos de interfaz.
 *
 * El contenido largo (perfil, experiencia, proyectos) vive en `src/content/`.
 * Aquí sólo van etiquetas cortas de UI que no cambian con el CV.
 */
export const locales = ['es', 'en'] as const;
export type Locale = (typeof locales)[number];
/** Español en la raíz (`/`); inglés bajo `/en/`. Debe coincidir con `i18n` en astro.config.ts. */
export const defaultLocale: Locale = 'es';

export const ui = {
  en: {
    'nav.route': 'Route',
    'nav.voices': 'Voices',
    'nav.experience': 'Career',
    'nav.work': 'Projects',
    'nav.stack': 'Stack',
    'nav.contact': 'Contact',
    'nav.cv': 'CV',
    'section.achievements': 'Key achievements',
    'section.experience': 'Career path',
    'section.work': 'Projects',
    'section.stack': 'Tech stack',
    'section.contact': 'Contact',
    'section.languages': 'Languages',
    'period.present': 'Present',
    'cta.email': 'Write me',
    'cta.cv': 'Download CV (PDF)',
    'cta.cvWeb': 'Web résumé',
    'cv.title': 'Résumé',
    'cv.summary': 'Profile',
    'cv.experience': 'Experience',
    'cv.extras': 'Also',
    'cv.print': 'Print or save as PDF',
    'cv.pdf': 'Download PDF',
    'cv.updated': 'Updated',
    'cta.linkedin': 'LinkedIn',
    'cta.github': 'GitHub',
    'lang.switch': 'Leer en español',
    'lang.current': 'English',
    'skills.languages': 'Languages',
    'skills.backend': 'Backend',
    'skills.frontend': 'Frontend',
    'skills.data': 'Data & events',
    'skills.cloud': 'Cloud & DevOps',
    'skills.observability': 'Observability',
    'skills.quality': 'Quality',
    'skills.architecture': 'Architecture',
    'skills.ai': 'AI engineering',
    'type.employment': 'Employee',
    'type.contract': 'Contractor',
    'type.freelance': 'Freelance',
    'type.early': 'Early career',
    'work.back': 'All projects',
    'work.prev': 'Previous',
    'work.next': 'Next',
    'work.open': 'View project',
    'work.notes': 'Notes',
    'work.site': 'Visit the site',
    'work.captureOf': 'Capture of',
    'work.schematic': 'Architecture sketch',
    'work.count': 'projects',
    'meta.title': 'Andrés Zapata · Software architect',
    'meta.description':
      'Software architect with 10+ years in fintech, banking, transport and logistics. Enterprise integration, event streaming with Kafka and AI-native development on Java and Node.js.',
    skip: 'Skip to content',
    'footer.built': 'Built with Astro. Source on GitHub.',
  },
  es: {
    'nav.route': 'Ruta',
    'nav.voices': 'Voces',
    'nav.experience': 'Trayectoria',
    'nav.work': 'Proyectos',
    'nav.stack': 'Stack',
    'nav.contact': 'Contacto',
    'nav.cv': 'CV',
    'section.achievements': 'Logros',
    'section.experience': 'Trayectoria',
    'section.work': 'Proyectos',
    'section.stack': 'Stack tecnológico',
    'section.contact': 'Contacto',
    'section.languages': 'Idiomas',
    'period.present': 'Actual',
    'cta.email': 'Escribime',
    'cta.cv': 'Descargar CV (PDF)',
    'cta.cvWeb': 'CV en la web',
    'cv.title': 'Hoja de vida',
    'cv.summary': 'Perfil',
    'cv.experience': 'Experiencia',
    'cv.extras': 'Además',
    'cv.print': 'Imprimir o guardar como PDF',
    'cv.pdf': 'Descargar PDF',
    'cv.updated': 'Actualizado',
    'cta.linkedin': 'LinkedIn',
    'cta.github': 'GitHub',
    'lang.switch': 'Read in English',
    'lang.current': 'Español',
    'skills.languages': 'Lenguajes',
    'skills.backend': 'Backend',
    'skills.frontend': 'Frontend',
    'skills.data': 'Datos y eventos',
    'skills.cloud': 'Cloud y DevOps',
    'skills.observability': 'Observabilidad',
    'skills.quality': 'Calidad',
    'skills.architecture': 'Arquitectura',
    'skills.ai': 'Ingeniería de IA',
    'type.employment': 'Empleado',
    'type.contract': 'Contratista',
    'type.freelance': 'Freelance',
    'type.early': 'Primeros años',
    'work.back': 'Todos los proyectos',
    'work.prev': 'Anterior',
    'work.next': 'Siguiente',
    'work.open': 'Ver proyecto',
    'work.notes': 'Notas',
    'work.site': 'Ver el sitio',
    'work.captureOf': 'Captura de',
    'work.schematic': 'Esquema de arquitectura',
    'work.count': 'proyectos',
    'meta.title': 'Andrés Zapata · Arquitecto de software',
    'meta.description':
      'Arquitecto de software con más de 10 años en fintech, banca, transporte y logística. Integración empresarial, event streaming con Kafka y desarrollo AI-native sobre Java y Node.js.',
    skip: 'Saltar al contenido',
    'footer.built': 'Hecho con Astro. Código en GitHub.',
  },
} as const satisfies Record<Locale, Record<string, string>>;

export type UiKey = keyof (typeof ui)['en'];

export function t(locale: Locale) {
  return (key: UiKey): string => ui[locale][key] ?? ui.en[key] ?? key;
}

export function isLocale(value: string | undefined): value is Locale {
  return locales.includes(value as Locale);
}

/** Locale de una entrada de colección a partir de su id (`en/...`, `es/...`, `en`, `es`). */
export function localeOf(id: string): Locale {
  const prefix = id.split('/')[0];
  return isLocale(prefix) ? prefix : defaultLocale;
}

/** Ruta localizada: `localePath('en', '/')` da `/en/`; `localePath('es', '/')` da `/`. */
export function localePath(locale: Locale, path = '/'): string {
  const clean = path.replace(/^\/+|\/+$/g, '');
  const prefix = locale === defaultLocale ? '' : `/${locale}`;
  const url = `${prefix}/${clean}`.replace(/\/+/g, '/');
  return url.endsWith('/') ? url : `${url}/`;
}

/**
 * Enlace a la portada de un idioma. En español lleva `?lang=es` porque Vercel redirige `/` a `/en/`
 * cuando el navegador prefiere inglés (`vercel.json`): el parámetro es la salida explícita de esa
 * redirección, así el conmutador y los enlaces de vuelta desde otras páginas respetan la elección.
 * Dentro de la propia portada se usan anclas (`#work`), nunca este enlace.
 */
export function homePath(locale: Locale): string {
  return locale === defaultLocale ? '/?lang=es' : localePath(locale, '/');
}

/** Segmento de la ruta de proyectos por idioma: `/proyectos/<slug>/` y `/en/work/<slug>/`. */
export const projectSegment: Record<Locale, string> = { es: 'proyectos', en: 'work' };

/** Ruta de la página de detalle de un proyecto en un idioma. */
export function projectPath(locale: Locale, slug: string): string {
  return localePath(locale, `${projectSegment[locale]}/${slug}`);
}

/** Idioma alterno para el conmutador. */
export function otherLocale(locale: Locale): Locale {
  return locale === 'en' ? 'es' : 'en';
}

const monthNames: Record<Locale, string[]> = {
  en: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
  es: ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'],
};

/** `2024-03` da `Mar 2024` (en) o `mar 2024` (es). */
export function formatYearMonth(value: string, locale: Locale): string {
  const [y, m] = value.split('-').map(Number);
  return `${monthNames[locale][(m ?? 1) - 1]} ${y}`;
}

/** `2024-03`, `null` da `Mar 2024 – Present`. */
export function formatPeriod(start: string, end: string | null, locale: Locale): string {
  const to = end ? formatYearMonth(end, locale) : t(locale)('period.present');
  return `${formatYearMonth(start, locale)} – ${to}`;
}

/** Duración legible: `2021-02`..`2023-07` da `2 yr 5 mo` (en) o `2 a 5 m` (es). */
export function formatDuration(
  start: string,
  end: string | null,
  locale: Locale,
  now = new Date(),
): string {
  const [sy, sm] = start.split('-').map(Number);
  const [ey, em] = end ? end.split('-').map(Number) : [now.getFullYear(), now.getMonth() + 1];
  const months = Math.max(1, (ey! - sy!) * 12 + (em! - sm!) + 1);
  const y = Math.floor(months / 12);
  const m = months % 12;
  const yl = locale === 'es' ? 'a' : 'yr';
  const ml = locale === 'es' ? 'm' : 'mo';
  return [y ? `${y} ${yl}` : '', m ? `${m} ${ml}` : ''].filter(Boolean).join(' ');
}
