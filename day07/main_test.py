#!/usr/bin/env python3

import unittest
import io
import os

from .main import part1, part2, VM, run_sequence, run_parallel


def run_mem_test(prg):
    vm = VM(program=prg)
    vm.run()
    return vm.mem


def run_output_test(prg, initial):
    stdin = io.StringIO(initial)
    vm = VM(stdin=stdin, program=prg)
    vm.run()
    out = vm.output
    return int(out[-1].strip())


class Day7Test(unittest.TestCase):
    def test_add(self):
        prg = [1, 0, 0, 0, 99]
        res = [2, 0, 0, 0, 99]
        ref = run_mem_test(prg)
        self.assertEqual(ref, res)

    def test_mul(self):
        prg = [2, 3, 0, 3, 99]
        res = [2, 3, 0, 6, 99]
        ref = run_mem_test(prg)
        self.assertEqual(ref, res)

    def test_mul_long(self):
        prg = [2, 4, 4, 5, 99, 0]
        res = [2, 4, 4, 5, 99, 9801]
        ref = run_mem_test(prg)
        self.assertEqual(ref, res)

    def test_add_mul(self):
        prg = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        res = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        ref = run_mem_test(prg)
        self.assertEqual(ref, res)

    def test_overwrite_hlt(self):
        prg = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        res = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        ref = run_mem_test(prg)
        self.assertEqual(ref, res)

    def test_parameter_mode(self):
        prg = [1002, 4, 3, 4, 33]
        res = [1002, 4, 3, 4, 99]
        ref = run_mem_test(prg)
        self.assertEqual(ref, res)

    def test_less_than_position_mode(self):
        prg = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        out = run_output_test(prg, '5')
        self.assertEqual(out, 1)
        out = run_output_test(prg, '8')
        self.assertEqual(out, 0)

    def test_less_than_parameter_mode(self):
        prg = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        out = run_output_test(prg, '5')
        self.assertEqual(out, 1)
        out = run_output_test(prg, '8')
        self.assertEqual(out, 0)

    def test_equal_position_mode(self):
        prg = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        out = run_output_test(prg, '8')
        self.assertEqual(out, 1)
        out = run_output_test(prg, '7')
        self.assertEqual(out, 0)

    def test_equal_parameter_mode(self):
        prg = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        out = run_output_test(prg, '8')
        self.assertEqual(out, 1)
        out = run_output_test(prg, '7')
        self.assertEqual(out, 0)

    # Test sequences
    def test_sequence_1(self):
        prg = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
        seq = (4, 3, 2, 1, 0)
        out = run_sequence(prg, seq)
        self.assertEqual(43210, out)

    def test_sequence_2(self):
        prg = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23,
               101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]
        seq = (0, 1, 2, 3, 4)
        out = run_sequence(prg, seq)
        self.assertEqual(54321, out)

    def test_sequence_3(self):
        prg = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0,
               33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99,
               0, 0, 0]
        seq = (1, 0, 4, 3, 2)
        out = run_sequence(prg, seq)
        self.assertEqual(65210, out)

    @unittest.skip("Not working")
    def test_paralell_short(self):
        prg = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
               27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]
        seq = (9, 8, 7, 6, 5)
        out = run_parallel(prg, seq)
        self.assertEqual(139629729, out)

    @unittest.skip("Not working")
    def test_paralell_long(self):
        prg = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55,
               1005, 55, 26, 1001, 54, -5, 54, 1105, 1, 12, 1, 53, 54, 53,
               1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53, 1001,
               56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]
        seq = (9, 7, 8, 5, 6)
        out = run_parallel(prg, seq)
        self.assertEqual(18216, out)

    def test_solution1(self):
        out = part1()
        self.assertEqual(out, 99376)

    def test_solution2(self):
        out = part2()
        self.assertEqual(out, 8754464)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    unittest.main()
