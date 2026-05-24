export const seoSite = {
  name: 'Luca Kosowski',
  canonicalDomain: 'https://lucakosowski.com',
  defaultLanguage: 'en',
  defaultImage: '/profile.jpg',
  description: 'Luca Kosowski portfolio, website-development service, diplomatic project work, articles, references, and multilingual professional background.',
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
    description: 'Professional reference letters for Luca Kosowski.',
    family: 'reference',
    language: 'en',
  },
  {
    path: '/website-development/',
    title: 'Website Development – Luca Kosowski',
    description: 'Website creation service by Luca Kosowski with ready showcase directions, static Astro builds, and simple scope-based delivery for small businesses and professionals.',
    family: 'service',
    language: 'en',
  },
  {
    path: '/website-development/demos/basic/atlas-family-foundation/',
    title: 'Atlas Family Foundation Website Demo – Luca Kosowski',
    description: 'Fictional foundation website demo for the Luca Kosowski website-development portfolio.',
    family: 'demo',
    language: 'en',
    demo: true,
    fictionalDemo: true,
  },
  {
    path: '/website-development/demos/basic/clearpath-commute-analytics/',
    title: 'Clearpath Commute Analytics Website Demo – Luca Kosowski',
    description: 'Fictional analytics website demo for the Luca Kosowski website-development portfolio.',
    family: 'demo',
    language: 'en',
    demo: true,
    fictionalDemo: true,
  },
  {
    path: '/website-development/demos/basic/harbor-legal-translation/',
    title: 'Harbor Legal Translation Website Demo – Luca Kosowski',
    description: 'Fictional legal translation website demo for the Luca Kosowski website-development portfolio.',
    family: 'demo',
    language: 'en',
    demo: true,
    fictionalDemo: true,
  },
  {
    path: '/website-development/demos/basic/mosaic-content-studio/',
    title: 'Mosaic Content Studio Website Demo – Luca Kosowski',
    description: 'Fictional content studio website demo for the Luca Kosowski website-development portfolio.',
    family: 'demo',
    language: 'en',
    demo: true,
    fictionalDemo: true,
  },
  {
    path: '/website-development/demos/basic/verde-lunch-club/',
    title: 'Verde Lunch Club Website Demo – Luca Kosowski',
    description: 'Fictional restaurant website demo for the Luca Kosowski website-development portfolio.',
    family: 'demo',
    language: 'en',
    demo: true,
    fictionalDemo: true,
  },
] as const;
