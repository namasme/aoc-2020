import re
from enum import auto, Enum

from aoc.utils import local_path


class InstructionType(Enum):
    MASK = auto()
    MEM = auto()


def parse_instruction(line):
    lhs, rhs = line.split (' = ')

    if lhs == 'mask':
        return (InstructionType.MASK, rhs)
    else:
        position = int(re.findall(r'\d+', lhs)[0])
        value = int(rhs)

        return (InstructionType.MEM, (position, value))


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return [parse_instruction(line.strip()) for line in input_file]


class Decoder:
    MASK_SIZE = 36
    WILDCARD = 'X'

    def __init__(self):
        self.and_mask = 1 << (self.MASK_SIZE - 1)
        self.or_mask = 0
        self.memory = {}

    def step(self, instruction):
        instruction_type, param = instruction

        if instruction_type == InstructionType.MASK:
            self.update_mask(param)
        else:
            self.store(*param)

    def update_mask(self, mask):
        self.and_mask = int(mask.replace(self.WILDCARD, '1'), 2)
        self.or_mask = int(mask.replace(self.WILDCARD, '0'), 2)

    def store(self, position, value):
        self.memory[position] = value & self.and_mask | self.or_mask

    def run(self, instructions):
        for instruction in instructions:
            self.step(instruction)

    def sum(self):
        return sum(value for value in self.memory.values())


def main():
    input_filename = '../input'
    instructions = parse_input(local_path(__file__, input_filename))
    decoder = Decoder()

    decoder.run(instructions)

    print(decoder.sum())


if __name__ == '__main__':
    main()
