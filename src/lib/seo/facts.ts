import { seoSite } from '../../data/seo/site';
import { assetUrl, canonicalUrl } from './url';

export const personId = canonicalUrl('/#person');
export const websiteId = canonicalUrl('/#website');
export const serviceId = 'https://websites.lucakosowski.com/#service';

export const personFacts = {
  '@type': 'Person',
  '@id': personId,
  name: 'Luca Kosowski',
  url: canonicalUrl('/'),
  image: assetUrl('/profile.jpg'),
  jobTitle: [
    'Digital and Marketing Services',
    'Italian Legal Advisor',
    'Website creator',
  ],
  knowsLanguage: ['Italian', 'Polish', 'English', 'Spanish', 'German'],
  address: {
    '@type': 'PostalAddress',
    addressLocality: 'Kuala Lumpur',
    addressCountry: 'MY',
  },
  sameAs: seoSite.sameAs,
} as const;

export const websiteFacts = {
  '@type': 'WebSite',
  '@id': websiteId,
  name: 'Luca Kosowski',
  url: canonicalUrl('/'),
  inLanguage: 'en',
  publisher: { '@id': personId },
} as const;
