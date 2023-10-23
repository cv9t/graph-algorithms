from .graph import Graph
from .utils import all_edge_weights_positive, create_path


class DijkstraError(Exception):
    pass


class Dijkstra:
    def __init__(self, graph) -> None:
        if not isinstance(graph, Graph):
            raise DijkstraError(
                'Argument must be an instance of the Graph class')
        if not all_edge_weights_positive(graph):
            raise DijkstraError(
                'All edge weights on the graph must be positive')
        self._graph = graph

    def search(self, start, end):
        if not self._graph.find_node_by_name(start):
            raise DijkstraError('Start vertex must be on the graph')
        if not self._graph.find_node_by_name(end):
            raise DijkstraError('End vertex must be on the graph')

        distances = {}
        paths = {}
        visited = {}

        for node in self._graph.nodes:
            distances[node.name] = float('inf')
            visited[node.name] = False

        distances[start] = 0

        for _ in range(len(self._graph.nodes)):
            min_node = None
            for node in self._graph.nodes:
                if not visited[node.name] and (min_node is None or distances[node.name] < distances[min_node.name]):
                    min_node = node

            if min_node is None:
                break

            visited[min_node.name] = True

            for neighbor, weight in min_node.neighbors:
                distance = distances[min_node.name] + weight
                if distances[neighbor] > distance:
                    distances[neighbor] = distance
                    paths[neighbor] = min_node.name

        return distances[end], create_path(start, end, paths)
