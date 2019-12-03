#!/bin/python3

from math import floor
import sys


def read_input(file_name):
    """
    Read input from file_name
    """
    input_list = []
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


def solve(part=1):
    """
    Solve the puzzle, given the input in input.txt
    """
    input_list = read_input('input.txt')
    # part 1
    if part == 1:
        return sum(map(fuel_required, input_list))
    # part 2
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
    if len(sys.argv) == 2 and int(sys.argv[1]) in [1, 2]:
        print(solve(part=int(sys.argv[1])))
    else:
        print("Usage: ./main.py [1,2]")
        print("Decide between part 1 and 2")
        sys.exit(1)
