/**
 * Vocabulario del plano: rótulos fijos de una hoja de dibujo técnico (bloque de
 * título, revisiones, lista de partes, detalles) y etiquetas del diagrama.
 *
 * No son textos del CV (esos viven en `src/content/`) ni claves compartidas entre
 * variantes (esas viven en `src/lib/i18n.ts`): son palabras propias de este mundo
 * visual, por eso se quedan dentro de la variante.
 */
import type { Locale } from '@/lib/i18n';

const vocab = {
  en: {
    // Juego de hojas
    sheet: 'Sheet',
    drawing: 'Drawing',
    route: 'Route',
    notes: 'Capabilities',
    revisions: 'Revisions',
    details: 'Details',
    detail: 'Detail',
    partsList: 'Tech stack',
    titleBlock: 'Title block',
    achievement: 'Achievement',
    generalNotes: 'General notes',
    primaryNav: 'Sheets of the drawing set',
    // Diagrama de la ruta
    inbound: 'inbound',
    yourProblem: 'your problem',
    routerLine1: 'content-based',
    routerLine2: 'router',
    aggregator: 'aggregator',
    outbound: 'outbound',
    production: 'production',
    prod: 'PROD',
    routeDiagram:
      'Integration route: your problem comes in through a channel, a content-based router sends it to architecture, integration or AI-native development, an aggregator joins the branches and production receives the result. Leadership runs alongside as the control bus.',
    // Bloque de título
    role: 'Role',
    experience: 'Experience',
    domains: 'Domains',
    scope: 'Scope',
    location: 'Location',
    contact: 'Contact',
    links: 'Links',
    availability: 'Availability',
    cv: 'CV',
    // Tablas
    rev: 'Rev',
    date: 'Date',
    description: 'Description',
    item: 'Item',
    group: 'Group',
    parts: 'Parts',
    value: 'Value',
    client: 'Client',
    period: 'Period',
    domain: 'Domain',
    stack: 'Stack',
    domainKnowledge: 'Domain knowledge',
    openLink: 'Open link',
    current: 'Current',
  },
  es: {
    sheet: 'Hoja',
    drawing: 'Plano',
    route: 'Ruta',
    notes: 'Capacidades',
    revisions: 'Revisiones',
    details: 'Detalles',
    detail: 'Detalle',
    partsList: 'Stack tecnológico',
    titleBlock: 'Bloque de título',
    achievement: 'Logro',
    generalNotes: 'Notas generales',
    primaryNav: 'Hojas del plano',
    inbound: 'entrada',
    yourProblem: 'tu problema',
    routerLine1: 'enrutador por',
    routerLine2: 'contenido',
    aggregator: 'agregador',
    outbound: 'salida',
    production: 'producción',
    prod: 'PROD',
    routeDiagram:
      'Ruta de integración: tu problema entra por un canal, un enrutador por contenido lo manda a arquitectura, integración o desarrollo AI-native, un agregador junta las ramas y producción recibe el resultado. El liderazgo corre al lado como control bus.',
    role: 'Rol',
    experience: 'Experiencia',
    domains: 'Dominios',
    scope: 'Alcance',
    location: 'Ubicación',
    contact: 'Contacto',
    links: 'Enlaces',
    availability: 'Disponibilidad',
    cv: 'CV',
    rev: 'Rev',
    date: 'Fecha',
    description: 'Descripción',
    item: 'Ítem',
    group: 'Grupo',
    parts: 'Partes',
    value: 'Valor',
    client: 'Cliente',
    period: 'Periodo',
    domain: 'Dominio',
    stack: 'Stack',
    domainKnowledge: 'Conocimiento de dominio',
    openLink: 'Abrir enlace',
    current: 'Actual',
  },
} as const satisfies Record<Locale, Record<string, string>>;

export type Vocab = { readonly [K in keyof (typeof vocab)['en']]: string };

export function vocabFor(locale: Locale): Vocab {
  return vocab[locale] ?? vocab.en;
}

/** `Andrés Zapata` da `andres-zapata`; sirve para el nombre del plano y los ids. */
export function slugify(value: string): string {
  return value
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

/** Nombre del plano que aparece en el bloque de título y en el sello de cada hoja. */
export function drawingNameOf(shortName: string): string {
  return `${slugify(shortName)}.route`;
}

/** `7` da `07`: numeración de revisiones e ítems con dos dígitos. */
export function pad2(n: number): string {
  return String(n).padStart(2, '0');
}

/** Orden fijo de las capacidades en la ruta: tres ramas y el control bus al final. */
export const capabilityOrder = ['architecture', 'integration', 'ai-native', 'leadership'] as const;
