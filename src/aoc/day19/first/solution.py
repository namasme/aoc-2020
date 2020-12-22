import re
from enum import auto, Enum
from functools import lru_cache

from aoc.utils import local_path


class RuleType(Enum):
    LITERAL = auto()
    CONCAT = auto()
    PIPE = auto()


def parse_rule(rule):
    if '"' in rule:
        return (RuleType.LITERAL, rule[1])
    elif '|' in rule:
        param = tuple([
            [int(number) for number in part.split()]
            for part in rule.split('|')
        ])
        return (RuleType.PIPE, param)
    else:
        return (RuleType.CONCAT, list(map(int, re.findall(r'\d+', rule))))


def parse_rules(lines):
    pairs = [line.strip().split(': ') for line in lines]

    return {
        int(index): parse_rule(rule)
        for index, rule in pairs
    }


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        rules, messages = input_file.read().split('\n\n')

        return (
            parse_rules(rules.split('\n')),
            messages.split()
        )


def build_root_rule(rules):
    @lru_cache(maxsize=None)
    def build_rule_aux(index):
        rule_type, param = rules[index]

        if rule_type == RuleType.LITERAL:
            return param
        elif rule_type == RuleType.CONCAT:
            return ''.join(build_rule_aux(subrule) for subrule in param)
        elif rule_type == RuleType.PIPE:
            return '({}|{})'.format(*(
                ''.join(build_rule_aux(subrule) for subrule in part)
                for part in param
            ))

    root_index = 0
    return build_rule_aux(root_index)


def matches_rule(message, rule):
    return re.match(rule + '$', message) is not None


def main():
    input_filename = '../input'
    rules, messages = parse_input(local_path(__file__, input_filename))
    root_rule = build_root_rule(rules)

    print(sum([matches_rule(message, root_rule) for message in messages]))


if __name__ == '__main__':
    main()
