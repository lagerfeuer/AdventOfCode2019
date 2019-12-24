#!/usr/bin/env python3

from os.path import dirname
from os.path import join
from collections import Counter


class Layer:
    def __init__(self, data, dimension):
        self.data = list(map(int, data))
        self.width, self.height = dimension

    def dump(self):
        return [self.data[i:i+self.width]
                for i in range(0, len(self.data), self.width)]

    def stream(self):
        return self.data


def read_input(file_name='input.txt'):
    # always open relative to current file
    file_name = join(dirname(__file__), file_name)
    with open(file_name, 'r') as f_in:
        return list(f_in.read().strip())


def chunkify(data, chunk_size):
    length = len(data)
    return [data[i:i+chunk_size] for i in range(0, length, chunk_size)]


def parse(data, dimension):
    width, height = dimension
    frame_size = width * height
    return [Layer(frame, dimension)
            for frame in chunkify(data, frame_size)]


def overlay(layers):
    layers = layers[::-1]
    data = layers[0].stream()
    for layer in layers[1:]:
        data = [new if new != 2 else old
                for old, new in zip(data, layer.stream())]
    return data


def part1():
    layers = parse(read_input(), (25, 6))
    layer = min(layers, key=lambda x: x.stream().count(0))
    cnt = Counter(layer.stream())
    return cnt[1] * cnt[2]


def part2():
    layers = parse(read_input(), (25, 6))
    data = overlay(layers)
    visual = [{0: ' ', 1: '#'}[e] for e in data]
    return '\n'.join(chunkify(''.join(visual), 25))


if __name__ == '__main__':
    print("Part 1:", part1())
    print("Part 2:\n")
    print(part2())
