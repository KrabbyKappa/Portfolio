export type SeoClaimRisk = 'low' | 'medium' | 'high';

export interface SeoClaim {
  id: string;
  slug: string;
  claim: string;
  sourcePath: string;
  sourceQuote: string;
  surfaces: string[];
  lastReviewed: string;
  risk: SeoClaimRisk;
}

export const seoClaims: SeoClaim[] = [
  {
    "id": "C001",
    "slug": "website-service-need",
    "claim": "Luca has a website-development service for people who need a new website or digital business card.",
    "sourcePath": "Astro Portfolio/src/pages/projects.astro",
    "sourceQuote": "Click on this tab if you are in need of a new website or digital business card.",
    "surfaces": [
      "/website-development/",
      "/projects.html"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "low"
  },
  {
    "id": "C002",
    "slug": "service-collaborative-intake",
    "claim": "Clients do not need to arrive with everything figured out; Luca can learn the business and shape structure, content, and message.",
    "sourcePath": "Astro Portfolio/src/pages/website-development/index.astro",
    "sourceQuote": "You do not need to arrive with everything figured out. I learn what your business does, suggest a few clear directions, help shape the structure, content, and message.",
    "surfaces": [
      "/website-development/"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "low"
  },
  {
    "id": "C003",
    "slug": "simple-site-timeline",
    "claim": "Simple template-like one-page websites are usually ready in 3 days after content and direction are provided, subject to scope.",
    "sourcePath": "Astro Portfolio/src/pages/website-development/index.astro",
    "sourceQuote": "Simple template-like one-page websites are usually ready in 3 days after you provide the content and direction, subject to scope.",
    "surfaces": [
      "/website-development/"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "medium"
  },
  {
    "id": "C004",
    "slug": "separate-domain-hosting",
    "claim": "Domain and hosting are separate costs, and Luca can help with setup.",
    "sourcePath": "Astro Portfolio/src/pages/website-development/index.astro",
    "sourceQuote": "I also make clear which costs are separate, such as domain and hosting, and can help you set them up.",
    "surfaces": [
      "/website-development/"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "low"
  },
  {
    "id": "C005",
    "slug": "clear-next-steps",
    "claim": "The service explains what Luca needs, what he handles, separate costs, and next steps.",
    "sourcePath": "Astro Portfolio/src/pages/website-development/index.astro",
    "sourceQuote": "I explain what I need from you, what I will handle, which costs are separate, and what the next steps look like.",
    "surfaces": [
      "/website-development/"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "low"
  },
  {
    "id": "C006",
    "slug": "showcases-adaptable",
    "claim": "Website showcases are examples that can be shaped around a real business, branding, wording, images, services, and goals.",
    "sourcePath": "Astro Portfolio/src/pages/website-development/index.astro",
    "sourceQuote": "I can use it as a template and shape it around your real business, branding, wording, images, services, and goals.",
    "surfaces": [
      "/website-development/"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "low"
  },
  {
    "id": "C007",
    "slug": "documented-improvable-setup",
    "claim": "The website setup is intended to be well documented and easy to improve over time.",
    "sourcePath": "Astro Portfolio/src/pages/website-development/index.astro",
    "sourceQuote": "You get a light, responsive website with smooth communication, thoughtful details, and a well-documented setup that can be edited or improved over time.",
    "surfaces": [
      "/website-development/"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "low"
  },
  {
    "id": "C008",
    "slug": "multilingual-kl-profile",
    "claim": "Luca is a multilingual professional based in Kuala Lumpur.",
    "sourcePath": "Astro Portfolio/src/pages/index.astro",
    "sourceQuote": "Multilingual professional based in Kuala Lumpur.",
    "surfaces": [
      "/"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "low"
  },
  {
    "id": "C009",
    "slug": "bizwholistic-role",
    "claim": "Luca currently provides digital and marketing services for Bizwholistic Ltd.",
    "sourcePath": "Astro Portfolio/src/pages/index.astro",
    "sourceQuote": "Digital and Marketing Services for Bizwholistic Ltd. \u00b7 Contract | Jan 2026 - Present \u00b7 5 mos.",
    "surfaces": [
      "/"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "low"
  },
  {
    "id": "C010",
    "slug": "legal-trust-safety-role",
    "claim": "Luca has Italian legal and operations work involving policy alignment, legal document review, privacy, security, and government requirements.",
    "sourcePath": "Astro Portfolio/src/pages/index.astro",
    "sourceQuote": "Engage in dialogue with governments, law firms, and corporations regarding Italian trust and safety governance for a top global video streaming platform.",
    "surfaces": [
      "/"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "medium"
  },
  {
    "id": "C011",
    "slug": "diplomatic-project-work",
    "claim": "Luca has coordinated and supported diplomatic projects with the Italian Embassy in Kuala Lumpur.",
    "sourcePath": "Astro Portfolio/src/pages/index.astro",
    "sourceQuote": "Served as Project Manager and Executive for the Italian National Day in Kuala Lumpur.",
    "surfaces": [
      "/",
      "/projects.html"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "low"
  },
  {
    "id": "C012",
    "slug": "language-list",
    "claim": "Luca lists Italian and Polish as native, English as fluent, Spanish as proficient, and German as intermediate.",
    "sourcePath": "Astro Portfolio/src/pages/index.astro",
    "sourceQuote": "Italian - Native; Polish - Native; English - Fluent; Spanish - Proficient; German - Intermediate.",
    "surfaces": [
      "/"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "low"
  },
  {
    "id": "C013",
    "slug": "digital-web-trust-skills",
    "claim": "Luca lists content moderation policy, static HTML/CSS websites, Astro static sites, basic SEO metadata, prompt engineering, and blockchain fundamentals.",
    "sourcePath": "Astro Portfolio/src/pages/index.astro",
    "sourceQuote": "Content Moderation Policy; Static HTML/CSS websites; Astro static sites; Basic SEO metadata; Prompt engineering; Blockchain Fundamentals.",
    "surfaces": [
      "/"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "low"
  },
  {
    "id": "C014",
    "slug": "diplomatic-cultural-projects",
    "claim": "The Projects page documents diplomatic, cultural, reporting, media, and website-development projects.",
    "sourcePath": "Astro Portfolio/src/pages/projects.astro",
    "sourceQuote": "Diplomatic events, cultural programmes, climate reporting, media work, and a separate website-development business.",
    "surfaces": [
      "/projects.html"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "low"
  },
  {
    "id": "C015",
    "slug": "cop24-climate-reporting",
    "claim": "Luca reported on COP24 climate policy and journalism topics.",
    "sourcePath": "Astro Portfolio/src/pages/articles.astro",
    "sourceQuote": "Climate reporting, Energy Web writing, technical localization, and multilingual public communication.",
    "surfaces": [
      "/articles.html"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "low"
  },
  {
    "id": "C016",
    "slug": "energy-web-writing-localization",
    "claim": "Luca wrote and localized Energy Web and blockchain technology materials.",
    "sourcePath": "Astro Portfolio/src/pages/articles.astro",
    "sourceQuote": "Technical writing and localization for the Energy Web Foundation.",
    "surfaces": [
      "/articles.html"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "low"
  },
  {
    "id": "C017",
    "slug": "professional-references",
    "claim": "The References page links professional reference letters in English and Italian.",
    "sourcePath": "Astro Portfolio/src/pages/references.astro",
    "sourceQuote": "Letters of recommendation of the Italian Ambassador of Italy to Malaysia attesting to my professional experience and character.",
    "surfaces": [
      "/references.html"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "low"
  },
  {
    "id": "C018",
    "slug": "bizwholistic-real-case",
    "claim": "Bizwholistic is presented as a real live case-study context for the website-development portfolio.",
    "sourcePath": "Astro Portfolio/src/pages/website-development/index.astro",
    "sourceQuote": "Live Bizwholistic case study.",
    "surfaces": [
      "/website-development/"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "low"
  },
  {
    "id": "C019",
    "slug": "contact-paths",
    "claim": "The portfolio provides email and LinkedIn contact paths.",
    "sourcePath": "Astro Portfolio/src/pages/index.astro",
    "sourceQuote": "For collaborations or inquiries, please use the contact information below or send me a message.",
    "surfaces": [
      "/",
      "#contact",
      "/website-development/#contact"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "low"
  },
  {
    "id": "C020",
    "slug": "demo-disclosure",
    "claim": "Website showcase pages are examples and demos unless explicitly marked as a real case study.",
    "sourcePath": "Astro Portfolio/public/llms-full.txt",
    "sourceQuote": "Website showcase pages and template examples are demos unless a page explicitly says it is a real client or real case study.",
    "surfaces": [
      "/website-development/"
    ],
    "lastReviewed": "2026-05-24",
    "risk": "medium"
  }
];

export const seoClaimIds = seoClaims.map((claim) => claim.id);

export function claimById(id: string): SeoClaim | undefined {
  return seoClaims.find((claim) => claim.id === id);
}
