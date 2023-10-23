import { Graph, type Node } from './graph';
import { type DijkstraSearchResult } from './types';
import { allEdgeWeightsPositive } from './utils';

export * from './graph';

export class DijkstraError extends Error {}

export class Dijkstra {
  _graph: Graph;

  constructor(graph: Graph) {
    this._graph = graph;
  }

  search(start: string, end: string): DijkstraSearchResult {
    return Dijkstra.search(this._graph, start, end);
  }

  static search(graph: Graph, start: string, end: string): DijkstraSearchResult {
    if (!(graph instanceof Graph)) {
      throw new DijkstraError('Argument must be an instance of the Graph class');
    }
    if (!allEdgeWeightsPositive(graph)) {
      throw new DijkstraError('All edge weights on the graph must be positive');
    }
    if (!graph.findNodeByName(start)) {
      throw new DijkstraError('Start vertex must be on the graph');
    }
    if (!graph.findNodeByName(end)) {
      throw new DijkstraError('End vertex must be on the graph');
    }

    const distances: Record<string, number> = {};
    const paths: Record<string, string> = {};
    const visitedNodes: Record<string, boolean> = {};

    for (const node of graph.nodes) {
      distances[node.name] = Infinity;
      visitedNodes[node.name] = false;
    }

    distances[start] = 0;

    for (let i = 0; i < graph.nodes.length; i++) {
      let minNode: Node | null = null;
      for (const node of graph.nodes) {
        if (!visitedNodes[node.name] && (!minNode || distances[node.name] < distances[minNode.name])) {
          minNode = node;
        }
      }

      if (!minNode) {
        break;
      }

      visitedNodes[minNode.name] = true;

      for (const [neighbor, weight] of minNode.neighbors) {
        const tmp = distances[minNode.name] + weight;
        if (distances[neighbor] > tmp) {
          distances[neighbor] = tmp;
          paths[neighbor] = minNode.name;
        }
      }
    }

    const path = Dijkstra._createPath(start, end, paths);

    return [distances[end], path];
  }

  private static _createPath(start: string, end: string, paths: Record<string, string>): string[] {
    const path: string[] = [end];
    let currentNode = end;

    while (currentNode !== start) {
      currentNode = paths[currentNode];
      path.unshift(currentNode);
    }

    return path;
  }
}
