import random
from .graph import *


class AntColony:
    def __init__(self, graph) -> None:
        self._graph = graph

    def search(self, generations):
        results = []
        for node in self._graph.nodes:
            results.append(self._search(node.name, generations))

        best_result = results[0]
        for result in results:
            if result[0] < best_result[0]:
                best_result = result

        return best_result

    def _search(self, start, generations):
        distances, paths = self._initialize_data()

        for _ in range(generations):
            visited, distance, skip = self._explore_path([start])
            if skip:
                continue
            distances, paths = self._update_pheromones(
                visited, distances, paths, distance)

        result = [float('inf'), []]
        for node in distances.keys():
            if distances[node] < result[0]:
                result = [distances[node], paths[node]]

        return result

    def _initialize_data(self):
        distances = {}
        paths = {}

        for node in self._graph.nodes:
            distances[node.name] = float('inf')
            paths[node.name] = []

        return distances, paths

    def _explore_path(self, visited):
        distance = 0
        skip = False

        while len(visited) < len(self._graph.nodes):
            current_node = self._graph.find_node_by_name(visited[-1])
            possibilities, visited_neighbor_count, attraction = self._get_node_data(
                current_node, visited)

            if visited_neighbor_count == len(current_node.neighbors):
                skip = True
                break

            visited, distance = self._choose_next_node(
                possibilities, attraction, visited, distance)

        return visited, distance, skip

    def _get_node_data(self, node, visited):
        possibilities = []
        visited_neighbor_count = 0
        attraction = 0

        for neighbor, weight, t, n in node.neighbors:
            if neighbor in visited:
                visited_neighbor_count += 1
                continue
            tn = t * n
            attraction += tn
            possibilities.append([neighbor, tn, weight])

        return possibilities, visited_neighbor_count, attraction

    def _choose_next_node(self, possibilities, attraction, visited, distance):
        for i in range(len(possibilities)):
            possibilities[i][1] /= attraction
            if i > 0:
                possibilities[i][1] += possibilities[i-1][1]

        random_value = random.random()
        for node, tn, weight in possibilities:
            if random_value < tn:
                visited.append(node)
                distance += weight
                break

        return visited, distance

    def _update_pheromones(self, visited, distances, paths, distance):
        for i in range(len(visited) - 1):
            current_node = self._graph.find_node_by_name(visited[i])
            for neighbor, _, t, _ in current_node.neighbors:
                if neighbor == visited[i + 1]:
                    t += 1 / distance

        if distances[visited[0]] > distance:
            distances[visited[0]] = distance
            paths[visited[0]] = visited

        return distances, paths
