#!/usr/bin/env python

import sys

with open('../inputs/2021_01.txt', 'r') as f:
    depths = [int(l) for l in f.readlines()]

increased = 0
previous = depths[0]
for d in depths[1:]:
    if d > previous:
        increased += 1
    previous = d

print(f'[2021_01a] There are {increased} number of depth increases.')

increased = 0
previous = sum(depths[:3])
for i in range(len(depths) - 3):
    current = previous - depths[i] + depths[i + 3]
    if current > previous:
        increased += 1
    previous = current

print(f'[2021-01b] There are {increased} number of depth increases.')
