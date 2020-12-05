import attr

from aoc.utils import local_path


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return parse_passports(input_file.read())


def parse_passports(raw_passports):
    return [
        parse_passport(raw_passport)
        for raw_passport in raw_passports.split('\n\n')
    ]


def parse_passport(raw_passport):
    return Passport(**dict([
        pair.split(':')
        for pair in raw_passport.split()
    ]))


@attr.s
class Passport:
    byr = attr.ib(default=None)
    iyr = attr.ib(default=None)
    eyr = attr.ib(default=None)
    hgt = attr.ib(default=None)
    hcl = attr.ib(default=None)
    ecl = attr.ib(default=None)
    pid = attr.ib(default=None)
    cid = attr.ib(default=None)

    def is_valid(self):
        required_attributes = [
            self.byr,self.iyr,self.eyr,self.hgt,
            self.hcl,self.ecl,self.pid,
        ]

        return all([
            required_attribute is not None
            for required_attribute in required_attributes
        ])


def main():
    input_filename = '../input'
    passports = parse_input(local_path(__file__, input_filename))

    print(sum(passport.is_valid() for passport in passports))


if __name__ == '__main__':
    main()
