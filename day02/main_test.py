#!/bin/python3

import unittest

import os

from .main import part1, part2, run


class Day2Test(unittest.TestCase):
    def test_add(self):
        prg = [1, 0, 0, 0, 99]
        res = [2, 0, 0, 0, 99]
        self.assertEqual(run(prg), res)

    def test_mul(self):
        prg = [2, 3, 0, 3, 99]
        res = [2, 3, 0, 6, 99]
        self.assertEqual(run(prg), res)

    def test_mul_long(self):
        prg = [2, 4, 4, 5, 99, 0]
        res = [2, 4, 4, 5, 99, 9801]
        self.assertEqual(run(prg), res)

    def test_add_mul(self):
        prg = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        res = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual(run(prg), res)

    def test_overwrite_hlt(self):
        prg = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        res = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        self.assertEqual(run(prg), res)

    def test_solution1(self):
        self.assertEqual(part1(), 2842648)

    def test_solution2(self):
        self.assertEqual(part2(), 9074)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    unittest.main()
