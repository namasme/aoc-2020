import pytest

from aoc.day16.first.solution import Rule
from aoc.utils import local_path

from .solution import (
    determine_fields, filter_failing_rules,
    filter_invalid_tickets, parse_input,
)


@pytest.fixture
def parsed_input():
    test_input_filename = '../test_input2'

    return parse_input(local_path(__file__, test_input_filename))


def test_filter_invalid_tickets(parsed_input):
    # all tickets in the input happen to be valid
    rules, _, tickets = parsed_input

    invalid_tickets = [
        [20, 0, 0],
        [0, 20, 0],
        [0, 0, 20],
    ]

    mixed_tickets = [0] * 6
    mixed_tickets[::2] = tickets
    mixed_tickets[1::2] = invalid_tickets

    assert filter_invalid_tickets(rules, mixed_tickets) == tickets


def test_filter_failing_rules(parsed_input):
    rules, _, tickets = parsed_input
    columns = list(zip(*tickets))

    assert len(filter_failing_rules(rules, columns[0])) == 1
    assert len(filter_failing_rules(rules, columns[1])) == 2
    assert len(filter_failing_rules(rules, columns[2])) == 3


def test_determine_fields(parsed_input):
    rules, _, tickets = parsed_input

    assert [
        rule.field_name
        for rule in determine_fields(rules, tickets)
    ] == ['row', 'class', 'seat']
