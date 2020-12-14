from enum import auto, Enum


class Direction(Enum):
    L = auto()
    U = auto()
    R = auto()
    D = auto()


class Orientation(Enum):
    CLOCKWISE = auto()
    COLINEAR = auto()
    COUNTERCLOCKWISE = auto()
