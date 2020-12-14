import pytest

from .solution import find_earliest_bus, parse_frequencies


def test_parsing():
    assert parse_frequencies('7,13,x,x,59,x,31,19') == [7, 13, 59, 31, 19]


def test_find_earliest_bus():
    timestamp = 939
    frequencies = [7, 13, 59, 31, 19]

    assert find_earliest_bus(timestamp, frequencies) == (5, 59)
