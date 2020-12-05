import pytest

from aoc.utils import local_path
from .solution import parse_passport, parse_passports, Passport

@pytest.fixture
def raw_passports():
    test_input_filename = '../test_input'

    with open(local_path(__file__, test_input_filename)) as test_input_file:
        return test_input_file.read()


@pytest.fixture
def passports(raw_passports):
    return parse_passports(raw_passports)


def test_parse_passports(raw_passports):
    parsed_passports = parse_passports(raw_passports)

    assert len(parsed_passports) == 4
    assert parsed_passports[0].ecl == 'gry'
    assert parsed_passports[1].hgt is None


def test_passport_validity(passports):
    validities = [passport.is_valid() for passport in passports]

    assert validities == [True, False, True, False]
