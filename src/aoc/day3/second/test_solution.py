import unittest

from aoc.day3.first.solution import parse_lines
from .solution import count_trees_in_path, generate_path, Tile


class TestSolution(unittest.TestCase):
    tiles = parse_lines([
        '..##.......',
        '#...#...#..',
        '.#....#..#.',
        '..#.#...#.#',
        '.#...##..#.',
        '..#.##.....',
        '.#.#.#....#',
        '.#........#',
        '#.##...#...',
        '#...##....#',
        '.#..#...#.#',
    ])

    def test_count(self):
        cases = [{
            'right': 1,
            'down': 1,
            'expected': 2,
        }, {
            'right': 3,
            'down': 1,
            'expected': 7,
        }, {
            'right': 5,
            'down': 1,
            'expected': 3,
        }, {
            'right': 7,
            'down': 1,
            'expected': 4,
        }, {
            'right': 1,
            'down': 2,
            'expected': 2,
        }]

        for case in cases:
            with self.subTest(case=case):
                self.assertEqual(
                    count_trees_in_path(self.tiles, generate_path(case['right'], case['down'])),
                    case['expected']
                )
