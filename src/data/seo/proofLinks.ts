export type ProofLinkStatus = 'live' | 'owned-file' | 'unchecked-external' | 'lost-or-archived';

export interface ProofLink {
  id: string;
  label: string;
  url: string;
  status: ProofLinkStatus;
  archiveUrl: string | null;
  claimIds: string[];
  lastChecked: string;
  note: string;
}

export const proofLinks: ProofLink[] = [
  {
    "id": "P001",
    "label": "Bizwholistic live website",
    "url": "https://bizwholistic.com/",
    "status": "live",
    "archiveUrl": null,
    "claimIds": [
      "C009",
      "C018"
    ],
    "lastChecked": "2026-05-24",
    "note": "Owned/live client context linked from the website-development page."
  },
  {
    "id": "P002",
    "label": "Luca Kosowski Medium profile",
    "url": "https://medium.com/@KappaK",
    "status": "live",
    "archiveUrl": null,
    "claimIds": [
      "C016"
    ],
    "lastChecked": "2026-05-24",
    "note": "Article source profile listed in sameAs and Articles page links."
  },
  {
    "id": "P003",
    "label": "Energy Web decarbonize crypto article",
    "url": "https://medium.com/@KappaK/how-can-you-decarbonize-your-crypto-assets-with-energy-web-chain-d3832514a10b",
    "status": "live",
    "archiveUrl": null,
    "claimIds": [
      "C016"
    ],
    "lastChecked": "2026-05-24",
    "note": "External source for Energy Web original writing."
  },
  {
    "id": "P004",
    "label": "Italian COP24 climate article",
    "url": "https://stampagiovanile.it/2018/12/14/scommessa-sul-clima-un-sacrificio-o-un-inevitabile-toccasana-per-il-lavoro/",
    "status": "unchecked-external",
    "archiveUrl": null,
    "claimIds": [
      "C015"
    ],
    "lastChecked": "2026-05-24",
    "note": "External article source; dead links should be archived rather than erasing the claim."
  },
  {
    "id": "P005",
    "label": "Italian Design Day event article",
    "url": "https://italcham.my/italian-design-day-in-malaysia-2024/",
    "status": "unchecked-external",
    "archiveUrl": null,
    "claimIds": [
      "C011",
      "C014"
    ],
    "lastChecked": "2026-05-24",
    "note": "External project-supporting event article linked from Projects page."
  },
  {
    "id": "P006",
    "label": "Italian National Day 2025 video",
    "url": "https://www.youtube.com/watch?v=hz1xPkvdhcI",
    "status": "live",
    "archiveUrl": null,
    "claimIds": [
      "C011",
      "C014"
    ],
    "lastChecked": "2026-05-24",
    "note": "Project video linked from the Projects page."
  },
  {
    "id": "P007",
    "label": "Perche ci siamo noi video",
    "url": "https://www.youtube.com/watch?v=yUjjPUTrvt0&t=110s",
    "status": "live",
    "archiveUrl": null,
    "claimIds": [
      "C014"
    ],
    "lastChecked": "2026-05-24",
    "note": "Older project video linked from the Projects page."
  },
  {
    "id": "P008",
    "label": "Reference Letter English PDF",
    "url": "https://lucakosowski.com/Reference_Letter_English.pdf",
    "status": "owned-file",
    "archiveUrl": null,
    "claimIds": [
      "C017"
    ],
    "lastChecked": "2026-05-24",
    "note": "Owned PDF surfaced on References page."
  },
  {
    "id": "P009",
    "label": "Reference Letter Italian PDF",
    "url": "https://lucakosowski.com/Reference_Letter_Italian.pdf",
    "status": "owned-file",
    "archiveUrl": null,
    "claimIds": [
      "C017"
    ],
    "lastChecked": "2026-05-24",
    "note": "Owned PDF surfaced on References page."
  }
];
