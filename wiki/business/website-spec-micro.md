---
type: business
description: Technical boilerplate spec for the micro emergency website package
last_updated: 2026-05-21
tags: [business, pricing, package, micro, emergency-website, spec, boilerplate]
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

# Website Spec: Micro

Back: [[business/business-service-offers]] · [[MOC/MOC-Business]]

## Purpose and Fit

The micro package maps to the fee-sheet `Micro Website - Emergency / testimonial` package. It is for a very fast, acceptable, mobile-readable online presence. It is not a strategic business website, not a lead-generation asset, and not a portfolio-level build.

Fee-sheet facts that must remain true:

| Field | Micro package scope |
|------|------|
| Price | Usually `$450-$650`. |
| Purpose | Need for a website to exist online quickly. |
| Best use | Bank-account proof, temporary company presence, friend/client favour, testimonial project. |
| Pages | Usually 1 page only. |
| Design | Template-led; minimal customization based on the client's profession. |
| Copy | Client supplies almost all text. |
| Images/logo | Client supplies, or simple placeholders are used. |
| Revisions | 1 correction round only. |
| SEO | Basic title and meta only. |
| Contact | Email link, WhatsApp link, or simple contact CTA. |
| CMS | Not provided. |
| Form/backend | Not provided. |
| Login | Not provided. |
| Analytics | Not provided. |
| Handover | Minimal. |
| Warranty | Bug and typo correction only, not new requests. |
| Obligation | Make it acceptable, live, mobile friendly, and looking clean. |

The micro tier is useful when the business needs public proof of existence, emergency contact, a temporary campaign page, a testimonial proof page, or a clean one-page presence while a larger site is not justified.

## Recommended Stack Decision

Default stack:

- One `index.html`.
- One `styles.css`.
- One optional `robots.txt`.
- Optional local image assets.
- No build step.
- No package manager.
- No JavaScript dependency.
- No backend.
- No form.
- No CMS.
- No login.
- No analytics.

Do not use Astro by default. Astro is only acceptable if the client explicitly upgrades to a larger tier or if this micro page is being inserted into an existing Astro website.

Decision table:

| Need | Micro decision |
|------|------|
| One-page online proof | Plain static HTML/CSS. |
| Emergency contact page | Plain static HTML/CSS with phone/WhatsApp/email CTAs. |
| Temporary company presence | Plain static HTML/CSS with legal name, address/service area, contact. |
| Testimonial project | Plain static HTML/CSS with quote/proof and CTA. |
| Menu/price list | Static repeated rows inside the same page. |
| Contact form | Not included; quote add-on or Basic/Medium. |
| Analytics | Not included; quote add-on or Basic/Medium. |
| CMS/editor | Not included; quote add-on or larger tier. |

## Non-Negotiable Scope Boundaries

Included:

- One page.
- Clean responsive layout.
- Clear first-screen identity.
- Direct contact CTA.
- Basic metadata.
- Basic image/logo placement.
- Minimal content sections.
- One correction round.
- Minimal handover.

Not included:

- Multi-page architecture.
- Strategic conversion copy.
- Custom design system.
- Professional copywriting.
- Translation.
- Form backend.
- CMS/editor.
- Login/user accounts.
- E-commerce/payments.
- Analytics.
- Ongoing SEO.
- Multiple revision rounds.
- Ongoing updates.
- Hosting/domain/email provider fees.
- Bank-account guarantee.
- Legal/compliance advice.

Micro change-control rule: if the client asks for "just one more section" that turns the page into a full business website, move it to Basic or Medium. Micro stays direct and small.

## Information Architecture

Default emergency/status micro IA:

| Section | Purpose | Required elements |
|------|------|------|
| Status strip | Immediate signal | Open/available/status text, last updated if relevant. |
| Header | Orientation | Name/logo, 2-4 anchors, contact CTA. |
| Hero | Main action | H1, short explanation, phone/WhatsApp/email CTA, service area. |
| Quick facts | Trust | 3 short facts: location, response time, service type, hours, license if true. |
| What we handle | Scope | 3-6 rows, no deep service copy. |
| What to do now | Action path | 3 short steps. |
| Proof | Confidence | One quote, review, credential, or "since" fact if true. |
| Contact/footer | Final action | Contact links, address/service area, hours, legal note if needed. |

Alternative testimonial/project micro IA:

| Section | Purpose |
|------|------|
| Hero | Project/person/company name and one-sentence credibility statement. |
| Proof | Quote, role, result, or client-approved testimonial. |
| Details | 3-5 factual rows. |
| Contact | Direct route to email/WhatsApp/LinkedIn. |

Keep the page under control. A micro site should usually fit in 5-8 visible sections and be easy to review in one pass.

## File Tree

```text
client-micro-site/
  index.html
  styles.css
  robots.txt
  favicon.svg
  images/
    logo.svg
    hero.jpg
```

If no real image is supplied:

- Use no image, or
- Use a simple color/media panel, or
- Use a client-approved placeholder.

Do not add:

```text
package.json
node_modules/
src/
cms/
api/
admin/
```

## Frontend Development Spec

HTML requirements:

- Use semantic HTML.
- One visible `<h1>`.
- Use section IDs for anchor navigation.
- Use direct CTAs with `mailto:`, `tel:`, WhatsApp, or directions links.
- Use lists for repeated services, steps, and facts.
- Use images only when they help the visitor understand the business/person/place.
- Do not include a form.
- Do not add tracking scripts.
- Do not add third-party widgets.

CSS requirements:

- Mobile-first.
- No framework.
- CSS variables for theme presets.
- Readable text at 320px.
- Buttons at least 44px tall.
- Stable image/media frames.
- No horizontal scroll.
- No nested cards.
- No hidden critical content.
- Use a sticky bottom CTA on mobile only if it does not obscure content.
- Use `prefers-reduced-motion` even if animation is minimal.

Permitted tiny interactions:

- None by default.
- Optional CSS-only anchor nav.
- Optional mobile menu only if needed; most micro pages should not need one.

Performance requirements:

- No webfont dependency unless approved.
- System fonts by default.
- Compress images.
- Avoid video.
- Avoid map embeds unless location is the core value.

## Backend and Contact Spec

No backend is included.

Allowed contact links:

```html
<a class="button button--primary" href="tel:+10000000000">Call now</a>
<a class="button button--secondary" href="https://wa.me/10000000000">WhatsApp</a>
<a class="button button--secondary" href="mailto:hello@example.com">Email</a>
<a class="button button--secondary" href="https://maps.google.com/?q=Client%20Address">Directions</a>
```

Rules:

- Publish only client-approved contact details.
- Do not imply 24/7 response unless confirmed.
- Do not collect personal data.
- Do not include newsletter signup.
- Do not include booking/payment.
- If a contact form is requested, quote the contact-form add-on or move to Basic/Medium.

## SEO and Launch Spec

Micro SEO is minimal:

- Title.
- Meta description.
- Viewport.
- Optional Open Graph tags.
- One `<h1>`.
- Basic headings.
- Alt text.
- `robots.txt`.

Optional `robots.txt`:

```txt
User-agent: *
Allow: /
```

Do not add:

- Sitemap unless the host requires it.
- Schema graph unless facts are obvious and verified.
- Keyword pages.
- `llms-full.txt`.
- Advanced SEO copy.
- Ranking claims.

Launch checks:

- Open page directly.
- Test at 320px.
- Click every contact CTA.
- Confirm title/description.
- Confirm images load.
- Confirm no placeholders remain.
- Confirm legal/compliance/bank guarantees are not implied.

## Design System Rules

Micro uses a template-level design system. It should look intentional, but it must not turn into a custom design system project.

Reference-style inputs gathered by specialized subagents:

| Reference | Usable style pattern | Access note |
|------|------|------|
| `https://rumbekeplatse.be` | Local/status style: ticker/status strip, compact header, oversized trust-building hero, direct CTAs, service/menu rows, reviews, hours/contact footer. | Live page and raw HTML/CSS reachable; no source/assets copied. |
| `https://piv.group` | Editorial/trust style: full-height hero, restrained typography, alternating calm sections, thin borders, persistent CTA, metrics/process rows. | Fetcher showed bot verification; read-only direct/static inspection was available to the subagent. |
| `https://www.omaralkhatib.com` | Personal-service style: sticky nav, two-column hero, portrait/trust signal, icon-led contact blocks, service/pricing cards. | Root had access friction; browser-like fetch/Jina reader exposed page order. |
| `https://mycommuters.com` | SaaS-guided style: dark hero, strong accent, scenario cards, numbered process, repeated final CTA. | Live page and public HTML/CSS were inspectable; no visual screenshot pass. |
| `https://shreej.al` | High-contrast row style: fixed header, large typographic hero, dark body sections, indexed rows, bordered action/resource lists. | Live page, HTML, JS, and CSS were accessible. |

Use those as style families, not as copied templates. Do not reuse their logos, images, exact copy, color hexes, motion systems, code, or brand voice.

Theme presets:

| Theme class | Inspired by | Best for | Visual rules |
|------|------|------|------|
| `theme-local` | Rumbeke Platse | Local emergency shop/service, food, repairs, neighborhood proof | Warm surface, dark hero, red/amber action color, status strip, hours footer. |
| `theme-institutional` | PIV-style editorial trust | Professional temporary presence, compliance-oriented proof | Off-white surfaces, navy/charcoal, sharp accent, thin borders, metric rows. |
| `theme-personal` | Omar personal-service pattern | Consultant/freelancer emergency page | Light gray, portrait media, teal accent, direct contact blocks. |
| `theme-guided` | MyCommuters SaaS journey | Product/demo/emergency process | Dark first viewport, bright accent, scenario cards, numbered process. |
| `theme-rows` | Shreej high-contrast rows | Developer/technical proof, urgent info page | Light hero, dark sections, indexed rows, strong typography. |

Micro typography:

- Use system fonts by default.
- Optional display serif only if it matches the theme and does not require a paid/external font.
- Keep body text 16px or larger.
- Keep headings large enough for clarity but not decorative.
- Letter spacing remains `0` except small uppercase labels.

## Content and Assets

Client supplies:

- Business/person name.
- One-sentence description.
- Contact email.
- Phone/WhatsApp if used.
- Service area/location if used.
- Hours/status if used.
- 1 quote/proof point if used.
- Logo/image if available.

Included:

- Place supplied copy into the template.
- Shorten obviously long lines.
- Basic typo cleanup.
- Basic image crop/compression.
- Basic title/meta description.

Not included:

- Writing copy from scratch.
- Brand identity.
- Logo design.
- New imagery.
- Translation.
- Legal/privacy drafting.
- SEO campaign.
- Analytics.

Content length targets:

| Area | Target |
|------|------|
| H1 | 5-12 words. |
| Lead | 1-2 short sentences. |
| Quick fact | 3-8 words each. |
| Service row | Title plus one sentence max. |
| Step | One direct action sentence. |
| Proof | One quote or one factual proof line. |

## Code Template

`index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Client Name | Emergency Service in City</title>
    <meta name="description" content="Client Name provides direct emergency service in City. Call, WhatsApp, or email for fast help.">
    <meta property="og:title" content="Client Name | Emergency Service in City">
    <meta property="og:description" content="Direct emergency service in City with phone, WhatsApp, and email contact.">
    <meta property="og:type" content="website">
    <meta property="og:image" content="images/hero.jpg">
    <link rel="icon" href="favicon.svg" type="image/svg+xml">
    <link rel="stylesheet" href="styles.css">
  </head>
  <body class="theme-local">
    <a class="skip-link" href="#main">Skip to content</a>

    <div class="status-strip" role="status">
      <span>Available today</span>
      <span>City service area</span>
      <span>Call for urgent help</span>
    </div>

    <header class="site-header">
      <div class="container header-inner">
        <a class="brand" href="#top" aria-label="Client Name home">Client Name</a>
        <nav class="nav" aria-label="Primary">
          <a href="#help">Help</a>
          <a href="#steps">Steps</a>
          <a href="#proof">Proof</a>
          <a href="#contact">Contact</a>
        </nav>
        <a class="header-cta" href="tel:+10000000000">Call</a>
      </div>
    </header>

    <main id="main">
      <section class="hero" id="top">
        <div class="container hero-grid">
          <div class="hero-copy">
            <p class="eyebrow">Emergency service / City</p>
            <h1>Fast help when the issue cannot wait.</h1>
            <p class="lead">Client Name helps with one clear emergency service. Use this line to state the exact problem handled, location, and next action.</p>
            <div class="actions" aria-label="Primary contact actions">
              <a class="button button--primary" href="tel:+10000000000">Call now</a>
              <a class="button button--secondary" href="https://wa.me/10000000000">WhatsApp</a>
              <a class="button button--ghost" href="mailto:hello@example.com">Email</a>
            </div>
          </div>
          <figure class="hero-card">
            <img src="images/hero.jpg" alt="Client Name team ready to help in City" width="900" height="720">
            <figcaption>Open today. Response depends on location and availability.</figcaption>
          </figure>
        </div>
      </section>

      <section class="facts" aria-label="Quick facts">
        <div class="container facts-grid">
          <p><strong>Area</strong><span>City and nearby</span></p>
          <p><strong>Contact</strong><span>Phone or WhatsApp</span></p>
          <p><strong>Scope</strong><span>Urgent service only</span></p>
        </div>
      </section>

      <section class="section" id="help" aria-labelledby="help-title">
        <div class="container split">
          <div>
            <p class="eyebrow">What we handle</p>
            <h2 id="help-title">Clear help, no complicated process.</h2>
          </div>
          <div class="rows">
            <article class="info-row">
              <span class="row-index">01</span>
              <div>
                <h3>Urgent issue type</h3>
                <p>One sentence explaining the specific problem handled.</p>
              </div>
            </article>
            <article class="info-row">
              <span class="row-index">02</span>
              <div>
                <h3>Same-day contact</h3>
                <p>Explain the fastest channel and realistic response expectation.</p>
              </div>
            </article>
            <article class="info-row">
              <span class="row-index">03</span>
              <div>
                <h3>Local proof</h3>
                <p>Add a service area, credential, review, or years active if true.</p>
              </div>
            </article>
          </div>
        </div>
      </section>

      <section class="section section--alt" id="steps" aria-labelledby="steps-title">
        <div class="container">
          <p class="eyebrow">What to do now</p>
          <h2 id="steps-title">Three steps.</h2>
          <ol class="steps">
            <li><strong>Call or message.</strong> Send the address, problem, and urgency.</li>
            <li><strong>Confirm availability.</strong> We confirm if this can be handled today.</li>
            <li><strong>Get the next action.</strong> You receive the time, route, or referral.</li>
          </ol>
        </div>
      </section>

      <section class="section" id="proof" aria-labelledby="proof-title">
        <div class="container proof-panel">
          <p class="eyebrow">Proof</p>
          <h2 id="proof-title">A short reason to trust this page.</h2>
          <blockquote>
            "Replace this with one approved testimonial or proof line. Do not invent reviews."
          </blockquote>
          <p class="proof-meta">Client-approved source, date, or context.</p>
        </div>
      </section>

      <section class="section contact-section" id="contact" aria-labelledby="contact-title">
        <div class="container contact-grid">
          <div>
            <p class="eyebrow">Contact</p>
            <h2 id="contact-title">Use the fastest route.</h2>
            <p>No contact form is included in the micro package. Use direct links only.</p>
          </div>
          <address class="contact-card">
            <a href="tel:+10000000000">+1 000 000 0000</a>
            <a href="https://wa.me/10000000000">WhatsApp</a>
            <a href="mailto:hello@example.com">hello@example.com</a>
            <span>City, Country</span>
          </address>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <div class="container footer-inner">
        <p>Client Name</p>
        <p>Bug/typo corrections only after launch unless a new scope is agreed.</p>
      </div>
    </footer>

    <a class="mobile-sticky-cta" href="tel:+10000000000">Call now</a>
  </body>
</html>
```

`styles.css`

```css
:root {
  --font: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --display: Georgia, "Times New Roman", serif;
  --bg: #f7f1e8;
  --surface: #ffffff;
  --surface-alt: #efe6d8;
  --text: #17110f;
  --muted: #665c55;
  --line: rgba(23, 17, 15, 0.16);
  --dark: #24110f;
  --on-dark: #fff8ef;
  --accent: #d83a24;
  --accent-strong: #a82012;
  --warning: #f2b84b;
  --radius: 18px;
  --button-radius: 999px;
  --container: 1120px;
  --section: clamp(3.5rem, 8vw, 6rem);
}

.theme-institutional {
  --bg: #f6f4ee;
  --surface-alt: #e9e7df;
  --text: #121827;
  --muted: #5b6170;
  --dark: #0d1b2f;
  --on-dark: #ffffff;
  --accent: #d92828;
  --accent-strong: #a90f14;
  --radius: 8px;
}

.theme-personal {
  --bg: #f4f6f7;
  --surface-alt: #e9eef0;
  --text: #121212;
  --muted: #5a6268;
  --dark: #101820;
  --on-dark: #ffffff;
  --accent: #008b8b;
  --accent-strong: #006b6b;
  --radius: 10px;
}

.theme-guided {
  --bg: #071724;
  --surface: #ffffff;
  --surface-alt: #eaf5ee;
  --text: #0f202b;
  --muted: #5b6770;
  --dark: #071724;
  --on-dark: #f3fbf7;
  --accent: #42d66b;
  --accent-strong: #21a34b;
  --radius: 24px;
}

.theme-rows {
  --bg: #fff9f0;
  --surface: #1c1c1c;
  --surface-alt: #242424;
  --text: #1c1c1c;
  --muted: #636363;
  --dark: #1c1c1c;
  --on-dark: #f0f0f0;
  --accent: #f05a3b;
  --accent-strong: #c93b21;
  --radius: 4px;
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
  line-height: 1.55;
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
  outline: 3px solid var(--accent);
  outline-offset: 4px;
}

.skip-link {
  position: absolute;
  z-index: 100;
  top: 1rem;
  left: 1rem;
  transform: translateY(-160%);
  padding: 0.75rem 1rem;
  background: var(--dark);
  color: var(--on-dark);
}

.skip-link:focus {
  transform: translateY(0);
}

.container {
  width: min(100% - 2rem, var(--container));
  margin-inline: auto;
}

.status-strip {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
  padding: 0.55rem 1rem;
  background: var(--accent);
  color: #ffffff;
  font-size: 0.78rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 20;
  border-bottom: 1px solid var(--line);
  background: color-mix(in srgb, var(--bg) 92%, transparent);
  backdrop-filter: blur(12px);
}

.header-inner {
  min-height: 64px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.brand {
  font-weight: 900;
  text-decoration: none;
}

.nav {
  display: none;
  gap: 1rem;
  align-items: center;
  font-size: 0.9rem;
  font-weight: 750;
}

.nav a {
  text-decoration: none;
  color: var(--muted);
}

.nav a:hover {
  color: var(--text);
}

.header-cta {
  min-height: 40px;
  display: inline-flex;
  align-items: center;
  padding-inline: 1rem;
  border-radius: var(--button-radius);
  background: var(--accent);
  color: #ffffff;
  font-weight: 850;
  text-decoration: none;
}

.hero {
  min-height: min(760px, calc(100dvh - 104px));
  display: grid;
  align-items: center;
  padding-block: var(--section);
  background: var(--dark);
  color: var(--on-dark);
}

.hero-grid {
  display: grid;
  gap: 2rem;
  align-items: center;
}

.eyebrow {
  margin: 0 0 1rem;
  color: var(--accent);
  font-size: 0.78rem;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.hero h1,
.section h2 {
  margin: 0;
  line-height: 1.03;
  letter-spacing: 0;
}

.theme-local .hero h1 {
  font-family: var(--display);
  font-weight: 700;
}

.hero h1 {
  max-width: 12ch;
  font-size: clamp(2.8rem, 13vw, 6.5rem);
}

.section h2 {
  max-width: 14ch;
  font-size: clamp(2rem, 8vw, 4rem);
}

.lead {
  max-width: 58ch;
  color: color-mix(in srgb, var(--on-dark) 78%, transparent);
  font-size: 1.1rem;
}

.actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1.5rem;
}

.button {
  min-height: 46px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.85rem 1.2rem;
  border: 1px solid currentColor;
  border-radius: var(--button-radius);
  text-decoration: none;
  font-weight: 900;
}

.button--primary {
  border-color: var(--accent);
  background: var(--accent);
  color: #ffffff;
}

.button--primary:hover {
  border-color: var(--accent-strong);
  background: var(--accent-strong);
}

.button--secondary {
  color: var(--on-dark);
}

.button--ghost {
  color: color-mix(in srgb, var(--on-dark) 78%, transparent);
}

.hero-card {
  margin: 0;
  overflow: hidden;
  border: 1px solid color-mix(in srgb, var(--on-dark) 18%, transparent);
  border-radius: var(--radius);
  background: color-mix(in srgb, var(--on-dark) 8%, transparent);
}

.hero-card img {
  width: 100%;
  aspect-ratio: 5 / 4;
  object-fit: cover;
}

.hero-card figcaption {
  padding: 1rem;
  color: color-mix(in srgb, var(--on-dark) 72%, transparent);
  font-size: 0.9rem;
}

.facts {
  padding-block: 1rem;
  background: var(--surface);
  border-bottom: 1px solid var(--line);
}

.facts-grid {
  display: grid;
  gap: 1rem;
}

.facts p {
  margin: 0;
  display: grid;
  gap: 0.2rem;
}

.facts strong {
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--accent);
}

.facts span {
  color: var(--muted);
}

.section {
  padding-block: var(--section);
}

.section--alt {
  background: var(--surface-alt);
}

.split,
.contact-grid {
  display: grid;
  gap: 2rem;
}

.rows {
  display: grid;
  gap: 0;
}

.info-row {
  display: grid;
  grid-template-columns: 3.5rem 1fr;
  gap: 1rem;
  padding-block: 1.25rem;
  border-top: 1px solid var(--line);
}

.info-row:last-child {
  border-bottom: 1px solid var(--line);
}

.row-index {
  color: var(--accent);
  font-weight: 900;
}

.info-row h3 {
  margin: 0 0 0.35rem;
}

.info-row p {
  margin: 0;
  color: var(--muted);
}

.steps {
  display: grid;
  gap: 1rem;
  padding: 0;
  margin: 2rem 0 0;
  list-style: none;
  counter-reset: step;
}

.steps li {
  counter-increment: step;
  padding: 1.25rem;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: var(--surface);
}

.steps li::before {
  content: counter(step, decimal-leading-zero);
  display: block;
  margin-bottom: 0.75rem;
  color: var(--accent);
  font-weight: 900;
}

.proof-panel {
  max-width: 860px;
}

blockquote {
  margin: 1.5rem 0 0;
  font-size: clamp(1.35rem, 4vw, 2.25rem);
  line-height: 1.25;
}

.proof-meta {
  color: var(--muted);
}

.contact-section {
  background: var(--dark);
  color: var(--on-dark);
}

.contact-section p {
  color: color-mix(in srgb, var(--on-dark) 76%, transparent);
}

.contact-card {
  display: grid;
  gap: 0.75rem;
  padding: 1.25rem;
  border: 1px solid color-mix(in srgb, var(--on-dark) 18%, transparent);
  border-radius: var(--radius);
  font-style: normal;
}

.contact-card a {
  color: var(--on-dark);
  font-weight: 850;
}

.site-footer {
  padding-block: 2rem 5rem;
  border-top: 1px solid var(--line);
}

.footer-inner {
  display: grid;
  gap: 0.5rem;
  color: var(--muted);
}

.mobile-sticky-cta {
  position: fixed;
  left: 1rem;
  right: 1rem;
  bottom: 1rem;
  z-index: 30;
  display: inline-flex;
  min-height: 52px;
  align-items: center;
  justify-content: center;
  border-radius: var(--button-radius);
  background: var(--accent);
  color: #ffffff;
  text-decoration: none;
  font-weight: 900;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.18);
}

@media (min-width: 760px) {
  .nav {
    display: flex;
  }

  .hero-grid {
    grid-template-columns: minmax(0, 1.1fr) minmax(280px, 0.72fr);
  }

  .facts-grid,
  .steps {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  .split,
  .contact-grid {
    grid-template-columns: minmax(0, 0.8fr) minmax(0, 1.2fr);
  }

  .mobile-sticky-cta {
    display: none;
  }

  .site-footer {
    padding-bottom: 2rem;
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

Switch style family by changing:

```html
<body class="theme-local">
```

to one of:

```html
<body class="theme-institutional">
<body class="theme-personal">
<body class="theme-guided">
<body class="theme-rows">
```

`robots.txt`

```txt
User-agent: *
Allow: /
```

No-JS CTA examples:

```html
<a href="tel:+10000000000">Call now</a>
<a href="https://wa.me/10000000000">WhatsApp</a>
<a href="mailto:hello@example.com?subject=Urgent%20request">Email</a>
<a href="https://maps.google.com/?q=Client%20Address">Directions</a>
```

## Agent Build Workflow

1. Confirm this really is micro scope: one page, direct contact, no backend.
2. Ask for client name, one-sentence description, contact details, service area, hours/status, proof line, and logo/image if available.
3. Choose one theme class from the five style families.
4. Replace all placeholder text.
5. Replace contact links.
6. Replace or remove the hero image.
7. Remove unused anchors/sections instead of adding complexity.
8. Set title and meta description.
9. Add `robots.txt`.
10. Open `index.html` directly and test mobile.
11. Apply one correction round.
12. Handover the folder and minimal notes.

## Verification Checklist

Micro acceptance:

- `index.html` opens directly without a build.
- `styles.css` loads.
- Page is readable at 320px.
- First viewport shows name, purpose, location/status, and primary CTA.
- Phone link works.
- WhatsApp link works if supplied.
- Email link works.
- No form exists.
- No analytics script exists.
- No CMS files exist.
- No package manager files exist.
- One visible `<h1>`.
- Metadata is not placeholder.
- Image paths load or image section is removed.
- Alt text is truthful.
- No claims of bank-account guarantee, legal advice, approval guarantees, or regulated outcomes.
- Footer repeats contact.
- One correction round is complete.

## Handover Package

Deliver:

```text
client-micro-site/
  index.html
  styles.css
  robots.txt
  favicon.svg
  images/
```

Minimal handover note:

```md
# Client Name Micro Website

Stack: plain HTML/CSS.
Main file: index.html.
Styles: styles.css.
Images: images/.

To edit:
- Text/contact links: index.html
- Colors/spacing/theme: styles.css
- Theme family: body class in index.html

Not included:
CMS, backend, form, login, analytics, ongoing updates, SEO campaign, translation.

Warranty:
Bug and typo correction only.
```

## Change-Control Rules

Allowed inside the one correction round:

- Fix typos.
- Replace a phone/email/link.
- Replace one supplied image.
- Adjust one theme class.
- Fix mobile spacing.
- Correct title/meta.

New scope:

- More pages.
- Full copywriting.
- More than one correction round.
- Contact form.
- Analytics.
- Translation.
- CMS/editor.
- Logo/design system.
- Booking/payment.
- Ongoing updates.
- SEO campaign.
- Portfolio/case-study buildout.

## Exclusions and Add-Ons

Hard exclusions:

- Bank-account guarantee.
- Legal/compliance advice.
- Professional copywriting.
- Translation.
- CMS/editor.
- Login/user accounts.
- E-commerce/payments.
- Contact form backend unless paid add-on.
- Custom design system.
- Multiple revision rounds.
- Ongoing SEO.
- Hosting/domain/email fees.
- Future updates.

Upgrade path:

| Request | Route |
|------|------|
| Add one or more pages | Basic add-on or Basic package. |
| Add real form/spam protection | Basic/Medium add-on. |
| Add analytics | Basic add-on or Medium. |
| Add CMS | Basic/Medium/Complex add-on depending on editor needs. |
| Add multilingual copy | Basic/Medium translation add-on. |
| Add strategic copy/SEO | Medium or Complex. |
| Add integrations/payments/login | Complex or custom application scope. |
