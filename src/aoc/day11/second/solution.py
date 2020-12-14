from aoc.day11.first.solution import Tile
from aoc.utils import local_path
from aoc.utils.spatial import Point2D



def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return SeatsLayout.parse([line.strip() for line in input_file])


class SeatsLayout:
    def __init__(self, initial_layout, n_row, n_col):
        self.i = 0
        self.n_row = n_row
        self.n_col = n_col
        self.layout = initial_layout
        self.visible = {
            position: list(self.find_visible(position))
            for position in self.layout
        }
        self.changed = False

    @staticmethod
    def parse(rows):
        seats_layout = {}

        for n_row, row in enumerate(rows):
            for n_col, char in enumerate(row):
                if Tile(char) == Tile.FLOOR:
                    continue

                seats_layout[Point2D(n_row, n_col)] = Tile(char)

        return SeatsLayout(seats_layout, len(rows), len(rows[0]))

    def find_visible(self, position):
        origin = Point2D(0, 0)
        frontier = Point2D(self.n_row - 1, self.n_col - 1)
        directions = origin.moore_neighbours()

        for direction in directions:
            radius = 0

            while True:
                radius +=1
                candidate = position + radius * direction

                if not candidate.lies_within(origin, frontier):
                    break

                if self.layout.get(candidate, Tile.FLOOR) != Tile.FLOOR:
                    yield candidate
                    break

    def step(self):
        self.i += 1
        print(self.i)

        next_ = {}
        self.changed = False

        for position, state in self.layout.items():
            visible_count = sum(
                self.layout.get(visible, Tile.FLOOR) == Tile.OCCUPIED
                for visible in self.visible[position]
            )

            if state == Tile.EMPTY and visible_count == 0:
                next_[position] = Tile.OCCUPIED
                self.changed = True
            elif state == Tile.OCCUPIED and visible_count >= 5:
                next_[position] = Tile.EMPTY
                self.changed = True
            else:
                next_[position] = state

        self.layout = next_

    def find_stable_layout(self):
        self.changed = True  # initial iteration

        while self.changed:
            self.step()

        return self.layout

    def __str__(self):
        return '\n'.join(
            ''.join(
                str(self.layout.get(Point2D(row, col), Tile.FLOOR).value)
                for col in range(self.n_col)
            )
            for row in range(self.n_row)
        )


def main():
    input_filename = '../input'
    seats_layout = parse_input(local_path(__file__, input_filename))

    seats_layout.find_stable_layout()

    print(sum(
        tile == Tile.OCCUPIED
        for tile in seats_layout.layout.values()
    ))


if __name__ == '__main__':
    main()
