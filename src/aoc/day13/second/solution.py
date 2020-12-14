# coding: utf-8

from functools import reduce
from operator import mul, neg

from aoc.utils import bezout, local_path


def parse_frequencies(frequencies_line):
    return [
        (i, int(frequency))
        for i, frequency in enumerate(frequencies_line.split(','))
        if frequency != 'x'
    ]


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        _, frequencies_line = input_file
        return parse_frequencies(frequencies_line)


def chinese_remainder(remainders, divisors):
    '''
    Adapted from rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
    '''
    N = reduce(mul, divisors)

    return sum(
        remainder * bezout(N // divisor, divisor)[1] * (N // divisor)
        #remainder * mul_inv(N // divisor, divisor) * (N // divisor)
        for remainder, divisor in zip(remainders, divisors)
    ) % N


def find_earliest_timestamp(frequencies):
    '''
    frequencies is a list of (index, bus ID). The solution timestamp should be
    index minutes smaller than a multiple of bus ID, or
                t ≡ -index (mod bus ID)
    Hence why the indices are negated.
    '''
    indices, divisors = zip(*frequencies)
    return chinese_remainder(map(neg, indices), divisors)


def main():
    input_filename = '../input'
    frequencies = parse_input(local_path(__file__, input_filename))

    print(find_earliest_timestamp(frequencies))


if __name__ == '__main__':
    main()
