import { type GraphObject, type NodeNeighbor } from './types';

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

export class Graph {
  private readonly _nodes: Node[] = [];

  constructor(graphObject: GraphObject) {
    for (const [name, neighbors] of Object.entries(graphObject)) {
      this.addNode(new Node(name, neighbors));
    }
  }

  get nodes(): Node[] {
    return this._nodes;
  }

  addNode(node: Node): void {
    this._nodes.push(node);
  }

  findNodeByName(name: string): Node | undefined {
    return this._nodes.find((node) => node.name === name);
  }
}
