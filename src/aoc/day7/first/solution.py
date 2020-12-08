import attr
from collections import defaultdict, deque
import re

from aoc.utils import local_path

@attr.s(frozen=True)
class BagColour:
    disambiguator = attr.ib()
    hue = attr.ib()


def parse_rule(rule):
    colour_pattern = r'(?P<disambiguator>\w+) (?P<hue>\w+)'
    content_pattern = r'\d+ (?P<disambiguator>\w+) (?P<hue>\w+)'

    return (
        BagColour(**re.match(colour_pattern, rule).groupdict()),
        [BagColour(*colour) for colour in re.findall(content_pattern, rule)]
    )


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return [parse_rule(line.strip()) for line in input_file]


def build_rules_graph(rules):
    graph = defaultdict(set)

    for parent, children in rules:
        for child in children:
            graph[child].add(parent)

    return graph


def find_reachable_colours(graph, origin):
    visitands = deque([origin])
    seen = set()

    while visitands:
        current = visitands.popleft()
        seen.add(current)

        for reachable in graph[current]:
            if reachable not in seen:
                visitands.append(reachable)


    return seen - {origin}


def main():
    input_filename = '../input'
    rules = parse_input(local_path(__file__, input_filename))
    graph = build_rules_graph(rules)

    print(len(find_reachable_colours(graph, BagColour('shiny', 'gold'))))


if __name__ == '__main__':
    main()
