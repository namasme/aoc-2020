import attr
from itertools import product

from aoc.day17.first.solution import parse_tile, run, step
from aoc.utils import local_path


# didn't see that one coming lmao
@attr.s(frozen=True)
class Point4D:
    x = attr.ib()
    y = attr.ib()
    z = attr.ib()
    w = attr.ib()

    def moore_neighbours(self):
        deltas = [-1, 0, 1]

        return (
            self + Point4D(x, y, z, w)
            for x, y, z, w in product(deltas, repeat=4)
            if x != 0 or y != 0 or z != 0 or w != 0
        )

    def __add__(self, other):
        return Point4D(
            self.x + other.x, self.y + other.y,
            self.z + other.z, self.w + other.w,
        )

    def __str__(self):
        return '(x = {}, y = {}, z = {}, w = {})'.format(
            self.x, self.y,
            self.z, self.w,
        )

    __repr__ = __str__


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        z = 0
        w = 0
        cells = {
            Point4D(x, y, z, w)
            for y, line in enumerate(input_file)
            for x, tile in enumerate(line.strip())
            if parse_tile(tile) == 1
        }

        return cells


def main():
    input_filename = '../input'
    cells = parse_input(local_path(__file__, input_filename))
    n_steps = 6

    final_cells = run(cells, n_steps)
    print(len(final_cells))


if __name__ == '__main__':
    main()
