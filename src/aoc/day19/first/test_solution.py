import pytest

from aoc.utils import local_path
from .solution import (
    build_root_rule, matches_rule, parse_input, parse_rule, RuleType,
)


@pytest.fixture
def parsed_input():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_parsing(parsed_input):
    rules, messages = parsed_input

    assert len(rules) == 6
    assert rules[0] == (RuleType.CONCAT, [4, 1, 5])
    assert rules[1] == (RuleType.PIPE, ([2, 3], [3, 2]))
    assert rules[4] == (RuleType.LITERAL, 'a')

    assert len(messages) == 5
    assert messages[0] == 'ababbb'

    assert parse_rule('7 | 12') == (RuleType.PIPE, ([7], [12]))


def test_build_root_rule(parsed_input):
    rules, _ = parsed_input

    assert build_root_rule(rules) == 'a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b'


def test_matches_rule():
    rule = 'a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b'

    assert matches_rule('aaaabb', rule)
    assert not matches_rule('aaaabbb', rule)
