import attr
import re
from collections import Counter
from enum import auto, Enum
from functools import reduce
from operator import mul

from aoc.utils import local_path


class Flip(Enum):
    HORIZONTAL = auto()
    VERTICAL = auto()


@attr.s
class Tile:
    TILE_WIDTH = 10

    tile_id = attr.ib()
    borders = attr.ib()

    @staticmethod
    def to_int(border):
        return int(
            border.translate(str.maketrans('.#', '01')),
            2,
        )

    @staticmethod
    def flip_border(border):
        full_binary = bin(border)[2:].zfill(Tile.TILE_WIDTH)
        return int(full_binary[::-1], 2)

    @staticmethod
    def parse(tile_section):
        lines = tile_section.split('\n')
        tile_id = int(re.findall(r'\d+', lines[0])[0])
        borders = list(map(Tile.to_int, [
            lines[1],  # top
            ''.join([line[-1] for line in lines[1:]]),  # right
            lines[-1][::-1],  # bottom
            ''.join([line[0] for line in lines[1:]][::-1]),  # left
        ]))

        return Tile(tile_id, borders)

    def flip(self, flip_type):
        if flip_type == Flip.HORIZONTAL:
            new_borders_order = [2, 1, 0, 3]
        elif flip_type == Flip.VERTICAL:
            new_borders_order = [0, 3, 2, 1]

        new_borders = [
            self.flip_border(self.borders[i])
            for i in new_borders_order
        ]

        return Tile(self.tile_id, new_borders)

    def generate_all_borders(self):
        return (
            self.borders
            + self.flip(Flip.HORIZONTAL).borders
            + self.flip(Flip.VERTICAL).borders
            + self.flip(Flip.HORIZONTAL).flip(Flip.VERTICAL).borders
        )


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return [
            Tile.parse(tile_section.strip())
            for tile_section in input_file.read().split('\n\n')
        ]


def find_corners(tiles):
    '''
    This is probably NOT guaranteed to work at all, but it was enough for my
    input (I'm willing to bet all inputs admitted this kind of trick
    for the first part).
    '''
    all_borders = sum([tile.generate_all_borders() for tile in tiles], [])
    borders_with_multiplicity = Counter(all_borders)

    assert min(borders_with_multiplicity.values()) == 2

    unmatched_borders = {
        border
        for border, multiplicity in borders_with_multiplicity.items()
        if multiplicity == 2
    }

    corners = [
        tile
        for tile in tiles
        if len(unmatched_borders.intersection(set(tile.borders))) == 2
    ]

    return corners


def main():
    input_filename = '../input'
    tiles = parse_input(local_path(__file__, input_filename))
    corner_tiles = find_corners(tiles)

    print(reduce(mul, [corner_tile.tile_id for corner_tile in corner_tiles]))


if __name__ == '__main__':
    main()
