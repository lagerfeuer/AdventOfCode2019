#!/usr/bin/env python3

import unittest
import io
import os

from .main import part1, part2, run


class Day5Test(unittest.TestCase):
    def test_add(self):
        prg = [1, 0, 0, 0, 99]
        res = [2, 0, 0, 0, 99]
        ref, _ = run(prg)
        self.assertEqual(ref, res)

    def test_mul(self):
        prg = [2, 3, 0, 3, 99]
        res = [2, 3, 0, 6, 99]
        ref, _ = run(prg)
        self.assertEqual(ref, res)

    def test_mul_long(self):
        prg = [2, 4, 4, 5, 99, 0]
        res = [2, 4, 4, 5, 99, 9801]
        ref, _ = run(prg)
        self.assertEqual(ref, res)

    def test_add_mul(self):
        prg = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        res = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        ref, _ = run(prg)
        self.assertEqual(ref, res)

    def test_overwrite_hlt(self):
        prg = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        res = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        ref, _ = run(prg)
        self.assertEqual(ref, res)

    def test_parameter_mode(self):
        prg = [1002, 4, 3, 4, 33]
        res = [1002, 4, 3, 4, 99]
        ref, _ = run(prg)
        self.assertEqual(ref, res)

    def test_less_than_position_mode(self):
        prg = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        stdin = io.StringIO('5')
        _, out = run(prg, stdin=stdin)
        self.assertEqual(int(out[-1].strip()), 1)
        stdin = io.StringIO('8')
        _, out = run(prg, stdin=stdin)
        self.assertEqual(int(out[-1].strip()), 0)

    def test_less_than_parameter_mode(self):
        prg = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        stdin = io.StringIO('5')
        _, out = run(prg, stdin=stdin)
        self.assertEqual(int(out[-1].strip()), 1)
        stdin = io.StringIO('8')
        _, out = run(prg, stdin=stdin)
        self.assertEqual(int(out[-1].strip()), 0)

    def test_equal_position_mode(self):
        prg = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        stdin = io.StringIO('8')
        _, out = run(prg, stdin=stdin)
        self.assertEqual(int(out[-1].strip()), 1)
        stdin = io.StringIO('7')
        _, out = run(prg, stdin=stdin)
        self.assertEqual(int(out[-1].strip()), 0)

    def test_equal_parameter_mode(self):
        prg = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        stdin = io.StringIO('8')
        _, out = run(prg, stdin=stdin)
        self.assertEqual(int(out[-1].strip()), 1)
        stdin = io.StringIO('7')
        _, out = run(prg, stdin=stdin)
        self.assertEqual(int(out[-1].strip()), 0)

    def test_solution1(self):
        out = part1()
        self.assertEqual(int(out[-1].strip()), 7259358)

    def test_solution2(self):
        out = part2()
        self.assertEqual(int(out[-1].strip()), 11826654)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    unittest.main()
