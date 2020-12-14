import pytest
from functools import reduce

from aoc.utils import local_path
from aoc.utils.spatial import Point2D
from .solution import find_stable_layout, parse_seats_layout, step, Tile


@pytest.fixture
def rows():
    test_input_filename = '../test_input'

    with open(local_path(__file__, test_input_filename)) as test_input_file:
        return [line.strip() for line in test_input_file]


@pytest.fixture
def initial_layout(rows):
    return parse_seats_layout(rows)


def test_parsing(rows):
    layout = parse_seats_layout(rows)

    assert all(tile == Tile.EMPTY for tile in layout.values())
    assert layout[Point2D(0, 0)] == Tile.EMPTY
    assert layout[Point2D(9, 9)] == Tile.EMPTY
    assert Point2D(0, 1) not in layout


def test_step(initial_layout):
    layout2 = step(initial_layout)
    layout3 = step(layout2)

    assert initial_layout.keys() == layout2.keys()
    assert all(tile == Tile.OCCUPIED for tile in layout2.values())
    assert initial_layout.keys() == layout3.keys()
    assert layout3[Point2D(0, 0)] == Tile.OCCUPIED
    assert layout3[Point2D(1, 1)] == Tile.EMPTY


def test_find_stable_layout(initial_layout):
    stable_layout = find_stable_layout(initial_layout)
    layout6 = reduce(lambda layout, _: step(layout), range(5), initial_layout)

    assert sum(
        tile == Tile.OCCUPIED
        for tile in stable_layout.values()
    ) == 37
    assert stable_layout == layout6
