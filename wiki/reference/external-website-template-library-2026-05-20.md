---
type: reference
description: Reusable website template library distilled from 15 downloaded external homepage snapshots
last_updated: 2026-05-20
tags: [reference, templates, website-patterns, design-research]
source: external live website homepage snapshots downloaded 2026-05-20
related_files:
  - external-references/website-template-snapshots/2026-05-20/adammirek.html
  - external-references/website-template-snapshots/2026-05-20/animalfreecircus.html
  - external-references/website-template-snapshots/2026-05-20/blueyard.html
  - external-references/website-template-snapshots/2026-05-20/brewitty.html
  - external-references/website-template-snapshots/2026-05-20/dolsten.html
  - external-references/website-template-snapshots/2026-05-20/extinctionmap.html
  - external-references/website-template-snapshots/2026-05-20/fundacionalcaraz.html
  - external-references/website-template-snapshots/2026-05-20/grumpyfrenchie.html
  - external-references/website-template-snapshots/2026-05-20/mycommuters.html
  - external-references/website-template-snapshots/2026-05-20/omaralkhatib.html
  - external-references/website-template-snapshots/2026-05-20/piv-group.html
  - external-references/website-template-snapshots/2026-05-20/rumbekeplatse.html
  - external-references/website-template-snapshots/2026-05-20/shreejal.html
  - external-references/website-template-snapshots/2026-05-20/stlouisvending.html
  - external-references/website-template-snapshots/2026-05-20/tehtariknation.html
  - external-references/website-template-full-source/2026-05-20/manifest.json
  - external-references/scrape_reference_assets.py
related:
  - reference/external-website-source-code-analysis-2026-05-20
  - business/business-service-offers
  - business/website-spec-micro
  - business/website-spec-basic
  - business/website-spec-medium
  - business/website-spec-complex
---

# External Website Template Library

Back: [[business/business-service-offers]]  
Governance: [[MOC/MOC-Reference]] · [[MOC/MOC-Graph]]

This page records reusable information architecture, section patterns, and interface elements from 15 external websites. Use it as a design and schema library for future website packages, not as permission to copy source code, visual assets, logos, copy, or brand-specific art.

Source-code layer: [[reference/external-website-source-code-analysis-2026-05-20]]

## Evidence Boundary

| Field | Status |
|-------|--------|
| Snapshot date | 2026-05-20 |
| Download scope | Homepage HTML snapshots only |
| Evidence paths | `external-references/website-template-snapshots/2026-05-20/*.html` |
| Full source-code evidence | `external-references/website-template-full-source/2026-05-20/manifest.json` |
| Visual certainty | Medium. The HTML and rendered text were inspected, but no screenshot QA was done in this pass. |
| Reuse rule | Reuse the schema and section logic. Redesign the visuals, copy, and assets for the actual client. |

## Source Sites

| Site | Snapshot | Template fit |
|------|----------|--------------|
| `https://rumbekeplatse.be` | `rumbekeplatse.html` | Local food business with menu, hours, route, reviews, and owner story |
| `https://piv.group` | `piv-group.html` | High-trust impact advisory or investment firm |
| `https://www.omaralkhatib.com` | `omaralkhatib.html` | Freelance service provider with pricing and bilingual route |
| `https://mycommuters.com` | `mycommuters.html` | B2B SaaS/product landing page |
| `https://shreej.al` | `shreejal.html` | Developer portfolio with motion and proof list |
| `https://www.adammirek.pl` | `adammirek.html` | Creator, educator, author, or public expert site |
| `https://stlouisvending.com` | `stlouisvending.html` | Local service lead-generation site |
| `https://www.dolsten.com` | `dolsten.html` | Premium creative studio with awards and case studies |
| `https://www.brewitty.com` | `brewitty.html` | Playful content agency landing page |
| `https://extinctionmap.org/index.html` | `extinctionmap.html` | Data-driven interactive advocacy map |
| `https://tehtariknation.com` | `tehtariknation.html` | Food and beverage brand manifesto with menu and outlets |
| `https://blueyard.com` | `blueyard.html` | Venture capital thesis and portfolio site |
| `https://grumpyfrenchie.com` | `grumpyfrenchie.html` | Video-first novelty product launch page |
| `https://fundacionalcaraz.org` | `fundacionalcaraz.html` | Nonprofit foundation with mission, pillars, and transparency |
| `https://animalfreecircus.com` | `animalfreecircus.html` | Longform advocacy scrollytelling site with sources |

## Reusable Template Families

| Family | Use for | Core schema | Good references |
|--------|---------|-------------|-----------------|
| Local food/menu | Restaurant, cafe, takeaway, bakery, bar, local hospitality | Open status, hero, owner story, reasons to visit, menu categories, featured item, reviews, map route, hours, contact, socials | Rumbeke Platse, Teh Tarik Nation |
| Local service lead-gen | Vending, trades, cleaning, clinics, small B2B services | Pain-point hero, CTA, benefit cards, service proof, contact form, privacy/legal, simple about | St Louis Vending |
| Freelancer or solo expert | Developer, consultant, coach, designer, specialist | Hero with role, about, expertise, services, portfolio, pricing, contact, optional second language | Omar Al Khatib, Shreejal |
| Creator/public figure | Author, educator, speaker, influencer, science communicator | Bio, audience proof, current news, books/products/media, events, collaborations, contact | Adam Mirek |
| B2B SaaS/product | Productized software, analytics, platform, business tool | Outcome hero, audience use cases, feature blocks, workflow, trust/security, team, demo CTA | My Commuters |
| Creative/content agency | Studio, marketing agency, creative production shop | Bold promise, service outcomes, impact metrics, client logos, case studies, team, contact | Dolsten, Brewitty |
| Investment/advisory | Fund, advisory firm, family-office service, serious B2B strategy | Thesis hero, principles, process, proof, portfolio, team/founder, manifesto, contact | BlueYard, PIV Group |
| Nonprofit/cause | Foundation, campaign, activist project, public-interest issue | Mission, problem, pillars, programs, evidence, partners, CTA, transparency/sources | Fundacion Alcaraz, Animal Free Circus, Extinction Map |
| Product teaser | Single product or prelaunch concept | Visual/video hero, product personality, social links, buy/waitlist/adopt CTA, minimal explanation | Grumpy Frenchie |

## Site-by-Site Patterns

### Rumbeke Platse

Template role: local restaurant or takeaway site.

Reusable schema:

1. Status ticker or small utility strip for open/closed state.
2. Anchor nav for story, menu, contact, and route.
3. Hero with name, simple promise, location, route CTA, and menu CTA.
4. Owner/founder story to make the local business feel human.
5. "Why visit" section with practical benefits.
6. Gift card or promo block.
7. Menu grouped by category with item names and prices.
8. Reviews, route CTA, hours, address, phone, email, socials, privacy/cookies.

Best reusable elements:

- The live-status strip.
- Menu-as-content rather than PDF-only menu.
- Owner story before the product catalog.
- Footer that acts like a compact local-business operations panel.

Use for: [[business/website-spec-basic]] or [[business/website-spec-medium]] local hospitality projects.

### PIV Group

Template role: high-stakes advisory or impact investment site.

Reusable schema:

1. Minimal brand nav with work, thinking, proof, about, and contact.
2. Principle-led hero built around three values.
3. A short thesis that names the hard problem and why the team exists.
4. Process steps: understand the problem, assemble the team, deliver the outcome.
5. Proof section with concrete examples and downloadable framework.
6. Founder bio and contact prompt.

Best reusable elements:

- Values as navigation-level positioning, not decorative copy.
- Process framing before selling services.
- Downloadable method artifact as trust proof.
- Small, serious content density instead of generic service cards.

Use for: [[business/website-spec-medium]] advisory sites or [[business/website-spec-complex]] when the method artifact, case studies, and research library are scoped.

### Omar Al Khatib

Template role: freelance developer or independent technical service provider.

Reusable schema:

1. Header with logo, anchor nav, language switch, and direct contact.
2. Hero with exact role, location/contact details, and hire/download actions.
3. About section explaining fit and work style.
4. Expertise grouped into development and security.
5. Services with concrete deliverables.
6. Portfolio examples.
7. Pricing section split by website and web-app offers.
8. Contact section with direct communication routes.

Best reusable elements:

- Pricing visible on the page.
- CV/download artifact for credibility.
- Bilingual route as a scoped add-on.
- Security capability folded into a normal service provider profile.

Use for: [[business/website-spec-basic]] when one-page, [[business/website-spec-medium]] when portfolio/pricing/language depth matters.

### My Commuters

Template role: B2B SaaS and analytics platform.

Reusable schema:

1. Product hero with audience outcome.
2. Mission and value proposition.
3. Use-case blocks for business decisions.
4. Feature set organized around measurable operational benefits.
5. Workflow/process explanation.
6. Data/security trust section.
7. Team section.
8. Demo CTA and language switch.

Best reusable elements:

- Outcome phrasing tied to departments and decisions.
- Use cases before feature detail.
- Trust section for data-sensitive products.
- Compact bilingual switch for a focused market.

Use for: [[business/website-spec-medium]] SaaS landing pages; [[business/website-spec-complex]] when dashboards, docs, schema, and localization are scoped.

### Shreejal

Template role: personal developer portfolio.

Reusable schema:

1. Full-screen intro hero with name and compact positioning.
2. About section with personality and portrait/avatar.
3. Work list with numbered project rows and external links.
4. Services/capabilities split by category.
5. Certifications or credentials list.
6. Network/infrastructure proof section.
7. Contact/social footer with stronger interaction and motion.

Best reusable elements:

- Numbered project-list format for dense portfolios.
- Capability lists that use categories rather than generic cards.
- Infrastructure/network proof as a differentiator.
- Motion used to reinforce craft, not to hide weak content.

Use for: [[business/website-spec-medium]] portfolios; [[business/website-spec-complex]] only if custom cursor, 3D, canvas, or heavy motion are part of the quote.

### Adam Mirek

Template role: creator, educator, author, or public expert.

Reusable schema:

1. Personal brand hero with field and mission.
2. Audience/social proof numbers.
3. Current news or latest updates.
4. Product/book/resource cards.
5. Events or speaking calendar.
6. Media, partnership, or collaboration proof.
7. Contact/collaboration CTA.

Best reusable elements:

- "What is new" content feed keeps the site alive.
- Social proof sits near the top because audience is the asset.
- Books, resources, and events all live under one expert brand.
- Brand personality is high, but the structure remains scannable.

Use for: [[business/website-spec-medium]] creator sites; [[business/website-spec-complex]] when there are events, products, newsletters, and media archives.

### St Louis Vending

Template role: local service lead-generation site.

Reusable schema:

1. Plain header with about and contact.
2. Hero naming the service and customer pain.
3. Primary CTA to start the inquiry.
4. Benefit cards for service quality, support, and selection.
5. Contact form or contact page.
6. Closing CTA and privacy/legal links.

Best reusable elements:

- Pain-point copy before service features.
- Very small route set.
- Clear CTA repeated without overbuilding the site.
- Suitable for clients who need leads, not editorial depth.

Use for: [[business/website-spec-micro]] or [[business/website-spec-basic]].

### Dolsten

Template role: premium creative studio.

Reusable schema:

1. Awards/recognitions as top-level proof.
2. Motion/video-led brand statement.
3. Featured work with case-study links.
4. About statement that explains the studio's positioning.
5. Press/news or awards archive.
6. Contact section.

Best reusable elements:

- Awards wall as a hero-level trust device.
- Case studies are the main product.
- Strong motion is justified because the client sells creative craft.
- Work links imply a deeper portfolio architecture.

Use for: [[business/website-spec-complex]] creative studios. Do not use this level of motion or case-study architecture for a basic service site.

### Brewitty

Template role: playful content or marketing agency.

Reusable schema:

1. Punchy hero with direct contact CTA.
2. Three outcome pillars.
3. Impact metrics with short supporting stories.
4. Logo strip.
5. Why-us section.
6. Team/crew section.
7. Contact form.

Best reusable elements:

- Metrics are grouped as mini case studies.
- Copy tone is the product, so the page demonstrates the service.
- Short one-page flow works for a focused agency offer.
- The contact form appears after proof, not before.

Use for: [[business/website-spec-basic]] if simplified; [[business/website-spec-medium]] when metrics, client logos, and team proof are real.

### Extinction Map

Template role: interactive data story.

Reusable schema:

1. Full-screen map or explorer as the primary interface.
2. Short narrative framing the stakes.
3. State/location/species detail interaction.
4. Share/action CTA.
5. Credits and data/reference notes.

Best reusable elements:

- The interface is the content, not a section below a normal landing page.
- Geography is used as navigation.
- Complex topic is made inspectable through a map.
- Sources and credits are part of the credibility layer.

Use for: [[business/website-spec-complex]] data stories, campaign microsites, or interactive reports.

### Teh Tarik Nation

Template role: expressive food and beverage brand.

Reusable schema:

1. Brand manifesto around cultural identity.
2. Product origin and craft story.
3. External validation or cultural proof.
4. Ingredients/sourcing/process detail.
5. Personality traits and brand voice.
6. Menu/product categories.
7. Catering, hiring, outlets, and contact.

Best reusable elements:

- Heritage story before menu.
- Product craft is treated as brand proof.
- Menu is still present, but it is not the entire site.
- Recruitment and catering are integrated into the main page.

Use for: [[business/website-spec-medium]] food brands; [[business/website-spec-complex]] when custom art, motion, menu systems, hiring, and outlet pages are all scoped.

### BlueYard

Template role: venture capital or thesis-led investment firm.

Reusable schema:

1. Manifesto hero with a strong worldview.
2. Sector navigation by investment domain.
3. Selected portfolio highlights.
4. Prior work and exit proof.
5. Team or "who we are" section.
6. Updates, manifesto, press, legal links.

Best reusable elements:

- Sectors are the main site architecture.
- Portfolio proof is concise but specific.
- Manifesto link turns the homepage into a gateway to deeper thinking.
- Useful for firms that need conviction, not generic corporate polish.

Use for: [[business/website-spec-medium]] if static and concise; [[business/website-spec-complex]] when portfolio filters, manifesto pages, press docs, and data-managed company profiles are scoped.

### Grumpy Frenchie

Template role: novelty product launch or teaser page.

Reusable schema:

1. Video/visual-first product introduction.
2. Minimal copy around what the product is.
3. Primary "buy/adopt/join" CTA.
4. Social links as the main follow-up path.
5. Lightweight modal or action state.

Best reusable elements:

- Product personality can carry the page when the offer is simple.
- Social-first distribution replaces heavy navigation.
- Works as a prelaunch page, not as a mature e-commerce site.

Use for: [[business/website-spec-micro]] or [[business/website-spec-basic]] product teasers.

### Fundacion Alcaraz

Template role: nonprofit foundation.

Reusable schema:

1. Mission statement centered on the beneficiary group.
2. Objective section.
3. Pillars or action lines.
4. Program dossier/download cards.
5. Language switch.
6. Social links, contact, legal, cookies, transparency.

Best reusable elements:

- Mission and pillars come before organizational detail.
- Downloadable program dossiers create credibility.
- Transparency/legal links are first-class nonprofit requirements.
- Simple bilingual handling is important for public-interest work.

Use for: [[business/website-spec-medium]] nonprofit sites; [[business/website-spec-complex]] when multilingual, transparency, downloadable reports, donation flows, and news are scoped.

### Animal Free Circus

Template role: longform advocacy campaign.

Reusable schema:

1. Fixed or repeated chapter navigation.
2. Emotional opening thesis.
3. Historical context.
4. Problem mechanics explained in chapters.
5. Case examples.
6. System and funding critique.
7. Rejection/action CTA.
8. Source list and share tools.

Best reusable elements:

- Chapter navigation makes a long single page usable.
- Claims are organized by argument, not by generic sections.
- Source list is part of the conversion mechanism because trust matters.
- Works when a campaign needs education before action.

Use for: [[business/website-spec-complex]] advocacy or public-interest storytelling.

## Component Bank

| Component | Pattern | Source examples | Build guidance |
|-----------|---------|-----------------|----------------|
| Live status strip | Compact ticker or utility line for open/closed/current state | Rumbeke Platse | Drive from data where possible; avoid fake urgency. |
| Anchor navigation | Single-page navigation to major sections | Rumbeke Platse, Omar, PIV, My Commuters | Use stable IDs and keyboard-friendly mobile menu. |
| Founder/owner block | Human story before offer detail | Rumbeke Platse, PIV, Adam Mirek | Use real portrait or useful fallback; keep it concise. |
| Menu/catalog | Category groups with prices or products | Rumbeke Platse, Teh Tarik Nation | Prefer structured data arrays over hard-coded repeated markup. |
| Proof metrics | Numbers with story context | Brewitty, Adam Mirek, Dolsten, BlueYard | Only use numbers the client can substantiate. |
| Portfolio rows | Numbered list of work with short proof | Shreejal, BlueYard, Dolsten | Better for dense proof than large decorative cards. |
| Pricing block | Transparent service tiers | Omar Al Khatib | Use when pricing is a trust advantage and scope is clear. |
| Data explorer | Map or interactive visualization as main content | Extinction Map | Complex-tier only; needs data, accessibility fallback, and QA. |
| Manifesto | Worldview-led brand statement | BlueYard, Teh Tarik Nation, PIV | Use when the client has a real point of view. |
| Transparency footer | Legal, cookies, contact, socials, reports | Fundacion Alcaraz, Rumbeke Platse | Important for public, nonprofit, and local business trust. |

## Package Mapping

| Package | Templates to borrow from | Keep | Avoid |
|---------|--------------------------|------|-------|
| [[business/website-spec-micro]] | St Louis Vending, Grumpy Frenchie | One clear offer, CTA, contact, mobile readability | Heavy motion, deep case studies, maps, CMS |
| [[business/website-spec-basic]] | Rumbeke Platse, Omar, Brewitty simplified | One-page structure, local proof, menu/services, contact | Overbuilt animation and complex filtering |
| [[business/website-spec-medium]] | My Commuters, Shreejal, Adam Mirek, Teh Tarik Nation, PIV concise | Multi-section storytelling, proof, portfolio/services, basic SEO, reusable components | Custom backend, large data visualizations, uncontrolled content systems |
| [[business/website-spec-complex]] | Dolsten, BlueYard, Extinction Map, Animal Free Circus, Fundacion Alcaraz expanded | Case-study architecture, data-driven sections, multilingual/public assets, reports, advanced interactions | Copying bespoke assets or shipping motion without screenshot/device verification |

## Astro Implementation Pattern

For future builds, model these patterns as data-driven section schemas instead of cloning pages.

Recommended section types:

```text
hero
utilityStatus
anchorNav
founderStory
proofMetrics
serviceCards
portfolioRows
menuCatalog
caseStudyGrid
dataExplorer
manifestoBlock
programPillars
downloadCards
reviews
faq
contactCta
operationsFooter
legalFooter
```

Recommended data files:

```text
src/data/site.ts
src/data/navigation.ts
src/data/proof.ts
src/data/services.ts
src/data/work.ts
src/data/menu.ts
src/data/programs.ts
src/data/faqs.ts
```

Default rule: start with the smallest schema that matches the client. Add motion, map interactions, multilingual routing, or case-study architecture only when the package and client evidence justify the extra maintenance.
