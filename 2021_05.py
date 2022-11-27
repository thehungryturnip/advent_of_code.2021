#!/usr/bin/env python

import helpers
import re
from collections import namedtuple, defaultdict

Coord = namedtuple('Coord', ['x', 'y'])
Vent = namedtuple('Vent', ['start', 'end'])


class VentsMap(defaultdict):
    def __init__(self, *args):
        super().__init__(int)

    def add_vent(self, vent):
        dx = vent.end.x - vent.start.x
        dy = vent.end.y - vent.start.y
        length = max(abs(dx), abs(dy)) + 1

        if dx > 0:
            dx = 1
        elif dx < 0:
            dx = -1

        if dy > 0:
            dy = 1
        elif dy < 0:
            dy = -1

        x = vent.start.x
        y = vent.start.y
        for i in range(length):
            self[Coord(x, y)] += 1
            x += dx
            y += dy

    def count_overlap(self):
        return sum(v > 1 for v in map_.values())


data = helpers.get_input('2021_05')

vents = []
for r in data:
    r = re.split(',| -> ', r)
    start = Coord(int(r[0]), int(r[1]))
    end = Coord(int(r[2]), int(r[3]))
    vent = Vent(start, end)
    vents.append(vent)

map_ = VentsMap()
for v in vents:
    if v.start.x == v.end.x or v.start.y == v.end.y:
        map_.add_vent(v)

print(f'Part 1: {map_.count_overlap()}')

for v in vents:
    if v.start.x != v.end.x and v.start.y != v.end.y:
        map_.add_vent(v)

print(f'Part 2: {map_.count_overlap()}')
