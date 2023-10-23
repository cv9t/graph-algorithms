def all_edge_weights_positive(graph):
    for node in graph.nodes:
        for _, weight in node.neighbors:
            if weight < 0:
                return False
    return True


def create_path(start, end, paths):
    path = [end]
    current_node = end

    while current_node != start:
        current_node = paths[current_node]
        path.insert(0, current_node)

    return path
