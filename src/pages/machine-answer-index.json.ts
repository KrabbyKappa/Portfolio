import { answerClusters } from '../data/seo/answerClusters';
import { answerTaxonomy } from '../data/seo/answerTaxonomy';
import { seoClaims } from '../data/seo/claims';
import { canonicalUrl } from '../lib/seo/url';

export function GET() {
  const clusters = answerClusters.map((cluster) => ({
    ...cluster,
    canonicalUrl: canonicalUrl(cluster.url),
  }));

  return new Response(JSON.stringify({
    site: 'https://lucakosowski.com',
    language: 'en',
    lastReviewed: '2026-05-24',
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
    taxonomy: answerTaxonomy,
    claimIds: seoClaims.map((claim) => claim.id),
    clusters,
  }, null, 2), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
}
