import attr
from functools import reduce

from aoc.day12.first.solution import Action, parse_input
from aoc.utils import local_path
from aoc.utils.spatial import Direction, Orientation, Point2D


@attr.s
class WaypointShip:
    position = attr.ib()
    waypoint = attr.ib()


def rotate_point(position, orientation):
    if orientation == Orientation.CLOCKWISE:
        return Point2D(position.y, -position.x)
    elif orientation == Orientation.COUNTERCLOCKWISE:
        return Point2D(-position.y, position.x)


def apply_instruction(ship, instruction):
    action, param = instruction

    if action == Action.ABSOLUTE:
        return WaypointShip(ship.position, ship.waypoint + param)
    elif action == Action.RELATIVE:
        return WaypointShip(
            ship.position + param * ship.waypoint,
            ship.waypoint
        )
    else:
        orientation, times = param
        new_waypoint = ship.waypoint

        for _ in range(times):
            new_waypoint = rotate_point(new_waypoint, orientation)

        return WaypointShip(ship.position, new_waypoint)


def main():
    input_filename = '../input'
    instructions = parse_input(local_path(__file__, input_filename))
    ship = WaypointShip(Point2D(0, 0), Point2D(10, 1))

    final_ship = reduce(apply_instruction, instructions, ship)

    print(abs(final_ship.position))



if __name__ == '__main__':
    main()
