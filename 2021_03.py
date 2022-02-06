#!/usr/bin/env python

import helpers

def filter_position(candidates, index, filter_by_more):
    delta = 0
    for c in candidates:
        delta += 1 if c[index] == '1' else -1

    more = '1'
    less = '0'
    if delta < 0:
        more, less = less, more

    target = more
    if not filter_by_more:
        target = less

    return [c for c in candidates if c[index] == target]

def filter(candidates, more):
    for i in range(len(candidates[0])):
        candidates = filter_position(candidates, i, more)
        if len(candidates) == 1:
            return candidates[0]

report = helpers.get_input('2021_03')

ones = [0] * len(report[0])

for entry in report:
    for i, b in enumerate(entry):
        ones[i] += 1 if b == '1' else -1

gamma = ''
epsilon = ''
for delta in ones:
    gamma += '1' if delta > 0 else '0'
    epsilon += '1' if delta < 0 else '0'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(f'Part 1: {gamma * epsilon}')

o2 = filter(report[:], True)
o2 = int(o2, 2)

co2 = filter(report[:], False)
co2 = int(co2, 2)

print(f'Part 2: {o2 * co2}')
