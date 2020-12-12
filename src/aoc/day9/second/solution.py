from aoc.utils import local_path, read_ints


def sized_window_sums(numbers, window_size):
    current = sum(numbers[:window_size])
    yield (current, 0)

    evicted = 0

    while evicted + window_size < len(numbers):
        current += numbers[evicted + window_size] - numbers[evicted]
        evicted += 1
        yield (current, evicted)


def window_sums(numbers):
    for window_size in range(2, len(numbers)):
        for candidate, start in sized_window_sums(numbers, window_size):
            yield (candidate, start, window_size)


def solve(numbers, target):
    for window_sum, start, window_size in window_sums(numbers):
        if window_sum == target:
            _range = numbers[start:start+window_size]

            return min(_range) + max(_range)


def main():
    input_filename = '../input'
    numbers = read_ints(local_path(__file__, input_filename))
    target = 10884537  # solution to the first challenge

    print(solve(numbers, target))


if __name__ == '__main__':
    main()
