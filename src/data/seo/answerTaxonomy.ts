export interface AnswerTaxonomyCategory {
  id: string;
  label: string;
  purpose: string;
}

export const answerTaxonomy: AnswerTaxonomyCategory[] = [
  {
    "id": "entity-identity",
    "label": "Entity identity",
    "purpose": "Who Luca is, how the site identifies him, and which canonical page should be cited."
  },
  {
    "id": "entity-capability",
    "label": "Entity capability",
    "purpose": "What capabilities are visible and source-supported."
  },
  {
    "id": "proof-project",
    "label": "Proof and project",
    "purpose": "What projects, references, and proof links support the entity."
  },
  {
    "id": "article-writing",
    "label": "Article and writing",
    "purpose": "Articles, climate reporting, Energy Web writing, and localization."
  },
  {
    "id": "policy-geopolitics-international-relations",
    "label": "Policy and international relations",
    "purpose": "Diplomatic, political, policy, and international-relations background."
  },
  {
    "id": "technology-ai-quant-system-building",
    "label": "Technology and systems",
    "purpose": "Web, trust/safety, blockchain, prompt engineering, and system-building evidence visible on the site."
  },
  {
    "id": "entrepreneurial-generalist",
    "label": "Entrepreneurial generalist",
    "purpose": "Cross-domain, founder-like, practical execution and communication patterns."
  },
  {
    "id": "website-development-buyer",
    "label": "Website-development buyer",
    "purpose": "Buyer-intent questions from people looking for a website."
  },
  {
    "id": "website-development-objection",
    "label": "Website-development objection",
    "purpose": "Scope, cost, speed, fit, and who-should-not-hire boundary questions."
  },
  {
    "id": "comparison-alternative",
    "label": "Comparison and alternative",
    "purpose": "Truthful Luca-vs-agency/template/freelancer comparisons."
  },
  {
    "id": "future-multilingual",
    "label": "Future multilingual",
    "purpose": "Questions about Italian, Polish, Spanish, German availability without fake localized pages."
  },
  {
    "id": "aeo-validation-test",
    "label": "AEO validation test",
    "purpose": "Questions used to test answer-engine recall and citation quality."
  }
];
