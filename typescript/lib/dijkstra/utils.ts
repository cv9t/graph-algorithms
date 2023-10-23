import { type Graph } from './graph';

export function allEdgeWeightsPositive(graph: Graph): boolean {
  return graph.nodes.every((node) => node.neighbors.every(([_, weight]) => weight >= 0));
}

export function createPath(start: string, end: string, paths: Record<string, string>): string[] {
  const path: string[] = [end];
  let currentNode = end;

  while (currentNode !== start) {
    currentNode = paths[currentNode];
    path.unshift(currentNode);
  }

  return path;
}
