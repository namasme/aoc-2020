import copy
import pytest

from aoc.utils import local_path
from aoc.utils.spatial import Point2D
from .solution import SeatsLayout, Tile


@pytest.fixture
def rows():
    test_input_filename = '../test_input'

    with open(local_path(__file__, test_input_filename)) as test_input_file:
        return [line.strip() for line in test_input_file]


@pytest.fixture
def initial_layout(rows):
    return SeatsLayout.parse(rows)


def test_step(initial_layout):
    layout = copy.deepcopy(initial_layout)

    layout.step()
    assert all(tile == Tile.OCCUPIED for tile in layout.layout.values())

    layout.step()
    assert layout.layout[Point2D(0, 0)] == Tile.OCCUPIED
    assert layout.layout[Point2D(1, 1)] == Tile.EMPTY
    assert layout.layout[Point2D(5, 6)] == Tile.EMPTY


def test_find_stable_layout(initial_layout):
    layout = copy.deepcopy(initial_layout)
    layout.find_stable_layout()

    assert sum(
        tile == Tile.OCCUPIED
        for tile in layout.layout.values()
    ) == 26
