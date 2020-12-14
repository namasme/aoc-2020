import pytest
from functools import reduce

from aoc.utils import local_path
from aoc.utils.spatial import Orientation, Point2D
from .solution import (
    Action, apply_instruction, parse_input, WaypointShip
)


@pytest.fixture
def instructions():
    test_input_filename = '../test_input'

    return parse_input(local_path(__file__, test_input_filename))


def test_apply_instruction(instructions):
    ship = WaypointShip(Point2D(0, 0), Point2D(10, 1))

    assert (
        apply_instruction(ship, (Action.ABSOLUTE, Point2D(0, -2)))
        == WaypointShip(Point2D(0, 0), Point2D(10, -1))
    )
    assert (
        apply_instruction(ship, (Action.RELATIVE, 5))
        == WaypointShip(Point2D(50, 5), Point2D(10, 1))
    )
    assert (
        apply_instruction(
            ship,
            (Action.ROTATION, (Orientation.COUNTERCLOCKWISE, 3))
        ) == WaypointShip(Point2D(0, 0), Point2D(1, -10))
    )

    final_ship = reduce(apply_instruction, instructions, ship)

    assert final_ship.position == Point2D(214, -72)
    assert final_ship.waypoint == Point2D(4, -10)
