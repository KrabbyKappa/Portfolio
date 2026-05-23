---
type: business
description: Agent-ready implementation spec for the Medium Complexity website offer
last_updated: 2026-05-21
tags: [business, pricing, website-spec, medium-complexity, astro]
source_file: "Luca Kosowski Website fees.docx"
related:
  - business/business-service-offers
  - projects/portfolio-main
  - implementation/impl-portfolio-static-site
  - projects/bizwholistic
  - implementation/impl-bizwholistic-astro
---

# Medium Complexity Website Spec

Backlink: [[business/business-service-offers]] · [[MOC/MOC-Business]]

## Purpose and Fit

This page turns the fee-sheet "Medium Complexity" package into a theoretical build spec for agents and humans working in this workspace.

The Medium package is for a polished multi-section or multi-page website for a professional service, consultant, small firm, portfolio, case-study site, or structured business presence. The fee-sheet range is `$2,000-$4,500`. This tier is appropriate when structure, polish, responsive layout, launch SEO, analytics, image treatment, and a clear conversion path matter, but the project does not need the architecture, integrations, multilingual system, CMS-heavy workflow, login, database, or custom backend of a Complex website.

Fee-sheet facts that must remain true:

| Field | Medium Complexity scope |
|------|------|
| Purpose | Polished business website with clear structure and stronger presentation. |
| Best use | Consultants, small firms, service providers, professional portfolios, case-study sites, multi-section business websites. |
| Price | `$2,000-$4,500`. |
| Pages | `4-8` pages, or one long landing page plus several subpages/templates. |
| Design | Custom visual direction, consistent components, responsive layout, refined spacing. |
| Copy | Client provides base copy; section structure, headlines, and light rewriting are included. |
| Images/logo | Image treatment, cropping, compression, icon use, and branded visual consistency. |
| Revisions | `2` structured revision rounds. |
| SEO | Basic metadata, headings, alt text, sitemap, clean URLs, and basic launch SEO. |
| Contact | Contact form with spam protection, email CTA, LinkedIn/WhatsApp links if scoped or required. |
| CMS | Optional only when explicitly scoped. |
| Form/backend | Static provider form is acceptable when scoped; custom backend is not included by default. |
| Login | Not provided. |
| Analytics | Basic analytics setup included. |
| Handover | Handover notes plus short walkthrough. |
| Warranty | 30-day bug-fix window. |

`Portfolio-main/` and `lucakosowski.com` are the barebones Medium reference. That site has multiple pages and sections, navigation, hero content, experience, education, projects, articles, references, contact information, CV download, embedded media, responsive styling, and analytics. It demonstrates the entry-tier content density that can justify a Medium classification. It should not be copied as the default implementation pattern for new paid Medium work because it repeats headers, metadata, and scripts across raw HTML pages and relies on a single large CSS file with inline page styles. That is acceptable for a personal static portfolio, but weaker than the preferred repeatable delivery model for client websites.

## Recommended Stack Decision

Use a static Astro site as the default implementation for Medium Complexity websites.

| Option | Verdict | Reason |
|------|------|------|
| Plain HTML/CSS like `Portfolio-main/` | Reference only | It is simple and deployable, but repeated headers, repeated metadata, manual page edits, and manual sitemap work become fragile across 4-8 pages. |
| Astro static output | Recommended | It keeps deployment static while giving agents reusable layouts, components, shared metadata, sitemap generation, clean page templates, and consistent CSS tokens. |
| Full Bizwholistic-style Astro architecture | Too large by default | Bizwholistic uses multilingual routing, richer schema, intent-page data, public AI-search assets, and a stronger editorial system. Those are Complex or add-on features unless quoted. |
| React / SPA | Do not use | Medium sites need crawlable HTML, low maintenance, and direct hosting, not client-side app state. |
| Database / login / CMS | Do not use by default | These change maintenance, risk, support, and cost. CMS is optional only when scoped. |

The recommended stack is:

- Astro static output.
- Plain Astro components.
- Shared `Base.astro` layout.
- Shared CSS tokens and global CSS.
- No React.
- No database.
- No login.
- No default CMS.
- No server runtime.
- Optional static form provider when scoped.
- Privacy-friendly analytics such as GoatCounter or Plausible.
- Sitemap integration.
- Public `robots.txt`.
- Public `llms.txt`.

This keeps the implementation lower than Complex while still more maintainable than the bare HTML reference.

## Non-Negotiable Scope Boundaries

Included in Medium:

- 4-8 public pages, or one long landing page plus supporting subpages/templates.
- Custom visual direction, but not a full enterprise design system.
- Consistent reusable components for header, footer, hero, section bands, service blocks, work cards, CTA bands, and contact sections.
- Responsive mobile, tablet, and desktop layout.
- Basic accessibility: semantic HTML, labels, focus states, skip link, keyboard-reachable navigation, readable contrast, truthful alt text.
- Basic launch SEO: metadata, headings, alt text, sitemap, clean URLs, canonical URLs, Open Graph tags, `robots.txt`.
- Basic analytics setup.
- Light copy structuring and rewriting from client-supplied base copy.
- Image treatment: crop, compression, stable aspect ratios, descriptive filenames, and consistent presentation.
- Two structured revision rounds.
- Handover notes plus short walkthrough.
- 30-day bug-fix window.

Not included unless separately scoped:

- Full copywriting from scratch.
- Translation or multilingual architecture.
- CMS/editor setup.
- Blog/news publishing workflow.
- Login or user accounts.
- Database.
- E-commerce, checkout, booking, payments, subscriptions, or member-only content.
- Custom backend/API integration.
- CRM integration.
- Legal/compliance advice.
- Ongoing SEO campaign.
- Ongoing content updates after handover.
- Provider fees for domain, hosting, email, stock assets, paid fonts, form provider, analytics provider, or paid APIs.
- New design direction after approval.
- More than two revision rounds.

A revision round means changes inside the agreed package, not a new site concept, new feature list, or new technical architecture.

## Information Architecture

Default Medium IA should use 4-8 pages. A long landing page is allowed when the offer is narrow, but the site should still include contact, privacy, and any scoped proof/case-study pages.

Recommended 6-page structure:

| Route | Page | Purpose | Required content |
|------|------|------|------|
| `/` | Home | Conversion overview and credibility | Hero, value proposition, proof, services preview, process, selected work, about preview, CTA. |
| `/about/` | About | Trust and story | Bio/company story, credentials, principles, proof points, CTA. |
| `/services/` | Services | Offer structure | Service groups, outcomes, fit/not-fit, process, FAQs, CTA. |
| `/work/` | Work or Case Studies | Proof | Project cards, results, media, roles, optional links to detail pages. |
| `/work/example-project/` | Case-study template | Deeper proof | Challenge, role, process, result, image/media, CTA. Use only if scoped. |
| `/contact/` | Contact | Conversion | Form if scoped, email, phone/WhatsApp/LinkedIn, response expectations. |
| `/privacy/` | Privacy | Launch hygiene | Client-approved privacy copy. Not legal advice. |

Alternative long landing structure:

| Section | Purpose |
|------|------|
| Hero | State the professional offer clearly and provide one primary CTA. |
| Trust strip | Show credentials, logos, numbers, testimonials, or publication references if supplied. |
| Services | Summarize 3-5 services with outcome-oriented copy. |
| Process | Explain how the engagement works. |
| Work or case studies | Present selected proof in stable cards or media frames. |
| About | Explain who is behind the service and why they are credible. |
| FAQ | Resolve common objections. |
| Contact CTA | Provide form or direct contact routes. |

Navigation rules:

- Header should contain 5-7 top-level links at most.
- Desktop header may include one primary CTA.
- Mobile navigation must use a real button with `aria-expanded`.
- Every page must have one visible `<h1>`.
- Section IDs must be stable and human-readable.
- Use pages instead of excessive anchor links when the content is substantial.

## File Tree

Recommended Astro file tree:

```text
client-medium-site/
  package.json
  astro.config.mjs
  public/
    favicon.svg
    og-image.jpg
    robots.txt
    llms.txt
    images/
      hero.jpg
      profile.jpg
      work-example.jpg
  src/
    components/
      SiteHeader.astro
      SiteFooter.astro
      SectionBand.astro
      ServiceCards.astro
      ContactForm.astro
    data/
      site.ts
      services.ts
      work.ts
    layouts/
      Base.astro
    pages/
      index.astro
      about.astro
      services.astro
      work/
        index.astro
        example-project.astro
      contact.astro
      privacy.astro
    styles/
      tokens.css
      global.css
```

Optional only when scoped:

```text
src/pages/blog/
src/content/
src/content.config.ts
src/data/testimonials.ts
public/llms-full.txt
```

Do not add by default:

```text
src/pages/admin/
src/pages/api/
src/server/
database/
auth/
cms/
```

## Frontend Development Spec

The frontend should feel professional, restrained, and repeatable. It should not feel like a marketing template filled with oversized decorative sections, nested cards, generic gradients, or fragile mobile behavior.

Build rules:

- Use semantic Astro templates and HTML.
- Use one shared `Base.astro` layout for metadata, analytics, header, footer, and page shell.
- Use shared components for header, footer, section bands, service cards, work cards, CTA bands, and contact form.
- Use full-width bands with constrained inner containers.
- Use cards only for repeated items such as services, work items, testimonials, FAQs, or team entries.
- Do not put cards inside other cards.
- Do not style page sections as floating cards.
- Use stable image frames with explicit `aspect-ratio`, `width`, `height`, or both.
- Use `object-fit: cover` only when cropping is acceptable.
- Use `object-fit: contain` for logos, diagrams, or images where cropping changes meaning.
- Use CSS custom properties for spacing, typography, color, radius, and shadows.
- Do not scale font size with viewport width.
- Keep letter spacing at `0` except small uppercase labels with modest positive tracking.
- Keep card radius at `8px` or less.
- Use real client images or useful generated/selected bitmap assets that reveal the actual person, service context, work, product, or place.
- Use tiny vanilla JavaScript only for navigation toggles or simple progressive enhancement.
- Avoid motion-heavy sections by default.

Accessibility rules:

- Include a skip link.
- All interactive controls must be keyboard reachable.
- Mobile menu must expose `aria-expanded`.
- Inputs must have visible labels.
- Links must use meaningful text.
- Images must have truthful alt text or empty alt for decorative images.
- Color contrast must be checked manually.
- Focus states must be visible.
- Form errors must not rely on color alone if custom validation is added.

## Backend and Form Spec

Medium does not include a custom backend by default.

Allowed form approach:

- Static HTML form posting to a scoped provider such as Formspree, Basin, Netlify Forms, Getform, or another approved static form provider.
- Provider-level spam protection such as honeypot, reCAPTCHA, Turnstile, domain allowlist, or rate limiting.
- Email notification to the client.
- Success redirect or provider-supported success message.
- No submissions stored in the repository.
- No custom database.
- No custom admin dashboard.

Default fallback if a form is not scoped:

- `mailto:` CTA.
- WhatsApp link if supplied.
- LinkedIn link if supplied.
- Phone link if supplied.

Escalate to add-on or Complex scope for:

- Custom server validation.
- CRM integration.
- Multi-step forms.
- File uploads.
- Booking logic.
- Payment capture.
- Conditional routing.
- Logged-in lead dashboard.
- Data retention or reporting system.

Minimum form fields when included:

| Field | Required | Notes |
|------|------|------|
| Name | Yes | Plain text. |
| Email | Yes | Use `type="email"`. |
| Company or website | Optional | Useful for service providers. |
| Project type | Optional | Select field with scoped choices. |
| Message | Yes | Use a reasonable character limit if provider supports it. |
| Consent | Optional | Include only if privacy/compliance requirements are supplied. |
| Honeypot | Yes | Hide visually and remove from normal tab order. |

## SEO and Analytics Spec

Medium SEO is launch SEO, not an ongoing search campaign.

Required SEO work:

- Unique title per page.
- Unique meta description per page.
- Canonical URL per page.
- Open Graph title, description, URL, type, image, dimensions, and image alt where possible.
- Twitter summary card metadata.
- One `<h1>` per page.
- Logical heading sequence.
- Descriptive internal links.
- Descriptive image alt text.
- Clean trailing-slash URLs.
- Build-generated sitemap.
- `public/robots.txt`.
- `public/llms.txt`.
- Page copy that states services, audience, market, proof, and contact path clearly.
- No fake locations, fake testimonials, fake guarantees, or unverifiable claims.

Recommended but optional:

- Minimal `Organization`, `Person`, `ProfessionalService`, or `WebSite` JSON-LD when facts are verified.
- `public/llms-full.txt` for richer answer-engine visibility.
- Basic event tracking for primary CTA clicks if scoped.
- Search Console and Bing Webmaster setup guidance in handover.

Analytics rules:

- Basic analytics setup is included.
- Prefer GoatCounter or Plausible for privacy-friendly static sites.
- Google Analytics can be used only if the client accepts privacy/cookie implications.
- Track pageviews by default.
- Track contact CTA clicks only if scoped.
- Do not build a custom reporting dashboard in Medium scope.

## Design System Rules

Medium uses a compact design system, not a full brand system.

Required token groups:

| Token group | Required values |
|------|------|
| Color | Background, surface, alternate surface, text, muted text, border, primary, primary dark, secondary/support, focus, error. |
| Type | Body font, heading font if different, size scale, line heights, weights. |
| Space | 4px/8px-based scale for sections, grids, cards, forms, and inline spacing. |
| Layout | Container width, narrow text width, grid minimum, image aspect ratios. |
| Radius | 4px and 8px maximum for normal UI. |
| Shadow | One subtle shadow for repeated cards only. |
| Motion | One transition token for hover/focus states. |

Component rules:

- Header must be stable and must not create layout shift.
- Mobile nav must be button-driven, accessible, and close after link click.
- Hero must state the offer, show useful media if available, and include one primary CTA.
- Service cards must have equal structure and no nested wrappers.
- Work cards must use stable media frames.
- CTA bands must be full-width bands, not floating cards.
- Footer must contain contact route, key links, copyright, and optional social links.
- Forms must use labels above fields and a single-column mobile layout.

Visual boundaries:

- Do not use Bizwholistic-level editorial complexity unless quoted.
- Do not use generic visual noise to compensate for weak content.
- Do not overbuild animation, parallax, or scroll effects.
- Do not hide the actual service or portfolio behind vague brand language.
- Do not make the site look like an app dashboard unless the client is a software product.
- Avoid one-note palettes. Use a neutral base, one primary accent, and one secondary/support color.

## Content and Assets

Client responsibilities:

- Supply core facts, base copy, bio/company information, service descriptions, contact details, testimonials, project summaries, and legal/privacy text.
- Supply logo, brand marks, images, case-study media, and proof assets where available.
- Approve claims, testimonials, compliance-sensitive statements, and final page copy.
- Pay third-party costs unless explicitly included in the quote.

Included content work:

- Restructure supplied copy into sections.
- Rewrite headings and short paragraphs lightly.
- Clarify service names and calls to action.
- Normalize tone across pages.
- Make portfolio/case-study entries easier to scan.
- Suggest missing proof points or content gaps.

Not included by default:

- Full copywriting from scratch.
- Interview-based content strategy.
- Long-form articles.
- Legal/privacy drafting.
- Translation.
- Brand naming.
- Logo design.
- Photography.
- Video editing.

Asset treatment rules:

- Convert oversized images to web-appropriate dimensions.
- Use descriptive filenames.
- Avoid uploading raw multi-megabyte images when a compressed version works.
- Preserve meaning when cropping.
- Keep all key images in stable frames.
- Use `loading="lazy"` for non-hero images.
- Use `decoding="async"` for normal content images.
- Do not use external hotlinked thumbnails for final client delivery unless the source is stable, permitted, and intentionally documented.

## Code Template

These templates define the baseline coding modality. They are intentionally smaller than Bizwholistic and more maintainable than repeating raw HTML pages as in `Portfolio-main/`.

`package.json`

```json
{
  "name": "client-medium-site",
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
  }
}
```

`astro.config.mjs`

```js
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://example.com',
  output: 'static',
  trailingSlash: 'always',
  integrations: [
    sitemap({
      lastmod: new Date(),
    }),
  ],
  build: {
    inlineStylesheets: 'auto',
  },
});
```

`src/layouts/Base.astro`

```astro
---
import '../styles/tokens.css';
import '../styles/global.css';
import SiteHeader from '../components/SiteHeader.astro';
import SiteFooter from '../components/SiteFooter.astro';

interface Props {
  title: string;
  description: string;
  image?: string;
}

const { title, description, image = '/og-image.jpg' } = Astro.props;
const canonical = new URL(Astro.url.pathname, Astro.site).toString();
const absoluteImage = new URL(image, Astro.site).toString();
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
    <meta name="theme-color" content="#f7f4ee" />
    <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
    <link rel="canonical" href={canonical} />
    <link rel="alternate" type="text/llms.txt" title="LLM-friendly summary" href="/llms.txt" />

    <title>{title}</title>
    <meta name="description" content={description} />
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large" />

    <meta property="og:title" content={title} />
    <meta property="og:description" content={description} />
    <meta property="og:type" content="website" />
    <meta property="og:url" content={canonical} />
    <meta property="og:image" content={absoluteImage} />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />

    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content={title} />
    <meta name="twitter:description" content={description} />
    <meta name="twitter:image" content={absoluteImage} />
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
    <SiteHeader />
    <main id="main">
      <slot />
    </main>
    <SiteFooter />

    {import.meta.env.PROD && (
      <script
        data-goatcounter="https://CLIENT_ACCOUNT.goatcounter.com/count"
        async
        src="//gc.zgo.at/count.js"
      ></script>
    )}
  </body>
</html>
```

`src/pages/index.astro` page template

```astro
---
import Base from '../layouts/Base.astro';
import SectionBand from '../components/SectionBand.astro';
import ServiceCards from '../components/ServiceCards.astro';

const services = [
  {
    title: 'Advisory and planning',
    text: 'Clear direction for clients who need practical decisions before execution.',
  },
  {
    title: 'Implementation support',
    text: 'Hands-on delivery for defined projects, workflows, or public-facing material.',
  },
  {
    title: 'Ongoing guidance',
    text: 'Structured support for teams that need an experienced external perspective.',
  },
];
---

<Base
  title="Client Name | Professional Service"
  description="Client Name helps defined audience achieve specific outcome through concise service category."
>
  <section class="hero band">
    <div class="container hero__grid">
      <div class="stack">
        <p class="eyebrow">Professional service</p>
        <h1>Practical support for a clear client outcome.</h1>
        <p class="lead">
          Replace this with a specific, truthful value proposition. Keep it concrete and easy to verify.
        </p>
        <div class="actions">
          <a class="button button--primary" href="/contact/">Start a conversation</a>
          <a class="button button--secondary" href="/work/">View selected work</a>
        </div>
      </div>
      <figure class="media-frame media-frame--portrait">
        <img src="/images/hero.jpg" alt="Client Name working with a professional client" width="900" height="1100" />
      </figure>
    </div>
  </section>

  <SectionBand eyebrow="Services" title="Focused services for defined needs">
    <ServiceCards items={services} />
  </SectionBand>
</Base>
```

`src/components/SiteHeader.astro` component template

```astro
---
const navItems = [
  { href: '/', label: 'Home' },
  { href: '/about/', label: 'About' },
  { href: '/services/', label: 'Services' },
  { href: '/work/', label: 'Work' },
  { href: '/contact/', label: 'Contact' },
];
---

<header class="site-header">
  <div class="container site-header__inner">
    <a class="site-logo" href="/" aria-label="Client Name home">Client Name</a>
    <button
      class="nav-toggle"
      type="button"
      aria-label="Open navigation"
      aria-controls="site-nav"
      aria-expanded="false"
      data-nav-toggle
    >
      <span></span>
      <span></span>
      <span></span>
    </button>
    <nav class="site-nav" id="site-nav" data-nav-menu>
      {navItems.map((item) => <a href={item.href}>{item.label}</a>)}
      <a class="button button--small" href="/contact/">Contact</a>
    </nav>
  </div>
</header>

<script>
  const toggle = document.querySelector('[data-nav-toggle]');
  const menu = document.querySelector('[data-nav-menu]');

  toggle?.addEventListener('click', () => {
    const expanded = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!expanded));
    menu?.toggleAttribute('data-open', !expanded);
  });

  menu?.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      toggle?.setAttribute('aria-expanded', 'false');
      menu?.removeAttribute('data-open');
    });
  });
</script>
```

`src/components/ServiceCards.astro` component template

```astro
---
interface ServiceItem {
  title: string;
  text: string;
}

interface Props {
  items: ServiceItem[];
}

const { items } = Astro.props;
---

<div class="card-grid">
  {items.map((item) => (
    <article class="card">
      <h3>{item.title}</h3>
      <p>{item.text}</p>
    </article>
  ))}
</div>
```

`src/styles/tokens.css`

```css
:root {
  color-scheme: light;

  --color-bg: #f7f4ee;
  --color-surface: #ffffff;
  --color-surface-alt: #eef3f1;
  --color-text: #1f2528;
  --color-muted: #5e686d;
  --color-border: #d9dedb;
  --color-primary: #315f72;
  --color-primary-dark: #214454;
  --color-secondary: #8a5a44;
  --color-focus: #111827;
  --color-error: #a13535;

  --font-body: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-heading: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;

  --text-xs: 0.8125rem;
  --text-sm: 0.9375rem;
  --text-md: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.375rem;
  --text-2xl: 1.75rem;
  --text-3xl: 2.25rem;

  --line-tight: 1.15;
  --line-normal: 1.6;

  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-5: 1.5rem;
  --space-6: 2rem;
  --space-7: 3rem;
  --space-8: 4rem;

  --container: 70rem;
  --container-narrow: 44rem;
  --radius-sm: 4px;
  --radius-md: 8px;
  --shadow-soft: 0 10px 30px rgb(31 37 40 / 0.08);
  --transition: 180ms ease;
}
```

`src/styles/global.css`

```css
* {
  box-sizing: border-box;
}

html {
  font-size: 16px;
  scroll-behavior: smooth;
}

body {
  margin: 0;
  font-family: var(--font-body);
  background: var(--color-bg);
  color: var(--color-text);
  line-height: var(--line-normal);
  -webkit-font-smoothing: antialiased;
}

img,
svg,
video {
  display: block;
  max-width: 100%;
}

a {
  color: var(--color-primary);
  text-decoration-thickness: 0.08em;
  text-underline-offset: 0.18em;
}

a:hover {
  color: var(--color-primary-dark);
}

:focus-visible {
  outline: 3px solid var(--color-focus);
  outline-offset: 3px;
}

.skip-link {
  position: absolute;
  left: var(--space-4);
  top: var(--space-4);
  z-index: 1000;
  transform: translateY(-150%);
  background: var(--color-text);
  color: var(--color-surface);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-sm);
}

.skip-link:focus {
  transform: translateY(0);
}

.container {
  width: min(100% - 2rem, var(--container));
  margin-inline: auto;
}

.band {
  padding-block: var(--space-8);
}

.stack > * + * {
  margin-top: var(--space-4);
}

h1,
h2,
h3 {
  font-family: var(--font-heading);
  line-height: var(--line-tight);
  letter-spacing: 0;
  margin: 0;
}

h1 {
  font-size: var(--text-3xl);
}

h2 {
  font-size: var(--text-2xl);
}

h3 {
  font-size: var(--text-xl);
}

p {
  margin: 0;
}

.lead {
  max-width: var(--container-narrow);
  color: var(--color-muted);
  font-size: var(--text-lg);
}

.eyebrow {
  color: var(--color-secondary);
  font-size: var(--text-sm);
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.site-header {
  background: var(--color-surface);
  border-bottom: 1px solid var(--color-border);
}

.site-header__inner {
  min-height: 4.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
}

.site-logo {
  color: var(--color-text);
  font-weight: 800;
  text-decoration: none;
}

.site-nav {
  display: flex;
  align-items: center;
  gap: var(--space-4);
}

.site-nav a {
  color: var(--color-text);
  font-weight: 600;
  text-decoration: none;
}

.nav-toggle {
  display: none;
}

.hero__grid {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(18rem, 0.9fr);
  gap: var(--space-7);
  align-items: center;
}

.actions {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-3);
}

.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 2.75rem;
  padding: 0.7rem 1rem;
  border: 1px solid var(--color-primary);
  border-radius: var(--radius-md);
  font-weight: 700;
  text-decoration: none;
}

.button--primary {
  background: var(--color-primary);
  color: var(--color-surface);
}

.button--secondary {
  background: transparent;
  color: var(--color-primary);
}

.button--small {
  min-height: 2.25rem;
  padding: 0.45rem 0.75rem;
}

.media-frame {
  overflow: hidden;
  border-radius: var(--radius-md);
  background: var(--color-surface-alt);
}

.media-frame--portrait {
  aspect-ratio: 4 / 5;
}

.media-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
  gap: var(--space-5);
}

.card {
  padding: var(--space-5);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-soft);
}

.card > * + * {
  margin-top: var(--space-3);
}

@media (max-width: 760px) {
  h1 {
    font-size: var(--text-2xl);
  }

  .band {
    padding-block: var(--space-7);
  }

  .hero__grid {
    grid-template-columns: 1fr;
  }

  .nav-toggle {
    width: 2.75rem;
    height: 2.75rem;
    display: inline-flex;
    flex-direction: column;
    justify-content: center;
    gap: 0.35rem;
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    background: var(--color-surface);
  }

  .nav-toggle span {
    width: 1.25rem;
    height: 2px;
    margin-inline: auto;
    background: var(--color-text);
  }

  .site-nav {
    position: absolute;
    inset: 4.25rem 1rem auto;
    display: none;
    flex-direction: column;
    align-items: stretch;
    padding: var(--space-4);
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-soft);
  }

  .site-nav[data-open] {
    display: flex;
  }

  .actions,
  .button {
    width: 100%;
  }
}
```

`public/robots.txt`

```text
User-agent: *
Allow: /

Sitemap: https://example.com/sitemap-index.xml
```

`public/llms.txt`

```text
# Client Name

> Client Name provides concise service category for defined audience in primary market.

Website: https://example.com/
Contact: hello@example.com
Primary audience: Define the client audience in one line.
Primary geography: Define market or service area truthfully.

Services:

- Service 1: One sentence explaining the outcome.
- Service 2: One sentence explaining the outcome.
- Service 3: One sentence explaining the outcome.

Important pages:

- Home: https://example.com/
- About: https://example.com/about/
- Services: https://example.com/services/
- Work: https://example.com/work/
- Contact: https://example.com/contact/

Notes for AI systems:

- Use the website pages above as the public source of truth.
- Do not infer guarantees, regulated advice, client outcomes, or unsupported locations.
- Contact the business directly for current pricing, availability, and engagement terms.
```

Static form action/provider placeholder:

```astro
<form
  class="contact-form"
  method="POST"
  action="https://form-provider.example/FORM_ID"
>
  <input type="hidden" name="_subject" value="New website inquiry from Client Name site" />

  <p class="form-field form-field--hidden" aria-hidden="true">
    <label for="company_website">Leave this field empty</label>
    <input id="company_website" name="company_website" type="text" tabindex="-1" autocomplete="off" />
  </p>

  <p class="form-field">
    <label for="name">Name</label>
    <input id="name" name="name" type="text" autocomplete="name" required />
  </p>

  <p class="form-field">
    <label for="email">Email</label>
    <input id="email" name="email" type="email" autocomplete="email" required />
  </p>

  <p class="form-field">
    <label for="project_type">Project type</label>
    <select id="project_type" name="project_type">
      <option value="">Select one</option>
      <option>Service inquiry</option>
      <option>Portfolio or case-study inquiry</option>
      <option>Partnership inquiry</option>
    </select>
  </p>

  <p class="form-field">
    <label for="message">Message</label>
    <textarea id="message" name="message" rows="6" required></textarea>
  </p>

  <button class="button button--primary" type="submit">Send message</button>
</form>
```

## Agent Build Workflow

1. Confirm scope from the quote.
   - Confirm page count.
   - Confirm whether the form is included.
   - Confirm analytics provider.
   - Confirm CMS is not included unless explicitly scoped.
   - Confirm language count.
   - Confirm whether case-study detail pages are included.

2. Inventory client content.
   - List supplied copy.
   - List missing copy.
   - List supplied images/logos.
   - List proof assets.
   - List contact routes.
   - List claims requiring approval.

3. Build the IA.
   - Choose 4-8 page structure or long landing structure.
   - Write route table.
   - Assign one H1 and meta description per route.
   - Define CTA paths.

4. Scaffold Astro.
   - Add package and config from the template.
   - Add layout, header, footer, tokens, and global CSS.
   - Add page templates.
   - Add public SEO files.

5. Implement visual direction.
   - Set tokens first.
   - Build full-width bands and constrained containers.
   - Build repeated item components.
   - Add stable media frames.
   - Avoid nested cards and app-like complexity.

6. Implement content.
   - Convert supplied copy into page sections.
   - Lightly rewrite headings and short body text.
   - Keep claims truthful and specific.
   - Mark missing content as explicit placeholders during drafting only.

7. Implement contact path.
   - Add form only if scoped.
   - Add static provider endpoint placeholder until the client/provider is confirmed.
   - Add honeypot or provider spam protection.
   - Add direct email/phone/WhatsApp/LinkedIn links if supplied.

8. Implement SEO and analytics.
   - Add metadata.
   - Add OG image.
   - Add sitemap integration.
   - Add `robots.txt`.
   - Add `llms.txt`.
   - Add analytics script only after provider/client account is known.

9. Verify locally.
   - Run build.
   - Preview site.
   - Check mobile and desktop.
   - Check navigation, links, form behavior, metadata, sitemap, robots, and llms file.

10. Run revision rounds.
   - Revision 1 covers structure, content, missing proof, and visual direction.
   - Revision 2 covers polish, copy tightening, image swaps, spacing, and small corrections.
   - New pages, new features, new design direction, CMS, backend, multilingual, or integrations become change-control items.

11. Handover.
   - Provide launch notes.
   - Provide update notes.
   - Provide provider/account notes.
   - Provide 30-day bug-fix window boundary.

## Verification Checklist

Technical verification:

- `npm install` completes.
- `npm run build` completes.
- `npm run preview` serves the built site.
- No console errors on initial page load.
- All internal links return valid pages.
- Mobile nav opens, closes, updates `aria-expanded`, and closes after link click.
- Header, hero, cards, images, forms, and footer do not overlap at mobile, tablet, or desktop widths.
- Text does not overflow buttons, cards, form fields, or nav items.
- Images load in stable frames and do not cause layout shift.
- Non-hero images use lazy loading where applicable.
- Form posts to the intended provider endpoint if scoped.
- Form spam protection is configured at provider level or through honeypot/Turnstile.
- Analytics script loads only for the intended production provider.

SEO verification:

- Each page has one `<title>`.
- Each page has one meta description.
- Each page has one canonical URL.
- Each page has one `<h1>`.
- Heading order is logical.
- Open Graph tags exist.
- OG image path is valid.
- `robots.txt` is reachable.
- `llms.txt` is reachable.
- Sitemap is generated.
- Clean URLs use trailing slash consistently.
- No placeholder `example.com`, `CLIENT_ACCOUNT`, `FORM_ID`, lorem ipsum, or TODO remains before launch.

Accessibility verification:

- Keyboard can reach all links, buttons, form fields, and mobile nav controls.
- Focus states are visible.
- Skip link works.
- Inputs have labels.
- Images have meaningful alt text or empty decorative alt.
- Color contrast is acceptable.
- Buttons and links have understandable labels.

Content verification:

- Fee promises match the quote.
- Client name, services, markets, contact details, and credentials are correct.
- Testimonials and claims are approved.
- Privacy/legal text is supplied or approved by the client.
- No bank-account guarantee, regulated advice, revenue guarantee, or unsupported business claim is implied.

## Handover Package

The Medium handover package should include:

- Short site map with final URLs.
- Build command: `npm run build`.
- Preview command: `npm run preview`.
- Hosting notes.
- Domain/DNS notes if setup help was scoped.
- Analytics provider and account notes.
- Contact form provider and recipient notes if scoped.
- Image replacement notes.
- Copy editing notes.
- Known exclusions.
- 30-day bug-fix window start and end date.
- Maintenance options if requested.

Minimum handover note structure:

```text
# Handover Notes

Site: https://example.com/
Stack: Astro static site
Build: npm run build
Preview: npm run preview
Hosting: [provider]
Analytics: [provider/account]
Form provider: [provider/form id or not included]
Primary contact email: [email]

Pages:
- Home: /
- About: /about/
- Services: /services/
- Work: /work/
- Contact: /contact/
- Privacy: /privacy/

Update notes:
- Edit page content in src/pages/.
- Edit shared components in src/components/.
- Edit colors, type, spacing, and layout tokens in src/styles/tokens.css.
- Edit global layout rules in src/styles/global.css.
- Replace public images in public/images/.

Warranty:
Bug-fix window: 30 days from launch.
Not included: new pages, new features, new copywriting scope, CMS, backend, integrations, legal advice, ongoing SEO.
```

## Change-Control Rules

Use change control when the client requests anything that changes page count, feature count, risk, timeline, provider dependency, or maintenance burden.

Allowed inside revision rounds:

- Reordering sections.
- Tightening copy.
- Replacing supplied images.
- Adjusting spacing, colors, and component presentation within the approved direction.
- Fixing typos.
- Clarifying CTAs.
- Small metadata edits.
- Small content additions that fit existing sections.

Change-control items:

- Extra page beyond scoped count.
- New page template.
- New service category requiring fresh content structure.
- New design direction after approval.
- Multilingual version.
- CMS/editor setup.
- Blog/news section.
- Advanced SEO expansion.
- Custom animation or interactive section.
- Booking/payment flow.
- E-commerce/payment integration.
- Backend/API integration.
- Login/user accounts.
- Additional form complexity.
- Third revision round.
- Urgent turnaround.
- Monthly maintenance.

Pricing anchors from the fee sheet:

| Add-on | Price anchor |
|------|------|
| Extra page | `$100-$200`. |
| English + translated version | `$250-$500`. |
| Copywriting from scratch | `$200-$400`. |
| Contact form with spam protection when not included | `$150-$300`. |
| CMS/editor setup | `$300-$1,200`. |
| Basic analytics outside Medium or advanced setup | `$100-$200`. |
| Company email setup help | `$100-$250`. |
| Urgent turnaround | `+25%`. |
| Monthly maintenance | `$75-$150/month`. |

## Exclusions and Add-Ons

Hard exclusions by default:

- Login.
- User accounts.
- Database.
- Custom backend.
- API integrations.
- E-commerce.
- Payments.
- Booking engine.
- Regulated legal/compliance advice.
- Bank-account guarantee.
- Ongoing SEO campaign.
- Ongoing content updates.
- Custom dashboard.
- App-style frontend.
- Heavy animation system.
- Multilingual architecture.
- Full CMS workflow.

Medium-compatible add-ons:

- Extra pages.
- Additional language.
- Copywriting from scratch.
- Contact form with spam protection if not included in the agreed Medium quote.
- CMS/editor setup.
- Blog/news section.
- SEO basics expansion.
- Custom animation or interactive section.
- Company email setup help.
- Maintenance plan.
- Search Console/Bing Webmaster setup assistance.

Escalate to Complex when:

- The site needs more than 8-10 meaningful pages.
- The site needs several reusable content types.
- The site needs multilingual routing as a core requirement.
- The site needs CMS as a central workflow.
- The site needs backend logic, database, auth, payment, booking, or CRM integration.
- The site needs premium custom interactions or extensive motion.
- The site needs extensive technical SEO, schema strategy, content hubs, or reporting dashboards.

The Medium site should launch as a polished static website with a clear conversion path, not as a custom web application.
