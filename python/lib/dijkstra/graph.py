from typing import List, Optional
from .types import NodeNeighbor, GraphObject


class Node:
    def __init__(self, name: str, neighbors: List[NodeNeighbor]) -> None:
        self._name = name
        self._neighbors = neighbors

    @property
    def name(self) -> str:
        return self._name

    @property
    def neighbors(self) -> List[NodeNeighbor]:
        return self._neighbors


class Graph:
    def __init__(self, graphObject: GraphObject) -> None:
        self._nodes: List[Node] = []
        for name, neighbors in graphObject.items():
            self.add_node(Node(name, neighbors))

    @property
    def nodes(self) -> List[Node]:
        return self._nodes

    def add_node(self, node: Node) -> None:
        self._nodes.append(node)

    def find_node_by_name(self, name: str) -> Optional[Node]:
        for node in self._nodes:
            if node.name == name:
                return node
        return None
