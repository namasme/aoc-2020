from aoc.utils import local_path
from aoc.day5.first.solution import calculate_seat_id, parse_input


def find_missing_seat_id(seat_ids):
    seen_ids = set(seat_ids)

    for seat_id in range(1024):  # 2^10
        if seat_id in seen_ids:
            continue

        if (seat_id - 1) in seen_ids and (seat_id + 1) in seen_ids:
            return seat_id


def find_missing_seat_id_alt(seat_ids):
    missing_seat_ids = list(sorted(set(range(1024)) - set(seat_ids)))

    for prev, next in zip(missing_seat_ids, missing_seat_ids[1:]):
        if prev + 1 != next:
            return next


def main():
    input_filename = '../input'
    seats = parse_input(local_path(__file__, input_filename))
    seat_ids = [calculate_seat_id(seat) for seat in seats]

    print(find_missing_seat_id_alt(seat_ids))


if __name__ == '__main__':
    main()
