#!/usr/bin/env python3

import unittest

import os

from .main import part1, part2, fuel_required


class Day1Test(unittest.TestCase):
    def test_12(self):
        self.assertEqual(fuel_required(12), 2)

    def test_14(self):
        self.assertEqual(fuel_required(14), 2)

    def test_1969(self):
        self.assertEqual(fuel_required(1969), 654)

    def test_100756(self):
        self.assertEqual(fuel_required(100756), 33583)

    def test_solution_1(self):
        self.assertEqual(part1(), 3421505)

    def test_solution_2(self):
        self.assertEqual(part2(), 5129386)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    unittest.main()
