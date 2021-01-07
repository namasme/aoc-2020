import pytest

from collections import Counter

from aoc.utils import local_path
from aoc.utils.spatial import Point2D

from .solution import (
    flip_tiles, parse_directions, parse_input, parse_tile,
    parse_token,
)


@pytest.fixture
def tiles():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_parse_token():
    assert parse_token('esew') == ('e', 'sew')
    assert parse_token('sew') == ('se', 'w')
    assert parse_token('w') == ('w', '')


def test_parse_directions():
    assert parse_directions('nwwswee') == ['nw', 'w', 'sw', 'e', 'e']


def test_parse_tile():
    assert parse_tile('esew') == Point2D(1, -1)
    assert parse_tile('nwwswee') == Point2D(0, 0)


def test_flip_tiles(tiles):
    assert len(tiles) == 20
    assert len(Counter(tiles)) == 15
    assert len(flip_tiles(tiles)) == 10
