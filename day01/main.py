#!/bin/python3

from math import floor


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


def solve():
    """
    Solve the puzzle, given the input in input.txt
    """
    input_list = read_input('input.txt')
    return sum(map(fuel_required, input_list))


if __name__ == '__main__':
    print(solve())
