import { Node, type NodeNeighbor } from './node';

export type GraphObject = Record<string, NodeNeighbor[]>;

export * from './node';

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
