import pytest

from aoc.utils import local_path
from .solution import GameConsole, parse_input, watch_console

@pytest.fixture
def program():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_watch_console(program):
    console = GameConsole(program)

    assert watch_console(console) == 5
