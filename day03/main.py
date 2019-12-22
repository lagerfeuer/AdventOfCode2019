#!/usr/bin/env python3

from os.path import dirname
from os.path import join


def read_input(file_name='input.txt'):
    """
    Read input from file_name
    """
    # always open relative to current file
    file_name = join(dirname(__file__), file_name)
    with open(file_name, 'r') as f_in:
        return [wire.strip().split(',')
                for wire in f_in.readlines()]


def parse_wire(raw_in):
    """
    origin: start of the wire (x,y)
    raw_in: movement of the wire in [RLDU][0-9]+
    return: dictionary of coords: length pairs
    """
    last = (0, 0)
    dist = 1
    wire = {}
    for movement in raw_in:
        direction = movement[0]
        length = int(movement[1:])
        x = y = 0
        if direction == 'R':
            x = 1
        if direction == 'L':
            x = -1
        if direction == 'U':
            y = 1
        if direction == 'D':
            y = -1
        for _ in range(length):
            last = (last[0] + x, last[1] + y)
            wire[last] = dist
            dist += 1
    return wire


def calc_min_distance(intersections):
    min_dist = min(intersections, key=lambda x: (abs(x[0]) + abs(x[1])))
    return min_dist


def calc_fewest_steps(wire1, wire2):
    intersections = wire1.keys() & wire2.keys()
    best = min(intersections, key=lambda x: wire1[x] + wire2[x])
    return wire1[best] + wire2[best]


def part1(wire1, wire2):
    """
    Solve the puzzle (part 1), given the input in input.txt
    """
    isects = wire1.keys() & wire2.keys()
    return sum(calc_min_distance(isects))


def part2(wire1, wire2):
    """
    Solve the puzzle (part 2), given the input in input.txt
    """
    return calc_fewest_steps(wire1, wire2)


if __name__ == '__main__':
    lines = read_input('input.txt')
    wire1, wire2 = [parse_wire(line) for line in lines]
    print("Part 1:", part1(wire1, wire2))
    print("Part 2:", part2(wire1, wire2))
