from aoc.utils import local_path

from .solution import parse_input, Point4D


def test_parsing():
    test_input_filename = '../test_input'
    alive_cells = parse_input(local_path(__file__, test_input_filename))

    assert len(alive_cells) == 5
    assert Point4D(0, 0, 0, 0) not in alive_cells
    assert Point4D(2, 2, 0, 0) in alive_cells
