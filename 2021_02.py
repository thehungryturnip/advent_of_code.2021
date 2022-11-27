#!/usr/bin/env python

import helpers

course = helpers.get_input('2021_02')
course = [l.split(' ') for l in course]

pos = 0
depth = 0

for c in course:
    cmd = c[0]
    amt = int(c[1])
    match cmd:
        case 'forward':
            pos += amt
        case 'down':
            depth += amt
        case 'up':
            depth -= amt

print(f'Part 1: {pos * depth}')

pos = 0
depth = 0
aim = 0

for c in course:
    cmd = c[0]
    amt = int(c[1])
    match cmd:
        case 'forward':
            pos += amt
            depth += aim * amt
        case 'down':
            aim += amt
        case 'up':
            aim -= amt

print(f'Part 2: {pos * depth}')
