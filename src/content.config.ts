/**
 * Colecciones de contenido (Astro Content Layer).
 *
 * Todo el contenido editable del portafolio vive en `src/content/`.
 * Las variantes visuales (`src/variants/*`) sólo leen de aquí: cambiar un dato
 * del CV es editar un archivo de contenido, nunca un componente.
 *
 * Convención de idioma: cada colección localizada tiene una carpeta por locale
 * (`en/`, `es/`). El locale se deriva del prefijo del `id` (`en/quind-flypass`).
 */
import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob, file } from 'astro/loaders';

const yearMonth = z
  .string()
  .regex(/^\d{4}-(0[1-9]|1[0-2])$/, 'Usar formato AAAA-MM, p. ej. 2024-03');

const link = z.object({
  label: z.string(),
  url: z.url(),
  /** slug de simple-icons o icono propio (ver `src/components/Icon.astro`) */
  icon: z.string(),
});

/** Perfil: un JSON por idioma (`en.json`, `es.json`). */
const profile = defineCollection({
  loader: glob({ pattern: '*.json', base: './src/content/profile' }),
  schema: z.object({
    name: z.string(),
    shortName: z.string(),
    title: z.string(),
    tagline: z.string(),
    summary: z.string(),
    location: z.string(),
    availability: z.string(),
    email: z.email(),
    /** Ruta pública del CV en PDF de este idioma (p. ej. `/cv/Andres-Zapata-CV-en.pdf`). */
    cv: z.string().startsWith('/'),
    links: z.array(link),
    domains: z.array(z.string()),
    languages: z.array(z.object({ name: z.string(), level: z.string() })),
    /** Cifras comprobables del CV. `value` ya viene formateado para mostrar. */
    metrics: z.array(
      z.object({ value: z.string(), label: z.string(), context: z.string() }),
    ),
    /**
     * Logros clave, en el mismo orden que el CV. `value` es la cifra (−98 %) o una
     * etiqueta corta (IP/REV) para la columna de valor; `title` el nombre del logro.
     */
    achievements: z.array(
      z.object({ value: z.string(), title: z.string(), body: z.string() }),
    ),
    /**
     * Cuatro capacidades. Las usa la variante "blueprint" como ramas de la ruta
     * (la cuarta, liderazgo, es el "control bus").
     */
    capabilities: z.array(
      z.object({
        id: z.enum(['architecture', 'integration', 'ai-native', 'leadership']),
        name: z.string(),
        lead: z.string(),
        body: z.string(),
        parts: z.array(z.string()),
      }),
    ),
    /** Tres voces. Las usa la variante "script" como estructura de guion. */
    voices: z.array(
      z.object({
        id: z.enum(['architect', 'builder', 'leader']),
        name: z.string(),
        tempo: z.string(),
        line: z.string(),
        body: z.string(),
        aside: z.string(),
      }),
    ),
    extras: z.array(z.object({ title: z.string(), body: z.string() })),
  }),
});

/** Experiencia laboral: un Markdown por puesto y por idioma. El cuerpo son los logros. */
const experience = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/experience' }),
  schema: z.object({
    company: z.string(),
    role: z.string(),
    client: z.string().optional(),
    sector: z.string(),
    location: z.string(),
    start: yearMonth,
    /** `null` = puesto actual */
    end: yearMonth.nullable(),
    type: z.enum(['employment', 'contract', 'freelance', 'early']),
    summary: z.string(),
    stack: z.array(z.string()).default([]),
    /** Para desempates al ordenar (menor = primero). */
    order: z.number().int().default(100),
  }),
});

/** Proyectos / casos destacados: un Markdown por caso y por idioma. */
const projects = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/projects' }),
  schema: z.object({
    title: z.string(),
    client: z.string(),
    period: z.string(),
    domain: z.string(),
    role: z.string(),
    summary: z.string(),
    stack: z.array(z.string()).default([]),
    metric: z.object({ value: z.string(), label: z.string() }).optional(),
    featured: z.boolean().default(false),
    order: z.number().int().default(100),
    /** Enlace público si existe (repo, nota de prensa, documentación). */
    url: z.url().optional(),
  }),
});

/** Stack técnico agrupado. Independiente del idioma; las etiquetas de grupo viven en `src/lib/i18n.ts`. */
const skills = defineCollection({
  loader: file('./src/content/skills.json'),
  schema: z.object({
    id: z.string(),
    order: z.number().int(),
    items: z.array(
      z.object({
        name: z.string(),
        /** slug de simple-icons; opcional si no existe logo */
        icon: z.string().optional(),
      }),
    ),
  }),
});

export const collections = { profile, experience, projects, skills };
