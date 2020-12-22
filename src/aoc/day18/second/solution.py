from functools import reduce
from itertools import zip_longest

from aoc.day18.first.solution import (
    evaluate_expression, Operator, Paren, parse_input, TokenType,
)
from aoc.utils import local_path


def find_matching_paren(subexpression):
    depth = 0

    for i, token in enumerate(subexpression):
        token_type, param = token

        if token_type != TokenType.PAREN:
            continue

        if param == Paren.CLOSE:
            depth += 1
        else:
            depth -= 1

        if depth == 0:
            return i


def find_summands_limits(expression, index):
    if expression[index - 1][0] == TokenType.NUMBER:
        left = index - 1
    else:
        left = index - 1 - find_matching_paren(reversed(expression[:index]))

    if expression[index + 1][0] == TokenType.NUMBER:
        right = index + 1
    else:
        right = index + 1 + find_matching_paren(expression[index+1:])

    return (left, right + 1)


def parenthesize_expression(expression):
    new_expression = expression[::]
    current = 0

    while current < len(new_expression):
        if new_expression[current] == (TokenType.OPERATOR, Operator.ADD):
            left, right = find_summands_limits(new_expression, current)
            # order is important so that indices don't get messed up
            new_expression.insert(right, (TokenType.PAREN, Paren.CLOSE))
            new_expression.insert(left, (TokenType.PAREN, Paren.OPEN))
            current += 1

        current += 1

    return new_expression


def main():
    input_filename = '../input'
    expressions = parse_input(local_path(__file__, input_filename))

    print(sum(
        map(evaluate_expression,
            map(parenthesize_expression, expressions)
        )
    ))


if __name__ == '__main__':
    main()
