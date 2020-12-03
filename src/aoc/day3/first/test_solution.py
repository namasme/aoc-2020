import unittest

from .solution import count_trees_in_path, parse_lines, Tile


class TestSolution(unittest.TestCase):
    case = [
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
    ]

    def test_parsing(self):
        tiles = parse_lines(self.case)

        self.assertEqual(tiles[0][0], Tile.EMPTY)
        self.assertEqual(tiles[0][1], Tile.EMPTY)
        self.assertEqual(tiles[1][0], Tile.TREE)
        self.assertEqual(tiles[1][1], Tile.EMPTY)

    def test_count(self):
        tiles = parse_lines(self.case)

        self.assertEqual(count_trees_in_path(tiles), 7)
