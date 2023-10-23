from typing import List, Dict, Optional
from .node import Node, NodeNeighbor

GraphObject = Dict[str, List[NodeNeighbor]]


class Graph:
    def __init__(self, graphObject: GraphObject) -> None:
        self._nodes: List[Node] = []
        for name, neighbors in graphObject.items():
            self.addNode(Node(name, neighbors))

    @property
    def nodes(self) -> List[Node]:
        return self._nodes

    def addNode(self, node: Node) -> None:
        self._nodes.append(node)

    def findNodeByName(self, name: str) -> Optional[Node]:
        return next((node for node in self._nodes if node.name == name), None)
