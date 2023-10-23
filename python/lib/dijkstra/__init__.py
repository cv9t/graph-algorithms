from typing import List, Tuple, Dict
from .graph import Graph
from .utils import all_edge_weights_positive

DijkstraSearchResult = Tuple[float, List[str]]


class DijkstraError(Exception):
    pass


class Dijkstra:
    def __init__(self, graph: Graph) -> None:
        self._graph = graph

    def search(self, start: str, end: str) -> DijkstraSearchResult:
        return Dijkstra.search(self._graph, start, end)

    @staticmethod
    def search(graph: Graph, start: str, end: str) -> DijkstraSearchResult:
        if not isinstance(graph, Graph):
            raise DijkstraError(
                'Argument must be an instance of the Graph class')
        if not all_edge_weights_positive(graph):
            raise DijkstraError(
                'All edge weights on the graph must be positive')
        if not graph.find_node_by_name(start):
            raise DijkstraError('Start vertex must be on the graph')
        if not graph.find_node_by_name(end):
            raise DijkstraError('End vertex must be on the graph')

        distances: Dict[str, int] = {}
        paths: Dict[str, str] = {}
        visited_nodes: Dict[str, bool] = {}

        for node in graph.nodes:
            distances[node.name] = float('inf')
            visited_nodes[node.name] = False

        distances[start] = 0

        for _ in range(len(graph.nodes)):
            min_node = None
            for node in graph.nodes:
                if not visited_nodes[node.name] and (min_node is None or distances[node.name] < distances[min_node.name]):
                    min_node = node

            if min_node is None:
                break

            visited_nodes[min_node.name] = True

            for neighbor, weight in min_node.neighbors:
                temp = distances[min_node.name] + weight
                if distances[neighbor] > temp:
                    distances[neighbor] = temp
                    paths[neighbor] = min_node.name

        path = Dijkstra._create_path(start, end, paths)

        return distances[end], path

    @staticmethod
    def _create_path(start: str, end: str, paths: Dict[str, str]) -> List[str]:
        path = [end]
        current_node = end

        while current_node != start:
            current_node = paths[current_node]
            path.insert(0, current_node)

        return path
