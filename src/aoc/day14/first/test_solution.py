import pytest

from aoc.utils import local_path

from .solution import Decoder, InstructionType, parse_input, parse_instruction

@pytest.fixture
def instructions():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_parsing():
    assert parse_instruction('mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X') == (
        InstructionType.MASK,
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
    )
    assert parse_instruction('mem[7] = 101') == (InstructionType.MEM, (7, 101))


def test_decoder(instructions):
    decoder = Decoder()
    decoder.run(instructions)

    assert decoder.and_mask == 68719476733
    assert decoder.or_mask == 64
    assert decoder.memory[7] == 101
    assert decoder.memory[8] == 64
    assert decoder.sum() == 165
