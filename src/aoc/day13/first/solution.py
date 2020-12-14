from aoc.utils import local_path


def parse_frequencies(frequencies_line):
    return [
        int(frequency)
        for frequency in frequencies_line.split(',')
        if frequency != 'x'
    ]


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        timestamp_line, frequencies_line = input_file
        return (
            int(timestamp_line.strip()),
            parse_frequencies(frequencies_line)
        )


def find_earliest_bus(timestamp, frequencies):
    return min(
        (frequency - (timestamp % frequency), frequency)
        for frequency in frequencies
    )

def main():
    input_filename = '../input'
    timestamp, frequencies = parse_input(local_path(__file__, input_filename))
    waiting_time, bus = find_earliest_bus(timestamp, frequencies)

    print(waiting_time * bus)


if __name__ == '__main__':
    main()
