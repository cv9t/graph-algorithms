export type GraphObject = Record<string, NodeNeighbor[]>;

export type NodeNeighbor = [string, number];

export type DijkstraSearchResult = [number, string[]];
