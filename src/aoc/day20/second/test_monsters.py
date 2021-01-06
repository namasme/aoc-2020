import pytest

from aoc.utils import local_path
from aoc.utils.spatial import Point2D
from .monsters import (
    find_water_roughness, generate_image_from_tiles,
    hstack, match_pattern, positions_from_mask, roughness,
)
from .solution import parse_input
from .tiles import TileBorders, TileContent, TileTransformation


@pytest.fixture
def tiles():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


@pytest.fixture
def arranged_tiles(tiles):
    solution = [  # (transformation_id, tile_index)
        (0b010, 1), (0b010, 0), (0, 8),
        (0b010, 7), (0b010, 3), (0b110, 5),
        (0b010, 6), (0b010, 4), (0b001, 2),
    ]

    return [
        TileTransformation.from_id(transformation_id).apply(tiles[tile_index])
        for transformation_id, tile_index in solution
    ]


@pytest.fixture
def image():
    image_filename = '../image'

    with open(local_path(__file__, image_filename)) as image_file:
        return image_file.read().strip().split('\n')


def test_hstack():
    matrices = [
        [
            'ab',
            'cd',
        ],
        [
            'ef',
            'gh',
        ],
        [
            'ij',
            'kl',
        ],
    ]

    assert hstack(*matrices) == [
        'abefij',
        'cdghkl',
    ]


def test_generate_image_from_tiles(arranged_tiles, image):
    assert generate_image_from_tiles(arranged_tiles) == image


def test_positions_from_mask():
    monster_mask = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   ',
    ]
    xs_per_row = [
        [
            column
            for column, character in enumerate(row)
            if character == '#'
        ]
        for row in monster_mask
    ]
    positions = [
        Point2D(x, y)
        for y, xs in enumerate(xs_per_row)
        for x in xs
    ]

    assert positions_from_mask(monster_mask) == positions


def test_match_pattern(image):
    mask = [
        ' #',
        '# ',
    ]
    image = [
        '.#.#',
        '###.',
        '.#.#',
        '####',
    ]
    xs_per_row = [
        [0, 2],
        [1],
        [0, 2]
    ]
    positions = [
        Point2D(x, y)
        for y, xs in enumerate(xs_per_row)
        for x in xs
    ]

    assert match_pattern(mask, image) == positions


def test_roughness(image):
    monster_mask = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   ',
    ]

    assert roughness(monster_mask) == 15
    assert roughness(image) == 303


def test_find_water_roughness(arranged_tiles, image):
    assert find_water_roughness(arranged_tiles, image) == 273
