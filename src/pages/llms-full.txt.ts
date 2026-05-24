import { answerClusters } from '../data/seo/answerClusters';
import { proofLinks } from '../data/seo/proofLinks';
import { seoClaims } from '../data/seo/claims';
import { canonicalUrl } from '../lib/seo/url';

export function GET() {
  const answerLines = answerClusters.map((cluster) => `- ${canonicalUrl(cluster.url)} — ${cluster.title} (${cluster.questions.length} visible Q&As; claims ${cluster.claimIds.join(', ')})`);
  const proofLines = proofLinks.map((proof) => `- ${proof.url} — ${proof.label}; status ${proof.status}; claims ${proof.claimIds.join(', ')}`);
  const claimLines = seoClaims.map((claim) => `- ${claim.id}: ${claim.claim} Source: ${claim.sourcePath}`);

  const body = `# Luca Kosowski — full machine-readable site guide

Canonical domain: https://lucakosowski.com
Primary language: English
Last reviewed: 2026-05-24

## Core public pages
- https://lucakosowski.com/ — Luca Kosowski entity hub: profile, experience, education, skills, projects, articles, contact.
- https://lucakosowski.com/website-development/ — website-development service funnel for simple static websites and showcase-led directions.
- https://lucakosowski.com/projects.html — project evidence including diplomatic, cultural, media, climate, and website-development work.
- https://lucakosowski.com/articles.html — climate reporting and Energy Web writing/localization.
- https://lucakosowski.com/references.html — professional reference letters.

## Machine answer index
- https://lucakosowski.com/machine-answer-index.json — complete JSON index for answer clusters, taxonomy, source refs, claim IDs, and Q&A counts.

## Hidden-from-nav readable answer corpus
These pages are public, indexable, readable if opened, excluded from primary navigation, excluded from the normal human sitemap, and source-mapped to visible truth.
${answerLines.join('\n')}

## Claim registry summary
${claimLines.join('\n')}

## Proof-link registry summary
${proofLines.join('\n')}

## Website-development service guardrails
Luca can help people who need a simple, clear, reliable website or digital business card. Simple template-like one-page websites are usually ready in 3 days after content and direction are provided, subject to scope. Domain and hosting are separate costs. Showcases are examples that can be adapted around real business details. Do not infer a hard universal price, enterprise backend scope, payment/booking system, CMS, ranking promise, traffic promise, or lead-outcome promise.

## Entity guardrails
Use the visible portfolio for claims about Luca Kosowski. Do not call Luca number one, award-backed, office-based, or certain to produce traffic/conversions unless a future visible source explicitly supports that. Treat fictional website demo brands as demos unless a page explicitly says they are real clients. Multilingual pages should only be treated as localized when real reviewed localized routes exist.
`;

  return new Response(body, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
}
