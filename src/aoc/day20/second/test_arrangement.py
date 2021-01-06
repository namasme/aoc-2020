import pytest

from aoc.utils import local_path
from aoc.utils.spatial import Direction
from .arrangement import (
    arrange_tiles, has_tile_above, has_tile_leftwards, to_coordinates, to_index,
)
from .tiles import Tile, TileBorders, TileContent
from .solution import parse_input


@pytest.fixture
def tiles():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_to_coordinates():
    assert to_coordinates(0, 3) == (0, 0)
    assert to_coordinates(3, 3) == (0, 1)
    assert to_coordinates(5, 3) == (2, 1)
    assert to_coordinates(8, 3) == (2, 2)


def test_to_index():
    assert to_index((0, 0), 3) == 0
    assert to_index((0, 1), 3) == 3
    assert to_index((2, 1), 3) == 5
    assert to_index((2, 2), 3) == 8


def test_has_tile_above():
    assert not has_tile_above(0, 3)
    assert not has_tile_above(1, 3)
    assert not has_tile_above(2, 3)
    assert has_tile_above(3, 3)


def test_has_tile_leftwards():
    assert not has_tile_leftwards(0, 3)
    assert not has_tile_leftwards(3, 3)
    assert not has_tile_leftwards(6, 3)
    assert has_tile_leftwards(1, 3)
    assert has_tile_leftwards(2, 3)


def test_arrange_tiles_simple():
    '''
         6       7
        ___     ___
       |   |   |   |
     5 | 0 | 2 | 1 | 8
       |   |   |   |
        ---     ---
         1       3
        ___     ___
       |   |   |   |
    12 | 3 | 4 | 2 | 9
       |   |   |   |
        ---     ---
         11      10
    '''
    tile_borders = [
        [6, 2, 1, 5],
        [7, 8, 3, 4],  # 0010 -> 0100
        [12, 9, 10, 4],  # 0011 -> 1100
        [8, 2, 11, 12],  # 0001 -> 1000, 0100 -> 0010
    ]
    shuffled = [borders[::-1] for borders in tile_borders][::-1]
    tiles = [
        Tile(
            i,
            TileBorders(borders, width=4),  # 4 bits
            content=TileContent([])
        )
        for i, borders in enumerate(shuffled)
    ]
    width = 2
    arranged_tiles = arrange_tiles(tiles)
    print(arranged_tiles)

    for tile_index, tile in enumerate(arranged_tiles):
        if has_tile_above(tile_index, width):
            above_tile = arranged_tiles[tile_index - width]
            assert tile.borders.borders_match(
                Direction.U, above_tile.borders, Direction.D,
            )

        if has_tile_leftwards(tile_index, width):
            left_tile = arranged_tiles[tile_index - 1]
            assert tile.borders.borders_match(
                Direction.L, left_tile.borders, Direction.R,
            )


def test_arrange_tiles(tiles):
    width = 3
    arranged_tiles = arrange_tiles(tiles)

    for tile_index, tile in enumerate(arranged_tiles):
        if has_tile_above(tile_index, width):
            above_tile = arranged_tiles[tile_index - width]
            assert tile.borders.borders_match(
                Direction.U, above_tile.borders, Direction.D,
            )

        if has_tile_leftwards(tile_index, width):
            left_tile = arranged_tiles[tile_index - 1]
            assert tile.borders.borders_match(
                Direction.L, left_tile.borders, Direction.R,
            )
