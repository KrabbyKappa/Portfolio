import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://lucakosowski.com',
  output: 'static',
  compressHTML: false,
  build: {
    format: 'preserve',
  },
});
