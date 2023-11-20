class Point:
    def __init__(self, x, y, prev=None) -> None:
        self.x = x
        self.y = y
        self.prev = prev

    def __str__(self):
        return f'{self.x}:{self.y}'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return str(self) < str(other)
