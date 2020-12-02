import re

from aoc.utils import local_path


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return [
            parse_policy_password(line.strip())
            for line in input_file
        ]


def parse_policy_password(line):
    pattern = r'(?P<min>\d+)-(?P<max>\d+) (?P<letter>[a-z]): (?P<password>[a-z]+)'
    search = re.search(pattern, line)

    return (
        (
            (int(search.group('min')), int(search.group('max'))),
            search.group('letter'),
        ),
        search.group('password'),
    )


def match_policy_password(policy, password):
    thresholds, letter = policy
    min_, max_ = thresholds

    return min_ <= password.count(letter) <= max_


def main():
    input_filename = '../input'
    policies_passwords = parse_input(local_path(__file__, input_filename))

    matches = [
        match_policy_password(*policy_password)
        for policy_password in policies_passwords
    ]

    print(sum(matches))


if __name__ == '__main__':
    main()
