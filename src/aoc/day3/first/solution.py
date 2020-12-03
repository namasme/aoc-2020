from enum import Enum

from aoc.utils import local_path


class Tile(Enum):
    EMPTY = '.'
    TREE = '#'


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return parse_lines(input_file)


def parse_lines(lines):
    return [
        [Tile(character) for character in line.strip()]
        for line in lines
    ]

def count_trees_in_path(tiles):
    row_count = len(tiles)
    column_count = len(tiles[0])
    positions = [(i, 3 * i % column_count) for i in range(1, row_count)]
    path = [tiles[row][column] for row, column in positions]

    return sum([tile == Tile.TREE for tile in path])


def main():
    input_filename = '../input'
    tiles = parse_input(local_path(__file__, input_filename))

    print(count_trees_in_path(tiles))


if __name__ == '__main__':
    main()
