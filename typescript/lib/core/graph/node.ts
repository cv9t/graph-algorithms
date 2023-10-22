export type NodeNeighbor = [string, number];

export class Node {
  constructor(
    private readonly _name: string,
    private readonly _neighbors: NodeNeighbor[],
  ) {}

  get name(): string {
    return this._name;
  }

  get neighbors(): NodeNeighbor[] {
    return this._neighbors;
  }
}
