from itertools import combinations, starmap
from operator import add

from aoc.utils import local_path, read_ints


def is_valid(candidate, window):
    return candidate in starmap(add, combinations(window, 2))


def find_first_invalid_number(numbers, preamble_size):
    for i, candidate in enumerate(numbers[preamble_size:]):
        if not is_valid(candidate, numbers[i:i + preamble_size]):
            return candidate


def main():
    input_filename = '../input'
    numbers = read_ints(local_path(__file__, input_filename))
    preamble_size = 25

    print(find_first_invalid_number(numbers, preamble_size))


if __name__ == '__main__':
    main()
