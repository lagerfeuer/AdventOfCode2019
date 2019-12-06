#!/usr/bin/env python3

import unittest

import os

from .main import part1, part2, parse_wire, calc_min_distance, read_input


class Day3Test(unittest.TestCase):
    def test_small(self):
        line1 = 'R8,U5,L5,D3'.split(',')
        line2 = 'U7,R6,D4,L4'.split(',')
        wire1 = parse_wire(line1)
        wire2 = parse_wire(line2)
        intersections = wire1.keys() & wire2.keys()
        min_coords = calc_min_distance(intersections)
        min_dist = sum(min_coords)
        self.assertEqual(min_dist, 6)

    def test_big_1(self):
        line1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
        line2 = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')
        wire1 = parse_wire(line1)
        wire2 = parse_wire(line2)
        intersections = wire1.keys() & wire2.keys()
        min_coords = calc_min_distance(intersections)
        min_dist = sum(min_coords)
        self.assertEqual(min_dist, 159)

    def test_big_2(self):
        line1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',')
        line2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')
        wire1 = parse_wire(line1)
        wire2 = parse_wire(line2)
        intersections = wire1.keys() & wire2.keys()
        min_coords = calc_min_distance(intersections)
        min_dist = sum(min_coords)
        self.assertEqual(min_dist, 135)

    def test_solution1(self):
        lines = read_input('input.txt')
        wire1, wire2 = [parse_wire(line) for line in lines]
        self.assertEqual(part1(wire1, wire2), 303)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    unittest.main()
