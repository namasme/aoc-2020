import pytest

from aoc.utils import local_path
from .solution import parse_answers

@pytest.fixture
def raw_answers():
    test_input_filename = '../test_input'

    with open(local_path(__file__, test_input_filename)) as test_input_file:
        return test_input_file.read()


def test_parsing(raw_answers):
    parsed_answers = list(parse_answers(raw_answers))

    assert 5 == len(parsed_answers)
    assert [3, 0, 1, 1, 1] == list(map(len, parsed_answers))
    assert set('abc') == parsed_answers[0]
    assert {'a'} == parsed_answers[2]
