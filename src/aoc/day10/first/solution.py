from collections import Counter
from itertools import starmap
from operator import sub

from aoc.utils import local_path, read_ints


def find_differences(jolts):
    sorted_jolts = sorted(jolts)

    return list(starmap(sub, zip(sorted_jolts[1:], sorted_jolts)))


def solve(jolts):
    differences = find_differences([0, max(jolts) + 3] + jolts)

    return differences.count(1) * differences.count(3)


def main():
    input_filename = '../input'
    jolts = read_ints(local_path(__file__, input_filename))

    print(solve(jolts))


if __name__ == '__main__':
    main()
