from lib.dijkstra import Dijkstra, Graph


class TestDijkstra():
    mockedGraph = Graph({
        '1': [
            ('2', 10),
            ('3', 6),
            ('4', 8),
        ],
        '2': [
            ('4', 5),
            ('5', 13),
            ('7', 11),
        ],
        '3': [('5', 3)],
        '4': [
            ('3', 2),
            ('5', 5),
            ('7', 12),
            ('6', 7),
        ],
        '5': [
            ('6', 9),
            ('9', 12),
        ],
        '6': [
            ('8', 8),
            ('9', 10),
        ],
        '7': [
            ('6', 4),
            ('8', 6),
            ('9', 16),
        ],
        '8': [('9', 15)],
        '9': [],
    })

    def test_search(self):
        dijkstra = Dijkstra(self.mockedGraph)
        distance, path = dijkstra.search('1', '9')

        assert distance == 21
        assert path == ['1', '3', '5', '9']
