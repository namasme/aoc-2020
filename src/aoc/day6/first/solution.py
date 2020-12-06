from functools import reduce

from aoc.utils import local_path


def parse_individual_answers(individual_answers):
    return set(individual_answers)


def parse_group_answers(group_answers):
    return reduce(set.union, [
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
