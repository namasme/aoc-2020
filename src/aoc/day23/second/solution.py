def affine_modular_add(base, a, b, limit):
    '''
    Addition in base + Z_{limit - base + 1}, i.e.:
        limit + 1 == limit - base + 1 + base == base
    '''
    return base + ((a + b - base) % (limit - base + 1))


def build_successors_map(cups):
    labels_to_successors = [0] * (len(cups) + 1)

    for a, b in zip(cups, cups[1:]):
        labels_to_successors[a] = b

    labels_to_successors[cups[-1]] = cups[0]

    return labels_to_successors


def destination(current, labels_to_successors):
    limit = len(labels_to_successors) - 1
    a = labels_to_successors[current]
    b = labels_to_successors[a]
    c = labels_to_successors[b]
    candidate = affine_modular_add(1, current, -1, limit)

    while candidate in (a, b, c):
        candidate = affine_modular_add(1, candidate, -1, limit)

    return candidate


def step(current, labels_to_successors):
    '''
    Mutation is justified to avoid copying over a million values in every single
    step (for 10M steps).
    '''
    destination_label = destination(current, labels_to_successors)

    a = labels_to_successors[current]
    b = labels_to_successors[a]
    c = labels_to_successors[b]

    labels_to_successors[current] = labels_to_successors[c]
    labels_to_successors[c] = labels_to_successors[destination_label]
    labels_to_successors[destination_label] = a

    return labels_to_successors[current]  # new current cup


def run(cups, n_steps):
    labels_to_successors = build_successors_map(cups)
    current_cup = cups[0]

    for _ in range(n_steps):
        current_cup = step(current_cup, labels_to_successors)

    return labels_to_successors


def extend_initial_cups_segment(initial_cups, limit):
    prefix = list(initial_cups)
    return prefix + list(range(max(prefix) + 1, limit + 1))


def solution(labels_to_successors):
    after_1 = labels_to_successors[1]
    return after_1 * labels_to_successors[after_1]


def main():
    cups = extend_initial_cups_segment(map(int, '157623984'), 1_000_000)
    n_steps = 10_000_000
    labels_to_successors = run(cups, n_steps)

    print(solution(labels_to_successors))


if __name__ == '__main__':
    main()
