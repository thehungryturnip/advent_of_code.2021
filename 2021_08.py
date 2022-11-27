#!/usr/bin/env python

import helpers
import re
from queue import Queue


class Entry:
    LEN_1478 = set([2, 3, 4, 7])

    def __init__(self, samples, message):
        self.samples = [set(s) for s in samples]
        self.message = [set(m) for m in message]
        self.decoded = {}

    def count_1478(self):
        return sum(len(m) in Entry.LEN_1478 for m in self.message)

    def decode(self):
        self._analyze_samples()
        num = 0
        for m in self.message:
            num *= 10
            for i in range(10):
                if m == self.decoded[i]:
                    num += i

        return num

    def _analyze_samples(self):
        len_5 = []
        len_6 = []
        for s in self.samples:
            match len(s):
                case 2:
                    self.decoded[1] = s
                case 4:
                    self.decoded[4] = s
                case 3:
                    self.decoded[7] = s
                case 7:
                    self.decoded[8] = s
                case 5:
                    len_5.append(s)
                case 6:
                    len_6.append(s)
        # 1 -> 3
        for i, s in enumerate(len_5):
            if self.decoded[1].issubset(s):
                self.decoded[3] = s
                del len_5[i]
                break

        # 3 -> 9
        for i, s in enumerate(len_6):
            if self.decoded[3].issubset(s):
                self.decoded[9] = s
                del len_6[i]
                break

        # 9 -> 5, 2
        for i, s in enumerate(len_5):
            if s.issubset(self.decoded[9]):
                self.decoded[5] = s
                del len_5[i]
                self.decoded[2] = len_5[0]

        # 5 -> 6
        for i, s in enumerate(len_6):
            if self.decoded[5].issubset(s):
                self.decoded[6] = s
                del len_6[i]
                self.decoded[0] = len_6[0]


class Decoder(list):
    def add(self, samples, message):
        self.append(Entry(samples, message))

    def count_1478(self):
        return sum(e.count_1478() for e in self)

    def sum(self):
        return sum(e.decode() for e in self)


data = helpers.get_input('2021_08')

decoder = Decoder()
for d in data:
    d = re.split(' \\| | ', d)
    decoder.add(d[:10], d[-4:])

print(f'Part 1: {decoder.count_1478()}')
print(f'Part 2: {decoder.sum()}')
