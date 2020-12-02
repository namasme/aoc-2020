from aoc.utils import local_path

from aoc.day2.first.solution import parse_input


def match_policy_password(policy, password):
    positions, letter = policy
    i, j = positions  # descriptive variable names ftw

    return (letter == password[i - 1]) ^ (letter == password[j - 1])


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
