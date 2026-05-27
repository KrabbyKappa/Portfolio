export const seoSite = {
  name: 'Luca Kosowski',
  canonicalDomain: 'https://lucakosowski.com',
  defaultLanguage: 'en',
  defaultImage: '/profile.jpg',
  description: 'Luca Kosowski portfolio, diplomatic project work, articles, references, multilingual professional background, and related website-development service.',
  goatCounter: 'https://lucakosowski.goatcounter.com/count',
  sameAs: [
    'https://medium.com/@KappaK',
    'https://www.youtube.com/@krabbykappa',
  ],
} as const;

export type RouteFamily = 'portfolio' | 'project' | 'article' | 'reference' | 'service' | 'demo';

export interface SeoRouteRecord {
  path: string;
  title: string;
  description: string;
  family: RouteFamily;
  language: 'en';
  demo?: boolean;
  fictionalDemo?: boolean;
}

export const seoRoutes: SeoRouteRecord[] = [
  {
    path: '/',
    title: 'Luca Kosowski – Digital Marketing, Legal Review & Diplomatic Coordination',
    description: 'Digital and marketing services, legal review, diplomatic coordination, and multilingual stakeholder communication profile for Luca Kosowski, based in Kuala Lumpur.',
    family: 'portfolio',
    language: 'en',
  },
  {
    path: '/projects.html',
    title: 'Projects & Other Projects – Luca Kosowski',
    description: 'Selected diplomatic, cultural, reporting, media, and website-development projects by Luca Kosowski.',
    family: 'project',
    language: 'en',
  },
  {
    path: '/articles.html',
    title: 'Articles – Luca Kosowski',
    description: 'Articles and publications by Luca Kosowski on climate policy, Energy Web writing, technical localization, and youth activism.',
    family: 'article',
    language: 'en',
  },
  {
    path: '/references.html',
    title: 'References – Luca Kosowski',
    description: 'Professional reference letters for Luca Kosowski in English and Italian, with direct PDF access and contact context for recruiters and collaborators.',
    family: 'reference',
    language: 'en',
  },
] as const;
