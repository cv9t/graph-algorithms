import { type Graph } from './graph';

export function allEdgeWeightsPositive(graph: Graph): boolean {
  return graph.nodes.every((node) => node.neighbors.every(([_, weight]) => weight >= 0));
}
