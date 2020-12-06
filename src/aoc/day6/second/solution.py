from functools import reduce

from aoc.utils import local_path
from aoc.day6.first.solution import parse_individual_answers

# I would have liked to have a solution that
# requires less copy-pasting but oh well
def parse_group_answers(group_answers):
    return reduce(set.intersection, [
        parse_individual_answers(individual_answers)
        for individual_answers in group_answers.split()
    ])


def parse_answers(all_answers):
    return map(parse_group_answers, all_answers.split('\n\n'))


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return parse_answers(input_file.read())


def main():
    input_filename = '../input'
    answers = parse_input(local_path(__file__, input_filename))

    print(sum(map(len, answers)))


if __name__ == '__main__':
    main()
