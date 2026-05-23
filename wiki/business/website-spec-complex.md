---
type: business
description: Technical boilerplate spec for the complex premium website package
last_updated: 2026-05-21
tags: [business, pricing, package, complex, spec, astro, boilerplate]
source_file: "Luca Kosowski Website fees.docx"
related_files:
  - graphify-out/converted/Luca Kosowski Website fees_cd1a932d.md
  - Bizwholistic/package.json
  - Bizwholistic/astro.config.mjs
  - Bizwholistic/src/layouts/Base.astro
related:
  - business/business-service-offers
  - projects/bizwholistic
  - implementation/impl-bizwholistic-astro
---

# Website Spec: Complex

Back: [[business/business-service-offers]] · [[MOC/MOC-Business]]

## Purpose and Fit

The complex package is the premium static-site architecture tier. It is for a larger public website that needs custom architecture, richer visual systems, multiple page templates, stronger launch SEO, optional multilingual routing, and scoped integrations. It is not a default web app, and it should not exceed Astro unless the client explicitly buys a custom backend or application layer.

Fee-sheet facts that must remain true:

| Field | Complex package scope |
|------|------|
| Name | Complex Website |
| Price evidence | Header says `$5,500-$12,500`; detail row says `$5,500-$12,000`. Reconcile before quoting. |
| Purpose | High-end custom site or operational web experience. |
| Best use | Multi-page company sites, multilingual websites, complex portfolios, custom interactions, integrations, premium brand presentation. |
| Pages | 8-20+ pages, multiple templates, or custom page types. |
| Design | Full custom design system, premium layouts, motion/interactions, component library, detailed responsive behavior. |
| Copy | Client provides core information; deeper content architecture and heavier rewriting can be included or quoted. |
| Images/logo | Advanced image direction, visual system, iconography, compression, and consistent media treatment. |
| Revisions | 3 structured revision rounds. |
| SEO | Expanded technical SEO basics, sitemap, metadata system, schema if relevant, launch checklist. |
| Contact | Advanced forms or multiple contact flows. |
| CMS | Optional only when explicitly scoped. |
| Form/backend | Integrations, payment logic, or APIs priced by complexity. |
| Login | Not provided unless separately scoped as an advanced add-on. |
| Analytics | Analytics, events, conversion tracking, and dashboard-style reporting if scoped. |
| Handover | Documentation, walkthrough, and handover session. |
| Warranty | 30-day bug-fix window. |

Use `Bizwholistic/` as the local implementation reference for a complex static marketing site: Astro 5, static output, sitemap integration, shared layout, components, route folders, typed data, `robots.txt`, `llms.txt`, `llms-full.txt`, canonical/hreflang handling, JSON-LD schema, and privacy-friendly analytics.

## Recommended Stack Decision

Default stack:

- Astro static output.
- TypeScript data modules.
- Plain Astro components.
- CSS custom properties in `tokens.css`.
- Global CSS plus component-scoped styles.
- `@astrojs/sitemap`.
- Static hosting.
- No React by default.
- No client-side SPA by default.
- No server runtime by default.
- No database by default.
- No authentication by default.

Decision table:

| Requirement | Default decision | Upgrade trigger |
|------|------|------|
| 8-20 public pages | Astro static routes | Use content collections if page count or repeated content types become large. |
| Multilingual public site | Astro i18n when scoped | Add language-specific data files and hreflang only after language count is approved. |
| Service/case-study templates | Astro components plus typed data | Add content collections only if non-technical editors will add entries. |
| Contact flow | Static form provider or scoped serverless endpoint | Custom API, CRM, booking, file upload, payment, or conditional routing. |
| CMS/editor | Not included | Quote CMS/editor setup separately. |
| Analytics | Basic analytics and optional events | Dashboard/reporting is separately scoped. |
| Payments/booking | Not included | Quote integration as advanced add-on. |
| Login/accounts | Not included | Escalate to custom app/back-end scope. |

The technical ceiling for this package is Astro. Do not introduce Next.js, SvelteKit SSR, a database, auth, or a custom server because it "might be useful." Only add them when the signed scope requires runtime behavior that static Astro cannot provide.

## Non-Negotiable Scope Boundaries

Included in the base complex build:

- Information architecture for the agreed page/template count.
- Custom component library for the site.
- Design tokens for color, type, spacing, layout, radius, motion, and media.
- Responsive layouts for mobile, tablet, desktop, and wide desktop.
- Header, footer, mobile navigation, content bands, CTA bands, proof sections, forms, and repeated content components.
- Metadata system for title, description, canonical, Open Graph, Twitter, and robots directives.
- Sitemap.
- `robots.txt`.
- `llms.txt`; `llms-full.txt` when answer-engine discoverability is scoped.
- JSON-LD schema when facts are verified.
- Basic performance controls: image compression, lazy loading, no avoidable client JavaScript.
- 3 structured revision rounds.
- 30-day bug-fix window.

Must be separately scoped:

- CMS/editor setup.
- Blog/news publishing workflow.
- Copywriting from scratch.
- Translation or language beyond the scoped count.
- Booking, payment, e-commerce, CRM, API, or automation integration.
- Custom backend.
- Login/user accounts.
- Dashboard/reporting UI.
- Legal, tax, compliance, or regulated-claim review.
- Hosting/domain/email provider fees.
- Ongoing SEO or content updates.
- Future feature additions after handover.

Change-control rule: if a request adds a route, template, language, provider dependency, integration, privacy burden, approval flow, or ongoing maintenance obligation, it is not "just a revision."

## Information Architecture

Default complex IA for a professional firm or premium service site:

| Route | Template | Purpose | Notes |
|------|------|------|------|
| `/` | Home | Positioning, proof, conversion path | Strong first-viewport signal, not a generic landing-page card stack. |
| `/about/` | About | Founder/company trust | Bio, timeline, values, credentials, proof. |
| `/services/` | Service index | Offer overview | Groups service categories and routes to details. |
| `/services/[slug]/` | Service detail | Intent-specific conversion | One template powered by typed data. |
| `/work/` | Case-study index | Proof | Grid/list of selected proof, not decorative cards. |
| `/work/[slug]/` | Case-study detail | Deep proof | Challenge, role, process, result, CTA. |
| `/insights/` | Insight index | Optional authority content | Add only if blog/news is scoped. |
| `/insights/[slug]/` | Article | Optional content hub | Use content collections when scoped. |
| `/contact/` | Contact | Primary conversion | Form or direct contact options. |
| `/privacy/` | Privacy | Launch hygiene | Client-provided/legal-approved copy. |
| `/terms/` | Terms | Optional | Only if client supplies approved copy. |
| `/[locale]/...` | Localized routes | Optional i18n | Include hreflang and translated content per language. |

For multilingual sites, use one of two shapes:

| Shape | Use when | Example |
|------|------|------|
| Prefixed default locale | The site is intentionally multilingual and each language has a full public version | `/en/`, `/pl/`, `/de/` |
| Single-language core plus EN-only intent pages | Only some pages have alternates | Use explicit `alternateUrls` and avoid fake hreflang. |

Navigation rules:

- Header must not expose every page. Keep primary nav to 5-7 items.
- Use footer for secondary routes, legal routes, and social links.
- Use breadcrumbs on deep service/work/article pages.
- Every page has exactly one visible `<h1>`.
- Repeated data-driven pages must have stable slugs and unique metadata.

## File Tree

Recommended starter tree:

```text
client-complex-site/
  package.json
  astro.config.mjs
  tsconfig.json
  public/
    favicon.svg
    og-image.png
    robots.txt
    llms.txt
    llms-full.txt
    _redirects
    images/
      hero.jpg
      founder.jpg
      work/
      services/
  src/
    components/
      Analytics.astro
      Breadcrumbs.astro
      ContactCTA.astro
      ContactForm.astro
      Footer.astro
      Header.astro
      JsonLd.astro
      MediaFrame.astro
      SectionBand.astro
      ServiceList.astro
      WorkList.astro
    data/
      site.ts
      navigation.ts
      services.ts
      work.ts
      schema.ts
      languages.ts
    layouts/
      Base.astro
    pages/
      index.astro
      about.astro
      services/
        index.astro
        [slug].astro
      work/
        index.astro
        [slug].astro
      contact.astro
      privacy.astro
    styles/
      tokens.css
      global.css
```

Optional only when scoped:

```text
src/content/
  config.ts
  insights/
src/pages/insights/
  index.astro
  [slug].astro
src/pages/api/
  contact.ts
src/integrations/
  crm.ts
  payments.ts
  booking.ts
```

Do not add by default:

```text
admin/
auth/
database/
server/
stripe/
cms/
```

## Frontend Development Spec

Implementation rules:

- Build static-first. HTML should be useful without JavaScript.
- Use Astro components for repeated UI; avoid copy/paste page shells.
- Keep client JavaScript small and purposeful.
- Use section bands, not nested decorative cards.
- Use cards only for repeated records: services, work, testimonials, people, FAQ rows, metrics.
- Do not put UI cards inside other cards.
- Use stable dimensions for media, icons, grids, buttons, and counters.
- Use `aspect-ratio` for fixed-format media.
- Use real headings, lists, buttons, labels, and links.
- Keep mobile first. Every desktop grid must collapse cleanly to one column.
- Do not make typography scale directly with viewport width.
- Avoid one-note palettes. Use neutral base, primary accent, support accent, and semantic states.
- Motion is progressive enhancement only. Respect `prefers-reduced-motion`.
- Use component-scoped CSS for local layout; use global CSS for tokens, resets, typography, containers, section bands, buttons, forms, and utilities.

Accessibility requirements:

- Skip link before header.
- Visible focus state.
- `aria-expanded` and `aria-controls` for mobile nav toggles.
- No hover-only access to critical content.
- Labels for every form field.
- Descriptive link text.
- Truthful alt text.
- Empty `alt=""` only for decorative images.
- Page title and meta description per route.
- Heading sequence must be logical.
- Color contrast manually checked.

Responsive breakpoints:

| Breakpoint | Rule |
|------|------|
| `< 640px` | One-column layout, large tap targets, no dense nav. |
| `640-899px` | Two-column only for short repeated records. |
| `900-1199px` | Main desktop grid begins. |
| `1200px+` | Max-width containers prevent stretched text. |

Performance rules:

- Use local assets.
- Compress images before commit.
- Hero image should be sized for real use, not raw camera dimensions.
- Non-hero images use `loading="lazy"` and `decoding="async"`.
- Do not import animation libraries unless the scoped design requires them.
- Avoid third-party scripts unless required.

## Backend and Integration Spec

Default backend position: none. Complex means architecture-rich, not automatically server-backed.

Allowed integration patterns:

| Need | Lowest-complexity implementation | Escalation |
|------|------|------|
| Contact form | Static provider with spam protection | Serverless endpoint only if provider cannot satisfy scope. |
| Multi-step inquiry | Static provider with hidden fields | Custom API if conditional routing is required. |
| CRM lead capture | Provider webhook | Custom integration module if transformation/retry logic is needed. |
| Booking | External booking link/embed | Custom booking flow is advanced add-on. |
| Payments | External payment link | E-commerce/checkout is advanced add-on. |
| CMS | Headless CMS or Git-based CMS | Scope editorial roles, preview, auth, and maintenance. |
| Reporting | Analytics provider dashboard | Custom dashboard is app scope. |

Serverless endpoint guardrails if explicitly scoped:

- Validate method.
- Validate origin or use a provider-side allowlist.
- Validate all required fields.
- Use honeypot or Turnstile/reCAPTCHA where appropriate.
- Do not log secrets.
- Keep API keys in provider environment variables, never in repo.
- Return generic error messages to the browser.
- Store only the data the client has approved.

## SEO and Answer-Engine Spec

Complex launch SEO includes machine-readable and crawler-friendly structure. It is still not an ongoing SEO campaign unless separately scoped.

Required:

- Unique title and description per page.
- Canonical URL per page.
- Open Graph metadata.
- Twitter card metadata.
- Sitemap with correct canonical URLs.
- `robots.txt`.
- Clean trailing slash policy.
- Internal links that match real routes.
- Alt text.
- Schema where facts are verified.
- `llms.txt`.
- `llms-full.txt` when answer-engine visibility is scoped.
- No stale legacy URLs in sitemap.
- Redirects for known old URLs when replacing an existing site.
- Hreflang only for real language equivalents.

Schema pattern:

- `Organization` or `ProfessionalService` for a company.
- `Person` for a named founder/principal.
- `WebSite`.
- `WebPage`.
- `BreadcrumbList`.
- `Service` for service detail pages where useful.
- `Article` or `BlogPosting` only for real articles.
- `FAQPage` only for visible FAQ content.

Never claim:

- Rankings.
- Guaranteed approvals.
- Licenses.
- Client counts.
- Partner status.
- Awards.
- Regulated credentials.

unless the client supplies verifiable evidence and approves the exact wording.

## Design System Rules

Design-system depth:

- Complex gets a full site-specific system.
- It should still be simple enough for agents and humans to extend.
- Do not create a design system that requires a design engineer to edit normal pages.

Required token groups:

| Token group | Required values |
|------|------|
| Color | Paper, surface, alternate surface, inverted surface, text, muted text, border, primary, primary dark, support, success, warning, error, focus. |
| Type | Sans, display, mono, display size, h1-h4, body, small, micro, line heights, weights. |
| Space | 4px base, section padding, component gaps, form gaps. |
| Layout | Narrow/default/wide/edge containers, page padding, grid minima. |
| Radius | 4px, 8px, optional 16px for large media only. |
| Shadow | Subtle shadow for elevated repeated components only. |
| Motion | Duration and easing, reduced-motion fallback. |

Component rules:

- Header: sticky or fixed only if it does not block content or break mobile.
- Footer: real contact, legal, and secondary nav.
- Hero: first-viewport signal of the company/product/person. No vague stock-like hero.
- Section bands: full-width, with constrained inner content.
- Forms: labels, help text, error state, success state, honeypot if scoped.
- Cards: repeated records only, 8px radius unless brand explicitly needs otherwise.
- Buttons: clear primary/secondary hierarchy, no text overflow, no layout shift on hover.

## Content and Assets

Client must supply or approve:

- Company/person legal name and public name.
- Contact details.
- Service list.
- Proof/testimonials.
- Images.
- Logo/brand assets.
- Privacy/legal copy.
- Language translations if scoped.
- Claims that may imply regulated advice, licensing, guarantees, or outcomes.

Included complex content work:

- Content architecture.
- Section structure.
- Heavier rewriting when included in the quote.
- Page-level metadata.
- CTA hierarchy.
- Image direction.
- Proof organization.
- Machine-readable summary.

Not automatically included:

- Full brand identity.
- Logo design.
- Photography.
- Video production.
- Legal drafting.
- Translation.
- Ongoing article production.

Asset rules:

- Do not ship raw oversized images.
- Use descriptive filenames.
- Keep `public/images/` organized by role.
- Preserve meaning when cropping.
- Set dimensions.
- Prefer local assets over hotlinks.
- Document any third-party asset license.

## Code Template

`package.json`

```json
{
  "name": "client-complex-site",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "astro dev",
    "start": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "@astrojs/sitemap": "^3.2.0",
    "astro": "^5.0.0"
  },
  "devDependencies": {}
}
```

`astro.config.mjs`

```js
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

const buildDate = new Date();
const site = 'https://example.com';

export default defineConfig({
  site,
  output: 'static',
  trailingSlash: 'always',
  compressHTML: false,
  integrations: [
    sitemap({
      lastmod: buildDate,
      filter: (page) => !page.endsWith('/legacy-page/'),
    }),
  ],
  build: {
    inlineStylesheets: 'auto',
  },
});
```

`src/data/site.ts`

```ts
export type SocialLink = {
  label: string;
  href: string;
};

export const site = {
  name: 'Client Name',
  legalName: 'Client Name LLC',
  url: 'https://example.com',
  email: 'hello@example.com',
  phone: '+10000000000',
  locale: 'en',
  ogImage: '/og-image.png',
  tagline: 'Specific outcome for a specific audience.',
  description:
    'Client Name helps a defined audience achieve a defined result with a clearly scoped professional service.',
  socials: [
    { label: 'LinkedIn', href: 'https://www.linkedin.com/company/example' },
  ] satisfies SocialLink[],
};
```

`src/data/services.ts`

```ts
export type Service = {
  slug: string;
  title: string;
  description: string;
  summary: string;
  fit: string[];
  notFit: string[];
  outcomes: string[];
};

export const services: Service[] = [
  {
    slug: 'advisory',
    title: 'Advisory',
    description: 'Short metadata description for the advisory service page.',
    summary: 'A concise public explanation of the service and its value.',
    fit: ['Client type that benefits from this service.'],
    notFit: ['Client type that should choose another path.'],
    outcomes: ['Concrete result or deliverable.'],
  },
];
```

`src/layouts/Base.astro`

```astro
---
import '../styles/tokens.css';
import '../styles/global.css';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
import { site } from '../data/site';

type AlternateUrls = Record<string, string | undefined>;

interface Props {
  title: string;
  description: string;
  image?: string;
  noindex?: boolean;
  alternateUrls?: AlternateUrls;
  extraSchemas?: object[];
}

const {
  title,
  description,
  image = site.ogImage,
  noindex = false,
  alternateUrls = {},
  extraSchemas = [],
} = Astro.props;

const canonical = new URL(Astro.url.pathname, site.url).toString();
const absoluteImage = new URL(image, site.url).toString();

const schemaGraph = {
  '@context': 'https://schema.org',
  '@graph': [
    {
      '@type': 'ProfessionalService',
      '@id': `${site.url}/#organization`,
      name: site.name,
      legalName: site.legalName,
      url: site.url,
      email: site.email,
      description: site.description,
    },
    {
      '@type': 'WebSite',
      '@id': `${site.url}/#website`,
      url: site.url,
      name: site.name,
      publisher: { '@id': `${site.url}/#organization` },
      inLanguage: site.locale,
    },
    {
      '@type': 'WebPage',
      '@id': `${canonical}#webpage`,
      url: canonical,
      name: title,
      description,
      isPartOf: { '@id': `${site.url}/#website` },
      about: { '@id': `${site.url}/#organization` },
      inLanguage: site.locale,
    },
    ...extraSchemas,
  ],
};
---

<!doctype html>
<html lang={site.locale}>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
    <meta name="theme-color" content="#f7f4ee" />
    <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
    <link rel="canonical" href={canonical} />
    {Object.entries(alternateUrls).map(([lang, href]) => href && (
      <link rel="alternate" hreflang={lang} href={href} />
    ))}
    <link rel="alternate" type="text/llms.txt" title="LLM-friendly summary" href="/llms.txt" />
    <title>{title}</title>
    <meta name="description" content={description} />
    <meta name="robots" content={noindex ? 'noindex, nofollow' : 'index, follow, max-snippet:-1, max-image-preview:large'} />
    <meta property="og:title" content={title} />
    <meta property="og:description" content={description} />
    <meta property="og:type" content="website" />
    <meta property="og:url" content={canonical} />
    <meta property="og:image" content={absoluteImage} />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta name="twitter:card" content="summary_large_image" />
    <script type="application/ld+json" set:html={JSON.stringify(schemaGraph)} />
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
    <Header />
    <main id="main">
      <slot />
    </main>
    <Footer />
  </body>
</html>
```

`src/pages/services/[slug].astro`

```astro
---
import Base from '../../layouts/Base.astro';
import { services } from '../../data/services';

export function getStaticPaths() {
  return services.map((service) => ({
    params: { slug: service.slug },
    props: { service },
  }));
}

const { service } = Astro.props;
---

<Base title={`${service.title} | Client Name`} description={service.description}>
  <section class="section section--pure">
    <div class="container container--wide split">
      <div class="stack">
        <p class="eyebrow">Service</p>
        <h1>{service.title}</h1>
        <p class="lead">{service.summary}</p>
        <a class="button button--primary" href="/contact/">Discuss this service</a>
      </div>
      <aside class="panel" aria-labelledby="outcomes-title">
        <h2 id="outcomes-title">Outcomes</h2>
        <ul class="check-list">
          {service.outcomes.map((item) => <li>{item}</li>)}
        </ul>
      </aside>
    </div>
  </section>
</Base>
```

`src/styles/tokens.css`

```css
:root {
  --color-paper: #f7f4ee;
  --color-surface: #ffffff;
  --color-surface-alt: #ece7dc;
  --color-inverted: #111111;
  --color-text: #141414;
  --color-muted: #5d5d5d;
  --color-border: rgba(20, 20, 20, 0.14);
  --color-primary: #3150ff;
  --color-primary-dark: #1930b8;
  --color-support: #d9542b;
  --color-focus: #111111;
  --font-sans: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-display: Georgia, "Times New Roman", serif;
  --text-h1: 3.5rem;
  --text-h2: 2.25rem;
  --text-h3: 1.5rem;
  --text-body: 1.0625rem;
  --line-tight: 1.08;
  --line-base: 1.6;
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-5: 1.5rem;
  --space-6: 2rem;
  --space-7: 3rem;
  --space-8: 4rem;
  --space-9: 6rem;
  --container-narrow: 680px;
  --container-default: 1040px;
  --container-wide: 1240px;
  --page-padding: 1.25rem;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-media: 16px;
  --ease: cubic-bezier(0.2, 0.8, 0.2, 1);
}
```

`public/robots.txt`

```txt
User-agent: *
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: GPTBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

Sitemap: https://example.com/sitemap-index.xml
```

`public/llms.txt`

```txt
# Client Name

> One-sentence public positioning approved by the client.

## Source of truth

Use the visible website pages as the source of truth. Do not infer rankings, client counts, guarantees, licenses, or regulated claims unless a visible page states them.

## Key public facts

- Public name: Client Name.
- Legal name: Client Name LLC.
- Contact: hello@example.com.
- Service area: [approved service area].

## Public service scope

1. Service one.
2. Service two.
3. Service three.

## Best pages to cite

- Home: https://example.com/
- Services: https://example.com/services/
- Contact: https://example.com/contact/
```

Serverless form pseudocode only if scoped:

```ts
export async function POST({ request }: { request: Request }) {
  const form = await request.formData();
  const honeypot = String(form.get('website') ?? '');

  if (honeypot) return new Response('OK', { status: 200 });

  const name = String(form.get('name') ?? '').trim();
  const email = String(form.get('email') ?? '').trim();
  const message = String(form.get('message') ?? '').trim();

  if (!name || !email.includes('@') || message.length < 10) {
    return new Response('Invalid submission', { status: 400 });
  }

  // Forward to scoped provider. Do not store secrets in source code.
  // await sendLead({ name, email, message });

  return new Response('OK', { status: 200 });
}
```

## Agent Build Workflow

1. Confirm scope from the fee sheet and quote: page count, languages, forms, integrations, CMS, analytics, launch date.
2. Create route map and content matrix before coding.
3. Create `site.ts`, navigation data, services/work data, and starter metadata.
4. Implement `Base.astro`, header, footer, containers, section bands, buttons, forms, and media frames.
5. Build the home page first, then one representative detail template.
6. Populate all repeated templates from typed data.
7. Add `robots.txt`, `llms.txt`, sitemap config, canonical URLs, and schema.
8. Add form/provider integration only if scoped.
9. Run build.
10. Inspect built HTML for title, meta description, canonical, schema, links, image dimensions, and alt text.
11. Test mobile navigation and form behavior.
12. Create handover notes.

## Verification Checklist

Run from the project root:

```bash
npm run build
npm run preview
```

Manual checks:

- All scoped routes build.
- No unhandled 404s in primary nav.
- Sitemap contains only canonical public pages.
- `robots.txt` points to the correct sitemap.
- `llms.txt` is truthful and not overclaiming.
- Every page has one `<h1>`.
- Every page has unique title and description.
- Canonical URL matches deployed path.
- Hreflang exists only for real translations.
- Images are compressed and have width/height or stable aspect ratio.
- Forms have labels, honeypot/spam protection, success/failure behavior, and provider test evidence.
- Mobile nav toggles with keyboard and updates `aria-expanded`.
- Layout has no horizontal scroll at 320px.
- Text does not overflow buttons/cards.
- No secrets are committed.
- No provider fees are hidden inside the package.

## Handover Package

Deliver:

- Source folder.
- Built output or deploy target.
- Handover notes.
- Page map.
- Editing guide for content/data files.
- Provider list.
- Analytics location.
- Form destination and spam-protection note.
- SEO asset list.
- Warranty terms.
- Known exclusions.

Minimum `HANDOVER.md`:

```md
# Client Name Website Handover

Stack: Astro static site.
Build: npm run build.
Preview: npm run preview.
Deploy target: [provider].
Domain: [domain].
Analytics: [provider/account].
Forms: [provider/form or not included].
CMS: [not included/provider].

Edit content:
- Site facts: src/data/site.ts
- Navigation: src/data/navigation.ts
- Services: src/data/services.ts
- Work: src/data/work.ts
- Page copy: src/pages/
- Styles: src/styles/tokens.css and src/styles/global.css
- Images: public/images/

Warranty:
30-day bug-fix window from launch.
Not included: new pages, new features, new integrations, new languages, legal advice, ongoing SEO, ongoing content updates.
```

## Change-Control Rules

Inside revision rounds:

- Copy tightening within existing sections.
- Image replacement using supplied assets.
- Section reordering.
- Spacing/color adjustment within approved design direction.
- CTA wording changes.
- Metadata corrections.
- Bug fixes.

Change-control:

- New template.
- New route beyond agreed page count.
- New language.
- CMS/editor.
- Blog/news.
- Form complexity beyond agreed flow.
- Booking/payment/e-commerce.
- API/CRM integration.
- Login/user accounts.
- Dashboard/reporting.
- New design direction.
- Additional revision round.
- Ongoing maintenance.

## Exclusions and Add-Ons

Fee-sheet anchors:

| Add-on | Price anchor |
|------|------|
| Blog/news section | `+$300-$1,000` |
| SEO basics expansion | `+$250-$750` |
| Custom animations or interactive sections | `+$200-$900` |
| Booking/payment flow | `+$500-$2,500+` |
| E-commerce/payment integrations | `+$1,000-$4,000+` |
| Backend/API integration | `+$500-$3,500+` |
| Login/user accounts | `+$1,500-$5,000+` |
| Additional language beyond EN/PL | `+$200-$500/language` |
| Ongoing content updates | `$50-$120/hour` or maintenance plan |

Hard exclusions unless written into scope:

- Bank-account guarantee.
- Legal/compliance advice.
- Hosting/domain/email provider fees.
- Third-party software fees.
- Paid APIs.
- Future updates.
- Ongoing SEO.
- Ongoing content operations.
- Custom app support.
