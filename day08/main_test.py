#!/usr/bin/env python3

import unittest
import os
from math import prod

from .main import part1, part2
from .main import parse, overlay


class Day8Test(unittest.TestCase):
    def test_layer_parse(self):
        data = list("123456789012")
        dim = (3, 2)
        ref = [
            [list(map(int, list(x))) for x in "123 456".split()],
            [list(map(int, list(x))) for x in "789 012".split()]
        ]
        out = [layer.dump() for layer in parse(data, dim)]
        self.assertEqual(ref, out)
        ref = [list(map(int, data[i:i+prod(dim)]))
               for i in range(0, len(data), prod(dim))]
        out = [layer.stream() for layer in parse(data, dim)]
        self.assertEqual(ref, out)

    def test_visualize(self):
        ref = list(map(int, "0110"))
        data = "0222112222120000"
        dim = (2, 2)
        layers = parse(data, dim)
        out = overlay(layers)
        self.assertEqual(ref, out)

    def test_solution1(self):
        out = part1()
        self.assertEqual(out, 1572)

    def test_solution2(self):
        ref = '\n'.join(["#  # #   ##  # #### #### ",
                         "# #  #   ##  # #    #    ",
                         "##    # # #### ###  ###  ",
                         "# #    #  #  # #    #    ",
                         "# #    #  #  # #    #    ",
                         "#  #   #  #  # #    #### "])
        out = part2()
        self.assertEqual(out, ref)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    unittest.main()
