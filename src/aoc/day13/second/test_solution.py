import pytest
from functools import reduce

from aoc.utils import local_path
from .solution import find_earliest_timestamp, parse_frequencies


def test_parsing():
    assert parse_frequencies('7,13,x,x,59,x,31,19') == [
        (0, 7), (1, 13), (4, 59), (6, 31), (7, 19)
    ]


def test_find_earliest_timestamp():
    frequencies_cases = map(parse_frequencies, [
        '7,13,x,x,59,x,31,19',
        '17,x,13,19',
        '67,7,59,61',
        '67,x,7,59,61',
        '67,7,x,59,61',
        '1789,37,47,1889',
    ])
    expected_results = [1068781, 3417, 754018, 779210, 1261476, 1202161486]

    for frequencies, expected in zip(frequencies_cases, expected_results):
        assert find_earliest_timestamp(frequencies) == expected
