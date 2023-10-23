from typing import List, Tuple

NodeNeighbor = Tuple[str, int]


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
