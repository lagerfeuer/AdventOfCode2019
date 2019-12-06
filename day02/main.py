#!/usr/bin/env python3

import sys
from enum import Enum
from os.path import dirname
from os.path import join


class OpCodes(Enum):
    ADD = 1
    MUL = 2
    HLT = 99


def read_input(file_name):
    """
    Read input from file_name
    """
    input_list = []
    # always open relative to current file
    file_name = join(dirname(__file__), file_name)
    with open(file_name, 'r') as f_in:
        input_list = f_in.read().split(',')
    return list(map(int, input_list))


def run(program_in):
    """
    An Intcode program is a list of integers separated
    by commas (like 1,0,0,3,99).
    To run one, start by looking at the first integer (called position 0).
    Here, you will find an opcode - either 1, 2, or 99.
    The opcode indicates what to do; for example,
    99 means that the program is finished and should immediately halt.
    Encountering an unknown opcode means something went wrong.
    """
    program = program_in.copy()
    pc = 0
    while pc < len(program):
        opcode = OpCodes(program[pc])

        if opcode == OpCodes.HLT:
            return program

        op1 = program[program[pc + 1]]
        op2 = program[program[pc + 2]]
        dst = program[pc + 3]
        func = None

        if opcode == OpCodes.ADD:
            func = lambda x, y: x + y
        if opcode == OpCodes.MUL:
            func = lambda x, y: x * y

        program[dst] = func(op1, op2)
        pc += 4

    raise RuntimeError("Invalid opcode")


def part1():
    """
    Solve the puzzle (part 1), given the input in input.txt
    ...before running the program,
    replace position 1 with the value 12 and
    replace position 2 with the value 2.
    """
    program = read_input('input.txt')
    program[1] = 12
    program[2] = 2
    return run(program)[0]


def part2():
    """
    Solve the puzzle (part 2), given the input in input.txt
    """
    program_in = read_input('input.txt')
    OUTPUT = 19690720
    for i in range(100):
        for j in range(100):
            program = program_in.copy()
            program[1] = i
            program[2] = j
            if run(program)[0] == OUTPUT:
                return 100 * i + j


if __name__ == '__main__':
    print("Part 1:", part1())
    print("Part 2:", part2())
