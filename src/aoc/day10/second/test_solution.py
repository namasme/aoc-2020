import pytest

from .solution import (
    find_arrangements, find_ones_streaks, find_suitable_partitions,
)

@pytest.fixture
def jolts():
    return [
        1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
        32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49,
    ]


def test_find_ones_streaks():
    assert find_ones_streaks([0, 0, 1, 1, 1, 0, 1, 0, 1]) == [3, 1, 1]


def test_find_suitable_partitions():
    assert find_suitable_partitions(4) == 7
    assert find_suitable_partitions(15) == 5768


def test_find_arrangements(jolts):
    assert find_arrangements(jolts) == 19208
