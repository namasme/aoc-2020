import unittest

from .solution import match_policy_password


class TestSolution(unittest.TestCase):
    cases = [
        (((1, 3), 'a'), 'abcde'),
        (((1, 3), 'b'), 'cdefg'),
        (((2, 9), 'c'), 'ccccccccc'),
    ]

    def test_matches(self):
        expected_outputs = [True, False, False]

        for case_input, expected_output in zip(self.cases, expected_outputs):
            with self.subTest(policy=case_input):
                self.assertEqual(
                    match_policy_password(*case_input),
                    expected_output
                )
