from collections import deque

from aoc.utils import local_path


def parse_deck(deck_section):
    lines = deck_section.split('\n')
    return deque([int(line.strip()) for line in lines[1:]])


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        deck1, deck2 = input_file.read().strip().split('\n\n')
        return parse_deck(deck1), parse_deck(deck2)


def play_round(card1, card2):
    if card1 > card2:
        return ([card1, card2], [])
    elif card2 > card1:
        return ([], [card2, card1])

    raise ValueError('Unexpected configuration, cards have the same value.')


def play_game(deck1, deck2):
    while deck1 and deck2:
        print(deck1, deck2)
        top1 = deck1.popleft()
        top2 = deck2.popleft()

        result1, result2 = play_round(top1, top2)
        deck1.extend(result1)
        deck2.extend(result2)

    return deck1 or deck2  # neat


def winning_score(deck):
    return sum(
        (index + 1) * card
        for index, card in enumerate(reversed(deck))
    )


def main():
    input_filename = '../input'
    deck1, deck2 = parse_input(local_path(__file__, input_filename))
    deck1, deck2 = deque([43, 19]), deque([2, 29, 14])
    winning_deck = play_game(deck1, deck2)

    print(winning_score(winning_deck))


if __name__ == '__main__':
    main()
