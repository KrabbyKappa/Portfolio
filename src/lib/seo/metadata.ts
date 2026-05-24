import type { SeoRouteRecord } from '../../data/seo/site';

const maxDescriptionLength = 170;

export function metadataForRoute(route: SeoRouteRecord) {
  return {
    title: route.title,
    description: route.description.length > maxDescriptionLength
      ? `${route.description.slice(0, maxDescriptionLength - 1).trim()}…`
      : route.description,
    language: route.language,
    family: route.family,
  };
}

export const metadataRules = {
  maxDescriptionLength,
  uniqueTitleRequired: true,
  uniqueFirstPhraseRequired: true,
  unsupportedClaimsForbidden: [
    'best',
    '#1',
    'guaranteed ranking',
    'guaranteed traffic',
    'office in',
  ],
  hreflangRequiresRealRoute: true,
} as const;
