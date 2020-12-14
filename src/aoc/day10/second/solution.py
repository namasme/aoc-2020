from functools import lru_cache, reduce
from itertools import groupby
from operator import mul

from aoc.utils import local_path, read_ints
from aoc.day10.first.solution import find_differences

@lru_cache(maxsize=None)
def find_suitable_partitions(streak_length):
    if streak_length <= 1:
        return 1
    elif streak_length == 2:
        return 2

    return sum(find_suitable_partitions(streak_length - i) for i in range(1, 4))


def find_ones_streaks(differences):
    return [
        len(list(group))
        for key, group in groupby(differences)
        if key == 1
    ]


def find_arrangements(jolts):
    differences = find_differences([0, max(jolts) + 3] + jolts)

    # This solutions assumes only differences of 1 and 3 appear.
    # This assumption has been validated for my input.

    return reduce(mul, [
        find_suitable_partitions(streak_length)
        for streak_length in find_ones_streaks(differences)
    ])


def main():
    input_filename = '../input'
    jolts = read_ints(local_path(__file__, input_filename))

    print(find_arrangements(jolts))


if __name__ == '__main__':
    main()
