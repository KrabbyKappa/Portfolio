---
type: reference
description: Full-source evidence map and implementation analysis for the 15 external website references
last_updated: 2026-05-20
tags: [reference, templates, source-code-analysis, design-research]
source: external live website homepage HTML, CSS, and JavaScript downloaded 2026-05-20
related_files:
  - external-references/scrape_reference_assets.py
  - external-references/website-template-full-source/2026-05-20/manifest.json
  - external-references/website-template-full-source/2026-05-20/README.md
  - wiki/reference/external-website-template-library-2026-05-20.md
related:
  - reference/external-website-template-library-2026-05-20
  - business/website-spec-micro
  - business/website-spec-basic
  - business/website-spec-medium
  - business/website-spec-complex
---

# External Website Source Code Analysis

Back: [[reference/external-website-template-library-2026-05-20]]  
Governance: [[MOC/MOC-Reference]] · [[MOC/MOC-Graph]]

This page explains how the 15 reference pages are built from their downloaded homepage HTML, CSS, JavaScript, inline style blocks, inline script blocks, and dependency manifests.

Important boundary: the raw third-party code is stored as local evidence under `external-references/website-template-full-source/2026-05-20/`. Do not paste or clone that third-party source into client projects. Use it to understand architecture, section logic, dependency choices, animation patterns, and maintenance tradeoffs. Build original code for our own sites.

## Evidence Boundary

| Field | Status |
|-------|--------|
| Download date | 2026-05-20 |
| Source list | [[reference/external-website-template-library-2026-05-20]] |
| Scraper | `external-references/scrape_reference_assets.py` |
| Full manifest | `external-references/website-template-full-source/2026-05-20/manifest.json` |
| Summary README | `external-references/website-template-full-source/2026-05-20/README.md` |
| Download scope | Homepage HTML, linked CSS, linked JavaScript, modulepreload JavaScript, inline `<style>`, inline `<script>`, and inline `style` attributes. |
| Out of scope | Full-site crawling, images, video files, font binaries, backend APIs, private source repositories, and client-side runtime screenshots. |
| Result | 15 homepages attempted, 15 homepages saved, 239 linked CSS/JS/modulepreload assets discovered, 238 saved, 1 failed CDN asset. |
| Failed asset | `https://cdn.jsdelivr.net/gh/Flowappz/cookie-consent-cdn@v1.1.15/cookie-consent.js` returned 404 for Adam Mirek. |
| Reuse rule | Study the implementation ideas. Rebuild with original markup, styles, copy, media, and assets. |

## Evidence Folder Contract

Each reference site has the same local evidence layout:

```text
external-references/website-template-full-source/2026-05-20/{site}/
  raw/homepage.html
  raw/headers.json
  assets/css/*.css
  assets/js/*.js
  inline/style-*.css
  inline/script-*.js
  inline/script-*.json
  inline/style-attributes.css
  manifest.json
  README.md
```

The global manifest is the source of truth for counts, source URLs, resolved URLs, saved local paths, content types, byte sizes, hashes, CSS URL dependencies, page headings, and detected technology hints.

## Scraper Code

The scraper is intentionally small and repeatable. Its job is not to mirror whole websites; its job is to capture the homepage implementation surface we need for design research.

### What It Does

1. Defines the 15 reference URLs with stable slugs and template roles.
2. Fetches each homepage with a research user agent.
3. Saves the exact HTML response as `raw/homepage.html`.
4. Saves response headers as `raw/headers.json`.
5. Parses the HTML with BeautifulSoup.
6. Downloads linked stylesheets.
7. Downloads linked script files and modulepreload chunks.
8. Extracts inline `<style>` blocks into standalone CSS files.
9. Extracts inline `<script>` blocks into standalone JS or JSON files.
10. Collects inline `style=""` attributes into `inline/style-attributes.css`.
11. Extracts CSS `url(...)` and `@import` references for dependency analysis.
12. Writes per-site `manifest.json` and `README.md`.
13. Writes a global `manifest.json` and `README.md`.

### How It Works

The important flow is:

```text
SITES -> scrape_site()
  -> request_url()
  -> write raw homepage and headers
  -> BeautifulSoup parse
  -> page_summary()
  -> save_inline_blocks()
  -> collect <link rel=stylesheet>, <link rel=modulepreload>, <script src>
  -> download_asset()
  -> detect_tech()
  -> write per-site manifest and README
```

The scraper keeps every saved asset traceable back to a source URL and a local file. That traceability matters because the analysis should be evidence-backed, not based on a visual impression.

### Why This Shape

- Stable slugs make future comparisons easy.
- Raw HTML is saved before parsing so we can re-inspect exact source.
- CSS and JS are separated into their own folders because those layers answer different questions.
- Inline blocks are saved separately because page builders often inject the real page-specific behavior inline.
- Manifest hashes make it possible to detect changed assets later.
- The scraper does not crawl full sites because the reference task is homepage pattern research, not archival mirroring.

## Aggregate Findings

| Metric | Count |
|--------|------:|
| Homepages saved | 15 |
| Linked CSS assets | 64 |
| Linked script assets | 160 |
| Modulepreload JS assets | 15 |
| Linked assets discovered | 239 |
| Linked assets saved | 238 |
| Linked assets failed | 1 |
| Total evidence size | 35 MB |
| Total evidence files | 639 |

The main lesson is that polished reference pages are usually simple content systems plus a heavy presentation layer. HTML provides crawlable structure, CSS creates most of the visual identity, and JavaScript is mostly used for motion, sliders, forms, analytics, cookie/email protection, or framework hydration.

## Site Code Inventory

| Site | HTML size | Elements | Linked assets | Inline CSS/JS | Detected implementation hints |
|------|----------:|---------:|--------------:|--------------:|-------------------------------|
| Rumbeke Platse | 984 KB | 3095 | 38 saved, 0 failed | 17 / 18 | WordPress, Elementor, GSAP, Site Kit, cookie/email protection |
| PIV Group | 251 KB | 409 | 3 saved, 0 failed | 1 / 5 | Mostly static HTML, small custom JS, one form |
| Omar Al Khatib | 38 KB | 324 | 21 saved, 0 failed | 0 / 1 | Bootstrap, jQuery, Owl, Fancybox, Isotope, portfolio scripts |
| My Commuters | 13 KB | 218 | 14 saved, 0 failed | 0 / 1 | GSAP, ScrollTrigger, ScrollSmoother, Swiper, Alpine |
| Shreejal | 27 KB | 220 | 5 saved, 0 failed | 0 / 2 | Webflow hints, GSAP, ScrollTrigger |
| Adam Mirek | 279 KB | 1561 | 11 saved, 1 failed | 2 / 9 | Webflow, Rive, CMS load, Isotope, image loading |
| St Louis Vending | 65 KB | 280 | 22 saved, 0 failed | 1 / 2 | Next.js chunks, form, static lead-gen flow |
| Dolsten | 224 KB | 1347 | 17 saved, 0 failed | 14 / 23 | Webflow, GSAP, ScrollTrigger, SplitText, Lenis, Swiper, HLS video |
| Brewitty | 167 KB | 259 | 12 saved, 0 failed | 0 / 2 | GSAP, ScrollTrigger, SplitText, Lottie, Lenis, email script |
| Extinction Map | 6906 KB | 26474 | 10 saved, 0 failed | 9 / 2 | Large inline data/DOM, GSAP, jQuery, custom species/map scripts |
| Teh Tarik Nation | 180 KB | 539 | 10 saved, 0 failed | 2 / 1 | WordPress hints, GSAP, MotionPath, ScrollTo, Lenis |
| BlueYard | 324 KB | 1827 | 18 saved, 0 failed | 11 / 3 | Nuxt/Vue, modulepreload chunks, Sanity config |
| Grumpy Frenchie | 11 KB | 128 | 6 saved, 0 failed | 0 / 2 | Vite app bundle, external loader, compact teaser page |
| Fundacion Alcaraz | 84 KB | 372 | 19 saved, 0 failed | 4 / 8 | WordPress, WPML, GSAP, Lottie, SplitText, Slick |
| Animal Free Circus | 2243 KB | 2091 | 32 saved, 0 failed | 88 / 97 | Tilda, longform page-builder blocks, lazyload, popup, zoom, galleries |

## Architecture Families

### Builder-Heavy WordPress Pages

Examples: Rumbeke Platse, Teh Tarik Nation, Fundacion Alcaraz.

How they work:

- Server-rendered HTML contains most visible content.
- WordPress and page-builder plugins emit many CSS files and runtime scripts.
- Page-specific layout is often expressed through generated classes and inline styles.
- Motion is added with GSAP or plugin scripts.
- Forms, cookies, language switching, and tracking are handled by plugins.

Why it works:

- Content is present in HTML, so the page can be crawled.
- Non-technical owners can update content through a builder.
- The tradeoff is asset weight, plugin coupling, and harder design-system reuse.

Use for our work:

- Borrow the content completeness and section order.
- Do not borrow builder class soup.
- Rebuild as typed Astro data and component templates when we control the code.

### Webflow And Motion Studio Pages

Examples: Dolsten, Shreejal, Adam Mirek.

How they work:

- HTML is exported or served with Webflow-style classes.
- A generated Webflow runtime coordinates interactions.
- GSAP, ScrollTrigger, SplitText, Lenis, Swiper, HLS, Rive, and image-loading utilities add craft.
- Case studies, awards, and personal proof are mostly static content with animated entrance and scroll behavior.

Why it works:

- Strong visual craft matches the offer.
- Motion reinforces agency or portfolio credibility.
- The risk is heavy JavaScript and fragile layout if copied without QA.

Use for our work:

- Use motion only when it proves the client's craft or product.
- Keep animation declarations close to components.
- Build no-motion fallbacks and verify mobile screenshots.

### App-Bundle Landing Pages

Examples: St Louis Vending, BlueYard, Grumpy Frenchie.

How they work:

- HTML contains a compact rendered shell.
- Framework chunks hydrate the page.
- CSS is hashed and scoped through the build system.
- BlueYard uses Nuxt/Vue with modulepreload chunks and a Sanity public config.
- St Louis Vending uses Next.js static chunks.
- Grumpy Frenchie uses a Vite bundle.

Why it works:

- Framework pipelines help teams ship reusable components.
- Asset hashes support cache stability.
- The tradeoff is that simple pages can load more JS than they need.

Use for our work:

- Use Astro islands or plain JS for simple marketing pages.
- Reserve heavier hydration for real interactive state.
- Keep the first viewport meaningful without waiting for client JS.

### Lightweight Static And Library Pages

Examples: PIV Group, Omar Al Khatib, My Commuters, Brewitty.

How they work:

- HTML is mostly static and direct.
- CSS supplies the brand system.
- JavaScript libraries add targeted behavior: carousel, filter grid, contact validation, smooth scroll, reveal animation, and email handling.
- Omar uses older jQuery-era plugins; My Commuters and Brewitty use modern motion libraries.

Why it works:

- The page can be understood as content first.
- Interaction is focused and localized.
- The risk is accumulating libraries for small effects.

Use for our work:

- Prefer one tiny custom script over multiple plugins when the behavior is simple.
- Keep forms, anchor navigation, and pricing visible without animation.
- Use structured arrays for repeated services, portfolio rows, pricing tiers, and proof metrics.

### Longform Interactive Advocacy

Examples: Extinction Map, Animal Free Circus.

How they work:

- The page itself is the experience.
- Large DOM or inline content blocks carry chapters, map states, or story sections.
- JavaScript orchestrates scroll, reveal, chapter transitions, popups, galleries, and data-driven text.
- The source payload is much larger than a normal marketing site.

Why it works:

- Complex topics become inspectable through interaction and chapters.
- The page can educate before asking for action.
- The tradeoff is performance, accessibility, and maintenance burden.

Use for our work:

- Treat this as a complex-package pattern only.
- Split data from presentation.
- Provide a non-JS fallback for core claims and sources.
- Test keyboard, mobile, and reduced-motion behavior.

## Layer Lessons

### HTML

Good reference pages use HTML as the content contract. The headings, links, forms, image references, and section order explain the business before CSS or JS runs.

Build rule:

- Put real content in source HTML.
- Use semantic landmarks and stable section IDs.
- Make primary CTAs and contact routes visible without JavaScript.
- Keep repeated content data-driven so menus, proof metrics, portfolio rows, and program cards do not become copy-paste markup.

### CSS

The visual system lives mostly in CSS: type scale, spacing, color, sticky headers, responsive grids, marquee/ticker effects, card density, art direction, and mobile behavior.

Build rule:

- Define tokens for color, spacing, type, radius, and layout width.
- Use components for repeated section shells.
- Keep one-off art direction isolated to the section that needs it.
- Avoid page-builder generated classes in our own source.

### JavaScript

The reference JavaScript falls into five groups:

1. Platform runtimes: WordPress plugins, Elementor, Webflow, Tilda, Next.js, Nuxt, Vite.
2. Motion libraries: GSAP, ScrollTrigger, ScrollSmoother, SplitText, Lenis, MotionPath.
3. UI utilities: Swiper, Slick, Owl, Fancybox, Isotope, Packery, Lottie, Rive, HLS.
4. Form and compliance helpers: validators, cookie scripts, language cookies, email decoding.
5. Site-specific scripts: map/species text, menu motion, portfolio filters, contact handling.

Build rule:

- Add JavaScript only for behavior the page truly needs.
- Keep content and navigation functional before enhancement.
- Use one animation pattern across the page instead of mixing several unrelated effects.
- Respect `prefers-reduced-motion`.

## Original Reusable Code Patterns

These snippets are original implementation patterns inspired by the reference structure. They are not copied from the downloaded sites.

### Data-Driven Section Contract

```ts
export type SectionKind =
  | "hero"
  | "utilityStatus"
  | "anchorNav"
  | "founderStory"
  | "proofMetrics"
  | "serviceCards"
  | "portfolioRows"
  | "menuCatalog"
  | "caseStudyGrid"
  | "dataExplorer"
  | "manifestoBlock"
  | "programPillars"
  | "downloadCards"
  | "reviews"
  | "faq"
  | "contactCta"
  | "operationsFooter"
  | "legalFooter";

export interface PageSection<T = unknown> {
  id: string;
  kind: SectionKind;
  heading?: string;
  intro?: string;
  data: T;
}
```

Why: it lets us copy the useful structure of reference pages without copying their HTML or CSS. Every package tier can choose the smallest section set that fits the client.

### Local Business Status Strip

```astro
---
interface Props {
  label: string;
  status: "open" | "closed" | "limited";
  detail: string;
}

const { label, status, detail } = Astro.props;
---

<aside class={`status-strip is-${status}`} aria-label={label}>
  <span class="status-dot" aria-hidden="true"></span>
  <strong>{label}</strong>
  <span>{detail}</span>
</aside>
```

Why: local business references work well when practical facts appear before decorative brand copy.

### Responsive Menu Catalog

```astro
---
interface MenuItem {
  name: string;
  description?: string;
  price?: string;
}

interface MenuGroup {
  title: string;
  items: MenuItem[];
}

const { groups } = Astro.props as { groups: MenuGroup[] };
---

<section class="menu-catalog" id="menu">
  {groups.map((group) => (
    <article class="menu-group">
      <h3>{group.title}</h3>
      <ul>
        {group.items.map((item) => (
          <li>
            <span>
              <strong>{item.name}</strong>
              {item.description && <small>{item.description}</small>}
            </span>
            {item.price && <data value={item.price}>{item.price}</data>}
          </li>
        ))}
      </ul>
    </article>
  ))}
</section>
```

Why: Rumbeke Platse and Teh Tarik Nation show that menu content should be first-class page content, not only a PDF.

### Minimal Reveal Enhancement

```js
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (!reduceMotion) {
  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    }
  }, { threshold: 0.2 });

  document.querySelectorAll("[data-reveal]").forEach((element) => {
    observer.observe(element);
  });
}
```

Why: many references use GSAP-level motion. For most client pages, this smaller pattern gives polish without the maintenance cost of a full animation stack.

### Proof Row Component

```astro
---
interface ProofItem {
  label: string;
  value: string;
  context: string;
}

const { items } = Astro.props as { items: ProofItem[] };
---

<section class="proof-rows" aria-labelledby="proof-heading">
  <h2 id="proof-heading">Proof</h2>
  <ol>
    {items.map((item) => (
      <li>
        <span class="proof-value">{item.value}</span>
        <strong>{item.label}</strong>
        <p>{item.context}</p>
      </li>
    ))}
  </ol>
</section>
```

Why: Shreejal, Brewitty, Dolsten, and BlueYard prove that dense rows are often better than decorative cards when evidence is the product.

### Data Explorer Skeleton

```ts
export interface ExplorerRecord {
  id: string;
  label: string;
  group: string;
  summary: string;
  coordinates?: [number, number];
  sources: Array<{ label: string; url: string }>;
}

export function filterExplorerRecords(records: ExplorerRecord[], group: string) {
  if (group === "all") return records;
  return records.filter((record) => record.group === group);
}
```

Why: Extinction Map demonstrates that interactive pages should split data from rendering. The data contract has to be testable before map or scroll effects are added.

## Package Guidance

| Package | Source-code stance |
|---------|--------------------|
| [[business/website-spec-micro]] | Static HTML, one CSS file, minimal or no JS. Use Grumpy Frenchie and St Louis Vending for structure, not their app bundles. |
| [[business/website-spec-basic]] | Data-driven sections, contact CTA, lightweight reveal script if needed. Avoid WordPress/Webflow-level runtime weight. |
| [[business/website-spec-medium]] | Reusable Astro components, content data files, proof sections, portfolio/menu/program lists, optional localized routing. Use one motion library only if it carries the brand. |
| [[business/website-spec-complex]] | Component system, content model, advanced interactions, data explorer or case-study architecture, accessibility fallbacks, screenshot/device QA, and performance budgets. |

## Build Rules For Better Webpages

1. Start from the content schema, not visual effects.
2. Keep the first viewport understandable without JavaScript.
3. Use CSS for layout and identity before adding animation.
4. Treat motion as an enhancement with reduced-motion fallbacks.
5. Keep repeated content in typed data files.
6. Choose framework hydration only when there is real state.
7. For longform/data pages, keep data, rendering, and narrative text separate.
8. Use manifest-backed evidence when borrowing a pattern from a reference.
9. Never copy third-party source code, media, branding, or prose into client work.

## Verification

Commands run:

```text
python3 -m py_compile external-references/scrape_reference_assets.py
python3 external-references/scrape_reference_assets.py
```

The first scrape run inside the sandbox failed DNS resolution for all sites. The approved outbound-network rerun completed and saved the evidence folder described above.
