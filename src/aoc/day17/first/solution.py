from aoc.utils import local_path
from aoc.utils.spatial import Point3D


def should_live(is_alive, alive_neighbours):
    return (
        (is_alive and 2 <= alive_neighbours <= 3)
        or (not is_alive and alive_neighbours == 3)
    )


def step(alive_cells):
    padded_cells = {
        neighbour
        for cell in alive_cells
        for neighbour in cell.moore_neighbours()
    }
    new_cells = {
        cell
        for cell in padded_cells
        if should_live(
                cell in alive_cells,
                len(alive_cells.intersection(cell.moore_neighbours()))
        )
    }

    return new_cells


def run(initial_cells, n_steps):
    alive_cells = initial_cells

    for _ in range(n_steps):
        alive_cells = step(alive_cells)

    return alive_cells


def parse_tile(tile):
    return '.#'.index(tile)


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        z = 0
        alive_cells = {
            Point3D(x, y, z)
            for y, line in enumerate(input_file)
            for x, tile in enumerate(line.strip())
            if parse_tile(tile) == 1
        }

        return alive_cells


def main():
    input_filename = '../input'
    alive_cells = parse_input(local_path(__file__, input_filename))
    n_steps = 6

    final_cells = run(alive_cells, n_steps)
    print(len(final_cells))


if __name__ == '__main__':
    main()
