export class DijkstraError extends Error {}

export type Graph = Record<string, Record<string, number>>;

export function dijkstraShortestPaths(graph: Graph, start: string): Record<string, number> {
  if (!graph[start]) {
    throw new DijkstraError('start must be graph vertex');
  }

  if (!areAllValuesPositive(graph)) {
    throw new DijkstraError('all values must be positive');
  }

  const paths: Record<string, number> = {};

  for (const vertex in graph) {
    paths[vertex] = Infinity;
  }

  paths[start] = 0;

  const queue = Object.keys(graph);
  while (queue.length > 0) {
    let minVertex = queue[0];
    for (const vertex of queue) {
      if (paths[vertex] < paths[minVertex]) {
        minVertex = vertex;
      }
    }

    queue.splice(queue.indexOf(minVertex), 1);

    for (const neighbor in graph[minVertex]) {
      paths[neighbor] = Math.min(paths[neighbor], paths[minVertex] + graph[minVertex][neighbor]);
    }
  }

  return paths;
}

function areAllValuesPositive(graph: Graph): boolean {
  for (const node in graph) {
    const neighbors = graph[node];
    for (const neighbor in neighbors) {
      if (neighbors[neighbor] < 0) {
        return false;
      }
    }
  }
  return true;
}
