import pytest

from collections import deque

from .solution import destination, run, solution, step


def test_destination():
    assert destination([3, 8, 9, 1, 2, 5, 4, 6, 7]) == 2
    assert destination([2, 8, 9, 1, 5, 4, 6, 7, 3]) == 7


def test_step():
    assert (
        step([3, 8, 9, 1, 2, 5, 4, 6, 7])
        ==
        deque([2, 8, 9, 1, 5, 4, 6, 7, 3])
    )
    assert (
        step([2, 8, 9, 1, 5, 4, 6, 7, 3])
        ==
        deque([5, 4, 6, 7, 8, 9, 1, 3, 2])
    )


def test_run():
    assert (
        run([3, 8, 9, 1, 2, 5, 4, 6, 7], 1)
        ==
        list(step([3, 8, 9, 1, 2, 5, 4, 6, 7]))
    )
    assert (
        run([3, 8, 9, 1, 2, 5, 4, 6, 7], 2)
        ==
        list(step(step([3, 8, 9, 1, 2, 5, 4, 6, 7])))
    )
    assert run([3, 8, 9, 1, 2, 5, 4, 6, 7], 10) == [8, 3, 7, 4, 1, 9, 2, 6, 5]


def test_solution():
    assert solution([5, 8, 3, 7, 4, 1, 9, 2, 6]) == [9, 2, 6, 5, 8, 3, 7, 4]


def test_run_solution():
    assert solution(run([3, 8, 9, 1, 2, 5, 4, 6, 7], 100)) == [
        6, 7, 3, 8, 4, 5, 2, 9,
    ]
