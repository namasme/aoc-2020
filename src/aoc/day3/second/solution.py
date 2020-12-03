from functools import reduce
from operator import mul

from aoc.utils import local_path

from aoc.day3.first.solution import parse_input, Tile


def generate_path(right, down):
    i = 0

    while True:
        yield (i * down, i * right)
        i += 1


def count_trees_in_path(tiles, path):
    row_count, column_count = len(tiles), len(tiles[0])
    trees_found = 0
    row, column = next(path)

    while row < row_count:
        if tiles[row][column % column_count] == Tile.TREE:
            trees_found += 1

        row, column = next(path)

    return trees_found


def main():
    input_filename = '../input'
    tiles = parse_input(local_path(__file__, input_filename))

    paths = [{
        'right': 1,
        'down': 1,
    }, {
        'right': 3,
        'down': 1,
    }, {
        'right': 5,
        'down': 1,
    }, {
        'right': 7,
        'down': 1,
    }, {
        'right': 1,
        'down': 2,
    }]

    trees = [count_trees_in_path(tiles, generate_path(**path)) for path in paths]

    print(reduce(mul, trees, 1))



if __name__ == '__main__':
    main()
