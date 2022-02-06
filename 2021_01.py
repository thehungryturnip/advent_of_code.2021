#!/usr/bin/env python

import helpers

depths = helpers.get_input('2021_01')
depths = [int(d) for d in depths]

count = 0
prev = depths[0]
for d in depths[1:]:
    if d > prev:
        count += 1
    prev = d

print(f'Part 1: {count}')

count = 0
prev = sum(depths[:3])
for i in range(len(depths) - 3):
    curr = prev - depths[i] + depths[i + 3]
    if curr > prev:
        count += 1
    prev = curr

print(f'Part 2: {count}')
