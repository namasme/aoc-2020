from collections import deque


def destination(cups):
    modulus = max(cups)
    candidate = 1 + ((cups[0] - 2) % modulus)
    selected_cups = [cups[1], cups[2], cups[3]]

    while candidate in selected_cups:
        candidate = 1 + ((candidate - 2) % modulus)

    return candidate


def step(cups):
    destination_value = destination(cups)
    destination_position = cups.index(destination_value)
    cups_list = list(cups)

    new_cups = deque(
        cups_list[:1]
        + cups_list[4:destination_position+1]
        + cups_list[1:4]
        + cups_list[destination_position+1:]
    )
    new_cups.rotate(-1)

    return new_cups


def run(cups, n_steps):
    for _ in range(n_steps):
        cups = step(cups)

    return list(cups)


def solution(cups):
    one_position = cups.index(1)
    return cups[one_position+1:] + cups[:one_position]


def main():
    cups = list(map(int, '157623984'))
    n_steps = 100
    final_cups = solution(run(cups, n_steps))

    print(''.join(map(str, final_cups)))


if __name__ == '__main__':
    main()
