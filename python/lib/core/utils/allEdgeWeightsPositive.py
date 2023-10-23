from ..graph import Graph


def allEdgeWeightsPositive(graph: Graph) -> bool:
    for node in graph.nodes:
        for _, weight in node.neighbors:
            if weight < 0:
                return False
    return True
