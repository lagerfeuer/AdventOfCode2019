#!/usr/bin/env python3

import io
from enum import Enum
from os.path import dirname
from os.path import join


class OpCodes(Enum):
    ADD = 1
    MUL = 2
    READ = 3
    PRNT = 4
    JMPT = 5  # jump if true
    JMPF = 6  # jump if false
    LT = 7  # less than
    EQ = 8  # equals
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


def dereference(mem, val, mode=1):
    """
    Dereference a value given the parameter mode
    """
    if mode == 0:
        return mem[mem[val]]
    if mode == 1:
        return mem[val]
    raise RuntimeError("Unknown parameter mode %d" % (mode))


def run(program_in, stdin=None, print_to_stdout=True):
    """
    Run the intcode program
    """
    stdout = []
    program = program_in.copy()
    pc = 0
    while pc < len(program):
        p_mode = None
        opcode = None
        raw_opcode = str(program[pc]).zfill(5)
        if int(raw_opcode) > 99:
            p_mode = [int(x) for x in raw_opcode[:-2]]
            opcode = OpCodes(int(raw_opcode[-2:]))
        else:
            p_mode = [0 for _ in range(3)]
            opcode = OpCodes(program[pc])

        # 0 parameter
        if opcode == OpCodes.HLT:
            return program, stdout

        # 1 parameter
        cont = False
        op1 = dereference(program, pc + 1, mode=p_mode[2])
        dst = program[pc + 1]

        if opcode == OpCodes.READ:
            cont = True
            if stdin is None:
                program[dst] = int(input())
            else:
                program[dst] = int(stdin.readline().strip())
        if opcode == OpCodes.PRNT:
            cont = True
            stdout.append("%s\n" % op1)
            if print_to_stdout:
                print(op1)

        if cont:
            pc += 2
            continue

        # 2 parameter
        op2 = dereference(program, pc + 2, mode=p_mode[1])
        if opcode == OpCodes.JMPT:
            cont = True
            if op1 != 0:
                pc = op2
                continue
        if opcode == OpCodes.JMPF:
            cont = True
            if op1 == 0:
                pc = op2
                continue
        if cont:
            pc += 3
            continue

        # 3 parameter
        dst = program[pc + 3]
        func = None

        if opcode == OpCodes.ADD:
            func = lambda x, y: x + y
        if opcode == OpCodes.MUL:
            func = lambda x, y: x * y
        if opcode == OpCodes.LT:
            func = lambda x, y: 1 if x < y else 0
        if opcode == OpCodes.EQ:
            func = lambda x, y: 1 if x == y else 0

        program[dst] = func(op1, op2)
        pc += 4

    return program, stdout


def part1():
    """
    Solve the puzzle (part 1), given the input in input.txt
    """
    program = read_input('input.txt')
    stdin = io.StringIO('1')
    program, out = run(program, stdin=stdin, print_to_stdout=False)
    return out


def part2():
    """
    Solve the puzzle (part 2), given the input in input.txt
    """
    program = read_input('input.txt')
    stdin = io.StringIO('5')
    program, out = run(program, stdin=stdin, print_to_stdout=False)
    return out


if __name__ == '__main__':
    print("Part 1:", part1()[-1].strip())
    print("Part 2:", part2()[-1].strip())
