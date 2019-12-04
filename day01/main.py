#!/usr/bin/env python3

from math import floor
import sys
from os.path import dirname
from os.path import join


def read_input(file_name):
    """
    Read input from file_name
    """
    input_list = []
    # always open relative to current file
    file_name = join(dirname(__file__), file_name)
    with open(file_name, 'r') as f_in:
        input_list = [line.strip()
                      for line in f_in.readlines()
                      if line.strip()]
    return map(int, input_list)


def fuel_required(mass):
    """
    Fuel required to launch a given module is based on its mass.
    Specifically, to find the fuel required for a module,
    take its mass, divide by three, round down, and subtract 2.

    For example:
    - For a mass of 12, divide by 3 and round down to get 4,
      then subtract 2 to get 2.
    - For a mass of 14, dividing by 3 and rounding down still yields 4,
      so the fuel required is also 2.
    """
    return int(floor(mass / 3) - 2)


def part1():
    """
    Solve the puzzle (part 1), given the input in input.txt
    """
    input_list = read_input('input.txt')
    return sum(map(fuel_required, input_list))


def part2():
    """
    Solve the puzzle (part 2), given the input in input.txt
    """
    input_list = read_input('input.txt')
    fuel_list = []
    for mass_in in input_list:
        helper = True
        total_fuel = 0
        mass = mass_in
        while helper or mass > 0:
            helper = False
            mass = fuel_required(mass)
            if mass > 0:
                total_fuel += mass
        fuel_list.append(total_fuel)
    return sum(fuel_list)


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
