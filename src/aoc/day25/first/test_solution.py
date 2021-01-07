import pytest

from aoc.utils import local_path, read_ints

from .solution import dual_bsgs, solution


@pytest.fixture
def public_keys():
    test_input_filename = '../test_input'

    return read_ints(local_path(__file__, test_input_filename))


def test_dual_bsgs(public_keys):
    g = 7
    p = 20201227
    ga, gb = public_keys

    pub_key, loop_size = dual_bsgs(g, p, ga, gb)

    assert pow((ga ^ gb ^ pub_key), loop_size, p) == 14897079


def test_solution(public_keys):
    assert solution(*public_keys) == 14897079
