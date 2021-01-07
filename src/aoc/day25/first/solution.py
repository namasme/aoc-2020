from math import ceil, sqrt

from aoc.utils import local_path, read_ints


def dual_bsgs(g, p, ga, gb):
    m = ceil(sqrt(p))
    table = {
        pow(g, j, p): j  # very wasteful but not noticeable
        for j in range(m)
    }
    inverse = pow(g, p - m - 1, p)  # == g^(-m)
    gamma_a, gamma_b = ga, gb

    for i in range(m):
        if gamma_a in table:
            return (ga, i * m + table[gamma_a])
        elif gamma_b in table:
            return (gb, i * m + table[gamma_b])
        else:
            gamma_a = (gamma_a * inverse) % p
            gamma_b = (gamma_b * inverse) % p

    return None


def solution(ga, gb):
    g = 7
    p = 20201227
    pub_key, loop_size = dual_bsgs(g, p, ga, gb)

    return pow((ga ^ gb ^ pub_key), loop_size, p)


def main():
    input_filename = '../input'
    public_keys = read_ints(local_path(__file__, input_filename))

    print(solution(*public_keys))


if __name__ == '__main__':
    main()
