from aoc.day22.first.solution import parse_input, winning_score
from aoc.utils import local_path


def play_subgame(deck1, deck2):
    seen = set()

    while deck1 and deck2:
        if (deck1, deck2) in seen:
            return (1, deck1)
        else:
            seen.add((deck1, deck2))

        card1, tail1 = deck1[0], deck1[1:]
        card2, tail2 = deck2[0], deck2[1:]

        if card1 <= len(tail1) and card2 <= len(tail2):
            winner, _ = play_subgame(tail1[:card1], tail2[:card2])
        elif card1 > card2:
            winner = 1
        elif card2 > card1:
            winner = 2
        else:
            raise ValueError('Unexpected configuration, cards have the same value.')

        if winner == 1:
            result1 = (card1, card2)
            result2 = ()
        elif winner == 2:
            result1 = ()
            result2 = (card2, card1)

        deck1 = tail1 + result1
        deck2 = tail2 + result2

    if deck1:
        return (1, deck1)
    elif deck2:
        return (2, deck2)


def main():
    input_filename = '../input'
    deck1, deck2 = parse_input(local_path(__file__, input_filename))
    _, winning_deck = play_subgame(tuple(deck1), tuple(deck2))

    print(winning_score(winning_deck))


if __name__ == '__main__':
    main()
