from lib import dijkstra_shortest_paths


def test_dijkstra_shortest_paths():
    graph = {
        '1': {'2': 10, '3': 6, '4': 8},
        '2': {'4': 5, '5': 13, '7': 11},
        '3': {'5': 3},
        '4': {'3': 2, '5': 5, '7': 12, '6': 7},
        '5': {'6': 9, '9': 12},
        '6': {'8': 8, '9': 10},
        '7': {'6': 4, '8': 6, '9': 16},
        '8': {'9': 15},
        '9': {},
    }

    start_vertex, end_vertex = '1', '9'
    paths, visited_nodes = dijkstra_shortest_paths(graph, start_vertex)

    assert paths[end_vertex] == 21, 'Not equal path'
    assert visited_nodes['9'] == [
        '1', '3', '5', '9'], 'Not equal visited nodes'
