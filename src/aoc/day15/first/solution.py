from collections import defaultdict


def store(turn, number, memory):
    memory[number].append(turn)
    memory[number] = memory[number][-2:]


def play_game(initial_numbers, turns):
    memory = defaultdict(list)

    for i, number in enumerate(initial_numbers):
        store(i + 1, number, memory)

    last_number = initial_numbers[-1]

    for turn in range(len(initial_numbers) + 1, turns + 1):
        turns = memory[last_number]

        if len(turns) == 1:
            last_number = 0
        else:
            a, b = turns
            last_number = b - a

        store(turn, last_number, memory)

    return last_number


def main():
    input_filename = '../input'
    initial_numbers = [7, 14, 0, 17, 11, 1, 2]
    turns = 2020

    print(play_game(initial_numbers, turns))


if __name__ == '__main__':
    main()
