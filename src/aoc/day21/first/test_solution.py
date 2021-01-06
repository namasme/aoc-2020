import pytest

from aoc.utils import local_path
from .solution import find_safe_ingredients, Food, parse_input, solve


@pytest.fixture
def foods():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_parsing(foods):
    assert len(foods) == 4
    assert foods[0] == Food(
        ['mxmxvkd', 'kfcds', 'sqjhc', 'nhms'],
        ['dairy', 'fish'],
    )


def test_find_safe_ingredients(foods):
    assert find_safe_ingredients(foods) == {'kfcds', 'nhms', 'sbzzf', 'trh'}


def test_solution(foods):
    assert solve(foods) == 5
