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
    'nav.experience': 'Experience',
    'nav.work': 'Selected work',
    'nav.stack': 'Stack',
    'nav.contact': 'Contact',
    'section.achievements': 'Key achievements',
    'section.experience': 'Experience',
    'section.work': 'Selected work',
    'section.stack': 'Tech stack',
    'section.contact': 'Contact',
    'section.languages': 'Languages',
    'period.present': 'Present',
    'cta.email': 'Write me',
    'cta.cv': 'Download CV (PDF)',
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
    'meta.title': 'Andrés Zapata · Software architect',
    'meta.description':
      'Software architect with 10+ years in fintech, banking, transport and logistics. Enterprise integration, event streaming with Kafka and AI-native development on Java and Node.js.',
    skip: 'Skip to content',
    'footer.built': 'Built with Astro. Source on GitHub.',
  },
  es: {
    'nav.route': 'Ruta',
    'nav.voices': 'Voces',
    'nav.experience': 'Experiencia',
    'nav.work': 'Proyectos',
    'nav.stack': 'Stack',
    'nav.contact': 'Contacto',
    'section.achievements': 'Logros',
    'section.experience': 'Experiencia',
    'section.work': 'Proyectos destacados',
    'section.stack': 'Stack tecnológico',
    'section.contact': 'Contacto',
    'section.languages': 'Idiomas',
    'period.present': 'Actual',
    'cta.email': 'Escribime',
    'cta.cv': 'Descargar CV (PDF)',
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
