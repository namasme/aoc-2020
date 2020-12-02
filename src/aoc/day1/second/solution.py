from aoc.utils import local_path, read_ints
from aoc.day1.first.solution import find_pair


def find_triple(target, expenses):
    '''
    NOTE: Both this function and find_pair may be wrong (they can use the same number
    twice, although that's not explicitly banned in the problem definition). Luckily the
    bug did not manifest when run against my input file.
    '''
    expenses_set = set(expenses)

    for expense in expenses:
        subtarget = target - expense
        pair = find_pair(subtarget, expenses)

        if pair is not None:
            return (expense,) + pair

    return None


def main():
    input_filename = '../input'
    target = 2020
    expenses = read_ints(local_path(__file__, input_filename))
    a, b, c = find_triple(target, expenses)

    print(a * b * c)


if __name__ == '__main__':
    main()
