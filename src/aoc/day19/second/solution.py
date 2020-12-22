from functools import lru_cache

from aoc.day19.first.solution import matches_rule, parse_input, RuleType
from aoc.utils import local_path


def generate_rule11(maximum_depth):
    return (RuleType.PIPE, [
        [42] * depth + [31] * depth
        for depth in range(1, maximum_depth + 1)
    ])


def build_rule(index, rules):
    @lru_cache(maxsize=None)
    def build_rule_aux(index):
        rule_type, param = rules[index]

        if rule_type == RuleType.LITERAL:
            return param
        elif rule_type == RuleType.CONCAT:
            return ''.join(build_rule_aux(subrule) for subrule in param)
        elif rule_type == RuleType.PIPE:
            return '({})'.format(
                '|'.join(
                    ''.join(build_rule_aux(subrule) for subrule in part)
                    for part in param
                )
            )

    return build_rule_aux(index)


def find_length(rule, rules):
    rule_type, param = rules[rule]

    if rule_type == RuleType.LITERAL:
        return len(param)
    elif rule_type == RuleType.CONCAT:
        return sum(find_length(subrule, rules) for subrule in param)
    elif rule_type == RuleType.PIPE:
        return max(
            sum(find_length(subrule, rules) for subrule in part)
            for part in param
        )


def find_all_matching_messages(rules, messages):
    rules[8] = (RuleType.LITERAL, build_rule(8, rules) + '+')
    maximum_depth = max(map(len, messages)) // find_length(11, rules)
    rules[11] = generate_rule11(maximum_depth)

    root_rule = build_rule(0, rules)
    print(root_rule, len(root_rule))

    return [message for message in messages if matches_rule(message, root_rule)]


def main():
    input_filename = '../input'
    rules, messages = parse_input(local_path(__file__, input_filename))

    print(len(find_all_matching_messages(rules, messages)))


if __name__ == '__main__':
    main()
