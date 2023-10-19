import { describe, expect, jest, test } from '@jest/globals';
import { DijkstraError, Graph, dijkstraShortestPaths } from '~lib/dijkstra-shortest-paths';

describe('dijkstra-shortest-paths', () => {
  const mockedGraph: Graph = {
    1: { 2: 10, 3: 6, 4: 8 },
    2: { 4: 5, 5: 13, 7: 11 },
    3: { 5: 3 },
    4: { 3: 2, 5: 5, 7: 12, 6: 7 },
    5: { 6: 9, 9: 12 },
    6: { 8: 8, 9: 10 },
    7: { 6: 4, 8: 6, 9: 16 },
    8: { 9: 15 },
    9: {},
  };

  test('finds the shortest paths for "1"', () => {
    const paths = dijkstraShortestPaths(mockedGraph, '1');
    expect(paths[9]).toBe(21);
  });

  test('throws an error if there is no vertex in the graph', () => {
    const mockFn = jest.fn(() => dijkstraShortestPaths(mockedGraph, '10'));
    expect(mockFn).toThrow(new DijkstraError('start must be graph vertex'));
  });

  test('throws an error if there are negative values in the graph', () => {
    const mockFn = jest.fn(() =>
      dijkstraShortestPaths({ 1: { 2: -100, 4: 30, 5: 100 }, 2: { 3: 50 }, 3: { 5: 10 }, 4: { 3: 20, 5: 60 }, 5: {} }, '1'),
    );
    expect(mockFn).toThrow(new DijkstraError('all values must be positive'));
  });
});
