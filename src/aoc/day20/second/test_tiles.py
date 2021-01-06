import pytest

from aoc.day20.first.solution import Flip
from aoc.utils import local_path
from aoc.utils.spatial import Direction
from .solution import parse_input
from .tiles import TileBorders, TileContent, TileTransformation


@pytest.fixture
def tiles():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_parsing(tiles):
    assert len(tiles) == 9

    # IDs
    assert tiles[0].tile_id == 2311
    assert tiles[-1].tile_id == 3079

    # Borders
    assert tiles[0].borders.borders == [210, 89, 924, 318]
    assert tiles[7].borders.borders == [
        0b0001010101,
        0b1001000000,
        0b0110001101,
        0b1111000010,
    ]
    assert tiles[-1].borders.borders == [702, 264, 116, 89]

    # Contents
    assert tiles[0].content.rows == [
        '#..#....',
        '...##..#',
        '###.#...',
        '#.##.###',
        '#...#.##',
        '#.#.#..#',
        '.#....#.',
        '##...#.#',
    ]
    assert tiles[-1].content.rows == [
        '#..#####',
        '.#......',
        '#####...',
        '###.#..#',
        '#...#.##',
        '.#####.#',
        '.#.###..',
        '.#......',
    ]


def test_tile_transformation(tiles):
    assert (
        TileTransformation.from_id(0b010)
        ==
        TileTransformation(False, True, False)
    )
    assert (
        TileTransformation.from_id(0b111)
        ==
        TileTransformation(True, True, True)
    )

    rotation = TileTransformation.from_id(0b100)
    assert rotation.apply(tiles[0].borders).borders == [318, 210, 89, 924]
    assert rotation.apply(tiles[0].content).rows == [
        '#.####.#',
        '##...#..',
        '..#.##..',
        '....#.##',
        '..##.##.',
        '#...#...',
        '.#.##...',
        '#.###.#.',
    ]

    vertical_flip = TileTransformation.from_id(0b001)
    assert vertical_flip.apply(tiles[2].content).rows == [
        '..#.##..',
        '#.#..#.#',
        '####.###',
        '###.###.',
        '##....##',
        '####...#',
        '####.##.',
        '..#..###',
    ]




def test_tile_borders_match(tiles):
    central_tile_borders = tiles[3].borders.flip(Flip.HORIZONTAL)
    central_up_borders = tiles[0].borders.flip(Flip.HORIZONTAL)

    assert central_tile_borders.borders[0] == TileBorders.to_int('..##.#..#.')
    assert central_up_borders.borders[2] == TileBorders.to_int(
        '..##.#..#.'[::-1]
    )
    assert central_tile_borders.borders_match(
        Direction.U, central_up_borders, Direction.D,
    )
    assert central_up_borders.borders_match(
        Direction.D, central_tile_borders, Direction.U,
    )


def test_tiles_transformations(tiles):
    for tile in tiles:
        for transformation_id in range(TileTransformation.SIZE):
            transformation = TileTransformation.from_id(transformation_id)
            transformed_tile = transformation.apply(tile)

            assert (
                transformed_tile.borders
                ==
                transformation.apply(tile.borders)
            )
            assert (
                transformed_tile.content
                ==
                transformation.apply(tile.content)
            )
