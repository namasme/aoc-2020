from .solution import play_game


def test_play_game():
    turn = 2020
    cases = [
        ([0, 3, 6], 436),
        ([1, 3, 2], 1),
        ([2, 1, 3], 10),
        ([1, 2, 3], 27),
        ([2, 3, 1], 78),
        ([3, 2, 1], 438),
        ([3, 1, 2], 1836),

    ]

    for initial_numbers, expected in cases:
        assert play_game(initial_numbers, turn) == expected
