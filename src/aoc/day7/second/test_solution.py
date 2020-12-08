import pytest

from aoc.utils import local_path
from .solution import BagColour, calculate_required_bags, parse_input

# not terribly happy about this but it works
@pytest.fixture(params=[('../test_input', 32), ('../test_input2', 126)])
def rules_expected(request):
    test_input_filename, expected = request.param

    return (parse_input(local_path(__file__, test_input_filename)), expected)


def test_calculate_required_bags(rules_expected):
    colour = BagColour('shiny', 'gold')
    rules, expected = rules_expected
    assert calculate_required_bags(colour, rules) == expected
