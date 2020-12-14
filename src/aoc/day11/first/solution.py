from enum import Enum

from aoc.utils import local_path
from aoc.utils.spatial import Point2D


class Tile(Enum):
    EMPTY = 'L'
    OCCUPIED = '#'
    FLOOR = '.'


def parse_seats_layout(rows):
    seats_layout = {}

    for n_row, row in enumerate(rows):
        for n_col, char in enumerate(row):
            if Tile(char) == Tile.FLOOR:
                continue

            seats_layout[Point2D(n_row, n_col)] = Tile(char)

    return seats_layout


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return parse_seats_layout([line.strip() for line in input_file])


def step(layout):
    next_ = {}

    for position, state in layout.items():
        neighbours_count = sum(
            layout.get(neighbour, Tile.FLOOR) == Tile.OCCUPIED
            for neighbour in position.moore_neighbours()
        )

        if state == Tile.EMPTY and neighbours_count == 0:
            next_[position] = Tile.OCCUPIED
        elif state == Tile.OCCUPIED and neighbours_count >= 4:
            next_[position] = Tile.EMPTY
        else:
            next_[position] = state

    return next_


def find_stable_layout(initial_layout):
    current = initial_layout
    updated = step(initial_layout)

    while current != updated:
        current = updated
        updated = step(updated)

    return current


def main():
    input_filename = '../input'
    layout = parse_input(local_path(__file__, input_filename))
    stable_layout = find_stable_layout(layout)

    print(sum(
        tile == Tile.OCCUPIED
        for tile in stable_layout.values()
    ))


if __name__ == '__main__':
    main()
