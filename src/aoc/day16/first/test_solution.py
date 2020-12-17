import pytest

from aoc.utils import local_path

from .solution import find_error_rate, parse_input, Rule

@pytest.fixture
def parsed_input():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_parsing():
    test_input_filename = '../test_input'
    result = parse_input(local_path(__file__, test_input_filename))

    assert result[0] == [
        Rule('class', (range(1, 4), range(5, 8))),
        Rule('row', (range(6, 12), range(33, 45))),
        Rule('seat', (range(13, 41), range(45, 51))),
    ]
    assert result[2] == [
        [7, 3, 47],
        [40, 4, 50],
        [55, 2, 20],
        [38, 6, 12],
    ]


def test_find_error_rate(parsed_input):
    rules, _, tickets = parsed_input

    assert find_error_rate(rules, tickets) == 71
