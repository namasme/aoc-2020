import re

from aoc.utils import local_path
from aoc.day4.first.solution import parse_passports, Passport


class StrictPassport(Passport):
    @staticmethod
    def parse(raw_passport):
        return StrictPassport(**dict([
            pair.split(':')
            for pair in raw_passport.split()
        ]))

    def validate_byr(self):
        return 1920 <= int(self.byr) <= 2002

    def validate_iyr(self):
        return 2010 <= int(self.iyr) <= 2020

    def validate_eyr(self):
        return 2020 <= int(self.eyr) <= 2030

    def validate_hgt(self):
        hgt, unit = int(self.hgt[:-2]), self.hgt[-2:]

        if unit == 'cm':
            return 150 <= hgt <= 193
        elif unit == 'in':
            return 59 <= hgt <= 76

        return False

    def validate_hcl(self):
        return bool(re.match(
            r'#[a-z0-9]{6}',
            self.hcl
        ))

    def validate_ecl(self):
        return self.ecl in [
            'amb', 'blu', 'brn', 'gry',
            'grn', 'hzl', 'oth',
        ]

    def validate_pid(self):
        return len(self.pid) == 9 and self.pid.isdigit()

    def is_strictly_valid(self):
        return (
            self.is_valid()
            and self.validate_byr()
            and self.validate_iyr()
            and self.validate_eyr()
            and self.validate_hgt()
            and self.validate_hcl()
            and self.validate_ecl()
            and self.validate_pid()
        )


def parse_passports(raw_passports):
    return [
        StrictPassport.parse(raw_passport)
        for raw_passport in raw_passports.split('\n\n')
    ]


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return parse_passports(input_file.read())


def main():
    input_filename = '../input'
    passports = parse_input(local_path(__file__, input_filename))

    print(sum(passport.is_strictly_valid() for passport in passports))



if __name__ == '__main__':
    main()
