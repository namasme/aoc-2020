import pytest

from aoc.utils import local_path
from aoc.utils.spatial import Point3D
from .solution import parse_input, run, step


@pytest.fixture
def parsed_input():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_parsing():
    test_input_filename = '../test_input'
    alive_cells = parse_input(local_path(__file__, test_input_filename))

    assert len(alive_cells) == 5
    assert Point3D(0, 0, 0) not in alive_cells
    assert Point3D(2, 2, 0) in alive_cells


def test_step(parsed_input):
    alive_cells = parsed_input

    new_cells = step(alive_cells)

    assert Point3D(0, 1, -1) in new_cells
    assert Point3D(0, 1, 0) in new_cells
    assert Point3D(0, 1, 1) in new_cells


def test_run(parsed_input):
    alive_cells = parsed_input

    final_cells = run(alive_cells, 6)

    assert len(final_cells) == 112
