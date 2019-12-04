#!/usr/bin/env python3

import unittest

import os

from .main import part1, part2, parse_wire, calculate_intersections, calculate_distances


class Day3Test(unittest.TestCase):
    def test_small(self):
        wire1 = 'R8,U5,L5,D3'.split(',')
        wire2 = 'U7,R6,D4,L4'.split(',')
        line1 = parse_wire(wire1)
        line2 = parse_wire(wire2)
        intersections = calculate_intersections(line1, line2)
        distances = calculate_distances(intersections)
        self.assertEqual(min(distances), 6)

    def test_big_1(self):
        wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
        wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')
        line1 = parse_wire(wire1)
        line2 = parse_wire(wire2)
        intersections = calculate_intersections(line1, line2)
        distances = calculate_distances(intersections)
        self.assertEqual(min(distances), 159)

    def test_big_2(self):
        wire1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',')
        wire2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')
        line1 = parse_wire(wire1)
        line2 = parse_wire(wire2)
        intersections = calculate_intersections(line1, line2)
        distances = calculate_distances(intersections)
        self.assertEqual(min(distances), 135)

    def test_solution1(self):
        self.assertEqual(part1(), 303)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    unittest.main()
