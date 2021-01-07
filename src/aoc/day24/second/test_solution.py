import pytest

from aoc.utils import local_path

from .solution import flip_tiles, parse_input, run, step


@pytest.fixture
def tiles():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


@pytest.fixture
def initial_tiles(tiles):
    return flip_tiles(tiles)


def test_step(initial_tiles):
    expected_black_tiles = [15, 12, 25, 14, 23, 28, 41, 37, 49, 37]
    black_tiles = set(initial_tiles)

    for expected_black_tiles in expected_black_tiles:
        black_tiles = step(black_tiles)
        assert len(black_tiles) == expected_black_tiles


def test_run(initial_tiles):
    assert len(run(initial_tiles, 10)) == 37
    assert len(run(initial_tiles, 50)) == 566
    assert len(run(initial_tiles, 90)) == 1844
    assert len(run(initial_tiles, 100)) == 2208
