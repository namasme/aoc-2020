from aoc.utils import local_path


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return [line.strip() for line in input_file]


def calculate_seat_id(seat):
    return int(seat.translate(str.maketrans('FLBR', '0011')), 2)


def main():
    input_filename = '../input'
    seats = parse_input(local_path(__file__, input_filename))

    print(max(calculate_seat_id(seat) for seat in seats))


if __name__ == '__main__':
    main()
