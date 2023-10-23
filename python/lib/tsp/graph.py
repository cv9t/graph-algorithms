class Node:
    def __init__(self, name, neighbors) -> None:
        self._name = name
        self._neighbors = neighbors

    @property
    def name(self):
        return self._name

    @property
    def neighbors(self):
        return self._neighbors


class Graph:
    def __init__(self, graph_object) -> None:
        self._nodes = []
        for name, neighbors in graph_object.items():
            self.add_node(Node(
                name, [(neighbor[0], neighbor[1], 1, 1 / neighbor[1]) for neighbor in neighbors]))

    @property
    def nodes(self):
        return self._nodes

    def add_node(self, node):
        self._nodes.append(node)

    def find_node_by_name(self, name):
        for node in self._nodes:
            if node.name == name:
                return node
        return None
