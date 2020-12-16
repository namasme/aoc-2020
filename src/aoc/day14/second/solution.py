# coding: utf-8

from itertools import product, starmap

from aoc.day14.first.solution import InstructionType, parse_input
from aoc.utils import local_path


class Decoderv2:
    MASK_SIZE = 36
    WILDCARD = 'X'

    def __init__(self):
        self.mask = '0' * self.MASK_SIZE
        self.memory = {}

    @staticmethod
    def apply_mask_bit(mask_bit, mem_address_bit):
        return mem_address_bit if mask_bit == '0' else mask_bit

    def apply_mask(self, mem_address):
        padded_mem_address = bin(mem_address)[2:].zfill(self.MASK_SIZE)

        return ''.join(
            starmap(self.apply_mask_bit, zip(self.mask, padded_mem_address))
        )

    @staticmethod
    def determine_mem_addresses(masked_address):
        floating_bits = masked_address.count(Decoderv2.WILDCARD)

        for assignment in product('01', repeat=floating_bits):
            current = masked_address

            for bit in assignment:
                current = current.replace(Decoderv2.WILDCARD, bit, 1)

            yield int(current, 2)

    def store(self, mem_address, value):
        self.memory.update({
            masked_address: value
            for masked_address in self.determine_mem_addresses(
                    self.apply_mask(mem_address)
            )
        })

    def step(self, instruction):
        instruction_type, param = instruction

        if instruction_type == InstructionType.MASK:
            self.mask = param
        else:
            self.store(*param)

    def run(self, instructions):
        for instruction in instructions:
            self.step(instruction)

    def sum(self):
        return sum(value for value in self.memory.values())



def main():
    input_filename = '../input'
    instructions = parse_input(local_path(__file__, input_filename))
    decoder = Decoderv2()

    decoder.run(instructions)

    print(decoder.sum())


if __name__ == '__main__':
    main()
