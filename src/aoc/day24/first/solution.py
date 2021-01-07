from collections import Counter

from aoc.utils import local_path
from aoc.utils.spatial import Point2D


def translate_direction(direction):
    return ({
        'e': Point2D(1, 0),
        'w': Point2D(-1, 0),
        'ne': Point2D(0, 1),
        'sw': Point2D(0, -1),
        'nw': Point2D(-1, 1),
        'se': Point2D(1, -1),
    })[direction]


def parse_token(line):
    if line.startswith('n') or line.startswith('s'):
        token_length = 2
    else:
        token_length = 1

    return (line[:token_length], line[token_length:])


def parse_directions(line):
    tokens = []

    while line:
        token, line = parse_token(line)
        tokens.append(token)

    return tokens


def parse_tile(line):
    tokens = parse_directions(line)

    return sum(map(translate_direction, tokens), Point2D(0, 0))


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return [parse_tile(line.strip()) for line in input_file]


def flip_tiles(tiles):
    flips = Counter(tiles)

    return [tile for tile, flips_count in flips.items() if flips_count % 2 == 1]


def main():
    input_filename = '../input'
    tiles = parse_input(input_filename)
    flipped_tiles = flip_tiles(tiles)

    print(len(flipped_tiles))


if __name__ == '__main__':
    main()
