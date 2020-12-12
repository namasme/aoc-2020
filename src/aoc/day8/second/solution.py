from aoc.utils import local_path
from aoc.day8.first.solution import (
    GameConsole, Instruction, InstructionType, parse_input
)


def run_console(console):
    executed = set()

    while console.ip not in executed and 0 <= console.ip < len(console.program):
        executed.add(console.ip)
        console.step()

    if console.ip != len(console.program):
        return None

    return console.acc


def find_executed_instructions(console):
    executed = set()

    while console.ip not in executed:
        executed.add(console.ip)
        console.step()

    return executed


def generate_programs(program, executed_instructions):
    for ip in executed_instructions:
        if program[ip].type == InstructionType.JMP:
            candidate = program[::]
            candidate[ip] = Instruction(InstructionType.NOP, program[ip].param)
            yield candidate
        elif program[ip].type == InstructionType.NOP:
            param = program[ip].param

            # account for program termination condition
            if 0 <= ip + param <= len(program):
                candidate = program[::]
                candidate[ip] = Instruction(InstructionType.JMP, param)
                yield candidate


def solve(program):
    executed_instructions = find_executed_instructions(GameConsole(program))

    for candidate in generate_programs(program, executed_instructions):
        console = GameConsole(candidate)

        final_acc = run_console(console)

        if final_acc is not None:
            return final_acc


def main():
    input_filename = '../input'
    program = parse_input(local_path(__file__, input_filename))

    print(solve(program))


if __name__ == '__main__':
    main()
