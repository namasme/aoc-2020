import pytest

from aoc.utils import local_path
from .solution import parse_input, play_subgame, winning_score


@pytest.fixture
def decks():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_play_subgame(decks):
    deck1, deck2 = decks


    # games 4 & 5
    assert play_subgame((8,), (10, 9, 7, 5)) == (2, (9, 7, 5, 10, 8))
    # game 3
    assert (
        play_subgame((8, 1), (3, 4, 10, 9, 7, 5))
        ==
        (2, (7, 5, 4, 1, 10, 8, 9, 3))
    )
    # game 2
    assert play_subgame((9, 8, 5, 2), (10, 1, 7)) == (2, (5, 10, 2, 9, 8, 7, 1))
    assert (
        play_subgame(tuple(deck1), tuple(deck2))
        ==
        (2, (7, 5, 6, 2, 4, 1, 10, 8, 9, 3))
    )
