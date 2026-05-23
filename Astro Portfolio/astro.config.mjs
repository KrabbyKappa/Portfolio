import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://lucakosowski.com',
  outDir: './docs',
  output: 'static',
  compressHTML: false,
  build: {
    format: 'preserve',
  },
});
