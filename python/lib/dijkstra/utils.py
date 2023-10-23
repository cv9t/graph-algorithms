from .graph import Graph


def all_edge_weights_positive(graph: Graph) -> bool:
    for node in graph.nodes:
        for _, weight in node.neighbors:
            if weight < 0:
                return False
    return True
