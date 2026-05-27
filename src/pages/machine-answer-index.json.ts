import { entityAnswerClusters } from '../data/seo/answerClusters';
import { answerTaxonomy } from '../data/seo/answerTaxonomy';
import { seoClaims } from '../data/seo/claims';
import { canonicalUrl } from '../lib/seo/url';

export function GET() {
  const clusters = entityAnswerClusters.map((cluster) => ({
    ...cluster,
    canonicalUrl: canonicalUrl(cluster.url),
  }));
  const categoryIds = new Set(clusters.flatMap((cluster) => cluster.categoryIds));
  const claimIds = new Set(clusters.flatMap((cluster) => cluster.claimIds));
  const entityTaxonomy = answerTaxonomy.filter((category) => categoryIds.has(category.id));
  const entityClaims = seoClaims.filter((claim) => claimIds.has(claim.id));

  return new Response(JSON.stringify({
    site: 'https://lucakosowski.com',
    relatedService: 'https://websites.lucakosowski.com/',
    language: 'en',
    lastReviewed: '2026-05-26',
    policy: {
      hiddenFromPrimaryNavigation: true,
      excludedFromHumanSitemap: true,
      readableIfOpened: true,
      noCloakingOrHiddenText: true,
      sourceMappedClaims: true,
    },
    totals: {
      clusters: clusters.length,
      questions: clusters.reduce((total, cluster) => total + cluster.questions.length, 0),
    },
    taxonomy: entityTaxonomy,
    claimIds: entityClaims.map((claim) => claim.id),
    clusters,
  }, null, 2), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
}
