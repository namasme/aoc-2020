import attr
import re

from aoc.day20.first.solution import Flip
from aoc.utils.spatial import Direction


@attr.s
class Tile:
    tile_id = attr.ib()
    borders = attr.ib()
    content = attr.ib()

    @staticmethod
    def parse_tile_id(header):
        return int(re.findall(r'\d+', header)[0])

    @staticmethod
    def parse(tile_section):
        lines = tile_section.strip().split('\n')
        return Tile(
            Tile.parse_tile_id(lines[0]),
            TileBorders.parse(lines[1:]),
            TileContent.parse(lines[1:]),
        )

    def rotate(self):
        return Tile(self.tile_id, self.borders.rotate(), self.content.rotate())

    def flip(self, flip_type):
        return Tile(
            self.tile_id,
            self.borders.flip(flip_type),
            self.content.flip(flip_type),
        )


@attr.s
class TileBorders:
    '''
    Most of the code is copied from the first part but with some
    modifications (such as the rotate method). F*ck DRY.
    '''
    borders = attr.ib()
    width = attr.ib()

    @staticmethod
    def to_int(border):
        return int(
            border.translate(str.maketrans('.#', '01')),
            2,
        )

    @staticmethod
    def parse(lines):
        borders = list(map(TileBorders.to_int, [
            lines[0],  # top
            ''.join([line[-1] for line in lines]),  # right
            lines[-1][::-1],  # bottom
            ''.join([line[0] for line in lines][::-1]),  # left
        ]))
        width = len(lines)

        return TileBorders(borders, width)

    def flip_border(self, border):
        full_binary = bin(border)[2:].zfill(self.width)
        return int(full_binary[::-1], 2)

    def flip(self, flip_type):
        if flip_type == Flip.HORIZONTAL:
            new_borders_order = [2, 1, 0, 3]
        elif flip_type == Flip.VERTICAL:
            new_borders_order = [0, 3, 2, 1]

        new_borders = [
            self.flip_border(self.borders[i])
            for i in new_borders_order
        ]

        return TileBorders(new_borders, self.width)

    def rotate(self):
        # assume clockwise
        return TileBorders([self.borders[-1]] + self.borders[:-1], self.width)

    def borders_match(self, direction, other_tile, other_direction):
        directions = [Direction.U, Direction.R, Direction.D, Direction.L]
        index = directions.index(direction)
        other_index = directions.index(other_direction)
        are_opposite = ((index - other_index) % 4) == 2
        assert are_opposite

        return (
            self.borders[index]
            ==
            other_tile.flip_border(other_tile.borders[other_index])
        )


@attr.s
class TileContent:
    rows = attr.ib()

    @staticmethod
    def parse(lines):
        rows = [line[1:-1] for line in lines[1:-1]]

        return TileContent(rows)

    def flip(self, flip_type):
        if flip_type == Flip.HORIZONTAL:
            new_rows = list(reversed(self.rows))
        elif flip_type == Flip.VERTICAL:
            new_rows = [''.join(reversed(row)) for row in self.rows]

        return TileContent(new_rows)

    def rotate(self):
        # assume clockwise
        return TileContent([
            ''.join(new_row)
            for new_row in zip(*reversed(self.rows))
        ])


@attr.s
class TileTransformation:
    SIZE = 8  # not the best name ever

    rotate = attr.ib()  # r
    flip_horizontally = attr.ib()  # s
    flip_vertically = attr.ib()  # r^2s

    @staticmethod
    def from_id(transformation_id):
        rotate = bool((transformation_id & 4) >> 2)
        flip_horizontally = bool((transformation_id & 2) >> 1)
        flip_vertically = bool(transformation_id & 1)

        return TileTransformation(rotate, flip_horizontally, flip_vertically)

    def apply(self, tile):
        temp = tile

        if self.rotate:
            temp = temp.rotate()

        if self.flip_horizontally:
            temp = temp.flip(Flip.HORIZONTAL)

        if self.flip_vertically:
            temp = temp.flip(Flip.VERTICAL)

        return temp
