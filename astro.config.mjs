import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

const site = 'https://lucakosowski.com';
const canonicalSitemapPages = [
  `${site}/`,
  `${site}/projects.html`,
  `${site}/articles.html`,
  `${site}/references.html`,
  `${site}/website-development/`,
];

export default defineConfig({
  site,
  outDir: './docs',
  output: 'static',
  compressHTML: false,
  build: {
    format: 'preserve',
  },
  integrations: [
    sitemap({
      customPages: canonicalSitemapPages,
      filter: (page) => canonicalSitemapPages.includes(page),
    }),
  ],
});
