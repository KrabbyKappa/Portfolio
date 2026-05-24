import { answerClusters } from '../../data/seo/answerClusters';

export const answerCorpusContract = {
  requiredClusterCount: 14,
  requiredQuestionCount: 126,
  minQuestionsPerCluster: 8,
  maxQuestionsPerCluster: 20,
  minSlugWords: 10,
  hiddenFromPrimaryNavigation: true,
  excludedFromHumanSitemap: true,
  includedInMachineIndex: true,
} as const;

export function answerSlugWordCount(slug: string) {
  return slug.split('-').filter(Boolean).length;
}

export function answerCorpusQuestionCount() {
  return answerClusters.reduce((total, cluster) => total + cluster.questions.length, 0);
}
