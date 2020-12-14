import attr
from enum import auto, Enum
from functools import reduce

from aoc.utils import local_path
from aoc.utils.spatial import Direction, Orientation, Point2D, rotate


class Action(Enum):
    ABSOLUTE = auto()
    RELATIVE = auto()
    ROTATION = auto()


@attr.s
class Ship:
    position = attr.ib()
    direction = attr.ib()


def parse_instruction(raw_instruction):
    action_char = raw_instruction[0]
    number = int(raw_instruction[1:])

    if action_char in 'NSEW':
        action = Action.ABSOLUTE

        units = {
            'N': Point2D(0, 1),
            'S': Point2D(0, -1),
            'E': Point2D(1, 0),
            'W': Point2D(-1, 0),
        }
        distance = number
        param = distance * units[action_char]
    elif action_char in 'LR':
        action = Action.ROTATION

        orientations = {
            'L': Orientation.COUNTERCLOCKWISE,
            'R': Orientation.CLOCKWISE,
        }
        degrees = number
        param = (orientations[action_char], (degrees % 360) // 90)
    else:
        action = Action.RELATIVE
        param = number

    return (action, param)


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return [parse_instruction(line.strip()) for line in input_file]


def apply_instruction(ship, instruction):
    action, param = instruction

    if action == Action.ABSOLUTE:
        return Ship(ship.position + param, ship.direction)
    elif action == Action.RELATIVE:
        return Ship(
            ship.position.move_by(ship.direction, param),
            ship.direction
        )
    else:
        orientation, times = param
        new_direction = ship.direction

        for _ in range(times):
            new_direction = rotate(new_direction, orientation)

        return Ship(ship.position, new_direction)


def main():
    input_filename = '../input'
    instructions = parse_input(local_path(__file__, input_filename))
    ship = Ship(Point2D(0, 0), Direction.R)

    final_ship = reduce(apply_instruction, instructions, ship)

    print(abs(final_ship.position))


if __name__ == '__main__':
    main()
