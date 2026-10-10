/**
 * Acceso tipado al contenido, ya filtrado por idioma y ordenado.
 * Las variantes visuales importan sólo de aquí.
 */
import { getCollection, getEntry, type CollectionEntry } from 'astro:content';
import { localeOf, type Locale } from './i18n';

export type Profile = CollectionEntry<'profile'>['data'];
export type Experience = CollectionEntry<'experience'>;
export type Project = CollectionEntry<'projects'>;
export type SkillGroup = CollectionEntry<'skills'>['data'];

export async function getProfile(locale: Locale): Promise<Profile> {
  const entry = await getEntry('profile', locale);
  if (!entry) throw new Error(`Falta src/content/profile/${locale}.json`);
  return entry.data;
}

/** Experiencia del idioma, más reciente primero (los puestos actuales arriba). */
export async function getExperience(locale: Locale): Promise<Experience[]> {
  const entries = await getCollection('experience', ({ id }) => localeOf(id) === locale);
  return entries.sort((a, b) => {
    const aCurrent = a.data.end === null ? 1 : 0;
    const bCurrent = b.data.end === null ? 1 : 0;
    if (aCurrent !== bCurrent) return bCurrent - aCurrent;
    if (a.data.start !== b.data.start) return b.data.start.localeCompare(a.data.start);
    return a.data.order - b.data.order;
  });
}

/** Proyectos del idioma: destacados primero, luego por `order`. */
export async function getProjects(locale: Locale): Promise<Project[]> {
  const entries = await getCollection('projects', ({ id }) => localeOf(id) === locale);
  return entries.sort((a, b) => {
    if (a.data.featured !== b.data.featured) return a.data.featured ? -1 : 1;
    return a.data.order - b.data.order;
  });
}

export async function getSkills(): Promise<SkillGroup[]> {
  const entries = await getCollection('skills');
  return entries.map((e) => e.data).sort((a, b) => a.order - b.order);
}

/** Identificador estable sin el prefijo de idioma (`en/quind-flypass` da `quind-flypass`). */
export function slugOf(entry: { id: string }): string {
  return entry.id.split('/').slice(1).join('/') || entry.id;
}
