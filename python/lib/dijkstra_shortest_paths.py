class DijkstraError(Exception):
    pass


def dijkstra_shortest_paths(graph, start_vertex):
    if start_vertex not in graph:
        raise DijkstraError('start_vertex must be graph vertex')

    if not are_all_values_positive(graph):
        raise DijkstraError('all values must be positive')

    paths = {}
    visited_nodes = {}

    for vertex in graph:
        paths[vertex] = float('inf')
        visited_nodes[vertex] = [start_vertex]

    paths[start_vertex] = 0
    queue = list(graph.keys())

    while queue:
        min_vertex = queue[0]
        for vertex in queue:
            if paths[vertex] < paths[min_vertex]:
                min_vertex = vertex

        queue.remove(min_vertex)

        for neighbor, weight in graph[min_vertex].items():
            if paths[min_vertex] + weight < paths[neighbor]:
                paths[neighbor] = paths[min_vertex] + weight
                visited_nodes[neighbor] = visited_nodes.get(
                    min_vertex, []) + [neighbor]

    return paths, visited_nodes


def are_all_values_positive(graph):
    for _, neighbors in graph.items():
        for _, weight in neighbors.items():
            if weight < 0:
                return False
    return True
