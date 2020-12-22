import pytest

from aoc.utils import local_path
from .solution import (
    evaluate_expression, find_tokens, initialize_stack, Operator, Paren,
    parse_expression, parse_input, parse_token, step, TokenType,
)


@pytest.fixture
def expressions():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_find_tokens():
    raw_expression = '1 + (2 * 3) + (4 * (5 + 6))'
    assert find_tokens(raw_expression) == list(raw_expression.replace(' ', ''))
    assert find_tokens('11 + (222 * 3333)') == [
        '11', '+', '(', '222',
        '*', '3333', ')',
    ]


def test_parse_token():
    assert parse_token('1234') == (TokenType.NUMBER, 1234)
    assert parse_token('+') == (TokenType.OPERATOR, Operator.ADD)
    assert parse_token('*') == (TokenType.OPERATOR, Operator.MUL)
    assert parse_token('(') == (TokenType.PAREN, Paren.OPEN)
    assert parse_token(')') == (TokenType.PAREN, Paren.CLOSE)


def test_step():
    assert step([1, Operator.ADD], (TokenType.NUMBER, 2)) == [3]
    assert step([1], (TokenType.OPERATOR, Operator.MUL)) == [1, Operator.MUL]
    assert step([1, Operator.ADD], (TokenType.PAREN, Paren.OPEN)) == [
        1, Operator.ADD,
        0, Operator.ADD,
    ]
    assert step([1, Operator.ADD, 5], (TokenType.PAREN, Paren.CLOSE)) == [6]


def test_initialize_stack():
    assert initialize_stack(parse_expression('1 + 2')) == (
        [1],
        parse_expression('+ 2'),
    )
    assert initialize_stack(parse_expression('(1 + 2) * 3')) == (
        [0, Operator.ADD, 1],
        parse_expression('+ 2) * 3'),
    )
    assert initialize_stack(parse_expression('((1 + 2) * 3) + 4')) == (
        [0, Operator.ADD, 0, Operator.ADD, 1],
        parse_expression('+ 2) * 3) + 4'),
    )


def test_evaluate_expression(expressions):
    expected_results = [51, 26, 437, 12240, 13632]

    for expression, expected in zip(expressions, expected_results):
        assert evaluate_expression(expression) == expected
