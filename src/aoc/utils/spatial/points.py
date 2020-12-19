from functools import total_ordering
from itertools import product

from .enums import Direction


@total_ordering
class Point2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def from_direction(direction):
        x, y = ({
            Direction.L: (-1, 0),
            Direction.U: (0, 1),
            Direction.R: (1, 0),
            Direction.D: (0, -1),
        })[direction]

        return Point2D(x, y)

    def lies_between(self, p, q):
        return (
            Point2D.are_colinear(self, p, q)
            and self.lies_within(p, q)
        )

    def lies_within(self, p, q):
        x, X = min(p.x, q.x), max(p.x, q.x)
        y, Y = min(p.y, q.y), max(p.y, q.y)

        return x <= self.x <= X and y <= self.y <= Y

    @staticmethod
    def get_orientation(p, q, r):
        orientation = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);

        if orientation > 0:
            return Orientation.CLOCKWISE
        elif orientation < 0:
            return Orientation.COUNTERCLOCKWISE
        else:
            return Orientation.COLINEAR

    @staticmethod
    def are_colinear(p, q, r):
        return Point2D.get_orientation(p, q, r) == Orientation.COLINEAR

    def move_by(self, direction, quantity=1):
        return self + quantity * Point2D.from_direction(direction)

    def distance_to(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def von_neumann_neighbours(self):
        for direction in Direction:
            yield self.move_by(direction)

    def moore_neighbours(self):
        deltas = [-1, 0, 1]

        for y in deltas:
            for x in deltas:
                if x == 0 and y == 0:
                    continue

                yield Point2D(self.x + x, self.y + y)

    def __abs__(self):
        return abs(self.x) + abs(self.y)

    def __add__(self, point):
        return Point2D(self.x + point.x, self.y + point.y)

    def __sub__(self, point):
        return Point2D(self.x - point.x, self.y - point.y)

    def __rmul__(self, scale):
        return Point2D(scale * self.x, scale * self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __le__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __str__(self):
        return '(x = {}, y = {})'.format(self.x, self.y)

    __repr__ = __str__


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other):
        return abs(self - other)

    def moore_neighbours(self):
        deltas = [-1, 0, 1]

        return (
            self + Point3D(x, y, z)
            for x, y, z in product(deltas, repeat=3)
            if x != 0 or y != 0 or z != 0
        )

    def __abs__(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self = self + other
        return self

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __isub__(self, other):
        self = self - other
        return self

    def __rmul__(self, scale):
        return Point3D(scale * self.x, scale * self.y, scale * self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __le__(self, other):
        return (self.x, self.y, self.z) < (other.x, other.y, other.z)

    def __str__(self):
        return '(x = {}, y = {}, z = {})'.format(self.x, self.y, self.z)

    __repr__ = __str__
