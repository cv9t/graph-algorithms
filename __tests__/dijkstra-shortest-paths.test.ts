import { describe, expect, jest, test } from '@jest/globals';
import { DijkstraError, Graph, dijkstraShortestPaths } from '~lib/dijkstra-shortest-paths';

describe('dijkstra-shortest-paths', () => {
  const mockedGraph: Graph = { 1: { 2: 10, 4: 30, 5: 100 }, 2: { 3: 50 }, 3: { 5: 10 }, 4: { 3: 20, 5: 60 }, 5: {} };

  test('finds the shortest paths for "1"', () => {
    const paths = dijkstraShortestPaths(mockedGraph, '1');

    expect(paths[1]).toBe(0);
    expect(paths[2]).toBe(10);
    expect(paths[3]).toBe(50);
    expect(paths[4]).toBe(30);
    expect(paths[5]).toBe(60);
  });

  test('finds the shortest paths for "2"', () => {
    const paths = dijkstraShortestPaths(mockedGraph, '2');

    expect(paths[1]).toBe(Infinity);
    expect(paths[2]).toBe(0);
    expect(paths[3]).toBe(50);
    expect(paths[4]).toBe(Infinity);
    expect(paths[5]).toBe(60);
  });

  test('finds the shortest paths for "5"', () => {
    const paths = dijkstraShortestPaths(mockedGraph, '5');

    expect(paths[1]).toBe(Infinity);
    expect(paths[2]).toBe(Infinity);
    expect(paths[3]).toBe(Infinity);
    expect(paths[4]).toBe(Infinity);
    expect(paths[5]).toBe(0);
  });

  test('throws an error if there is no vertex in the graph', () => {
    const mockFn = jest.fn(() => dijkstraShortestPaths(mockedGraph, '6'));

    expect(mockFn).toThrow(new DijkstraError('start must be graph vertex'));
  });

  test('throws an error if there are negative values in the graph', () => {
    const mockFn = jest.fn(() =>
      dijkstraShortestPaths({ 1: { 2: -100, 4: 30, 5: 100 }, 2: { 3: 50 }, 3: { 5: 10 }, 4: { 3: 20, 5: 60 }, 5: {} }, '1'),
    );

    expect(mockFn).toThrow(new DijkstraError('all values must be positive'));
  });
});
