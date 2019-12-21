#!/usr/bin/env python3

import unittest
import os

from .main import part1, part2, parse_orbits, calc_orbits, calc_distance


class Day6Test(unittest.TestCase):
    def test_parse(self):
        raw_in = 'COM)B B)C C)D D)E E)F B)G G)H D)I E)J J)K K)L'.split()
        dict_out, lookup_tbl = parse_orbits(raw_in)
        parsed_out = {k: v for k, v in dict_out.items() if len(v)}
        steps_out = {v: calc_distance(dict_out, lookup_tbl, v)[0]
                     for v in lookup_tbl.keys()}
        parsed_ref = {'COM': ['B'], 'B': ['C', 'G'], 'C': ['D'],
                      'D': ['E', 'I'], 'E': ['F', 'J'], 'G': ['H'],
                      'J': ['K'], 'K': ['L'], }
        steps_ref = {'B': 1, 'C': 2, 'D': 3,
                     'E': 4, 'F': 5, 'G': 2, 'H': 3,
                     'I': 4, 'J': 5, 'K': 6, 'L': 7}
        self.assertEqual(parsed_out, parsed_ref)
        self.assertEqual(steps_out, steps_ref)

    def test_calc(self):
        raw_in = 'COM)B B)C C)D D)E E)F B)G G)H D)I E)J J)K K)L'.split()
        orbits, lookup = parse_orbits(raw_in)
        ref = 42
        out = calc_orbits(orbits, lookup)
        self.assertEqual(ref, out)

    def test_calc_2(self):
        raw_in = \
            'G)H B)C C)D D)E E)F COM)B B)G D)I E)J J)K K)L K)L I)M'.split()
        orbits, lookup = parse_orbits(raw_in)
        ref = 47
        out = calc_orbits(orbits, lookup)
        self.assertEqual(ref, out)

    def test_solution1(self):
        self.assertEqual(part1(), 247089)

    def test_solution2(self):
        self.assertEqual(part2(), 442)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    unittest.main()
