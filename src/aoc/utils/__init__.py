from pathlib import Path


def bezout(a, b):
    '''
    The return value of this function verifies that
             r * a + s * b = gcd = gcd(a, b)
    '''
    prev_m, m = 1, 0
    prev_n, n = 0, 1

    while b != 0:
        q, r = divmod(a, b)

        a, b = b, r
        prev_m, m = m, prev_m - q * m
        prev_n, n = n, prev_n - q * n

    gcd, r, s = a, prev_m, prev_n
    return (gcd, r, s)


def local_path(base, filename):
    return Path(base).resolve().parent.joinpath(filename)


def read_ints(path, separator=None):
    with open(path) as input_file:
        if separator == None:
            integers = input_file.readlines()  # assume \n
        else:
            integers = input_file.read().split(separator)

        return [int(_) for _ in integers]
