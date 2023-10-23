from .core import Graph, allEdgeWeightsPositive
from typing import List, Tuple

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
        validateSearchArguments(graph, start, end)

        distances = {node.name: float('inf') for node in graph.nodes}
        paths = {node.name: '' for node in graph.nodes}
        visitedNodes = {node.name: False for node in graph.nodes}

        distances[start] = 0

        for _ in range(len(graph.nodes)):
            minNode = None
            for node in graph.nodes:
                if not visitedNodes[node.name] and (minNode is None or distances[node.name] < distances[minNode.name]):
                    minNode = node

            if minNode is None:
                break

            visitedNodes[minNode.name] = True

            for neighbor, weight in minNode.neighbors:
                temp = distances[minNode.name] + weight
                if distances[neighbor] > temp:
                    distances[neighbor] = temp
                    paths[neighbor] = minNode.name

        path = createPath(start, end, paths)

        return distances[end], path


def validateSearchArguments(graph: Graph, start: str, end: str) -> None:
    if not isinstance(graph, Graph):
        raise DijkstraError('Argument must be an instance of the Graph class')
    if not allEdgeWeightsPositive(graph):
        raise DijkstraError('All edge weights on the graph must be positive')
    if not graph.findNodeByName(start):
        raise DijkstraError('Start vertex must be on the graph')
    if not graph.findNodeByName(end):
        raise DijkstraError('End vertex must be on the graph')


def createPath(start: str, end: str, paths: dict) -> List[str]:
    path = [end]
    currentNode = end

    while currentNode != start:
        currentNode = paths[currentNode]
        path.insert(0, currentNode)

    return path
