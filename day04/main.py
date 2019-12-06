#!/usr/bin/env python3

from collections import Counter

global START
global END
START, END = list(map(int, "136760-595730".split('-')))
END += 1


def check1(pw):
    """
    - It is a six-digit number.
    - The value is within the range given in your puzzle input.
    - Two adjacent digits are the same (like 22 in 122345).
    - Going from left to right, the digits never decrease;
      they only ever increase or stay the same (like 111123 or 135679).
    """
    pw = list(str(pw))
    return (len(set(pw)) < len(pw)) and (sorted(pw) == pw)


def check2(pw):
    pw = list(str(pw))
    return (sorted(pw) == pw) and (2 in Counter(pw).values())


def part1():
    """
    Solve the puzzle (part 1)
    """
    return sum(check1(pw) for pw in range(START, END))


def part2():
    """
    Solve the puzzle (part 2)
    """
    return sum(check2(pw) for pw in range(START, END))


if __name__ == '__main__':
    print("Part 1:", part1())
    print("Part 2:", part2())
