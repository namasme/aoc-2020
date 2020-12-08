import pytest

from aoc.utils import local_path
from .solution import (
    build_rules_graph, BagColour, find_reachable_colours,
    parse_input, parse_rule
)


@pytest.fixture
def rules():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


@pytest.mark.parametrize("raw_rule,expected", [
    (
        'dotted magenta bags contain 1 mirrored maroon bag, 3 shiny red bags, 2 faded blue bags, 2 mirrored purple bags.',
        (BagColour('dotted', 'magenta'), [
            BagColour('mirrored', 'maroon'),
            BagColour('shiny', 'red'),
            BagColour('faded', 'blue'),
            BagColour('mirrored', 'purple'),
        ])
    ),
    (
        'shiny plum bags contain no other bags.',
        (BagColour('shiny', 'plum'), [])
    )
])
def test_parsing(raw_rule, expected):
    assert parse_rule(raw_rule) == expected


def test_graph(rules):
    graph = build_rules_graph(rules)


    assert graph[BagColour('shiny', 'gold')] == {
        BagColour('muted', 'yellow'),
        BagColour('bright', 'white'),
    }
    assert graph[BagColour('muted', 'yellow')] == {
        BagColour('light', 'red'),
        BagColour('dark', 'orange'),
    }


def test_reachable_colours(rules):
    graph = build_rules_graph(rules)
    origin = BagColour('shiny', 'gold')

    assert find_reachable_colours(graph, origin) == set([
        BagColour(*colour.split())
        for colour in [
                'bright white', 'muted yellow',
                'dark orange', 'light red',
        ]
    ])
