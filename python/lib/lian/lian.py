from queue import PriorityQueue
from point import Point
from vector import Vector


class Lian:
    def __init__(self, image) -> None:
        self.__image = image
        self.__open = PriorityQueue()
        self.__closed = []

    def __reset(self):
        self.__open = PriorityQueue()
        self._closed = []

    def search(self, start, end, delta, max_angle):
        self.__reset()
        start.prev = start
        self.__open.put((0, start))
        while not self.__open.empty():
            _, point = self.__open.get()
            line = self.__get_bresenham_line(point.prev, point)
            self.__closed.append(point)
            if self.__is_path_available(line):
                if point == end:
                    end.prev = point.prev
                    return self.__create_path(start, end)
                successors = self.__gen_successors(
                    circle_center=point, start=start, end=end, delta=delta, max_angle=max_angle)
                for go_to in successors:
                    weight = Vector(go_to, end).get_length()
                    go_to.prev = point
                    self.__open.put((weight, go_to))
        return []

    def __is_point_exists(self, point):
        return 0 <= point.x < self.__image.shape[1] and 0 <= point.y < self.__image.shape[0]

    def __is_path_available(self, line):
        for point in line:
            if self.__image[point.y, point.x] == 0:
                return False
        return True

    def __create_path(self, start, end):
        path = []
        curr = end
        while curr != start:
            line = self.__get_bresenham_line(curr.prev, curr)
            path.extend(line)
            curr = curr.prev
        path.append(start)
        return list(reversed(path))

    def __gen_successors(self, start, end, delta, max_angle, circle_center):
        successors = []
        vec1 = Vector(circle_center.prev, circle_center)
        circle = self.__get_midpoint_circle(circle_center, delta)
        for point in circle:
            vec2 = Vector(circle_center, point)
            if point in self.__closed or \
                self.__image[point.y, point.x] == 0 or \
                ((circle_center != start) and (Vector.angle_between(vec1, vec2) > max_angle)) or \
                    not self.__is_point_exists(point):
                continue
            successors.append(point)
        vec2 = Vector(circle_center, end)
        if Vector(circle_center, end).get_length() < delta and Vector.angle_between(vec1, vec2) < max_angle:
            successors.append(end)
        return successors

    def __get_midpoint_circle(self, center, delta):
        circle = []
        cx, cy = center.x, center.y
        x, y = delta, 0
        if self.__is_point_exists(Point(x + cx, y + cy)):
            circle.append(Point(x + cx, y + cy))
        if delta > 0:
            if self.__is_point_exists(Point(x + cx, -y + cy)):
                circle.append(Point(x + cx, -y + cy))
            if self.__is_point_exists(Point(y + cx, x + cy)):
                circle.append(Point(y + cx, x + cy))
            if self.__is_point_exists(Point(-x + cx, -y + cy)):
                circle.append(Point(-x + cx, -y + cy))
            if self.__is_point_exists(Point(y + cx, -x + cy)):
                circle.append(Point(y + cx, -x + cy))
        P = 1 - delta
        while x > y:
            y += 1
            if P <= 0:
                P = P + 2 * y + 1
            else:
                x -= 1
                P = P + 2 * y - 2 * x + 1
            if (x < y):
                break
            if self.__is_point_exists(Point(x + cx, y + cy)):
                circle.append(Point(x + cx, y + cy))
            if self.__is_point_exists(Point(-x + cx, y + cy)):
                circle.append(Point(-x + cx, y + cy))
            if self.__is_point_exists(Point(x + cx, -y + cy)):
                circle.append(Point(x + cx, -y + cy))
            if self.__is_point_exists(Point(-x + cx, -y + cy)):
                circle.append(Point(-x + cx, -y + cy))
            if x != y:
                if self.__is_point_exists(Point(y + cx, x + cy)):
                    circle.append(Point(y + cx, x + cy))
                if self.__is_point_exists(Point(-y + cx, x + cy)):
                    circle.append(Point(-y + cx, x + cy))
                if self.__is_point_exists(Point(y + cx, -x + cy)):
                    circle.append(Point(y + cx, -x + cy))
                if self.__is_point_exists(Point(-y + cx, -x + cy)):
                    circle.append(Point(-y + cx, -x + cy))
        return circle

    def __get_bresenham_line(self, start, end):
        line = []
        dx = end.x - start.x
        dy = end.y - start.y
        sx = 1 if dx > 0 else -1 if dx < 0 else 0
        sy = 1 if dy > 0 else -1 if dy < 0 else 0
        if dx < 0:
            dx = -dx
        if dy < 0:
            dy = -dy
        if dx > dy:
            pdx, pdy = sx, 0
            es, el = dy, dx
        else:
            pdx, pdy = 0, sy
            es, el = dx, dy
        x, y = start.x, start.y
        line.append(start)
        err, t = el / 2, 0
        while t < el:
            err -= es
            if err < 0:
                err += el
                x += sx
                y += sy
            else:
                x += pdx
                y += pdy
            t += 1
            line.append(Point(x, y))
        return line
