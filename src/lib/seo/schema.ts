import { seoSite, type RouteFamily } from '../../data/seo/site';
import { canonicalUrl } from './url';
import { personId, serviceId, websiteId, personFacts, websiteFacts } from './facts';

export interface WebPageSchemaInput {
  path: string;
  title: string;
  description: string;
  family?: RouteFamily;
  faqItems?: FaqSchemaItem[];
}

export interface FaqSchemaItem {
  question: string;
  answer: string;
}

export interface AnswerClusterSchemaInput {
  id: string;
  family: 'entity' | 'service';
  url: string;
  title: string;
  summary: string;
  lastReviewed: string;
  questions: FaqSchemaItem[];
  claimIds: string[];
  sourceRefs: string[];
}

export function webPageSchema(input: WebPageSchemaInput) {
  const url = canonicalUrl(input.path);
  return {
    '@context': 'https://schema.org',
    '@type': input.family === 'article' ? 'CollectionPage' : 'WebPage',
    '@id': `${url}#webpage`,
    url,
    name: input.title,
    description: input.description,
    inLanguage: 'en',
    isPartOf: { '@id': websiteId },
    about: input.family === 'service' ? { '@id': serviceId } : { '@id': personId },
  };
}

export function serviceSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'Service',
    '@id': serviceId,
    name: 'Website creation by Luca Kosowski',
    serviceType: 'Static website creation and website-development support',
    url: canonicalUrl('/website-development/'),
    provider: { '@id': personId },
    areaServed: 'Worldwide',
    availableLanguage: ['English', 'Italian', 'Polish', 'Spanish', 'German'],
    description: 'Scope-based website creation using ready showcase directions and static Astro builds for small businesses and professionals.',
  };
}

export function faqPageSchema(path: string, title: string, items: FaqSchemaItem[]) {
  const url = canonicalUrl(path);
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    '@id': `${url}#faq`,
    name: `${title} Q&A`,
    inLanguage: 'en',
    mainEntity: items.map((item) => ({
      '@type': 'Question',
      name: item.question,
      acceptedAnswer: {
        '@type': 'Answer',
        text: item.answer,
      },
    })),
  };
}

export function breadcrumbSchema(path: string, title: string) {
  const url = canonicalUrl(path);
  const items: Array<Record<string, unknown>> = [
    {
      '@type': 'ListItem',
      position: 1,
      name: seoSite.name,
      item: canonicalUrl('/'),
    },
  ];
  if (path !== '/') {
    items.push({
      '@type': 'ListItem',
      position: 2,
      name: title,
      item: url,
    });
  }
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    '@id': `${url}#breadcrumb`,
    itemListElement: items,
  };
}

export function schemaForRoute(input: WebPageSchemaInput) {
  const graph: Array<Record<string, unknown>> = [personFacts, websiteFacts, webPageSchema(input), breadcrumbSchema(input.path, input.title)];
  if (input.family === 'service') graph.push(serviceSchema());
  if (input.faqItems?.length) graph.push(faqPageSchema(input.path, input.title, input.faqItems));
  return {
    '@context': 'https://schema.org',
    '@graph': graph,
  };
}

export function answerClusterSchema(cluster: AnswerClusterSchemaInput) {
  const family = cluster.family === 'service' ? 'service' : 'portfolio';
  const page = webPageSchema({ path: cluster.url, title: cluster.title, description: cluster.summary, family });
  return {
    '@context': 'https://schema.org',
    '@graph': [
      personFacts,
      websiteFacts,
      page,
      breadcrumbSchema(cluster.url, cluster.title),
      faqPageSchema(cluster.url, cluster.title, cluster.questions),
      {
        '@type': 'CreativeWork',
        '@id': `${canonicalUrl(cluster.url)}#source-map`,
        name: `${cluster.title} source map`,
        about: cluster.family === 'service' ? { '@id': serviceId } : { '@id': personId },
        dateModified: cluster.lastReviewed,
        citation: cluster.sourceRefs,
        keywords: cluster.claimIds,
      },
      ...(cluster.family === 'service' ? [serviceSchema()] : []),
    ],
  };
}
