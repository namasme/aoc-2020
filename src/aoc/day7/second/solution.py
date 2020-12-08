import re

from aoc.utils import local_path
from aoc.day7.first.solution import BagColour

def parse_rule(rule):
    colour_pattern = r'(?P<disambiguator>\w+) (?P<hue>\w+)'
    content_pattern = r'(?P<count>\d+) (?P<disambiguator>\w+) (?P<hue>\w+)'

    return (
        BagColour(**re.match(colour_pattern, rule).groupdict()),
        [
            (int(count), BagColour(disambiguator, hue))
            for count, disambiguator, hue in re.findall(content_pattern, rule)
        ]
    )


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return dict(parse_rule(line.strip()) for line in input_file)


def calculate_required_bags_inclusive(colour, rules):
    return 1 + sum(
        count * calculate_required_bags_inclusive(child, rules)
        for count, child in rules[colour]
    )


def calculate_required_bags(colour, rules):
    return calculate_required_bags_inclusive(colour, rules) - 1


def main():
    input_filename = '../input'
    rules = parse_input(local_path(__file__, input_filename))

    print(calculate_required_bags(BagColour('shiny', 'gold'), rules))


if __name__ == '__main__':
    main()
