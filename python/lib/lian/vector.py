import math
from point import Point


class Vector:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def get_coords(self):
        return Point(self.end.x - self.start.x, self.end.y - self.start.y)

    def get_length(self):
        coords = self.get_coords()
        return math.sqrt(coords.x ** 2 + coords.y ** 2)

    @staticmethod
    def angle_between(vec1, vec2):
        vec1_coords = vec1.get_coords()
        vec2_coords = vec2.get_coords()
        numen = vec1_coords.x * vec2_coords.x + vec1_coords.y * vec2_coords.y
        denom = vec1.get_length() * vec2.get_length()
        if denom == 0:
            return 0
        return round(math.acos(numen / round(denom)) * (180 / math.pi))
