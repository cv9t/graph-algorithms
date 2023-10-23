import { Graph, type Node } from './graph';
import { type DijkstraSearchResult } from './types';
import { allEdgeWeightsPositive, createPath } from './utils';

export * from './graph';

export class DijkstraError extends Error {}

export class Dijkstra {
  _graph: Graph;

  constructor(graph: Graph) {
    if (!(graph instanceof Graph)) {
      throw new DijkstraError('Argument must be an instance of the Graph class');
    }
    if (!allEdgeWeightsPositive(graph)) {
      throw new DijkstraError('All edge weights on the graph must be positive');
    }
    this._graph = graph;
  }

  search(start: string, end: string): DijkstraSearchResult {
    if (!this._graph.findNodeByName(start)) {
      throw new DijkstraError('Start vertex must be on the graph');
    }
    if (!this._graph.findNodeByName(end)) {
      throw new DijkstraError('End vertex must be on the graph');
    }

    const distances: Record<string, number> = {};
    const paths: Record<string, string> = {};
    const visited: Record<string, boolean> = {};

    for (const node of this._graph.nodes) {
      distances[node.name] = Infinity;
      visited[node.name] = false;
    }

    distances[start] = 0;

    for (let i = 0; i < this._graph.nodes.length; i++) {
      let minNode: Node | null = null;
      for (const node of this._graph.nodes) {
        if (!visited[node.name] && (!minNode || distances[node.name] < distances[minNode.name])) {
          minNode = node;
        }
      }

      if (!minNode) {
        break;
      }

      visited[minNode.name] = true;

      for (const [neighbor, weight] of minNode.neighbors) {
        const distance = distances[minNode.name] + weight;
        if (distances[neighbor] > distance) {
          distances[neighbor] = distance;
          paths[neighbor] = minNode.name;
        }
      }
    }

    return [distances[end], createPath(start, end, paths)];
  }
}
