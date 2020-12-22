import re
from enum import auto, Enum
from functools import reduce
from itertools import takewhile

from aoc.utils import local_path


class TokenType(Enum):
    NUMBER = auto()
    OPERATOR = auto()
    PAREN = auto()


class Operator(Enum):
    ADD = '+'
    MUL = '*'


class Paren(Enum):
    OPEN = '('
    CLOSE = ')'


def find_tokens(line):
    return re.findall(r'([+*()]|\d+)', line)


def parse_token(raw_token):
    if raw_token.isdigit():
        return (TokenType.NUMBER, int(raw_token))
    elif raw_token in '+*':
        return (TokenType.OPERATOR, Operator(raw_token))
    elif raw_token in '()':
        return (TokenType.PAREN, Paren(raw_token))


def parse_expression(line):
    return list(map(parse_token, find_tokens(line)))


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return [parse_expression(line.strip()) for line in input_file]


def apply_operator(operator, a, b):
    return (
        a + b if operator == Operator.ADD
        else a * b
    )


def step(stack, token):
    token_type, param = token

    if token_type == TokenType.NUMBER:
        other, operator = stack[-2:]
        return stack[:-2] + [apply_operator(operator, other, param)]
    elif token_type == TokenType.OPERATOR:
        return stack + [param]
    elif token_type == TokenType.PAREN:
        if param == Paren.OPEN:
            return stack + [0, Operator.ADD]  # kind of hacky but oh well
        elif param == Paren.CLOSE:
            return stack[:-3] + [
                apply_operator(stack[-2], stack[-3], stack[-1])
            ]


def initialize_stack(expression):
    initial_parens = len(list(takewhile(
        lambda token: token == (TokenType.PAREN, Paren.OPEN),
        expression,
    )))
    initial_stack = (
        [0, Operator.ADD] * initial_parens
        + [expression[initial_parens][1]]
    )
    return initial_stack, expression[initial_parens+1:]


def evaluate_expression(expression):
    initial_stack, subexpression = initialize_stack(expression)
    return reduce(step, subexpression, initial_stack)[0]


def main():
    input_filename = '../input'
    expressions = parse_input(local_path(__file__, input_filename))

    print(sum(map(evaluate_expression, expressions)))


if __name__ == '__main__':
    main()
