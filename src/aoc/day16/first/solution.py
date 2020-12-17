import attr
import re

from aoc.utils import local_path

@attr.s(frozen=True)
class Rule:
    field_name = attr.ib()
    ranges = attr.ib()

    @staticmethod
    def parse(line):
        field_name, raw_thresholds = line.split(':')
        thresholds = [
            int(threshold)
            for threshold in re.findall(r'\d+', raw_thresholds)
        ]

        ranges = (
            range(thresholds[0], thresholds[1] + 1),
            range(thresholds[2], thresholds[3] + 1),
        )

        return Rule(field_name, ranges)

    def matches(self, value):
        return value in self.ranges[0] or value in self.ranges[1]


def parse_ticket(line):
    return [
        int(value)
        for value in re.findall(r'\d+', line)
    ]


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        raw_rules, raw_own_ticket, raw_tickets = input_file.read().split('\n\n')

        return (
            [Rule.parse(line.strip()) for line in raw_rules.split('\n')],
            parse_ticket(raw_own_ticket.split('\n')[1].strip()),
            [
                parse_ticket(line.strip())
                # first line is a header, file ends with \n
                for line in raw_tickets.split('\n')[1:-1]
            ],
        )


def find_error_rate(rules, tickets):
    return sum([
        value
        for ticket in tickets
        for value in ticket
        if all(not rule.matches(value) for rule in rules)
    ])


def main():
    input_filename = '../input'
    rules, _, tickets = parse_input(local_path(__file__, input_filename))

    print(find_error_rate(rules, tickets))


if __name__ == '__main__':
    main()
