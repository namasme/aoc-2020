from pathlib import Path


def local_path(base, filename):
    return Path(base).resolve().parent.joinpath(filename)


def read_ints(path, separator=None):
    with open(path) as input_file:
        if separator == None:
            integers = input_file.readlines()  # assume \n
        else:
            integers = input_file.read().split(separator)

        return [int(_) for _ in integers]
