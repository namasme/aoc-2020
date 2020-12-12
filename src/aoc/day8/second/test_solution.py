import pytest

from aoc.utils import local_path
from .solution import parse_input, solve

@pytest.fixture
def program():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_solution(program):
    assert solve(program) == 8
