import pytest

from aoc.utils import local_path
from .solution import (
    build_rule, find_all_matching_messages,
    find_length, matches_rule, parse_input,
)


@pytest.fixture
def parsed_input():
    test_input_filename = '../test_input2'

    return parse_input(local_path(__file__, test_input_filename))


def test_find_length(parsed_input):
    rules, _ = parsed_input

    assert find_length(4, rules) == 2
    assert find_length(20, rules) == 2
    assert find_length(27, rules) == 3


def test_find_all_matching_messages(parsed_input):
    rules, messages = parsed_input
    root_rule = build_rule(0, rules)

    assert sum([matches_rule(message, root_rule) for message in messages]) == 3
    assert find_all_matching_messages(rules, messages) == [
        'bbabbbbaabaabba',
        'babbbbaabbbbbabbbbbbaabaaabaaa',
        'aaabbbbbbaaaabaababaabababbabaaabbababababaaa',
        'bbbbbbbaaaabbbbaaabbabaaa',
        'bbbababbbbaaaaaaaabbababaaababaabab',
        'ababaaaaaabaaab',
        'ababaaaaabbbaba',
        'baabbaaaabbaaaababbaababb',
        'abbbbabbbbaaaababbbbbbaaaababb',
        'aaaaabbaabaaaaababaa',
        'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa',
        'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba',
    ]
