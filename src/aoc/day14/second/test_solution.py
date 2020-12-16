import pytest

from aoc.utils import local_path

from .solution import Decoderv2, parse_input

@pytest.fixture
def instructions():
    test_input_filename = '../test_input2'

    return parse_input(local_path(__file__, test_input_filename))


def test_decoder(instructions):
    decoder = Decoderv2()
    decoder.run(instructions)

    assert decoder.memory == {
        16: 1,
        17: 1,
        18: 1,
        19: 1,
        24: 1,
        25: 1,
        26: 1,
        27: 1,
        58: 100,
        59: 100,
    }
    assert decoder.sum() == 208
