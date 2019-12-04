#!/usr/bin/env python3

import sys
from os.path import dirname
from os.path import join

from shapely.geometry import LineString, Point


def read_input(file_name):
    """
    Read input from file_name
    """
    input_list = []
    # always open relative to current file
    file_name = join(dirname(__file__), file_name)
    with open(file_name, 'r') as f_in:
        input_list = [wire.strip().split(',')
                      for wire in f_in.readlines()]
    return input_list


def parse_wire(raw_in):
    """
    origin: start of the wire (x,y)
    raw_in: movement of the wire in [RLDU][0-9]+
    return: LineString containing the segments
    """
    line = [Point(0, 0)]
    next_p = Point(0, 0)
    for movement in raw_in:
        direction = movement[0]
        length = int(movement[1:])
        x = y = 0
        if direction == 'R':
            x += length
        if direction == 'L':
            x -= length
        if direction == 'U':
            y += length
        if direction == 'D':
            y -= length
        next_p = Point((next_p.x + x, next_p.y + y))
        line.append(next_p)
    return LineString(line)


def calculate_intersections(wire1, wire2):
    """
    The wires twist and turn, but the two wires occasionally cross paths.
    To fix the circuit, you need to find the intersection point closest
    to the central port.
    Because the wires are on a grid, use the Manhattan distance for
    this measurement.
    While the wires do technically cross right at the central port
    where they both start, this point does not count,
    nor does a wire count as crossing with itself.
    """
    intersections = wire1.intersection(wire2)
    return intersections


def calculate_distances(intersections):
    return [x for x in [int(abs(isect.x) + abs(isect.y))
                        for isect in intersections]
            if x]  # remove x if x == 0 (center)


def part1():
    """
    Solve the puzzle (part 1), given the input in input.txt
    ...before running the program,
    replace position 1 with the value 12 and
    replace position 2 with the value 2.
    """
    line1, line2 = read_input('input.txt')
    wire1 = parse_wire(line1)
    wire2 = parse_wire(line2)
    intersections = calculate_intersections(wire1, wire2)
    distances = calculate_distances(intersections)
    return min(distances)


def part2():
    """
    Solve the puzzle (part 2), given the input in input.txt
    """
    wires = read_input('input.txt')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        arg = int(sys.argv[1])
        if arg == 1:
            print(part1())
        if arg == 2:
            print(part2())
    else:
        print("Usage: ./main.py [1,2]")
        print("Decide between part 1 and 2")
        sys.exit(1)
