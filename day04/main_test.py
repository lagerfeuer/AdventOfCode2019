#!/usr/bin/env python3

import unittest

import os

from .main import part1, part2, check1, check2


class Day4Test(unittest.TestCase):
    def test_check(self):
        self.assertTrue(check1(111111))
        self.assertFalse(check1(223450))
        self.assertFalse(check1(123789))

    def test_extended_check(self):
        self.assertTrue(check2(112233))
        self.assertFalse(check2(123444))
        self.assertTrue(check2(111122))

    def test_solution1(self):
        self.assertEqual(part1(), 1873)

    def test_solution2(self):
        self.assertEqual(part2(), 1264)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    unittest.main()
