import pytest

from collections import deque

from aoc.utils import local_path
from .solution import parse_input, play_game, play_round, winning_score


@pytest.fixture
def decks():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_parsing(decks):
    deck1, deck2 = decks

    assert deck1 == deque([9, 2, 6, 3, 1])
    assert deck2 == deque([5, 8, 4, 7, 10])


def test_play_round():
    assert play_round(9, 5) == ([9, 5], [])
    assert play_round(2, 8) == ([], [8, 2])
    assert play_round(6, 4) == ([6, 4], [])
    assert play_round(1, 7) == ([], [7, 1])


def test_play_game(decks):
    # copying
    deck1 = deque(decks[0])
    deck2 = deque(decks[1])

    assert play_game(deck1, deck2) == deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])


def test_winning_score():
    assert winning_score([3, 2, 10, 6, 8, 5, 9, 4, 7, 1]) == 306
