import pytest

from .solution import (
    affine_modular_add, build_successors_map, destination,
    extend_initial_cups_segment, run, solution, step,
)


def test_affine_modular_add():
    assert affine_modular_add(1, 3, 4, 9) == 7
    assert affine_modular_add(1, 4, 5, 9) == 9
    assert affine_modular_add(1, 5, 5, 9) == 1
    assert affine_modular_add(1, 1, -1, 9) == 9


def test_build_successors_map():
    assert (
        build_successors_map([3, 8, 9, 1, 2, 5, 4, 6, 7])
        ==
        [0, 2, 5, 8, 6, 4, 7, 3, 9, 1]
    )


def test_destination():
    labels_to_successors = build_successors_map([3, 8, 9, 1, 2, 5, 4, 6, 7])
    assert destination(3, labels_to_successors) == 2

    labels_to_successors = build_successors_map([3, 2, 8, 9, 1, 5, 4, 6, 7])
    assert destination(2, labels_to_successors) == 7


def test_step():
    labels_to_successors = build_successors_map([3, 8, 9, 1, 2, 5, 4, 6, 7])
    new_current = step(3, labels_to_successors)
    assert new_current == 2
    assert (
        labels_to_successors
        ==
        build_successors_map([3, 2, 8, 9, 1, 5, 4, 6, 7])
    )

    new_current = step(2, labels_to_successors)
    assert new_current == 5
    assert (
        labels_to_successors
        ==
        build_successors_map([3, 2, 5, 4, 6, 7, 8, 9, 1])
    )


def test_run():
    assert (
        run([3, 8, 9, 1, 2, 5, 4, 6, 7], 10)
        ==
        build_successors_map([8, 3, 7, 4, 1, 9, 2, 6, 5])
    )


def test_solution():
    initial_cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    cups = extend_initial_cups_segment(initial_cups, 1_000_000)
    assert len(cups) == 1e6

    n_steps = 10_000_000
    labels_to_successors = run(cups, n_steps)

    assert labels_to_successors[1] == 934001
    assert labels_to_successors[934001] == 159792
    assert solution(labels_to_successors) == 149245887792
