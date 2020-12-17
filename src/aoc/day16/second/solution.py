from functools import reduce
from operator import mul

from aoc.day16.first.solution import parse_input
from aoc.utils import local_path


def filter_invalid_tickets(rules, tickets):
    return [
        ticket for ticket in tickets
        if all(
                any(rule.matches(value) for rule in rules)
                for value in ticket
        )
    ]


def filter_failing_rules(rules, values):
    return {
        rule
        for rule in rules
        if all(map(rule.matches, values))
    }


def eliminate_determinates(candidates):
    sorted_candidates = sorted(
        enumerate(candidates),
        key=lambda field: len(field[1])
    )
    used = set()
    assignments = {}

    for original_index, field_candidates in sorted_candidates:
        if len(field_candidates.intersection(used)) < len(field_candidates) - 1:
            break  # can't recover from that

        assignments[original_index] = list(field_candidates - used)[0]
        used = field_candidates

    return assignments


def determine_fields(rules, valid_tickets):
    candidates = [
        filter_failing_rules(rules, field_values)
        for field_values in zip(*valid_tickets)
    ]

    partial_assignments = eliminate_determinates(candidates)

    '''
    This happens to be enough based on my input, otherwise a DFS would be required to
    explore all possible assignments. I originally implemented it until I thought of this
    trick, but it wasn't necessary in the end.
    '''

    def fst(pair):
        return pair[0]

    def snd(pair):
        return pair[1]

    # sort the items based on their key (i.e., the index) and project the value
    return list(map(snd, sorted(partial_assignments.items(), key=fst)))


def solve(fields_assignment, ticket):
    # fields_assignment is actually a list of rules, but whatever
    return reduce(mul, [
        value
        for rule, value in zip(fields_assignment, ticket)
        if rule.field_name.startswith('departure')
    ])


def main():
    input_filename = '../input'
    rules, ticket, tickets = parse_input(local_path(__file__, input_filename))
    valid_tickets = filter_invalid_tickets(rules, tickets)
    fields_assignment = determine_fields(rules, valid_tickets)

    print(solve(fields_assignment, ticket))


if __name__ == '__main__':
    main()
