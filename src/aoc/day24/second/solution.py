from aoc.day24.first.solution import flip_tiles, parse_input
from aoc.utils.spatial import Point2D


def hex_neighbours(point):
    return [
        point + direction
        for direction in [
                Point2D(1, 0),
                Point2D(-1, 0),
                Point2D(0, 1),
                Point2D(0, -1),
                Point2D(-1, 1),
                Point2D(1, -1),
        ]
    ]


def step(black_tiles):
    candidates = {
        neighbour
        for tile in black_tiles
        for neighbour in hex_neighbours(tile)
    }
    new_black_tiles = set()

    for candidate in candidates:
        black_neighbours = len(
            black_tiles.intersection(hex_neighbours(candidate))
        )

        if candidate in black_tiles:
            if 0 < black_neighbours <= 2:
                new_black_tiles.add(candidate)
        else:
            if black_neighbours == 2:
                new_black_tiles.add(candidate)

    return new_black_tiles


def run(initial_tiles, n_steps):
    black_tiles = set(initial_tiles)

    for _ in range(n_steps):
        black_tiles = step(black_tiles)

    return black_tiles


def main():
    input_filename = '../input'
    initial_tiles = flip_tiles(parse_input(input_filename))
    n_steps = 100
    flipped_tiles = run(initial_tiles, n_steps)

    print(len(flipped_tiles))


if __name__ == '__main__':
    main()
