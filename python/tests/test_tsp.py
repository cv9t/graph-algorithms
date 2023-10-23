from lib.tsp import AntColony, Graph


class TestTsp():
    mockedGraph = Graph({
        'a': [('b', 3), ('f', 1)],
        'b': [('a', 3), ('c', 8), ('g', 3)],
        'c': [('b', 3), ('d', 1), ('g', 1)],
        'd': [('c', 8), ('f', 1)],
        'f': [('d', 3), ('a', 3)],
        'g': [('a', 3), ('b', 3), ('c', 3), ('d', 5), ('f', 4)]
    })

    def test_search(self):
        antColony = AntColony(self.mockedGraph)
        distance, path = antColony.search(10000)

        print(path, distance)
        assert distance == 11
        assert path == ['a', 'b', 'g', 'c', 'd', 'f']
