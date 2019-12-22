#!/usr/bin/env python3

import sys
import io
from itertools import permutations
from enum import Enum
from os.path import dirname
from os.path import join


SIZE = 5


def read_input(file_name='input.txt'):
    """
    Read input from file_name
    """
    # always open relative to current file
    file_name = join(dirname(__file__), file_name)
    with open(file_name, 'r') as f_in:
        return list(map(int, f_in.read().split(',')))


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


class VM:
    def __init__(self, stdin=sys.stdin, stdout=sys.stdout,
                 program=None, print_to_stdout=False):
        self.stdin = stdin
        self.stdout = stdout
        self.input = []
        self.output = []
        self.print_to_stdout = print_to_stdout
        self.print_to_stdout |= (stdout != sys.__stdout__)
        self.mem = None
        self.pc = 0
        if program is not None:
            self.load(program)
        self.halted = False

    def load(self, program):
        self.mem = program

    def dereference(self, val, mode=1):
        """
        Dereference a value given the parameter mode
        """
        if mode == 0:
            return self.mem[self.mem[val]]
        if mode == 1:
            return self.mem[val]
        raise RuntimeError("Unknown parameter mode %d" % (mode))

    def new_input(self, val):
        self.input.insert(0, val)

    def get_output(self):
        length = len(self.output)
        while length == len(self.output) and not self.halted:
            self.step()
        return None if self.halted else int(self.output[-1])

    def run(self):
        while not self.halted:
            self.step()

    def step(self):
        """
        Run the intcode program
        """
        if self.pc >= len(self.mem) and not self.halted:
            raise RuntimeError("End of Program and no HLT found")
        if self.halted:
            raise RuntimeError("Program already halted")
        p_mode = None
        opcode = None
        raw_opcode = str(self.mem[self.pc]).zfill(5)
        if int(raw_opcode) > 99:
            p_mode = [int(x) for x in raw_opcode[:-2]]
            opcode = OpCodes(int(raw_opcode[-2:]))
        else:
            p_mode = [0 for _ in range(3)]
            opcode = OpCodes(self.mem[self.pc])

        # 0 parameter
        if opcode == OpCodes.HLT:
            self.halted = True
            return

        # 1 parameter
        cont = False
        op1 = self.dereference(self.pc + 1, mode=p_mode[2])
        dst = self.mem[self.pc + 1]

        if opcode == OpCodes.READ:
            cont = True
            if len(self.input):
                self.mem[dst] = self.input.pop()
            else:
                self.mem[dst] = int(self.stdin.readline().strip())
        if opcode == OpCodes.PRNT:
            cont = True
            self.output.append('%s\n' % op1)
            if self.stdout is not None:
                if self.print_to_stdout and self.stdout == sys.__stdout__:
                    print(op1, flush=True)
                elif self.stdout != sys.__stdout__:
                    print(op1, file=self.stdout, flush=True)

        if cont:
            self.pc += 2
            return

        # 2 parameter
        op2 = self.dereference(self.pc + 2, mode=p_mode[1])
        if opcode == OpCodes.JMPT:
            cont = True
            if op1 != 0:
                self.pc = op2
                return
        if opcode == OpCodes.JMPF:
            cont = True
            if op1 == 0:
                self.pc = op2
                return
        if cont:
            self.pc += 3
            return

        # 3 parameter
        dst = self.mem[self.pc + 3]
        func = None

        if opcode == OpCodes.ADD:
            func = lambda x, y: x + y
        if opcode == OpCodes.MUL:
            func = lambda x, y: x * y
        if opcode == OpCodes.LT:
            func = lambda x, y: 1 if x < y else 0
        if opcode == OpCodes.EQ:
            func = lambda x, y: 1 if x == y else 0

        self.mem[dst] = func(op1, op2)
        self.pc += 4


def run_sequence(program, seq):
    """
    Run a specific sequence
    """
    signal = 0
    for phase in seq:
        stdin = io.StringIO('\n'.join([str(e) for e in [phase, signal]]))
        vm = VM(stdin=stdin, program=program)
        vm.run()
        signal = int(vm.output[0].strip())
    return signal


def run_parallel(program, seq):
    vms = [VM(program=program) for idx in range(SIZE)]
    for phase, vm in zip(seq, vms):
        vm.new_input(phase)

    prev = 0
    while all(not vm.halted for vm in vms):
        for vm in vms:
            vm.new_input(prev)
            if not vm.halted:
                output = vm.get_output()
                if output is not None:
                    prev = output
    return prev


def part1():
    """
    Solve the puzzle (part 1), given the input in input.txt
    """
    phase_settings = list(permutations(range(SIZE)))
    return max([run_sequence(read_input('input.txt'), setting)
                for setting in phase_settings])


def part2():
    """
    Solve the puzzle (part 2), given the input in input.txt
    """
    phase_settings = list(permutations(range(SIZE, SIZE * 2)))
    return max([run_parallel(read_input('input.txt'), setting)
                for setting in phase_settings])


if __name__ == '__main__':
    print("Part 1:", part1())
    print("Part 2:", part2())
