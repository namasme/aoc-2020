import pytest

from aoc.utils import local_path
from .solution import find_corners, Flip, parse_input, Tile


@pytest.fixture
def tiles():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_parsing():
    test_input_filename = '../test_input'

    tiles = parse_input(local_path(__file__, test_input_filename))

    assert len(tiles) == 9
    assert tiles[0].tile_id == 2311
    assert tiles[0].borders == [210, 89, 924, 318]


def test_flip_border():
    borders = [
        '..##.#..#.', '#.##...##.', '####...##.',
        '###.##.#..', '##.#.#....', '#....####.',
        '..#.#....#', '...#.#.#.#', '#.#.#####.',
    ]
    for border in borders:
        assert Tile.flip_border(
            Tile.to_int(border)
        ) == Tile.to_int(border[::-1])


def test_flip():
    original_tile = [
        '..##.#..#.',
        '##..#.....',
        '#...##..#.',
        '####.#...#',
        '##.##.###.',
        '##...#.###',
        '.#.#.#..##',
        '..#....#..',
        '###...#.#.',
        '..###..###',
    ]

    horizontally_flipped = original_tile[::-1]
    vertically_flipped = [row[::-1] for row in original_tile]
    vertical_then_horizontal = vertically_flipped[::-1]
    horizontal_then_vertical = [row[::-1] for row in horizontally_flipped]
    header = ['1234']

    assert (
        Tile.parse('\n'.join(header + original_tile)).flip(Flip.HORIZONTAL)
        ==
        Tile.parse('\n'.join(header + horizontally_flipped))
    )
    assert (
        Tile.parse('\n'.join(header + original_tile)).flip(Flip.VERTICAL)
        ==
        Tile.parse('\n'.join(header + vertically_flipped))
    )
    assert (
        Tile.parse('\n'.join(header + original_tile))
        .flip(Flip.HORIZONTAL)
        .flip(Flip.VERTICAL)
        ==
        Tile.parse('\n'.join(header + horizontal_then_vertical))
    )
    assert (
        Tile.parse('\n'.join(header + original_tile))
        .flip(Flip.VERTICAL)
        .flip(Flip.HORIZONTAL)
        ==
        Tile.parse('\n'.join(header + vertical_then_horizontal))
    )


def test_flip_involution(tiles):
    for tile in tiles:
        assert tile.flip(Flip.HORIZONTAL).flip(Flip.HORIZONTAL) == tile
        assert tile.flip(Flip.VERTICAL).flip(Flip.VERTICAL) == tile


def test_flip_symmetric(tiles):
    for tile in tiles:
        assert (
            tile.flip(Flip.HORIZONTAL).flip(Flip.VERTICAL)
            ==
            tile.flip(Flip.VERTICAL).flip(Flip.HORIZONTAL)
        )


def test_find_corners(tiles):
    corner_tiles = find_corners(tiles)

    assert set(corner_tile.tile_id for corner_tile in corner_tiles) == {
        1171, 1951, 2971, 3079,
    }
