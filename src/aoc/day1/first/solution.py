from aoc.utils import local_path, read_ints


def find_pair(target, expenses):
    expenses_set = set(expenses)

    for expense in expenses:
        if (target - expense) in expenses_set:
            return (expense, target - expense)

    return None


def main():
    input_filename = '../input'
    target = 2020
    expenses = read_ints(local_path(__file__, input_filename))
    a, b = find_pair(target, expenses)

    print(a * b)


if __name__ == '__main__':
    main()
