import pytest

from aoc.utils import local_path
from aoc.day18.first.solution import parse_expression
from .solution import (
    evaluate_expression, find_matching_paren, find_summands_limits,
    parenthesize_expression, parse_input,
)


@pytest.fixture
def expressions():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_find_matching_paren():
    assert find_matching_paren(parse_expression('(1 + 2) * 3')) == 4
    assert find_matching_paren(reversed(parse_expression('1 + (2 * 3)'))) == 4
    assert find_matching_paren(
        parse_expression('(1 + (2 * (3 + 4))) + 5')
    ) == 12


def test_summands_limits():
    expression = parse_expression('1 + (2 * 3) + ((4 * 5) + 6)')

    assert find_summands_limits(expression, 1) == (0, 7)
    assert find_summands_limits(expression, 7) == (2, 17)
    assert find_summands_limits(expression, 14) == (9, 16)


def test_parenthesize_expression():
    original_expression = parse_expression(
        '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
    )
    parenthesized_expression = parse_expression(
        '5 * 9 * (7 * 3 * (3 + 9) * (3 + ((8 + 6) * 4)))'
    )

    assert (
        parenthesize_expression(original_expression) == parenthesized_expression
    )


def test_solution(expressions):
    expected_results = [51, 46, 1445, 669060, 23340]

    for original_expression, expected in zip(expressions, expected_results):
        assert (
            evaluate_expression(parenthesize_expression(original_expression))
            ==
            expected
        )
