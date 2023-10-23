import { describe, expect, test } from '@jest/globals';

import { Graph, Dijkstra } from '~lib/dijkstra';

describe("Dijkstra's algorithm", () => {
  const mockedGraph = new Graph({
    '1': [
      ['2', 10],
      ['3', 6],
      ['4', 8],
    ],
    '2': [
      ['4', 5],
      ['5', 13],
      ['7', 11],
    ],
    '3': [['5', 3]],
    '4': [
      ['3', 2],
      ['5', 5],
      ['7', 12],
      ['6', 7],
    ],
    '5': [
      ['6', 9],
      ['9', 12],
    ],
    '6': [
      ['8', 8],
      ['9', 10],
    ],
    '7': [
      ['6', 4],
      ['8', 6],
      ['9', 16],
    ],
    '8': [['9', 15]],
    '9': [],
  });

  test("finds the shortest path from '1' to '9'", () => {
    const [distance, path] = Dijkstra.search(mockedGraph, '1', '9');

    expect(distance).toBe(21);
    expect(path).toEqual(['1', '3', '5', '9']);
  });
});
