#!/bin/python3

import unittest

from main import solve, fuel_required


class Day1Test(unittest.TestCase):
    def test_12(self):
        self.assertEqual(fuel_required(12), 2)

    def test_14(self):
        self.assertEqual(fuel_required(14), 2)

    def test_1969(self):
        self.assertEqual(fuel_required(1969), 654)

    def test_100756(self):
        self.assertEqual(fuel_required(100756), 33583)

    def test_solution(self):
        self.assertEqual(solve(), 3421505)


if __name__ == "__main__":
    unittest.main()
