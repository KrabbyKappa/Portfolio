import { answerClusters } from '../../data/seo/answerClusters';

export function siblingAnswerLinks(currentId: string, limit = 3) {
  const current = answerClusters.find((cluster) => cluster.id === currentId);
  if (!current) return [];
  return answerClusters
    .filter((cluster) => cluster.family === current.family && cluster.id !== currentId)
    .slice(0, limit)
    .map((cluster) => ({ title: cluster.title, url: cluster.url }));
}
