import attr
from enum import Enum

from aoc.utils import local_path


class InstructionType(Enum):
    NOP = 'nop'
    ACC = 'acc'
    JMP = 'jmp'


@attr.s
class Instruction:
    type = attr.ib()
    param = attr.ib()

    @staticmethod
    def parse(raw_instruction):
        _type, _param = raw_instruction.split()

        return Instruction(InstructionType(_type), int(_param))


class GameConsole:
    def __init__(self, program):
        self.program = program
        self.ip = 0
        self.acc = 0

    def _nop(self, param):
        pass  # sic

    def _acc(self, param):
        self.acc += param

    def _jmp(self, param):
        self.ip += param - 1

    def dispatch_instruction(self, instruction):
        if instruction.type == InstructionType.NOP:
            self._nop(instruction.param)
        if instruction.type == InstructionType.ACC:
            self._acc(instruction.param)
        if instruction.type == InstructionType.JMP:
            self._jmp(instruction.param)

    def step(self):
        self.dispatch_instruction(self.program[self.ip])
        self.ip += 1


def watch_console(console):
    visited = set()

    while console.ip not in visited:
        visited.add(console.ip)
        console.step()

    return console.acc


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return [Instruction.parse(line.strip()) for line in input_file]


def main():
    input_filename = '../input'
    program = parse_input(local_path(__file__, input_filename))
    console = GameConsole(program)

    print(watch_console(console))


if __name__ == '__main__':
    main()
