---
type: business
description: Technical boilerplate spec for the basic simple website package
last_updated: 2026-05-21
tags: [business, pricing, package, basic, simple-website, spec, boilerplate]
source_file: "Luca Kosowski Website fees.docx"
related_files:
  - graphify-out/converted/Luca Kosowski Website fees_cd1a932d.md
  - Portfolio-main/index.html
  - Portfolio-main/styles.css
related:
  - business/business-service-offers
  - projects/portfolio-main
  - implementation/impl-portfolio-static-site
---

# Website Spec: Basic

Back: [[business/business-service-offers]] · [[MOC/MOC-Business]]

## Purpose and Fit

The basic package maps to the fee-sheet `Simple Website` package. It is a real small public website with intentional design and professional presentation. It is the lowest recommended tier for a credible public website rather than a temporary placeholder.

Fee-sheet facts that must remain true:

| Field | Basic/simple package scope |
|------|------|
| Name | Simple Website |
| Price | `$750-$1,200`, depending on market and supplied content. |
| Purpose | Real small public website. |
| Best use | One-page consultant site, small business presence, simple portfolio, clean landing page. |
| Pages | 1 full page, or up to 2-3 very simple pages. |
| Design | Simple but intentionally designed. |
| Copy | Client supplies copy; text is lightly structured and polished. |
| Images/logo | Basic placement, cropping, and optimization. |
| Revisions | 1 thorough revision round. |
| SEO | Basic metadata, headings, alt text, sitemap if relevant. |
| Contact | Email link, WhatsApp link, or simple contact CTA. |
| CMS | Optional paid add-on. |
| Form/backend | Not provided by default. |
| Login | Not provided. |
| Analytics | Optional basic setup. |
| Handover | Short handover notes. |
| Warranty | One month for slight enhancements and improvement window. |

Use `Portfolio-main/` as the local reference for the basic static-site modality: direct HTML files, one shared CSS file, assets in the same project folder, no package manager, no build step, and simple navigation.

## Recommended Stack Decision

Default stack:

- Plain HTML.
- Plain CSS.
- Optional tiny vanilla JavaScript only for mobile navigation.
- No build pipeline.
- No package manager.
- No backend.
- No CMS.
- No login.
- No database.

Choose the smaller implementation that satisfies the actual scope:

| Scope | Recommended stack | Reason |
|------|------|------|
| 1 page | Plain `index.html` plus `styles.css` | Fastest, easiest for agents/humans to inspect and edit. |
| 2-3 very simple pages | Plain HTML files plus shared `styles.css` | Still manageable if nav/meta are not complex. |
| 2-3 pages with repeated components, sitemap, or future page additions | Astro static output | Prevents duplicated header/footer/meta drift. |
| Multilingual, CMS, blog, forms, integrations | Not Basic | Quote as add-on or move to Medium/Complex. |

Basic is intentionally not a miniature complex project. Do not add Astro unless it reduces real duplication. Do not add React, Tailwind, Bootstrap, databases, auth, CMS, or form services by default.

## Non-Negotiable Scope Boundaries

Included:

- 1 full page or up to 2-3 very simple pages.
- Responsive layout.
- Basic header/navigation where useful.
- Hero with clear offer, audience, and CTA.
- 3-6 content sections.
- Contact CTA using direct links.
- Basic metadata.
- Basic image optimization.
- Light copy structuring.
- One thorough revision round.
- Short handover notes.

Not included by default:

- Contact form backend.
- CMS/editor.
- Multiple revision rounds.
- Copywriting from scratch.
- Translation.
- Advanced SEO.
- Blog/news.
- Booking/payments.
- E-commerce.
- API integration.
- Login/user accounts.
- Analytics unless added.
- Hosting/domain/email provider fees.
- Ongoing updates.

Inside a revision round:

- Edit supplied copy.
- Replace supplied images.
- Adjust spacing/colors within the chosen direction.
- Reorder existing sections.
- Fix mobile spacing.
- Fix typos and metadata.

Outside a revision round:

- New page.
- New language.
- New design direction.
- New technical feature.
- New backend/service provider.
- New copywriting scope.

## Information Architecture

Default one-page IA:

| Section | Purpose | Required elements |
|------|------|------|
| Header | Orientation | Brand/name, 3-5 anchor links, contact CTA if room. |
| Hero | Immediate clarity | H1, short lead, primary CTA, optional secondary CTA, optional image. |
| Trust strip | Credibility | 3 proof points, years, locations, services, clients, or credentials if true. |
| Services/offer | What is provided | 3-4 short service blocks. |
| Process | How it works | 3 steps, no dense copy. |
| About | Who is behind it | Short bio/company note and optional image. |
| Contact | Action | Email/WhatsApp/phone/location links. |
| Footer | Closure | Copyright, privacy link if present, contact repeat. |

Optional 2-3 page IA:

| File | Purpose |
|------|------|
| `index.html` | Home / offer / contact CTA. |
| `about.html` | Bio, credentials, story. |
| `services.html` | Service details and FAQ. |

Keep page count small. If each page starts needing its own components, templates, and SEO logic, use the Medium Astro spec instead.

## File Tree

Default plain static tree:

```text
client-basic-site/
  index.html
  styles.css
  robots.txt
  llms.txt
  favicon.svg
  og-image.jpg
  images/
    hero.jpg
    profile.jpg
```

Optional 2-3 page plain tree:

```text
client-basic-site/
  index.html
  about.html
  services.html
  styles.css
  script.js
  robots.txt
  sitemap.xml
  llms.txt
  images/
```

Optional Astro alternate:

```text
client-basic-astro/
  package.json
  astro.config.mjs
  public/
    robots.txt
    llms.txt
    images/
  src/
    layouts/Base.astro
    components/Header.astro
    components/Footer.astro
    pages/index.astro
    pages/about.astro
    pages/services.astro
    styles/global.css
```

## Frontend Development Spec

HTML rules:

- Use semantic tags: `header`, `nav`, `main`, `section`, `article`, `footer`.
- One visible `<h1>`.
- Heading order must be logical.
- Use anchors for direct CTAs: `mailto:`, `tel:`, WhatsApp, directions.
- Use real lists for process and service lists.
- Use `button` only for real interactive controls.
- Do not use empty decorative divs to create layout.
- Do not inline large styles in HTML.
- Do not duplicate the same CSS rule across page files.

CSS rules:

- Mobile-first.
- Use CSS custom properties.
- Use a restrained color system.
- Stable content width.
- Stable image frames.
- Buttons must not overflow on small screens.
- Cards only for repeated items.
- No nested cards.
- No heavy shadows or generic glossy template treatment.
- Keep line length readable, ideally `60-75ch` for paragraphs.
- Use `@media (min-width: 760px)` for the main desktop split.
- Use `@media (prefers-reduced-motion: reduce)`.

JavaScript rules:

- No JS required for content access.
- Optional mobile nav toggle only.
- No dependencies.
- No carousels.
- No animation framework.
- No tracking script unless analytics is explicitly added.

Accessibility rules:

- Include a skip link.
- Visible focus state.
- Mobile nav button has `aria-expanded`.
- Image alt text is truthful.
- Decorative images use empty alt.
- Link text describes the action.
- Tap targets are at least comfortable thumb size.
- Color contrast is manually checked.

## Backend and Contact Spec

No backend is included.

Default contact methods:

```html
<a class="button button--primary" href="mailto:hello@example.com">Email us</a>
<a class="button button--secondary" href="https://wa.me/10000000000">WhatsApp</a>
<a class="button button--secondary" href="tel:+10000000000">Call</a>
```

Rules:

- Do not add a `<form>` unless contact form add-on is purchased.
- Do not add Formspree/Basin/Netlify Forms unless scoped.
- Do not collect personal data in a static page without privacy copy.
- Do not imply 24/7 availability unless the client approves it.
- Do not publish phone, address, or social links unless client confirms them.

If contact form add-on is purchased:

- Move to Medium form pattern or add a static provider.
- Add honeypot or provider spam protection.
- Add success/failure behavior.
- Add privacy note if personal data is collected.

## SEO and Launch Spec

Basic SEO:

- `<title>`.
- Meta description.
- Viewport tag.
- Open Graph title/description/image if an image exists.
- Clean headings.
- Descriptive links.
- Alt text.
- `robots.txt`.
- `llms.txt` if useful.
- `sitemap.xml` only if there are multiple public pages or the host does not generate one.

Do not include:

- Schema strategy unless facts are simple and verified.
- Keyword pages.
- Blog.
- Ongoing SEO plan.
- Ranking claims.
- AI-search claims beyond a truthful `llms.txt`.

Launch checks:

- Open `index.html` directly in browser.
- Test at 320px, 390px, 768px, and desktop.
- Click contact links.
- Check image paths.
- Check metadata.
- Check no horizontal scroll.
- Check spelling.
- Confirm provider/domain paths if deployed.

## Design System Rules

Basic design system:

| Token | Default role |
|------|------|
| `--bg` | Page background. |
| `--surface` | Repeated content cards or panels. |
| `--text` | Primary text. |
| `--muted` | Secondary text. |
| `--line` | Borders/dividers. |
| `--accent` | Primary CTA and link accent. |
| `--accent-dark` | Hover/focus/pressed state. |
| `--radius` | 8px maximum for cards/buttons. |
| `--container` | Max content width. |

Layout rules:

- Header should be compact.
- Hero should show the actual business/person/service signal in the first viewport.
- Do not use a hero that is just vague abstract copy.
- Use full-width page sections with inner containers.
- Use one primary CTA per section.
- Avoid card-heavy marketing pages.
- If using a hero image, it should be meaningful and not dark/blurred stock filler.
- Footer should repeat contact and include the business name.

## Content and Assets

Client supplies:

- Business/person name.
- Contact email.
- Phone/WhatsApp if used.
- Location/service area if used.
- Logo if available.
- 1-4 images if available.
- Core copy.
- Proof/testimonial if used.
- Any legal/privacy copy if needed.

Included:

- Light copy polish.
- Section ordering.
- Headline tightening.
- Basic image cropping and compression.
- Alt text.
- Metadata.

Not included:

- Full copywriting.
- Brand identity.
- Logo design.
- Photography.
- Translation.
- Legal/privacy drafting.
- Ongoing updates.

Asset rules:

- Store images in `images/`.
- Use lowercase hyphen filenames.
- Compress images before launch.
- Use `width` and `height` on images.
- Use SVG favicon only if simple and owned/approved.

## Code Template

`index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Client Name | Clear Service Outcome</title>
    <meta name="description" content="Client Name helps a defined audience with a defined service outcome in a defined market.">
    <meta property="og:title" content="Client Name | Clear Service Outcome">
    <meta property="og:description" content="Client Name helps a defined audience with a defined service outcome in a defined market.">
    <meta property="og:type" content="website">
    <meta property="og:image" content="og-image.jpg">
    <link rel="icon" href="favicon.svg" type="image/svg+xml">
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>

    <header class="site-header">
      <div class="container header-inner">
        <a class="logo" href="#top" aria-label="Client Name home">Client Name</a>
        <button class="menu-toggle" type="button" aria-controls="site-nav" aria-expanded="false">
          <span class="menu-toggle__line"></span>
          <span class="menu-toggle__line"></span>
          <span class="menu-toggle__line"></span>
          <span class="visually-hidden">Menu</span>
        </button>
        <nav class="site-nav" id="site-nav">
          <a href="#services">Services</a>
          <a href="#process">Process</a>
          <a href="#about">About</a>
          <a href="#contact">Contact</a>
        </nav>
      </div>
    </header>

    <main id="main">
      <section class="hero section" id="top">
        <div class="container hero-grid">
          <div class="hero-copy">
            <p class="eyebrow">Service category in location</p>
            <h1>Clear result for the people who need it.</h1>
            <p class="lead">Replace this with one concrete paragraph explaining who the client helps, what they do, and why the visitor should act now.</p>
            <div class="actions">
              <a class="button button--primary" href="mailto:hello@example.com">Email us</a>
              <a class="button button--secondary" href="https://wa.me/10000000000">WhatsApp</a>
            </div>
          </div>
          <figure class="hero-media">
            <img src="images/hero.jpg" alt="Client Name providing the service in a real context" width="900" height="700">
          </figure>
        </div>
      </section>

      <section class="section section--surface" aria-labelledby="trust-title">
        <div class="container">
          <h2 id="trust-title">Why clients use this service</h2>
          <div class="proof-grid">
            <p><strong>Local.</strong> Service area or market proof.</p>
            <p><strong>Direct.</strong> Fast contact path without account creation.</p>
            <p><strong>Clear.</strong> Simple scope and realistic next step.</p>
          </div>
        </div>
      </section>

      <section class="section" id="services" aria-labelledby="services-title">
        <div class="container">
          <p class="eyebrow">Services</p>
          <h2 id="services-title">Focused support without overcomplication.</h2>
          <div class="card-grid">
            <article class="card">
              <h3>Service one</h3>
              <p>Short description of the outcome and when it is useful.</p>
            </article>
            <article class="card">
              <h3>Service two</h3>
              <p>Short description of the outcome and when it is useful.</p>
            </article>
            <article class="card">
              <h3>Service three</h3>
              <p>Short description of the outcome and when it is useful.</p>
            </article>
          </div>
        </div>
      </section>

      <section class="section section--surface" id="process" aria-labelledby="process-title">
        <div class="container">
          <p class="eyebrow">Process</p>
          <h2 id="process-title">How it works</h2>
          <ol class="steps">
            <li><strong>Contact.</strong> Send the basic details and preferred contact method.</li>
            <li><strong>Confirm.</strong> The scope, timing, and next action are confirmed.</li>
            <li><strong>Proceed.</strong> Work starts or the client receives the right referral.</li>
          </ol>
        </div>
      </section>

      <section class="section" id="about" aria-labelledby="about-title">
        <div class="container narrow">
          <p class="eyebrow">About</p>
          <h2 id="about-title">A short credibility note.</h2>
          <p>Use this section for a brief founder/company note, not a full biography. Keep it factual, specific, and easy to scan.</p>
        </div>
      </section>

      <section class="section cta-section" id="contact" aria-labelledby="contact-title">
        <div class="container">
          <p class="eyebrow">Contact</p>
          <h2 id="contact-title">Ready to speak?</h2>
          <p>Use direct contact links. A form is not included in the basic package unless purchased as an add-on.</p>
          <div class="actions">
            <a class="button button--primary" href="mailto:hello@example.com">hello@example.com</a>
            <a class="button button--secondary" href="tel:+10000000000">Call</a>
          </div>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <div class="container footer-inner">
        <p>Client Name</p>
        <p><a href="mailto:hello@example.com">hello@example.com</a></p>
      </div>
    </footer>

    <script src="script.js" defer></script>
  </body>
</html>
```

`styles.css`

```css
:root {
  --bg: #f7f4ee;
  --surface: #ffffff;
  --surface-alt: #ece7dc;
  --text: #171717;
  --muted: #5e5e5e;
  --line: rgba(23, 23, 23, 0.14);
  --accent: #1d4ed8;
  --accent-dark: #153a9b;
  --focus: #111111;
  --radius: 8px;
  --container: 1120px;
  --narrow: 720px;
  --space-section: clamp(4rem, 8vw, 7rem);
  --font: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  font-family: var(--font);
  color: var(--text);
  background: var(--bg);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

img {
  display: block;
  max-width: 100%;
  height: auto;
}

a {
  color: inherit;
}

:focus-visible {
  outline: 3px solid var(--focus);
  outline-offset: 4px;
}

.skip-link {
  position: absolute;
  left: 1rem;
  top: 1rem;
  z-index: 100;
  transform: translateY(-160%);
  background: var(--text);
  color: var(--surface);
  padding: 0.75rem 1rem;
}

.skip-link:focus {
  transform: translateY(0);
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}

.container {
  width: min(100% - 2rem, var(--container));
  margin-inline: auto;
}

.narrow {
  max-width: var(--narrow);
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 20;
  background: color-mix(in srgb, var(--bg) 92%, transparent);
  border-bottom: 1px solid var(--line);
  backdrop-filter: blur(10px);
}

.header-inner,
.footer-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding-block: 1rem;
}

.logo {
  font-weight: 800;
  text-decoration: none;
}

.site-nav {
  display: none;
  gap: 1rem;
  align-items: center;
}

.site-nav a {
  text-decoration: none;
  color: var(--muted);
  font-weight: 650;
}

.site-nav a:hover {
  color: var(--text);
}

.menu-toggle {
  display: inline-grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: var(--surface);
  gap: 4px;
}

.menu-toggle__line {
  width: 18px;
  height: 2px;
  background: var(--text);
}

.site-nav.is-open {
  display: grid;
  position: absolute;
  left: 1rem;
  right: 1rem;
  top: calc(100% + 0.5rem);
  padding: 1rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
}

.section {
  padding-block: var(--space-section);
}

.section--surface {
  background: var(--surface-alt);
}

.hero {
  min-height: min(760px, calc(100dvh - 76px));
  display: grid;
  align-items: center;
}

.hero-grid {
  display: grid;
  gap: 2rem;
}

.hero h1,
.section h2 {
  margin: 0;
  line-height: 1.08;
  letter-spacing: 0;
}

.hero h1 {
  font-size: clamp(2.4rem, 10vw, 4.75rem);
  max-width: 12ch;
}

.section h2 {
  font-size: clamp(2rem, 7vw, 3.25rem);
  max-width: 16ch;
}

.lead {
  max-width: 58ch;
  color: var(--muted);
  font-size: 1.125rem;
}

.eyebrow {
  margin: 0 0 1rem;
  color: var(--accent);
  font-size: 0.78rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1.5rem;
}

.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 0.8rem 1.1rem;
  border: 1px solid var(--accent);
  border-radius: var(--radius);
  text-decoration: none;
  font-weight: 800;
}

.button--primary {
  background: var(--accent);
  color: #ffffff;
}

.button--primary:hover {
  background: var(--accent-dark);
  border-color: var(--accent-dark);
}

.button--secondary {
  color: var(--accent);
  background: transparent;
}

.hero-media {
  margin: 0;
  border-radius: var(--radius);
  overflow: hidden;
  aspect-ratio: 4 / 3;
  background: var(--surface-alt);
}

.hero-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.proof-grid,
.card-grid {
  display: grid;
  gap: 1rem;
  margin-top: 2rem;
}

.card {
  padding: 1.25rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
}

.card h3 {
  margin: 0 0 0.5rem;
}

.steps {
  display: grid;
  gap: 1rem;
  padding: 0;
  margin: 2rem 0 0;
  list-style: none;
  counter-reset: steps;
}

.steps li {
  counter-increment: steps;
  padding-top: 1rem;
  border-top: 1px solid var(--line);
}

.steps li::before {
  content: counter(steps, decimal-leading-zero);
  display: block;
  color: var(--accent);
  font-weight: 800;
  margin-bottom: 0.5rem;
}

.cta-section {
  background: var(--text);
  color: var(--surface);
}

.cta-section p {
  color: color-mix(in srgb, var(--surface) 78%, transparent);
}

.site-footer {
  border-top: 1px solid var(--line);
}

@media (min-width: 760px) {
  .menu-toggle {
    display: none;
  }

  .site-nav {
    display: flex;
  }

  .hero-grid {
    grid-template-columns: minmax(0, 1.05fr) minmax(280px, 0.8fr);
    align-items: center;
  }

  .proof-grid,
  .card-grid,
  .steps {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    scroll-behavior: auto !important;
    transition: none !important;
  }
}
```

`script.js`

```js
const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#site-nav');

toggle?.addEventListener('click', () => {
  const isOpen = nav?.classList.toggle('is-open') ?? false;
  toggle.setAttribute('aria-expanded', String(isOpen));
});

nav?.addEventListener('click', (event) => {
  if (event.target instanceof HTMLAnchorElement) {
    nav.classList.remove('is-open');
    toggle?.setAttribute('aria-expanded', 'false');
  }
});
```

`robots.txt`

```txt
User-agent: *
Allow: /

Sitemap: https://example.com/sitemap.xml
```

`llms.txt`

```txt
# Client Name

> Client-approved one-sentence description.

## Key facts

- Public name: Client Name.
- Service: [service].
- Service area: [area].
- Contact: hello@example.com.

## Pages

- Home: https://example.com/
- Contact: https://example.com/#contact

## Do not claim

Do not infer rankings, guarantees, licenses, client counts, or legal outcomes unless the visible website states them.
```

Optional Astro alternate:

```astro
---
// src/layouts/Base.astro
interface Props {
  title: string;
  description: string;
}
const { title, description } = Astro.props;
---
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{title}</title>
    <meta name="description" content={description} />
    <link rel="stylesheet" href="/src/styles/global.css" />
  </head>
  <body>
    <slot />
  </body>
</html>
```

## Agent Build Workflow

1. Confirm whether this is 1 page or 2-3 simple pages.
2. Confirm contact routes: email, WhatsApp, phone, directions.
3. Collect client copy and assets.
4. Choose plain static default unless duplication justifies Astro.
5. Build HTML structure before styling.
6. Add CSS tokens and layout.
7. Add images with dimensions and alt text.
8. Add metadata.
9. Add `robots.txt` and optional `llms.txt`.
10. Inspect desktop and mobile.
11. Apply one revision round.
12. Write short handover notes.

## Verification Checklist

For plain HTML:

- Open `index.html` directly.
- Resize to 320px, 390px, 768px, desktop.
- Test contact links.
- Test mobile nav if used.
- Validate every image path.
- Confirm no horizontal scroll.
- Confirm one `<h1>`.
- Confirm heading order.
- Confirm title/description.
- Confirm no placeholder copy remains.
- Confirm no form/backend exists unless scoped.

If Astro was used:

```bash
npm run build
npm run preview
```

## Handover Package

Deliver:

- `index.html`.
- `styles.css`.
- `script.js` if used.
- `images/`.
- `robots.txt`.
- `llms.txt` if used.
- Short `HANDOVER.md`.

Minimum `HANDOVER.md`:

```md
# Client Name Basic Website Handover

Stack: plain HTML/CSS.
Main page: index.html.
Styles: styles.css.
Images: images/.
Contact links:
- Email: hello@example.com
- WhatsApp: [link]
- Phone: [link]

Warranty:
One month for slight enhancements and improvement window.

Not included:
Forms, backend, CMS, login, payment, ongoing SEO, future updates, new pages, translation.
```

## Change-Control Rules

Allowed in the revision round:

- Text corrections.
- Image replacement.
- CTA wording changes.
- Minor section reorder.
- Minor color/spacing changes.
- Metadata correction.
- Mobile fix.

Add-on or new quote:

- Extra page.
- Translated version.
- Copywriting from scratch.
- Contact form with spam protection.
- Basic analytics.
- Company email setup help.
- Urgent turnaround.
- Monthly maintenance.
- CMS/editor setup.
- New design direction.

## Exclusions and Add-Ons

Fee-sheet anchors:

| Add-on | Price anchor |
|------|------|
| Extra page | `$100-$200` |
| English + translated version | `$250-$500` |
| Copywriting from scratch | `$200-$400` |
| Contact form with spam protection | `$150-$300` |
| Basic analytics | `$100-$200` |
| Company email setup help | `$100-$250` |
| Urgent turnaround | `+25%` |
| Monthly maintenance | `$75-$150/month` |
| CMS/editor setup | `$300-$1,200` |

Hard exclusions:

- Bank-account guarantee.
- Legal/compliance advice.
- Hosting/domain/email provider fees.
- Future updates outside the included window.
- Login/user accounts.
- E-commerce/payments.
- Custom backend/API.
- Ongoing SEO.
