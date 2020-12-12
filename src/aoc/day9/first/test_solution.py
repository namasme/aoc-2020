from .solution import find_first_invalid_number


def test_solution():
    numbers = [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]
    preamble_size = 5

    assert find_first_invalid_number(numbers, preamble_size) == 127
