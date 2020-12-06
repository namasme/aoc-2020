import pytest

from .solution import calculate_seat_id

@pytest.mark.parametrize("seat,expected", [
    ('BFFFBBFRRR', 567),
    ('FFFBBBFRRR', 119),
    ('BBFFBBFRLL', 820),
])
def test_calculate_seat_id(seat, expected):
    assert calculate_seat_id(seat) == expected
