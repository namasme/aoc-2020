import pytest

from aoc.utils import local_path
from .solution import (
    build_allergens_to_ingredients_map, canonical_dangerous_ingredient_list,
    eliminate_determinates, parse_input,
)


@pytest.fixture
def foods():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_assignments(foods):
    assert eliminate_determinates(
        build_allergens_to_ingredients_map(foods)
    ) == {
        'dairy': 'mxmxvkd',
        'fish': 'sqjhc',
        'soy': 'fvjkl',
    }


def test_canonical_dangerous_ingredient_list():
    allergen_to_ingredient = {
        'dairy': 'mxmxvkd',
        'fish': 'sqjhc',
        'soy': 'fvjkl',
    }

    assert (
        canonical_dangerous_ingredient_list(allergen_to_ingredient)
        ==
        'mxmxvkd,sqjhc,fvjkl'
    )
