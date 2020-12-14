import pytest
from functools import reduce

from aoc.utils import local_path
from aoc.utils.spatial import Direction, Orientation, Point2D
from .solution import (
    Action, apply_instruction, parse_input, parse_instruction, Ship
)


@pytest.fixture
def instructions():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_parsing():
    assert parse_instruction('F10') == (Action.RELATIVE, 10)
    assert parse_instruction('N3') == (Action.ABSOLUTE, Point2D(0, 3))
    assert parse_instruction('R90') == (
        Action.ROTATION,
        (Orientation.CLOCKWISE, 1)
    )


def test_apply_instruction(instructions):
    ship = Ship(Point2D(0, 0), Direction.R)

    assert apply_instruction(ship, (Action.ABSOLUTE, Point2D(0, -2))) == Ship(
        Point2D(0, -2),
        Direction.R
    )
    assert apply_instruction(ship, (Action.RELATIVE, 5)) == Ship(
        Point2D(5, 0),
        Direction.R
    )
    assert (
        apply_instruction(
            ship,
            (Action.ROTATION, (Orientation.COUNTERCLOCKWISE, 3))
        ) == Ship(Point2D(0, 0), Direction.D)
    )

    final_ship = reduce(apply_instruction, instructions, ship)

    assert final_ship.position == Point2D(17, -8)
    assert final_ship.direction == Direction.D
