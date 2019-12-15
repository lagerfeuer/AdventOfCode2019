#!/usr/bin/env python3

from collections import defaultdict
from os.path import dirname
from os.path import join


def read_input(file_name):
    """
    Read input from file_name
    """
    # always open relative to current file
    file_name = join(dirname(__file__), file_name)
    with open(file_name, 'r') as f_in:
        return f_in.read().strip().split('\n')


def parse_orbits(input_list):
    """
    Parse all orbits from an input list,
    also return a reverse lookup table (for speed)
    """
    orbits = defaultdict(list)
    rev_lookup = {}  # reverse lookup table to increase speed
    for orbit in input_list:
        center, space_obj = orbit.split(')')
        orbits[center].append(space_obj)
        rev_lookup[space_obj] = center
    return orbits, rev_lookup


def calc_distance(orbit_dict, lookup_tbl, space_obj):
    """
    Calculate the distance of one node to the center and
    additionally return the path
    """
    node = space_obj
    cnt = 0
    route = [node]
    while node != 'COM' and node is not None:
        node = lookup_tbl[node]
        cnt += 1
        route.append(node)
    return cnt, route


def calc_orbits(orbit_dict, lookup_tbl):
    """
    Calculate the total number of direct and indirect orbs
    """
    return sum([calc_distance(orbit_dict, lookup_tbl, e)[0]
                for e in lookup_tbl.keys()
                if e != 'COM'])


def part1():
    """
    Solve the puzzle (part 1), given the input in input.txt
    """
    orbit_dict, lookup_tbl = parse_orbits(read_input('input.txt'))
    return calc_orbits(orbit_dict, lookup_tbl)


def part2():
    """
    Solve the puzzle (part 2), given the input in input.txt
    """
    orbit_dict, lookup_tbl = parse_orbits(read_input('input.txt'))
    _, santa_route = calc_distance(orbit_dict, lookup_tbl, 'SAN')
    _, my_route = calc_distance(orbit_dict, lookup_tbl, 'YOU')
    while santa_route[-1] == my_route[-1]:
        santa_route.pop()
        my_route.pop()
    return len(santa_route) + len(my_route) - 2


if __name__ == '__main__':
    print("Part 1:", part1())
    print("Part 2:", part2())
