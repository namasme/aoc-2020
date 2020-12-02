import unittest

from .solution import parse_policy_password, match_policy_password


class TestSolution(unittest.TestCase):
    cases = [
        '1-3 a: abcde',
        '1-3 b: cdefg',
        '2-9 c: ccccccccc',
    ]

    def test_parsing(self):
        expected_outputs = [
            (((1, 3), 'a'), 'abcde'),
            (((1, 3), 'b'), 'cdefg'),
            (((2, 9), 'c'), 'ccccccccc'),
        ]

        for case_input, expected_output in zip(self.cases, expected_outputs):
            with self.subTest(policy=case_input):
                self.assertEqual(
                    parse_policy_password(case_input),
                    expected_output
                )

    def test_matches(self):
        expected_outputs = [True, False, True]

        for case_input, expected_output in zip(self.cases, expected_outputs):
            with self.subTest(policy=case_input):
                self.assertEqual(
                    # probably should test in isolation but I'm lazy
                    match_policy_password(*parse_policy_password(case_input)),
                    expected_output
                )
