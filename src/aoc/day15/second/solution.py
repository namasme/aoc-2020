def play_game(initial_numbers, turns):
    memory = [-1] * turns

    for i, number in enumerate(initial_numbers):
        memory[number] = i + 1

    last_number = initial_numbers[-1]

    for current_turn in range(len(initial_numbers) + 1, turns + 1):
        last_turn = memory[last_number]

        if last_turn == -1:
            new_number = 0
        else:
            new_number = (current_turn - 1) - last_turn

        memory[last_number] = current_turn - 1
        last_number = new_number

    return last_number


def main():
    input_filename = '../input'
    initial_numbers = [7, 14, 0, 17, 11, 1, 2]
    turns = 30000000

    print(play_game(initial_numbers, turns))


if __name__ == '__main__':
    main()
