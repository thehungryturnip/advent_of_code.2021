#!/usr/bin/env python

import helpers

PART_1_DAYS = 80
PART_2_DAYS = 256


class SchoolOfFish(list):

    def __init__(self):
        for _ in range(9):
            self.append(0)

    def add_fish(self, clock=8):
        self[clock] += 1

    def age(self):
        new_count = self[0]
        for i in range(1, 9):
            self[i - 1] = self[i]
        self[6] += new_count
        self[8] = new_count

    def count_fish(self):
        return sum(self)


data = helpers.get_input('2021_06')

school = SchoolOfFish()
for d in data[0].split(','):
    school.add_fish(int(d))

for _ in range(PART_1_DAYS):
    school.age()

print(f'Part 1: {school.count_fish()}')

for _ in range(PART_2_DAYS - PART_1_DAYS):
    school.age()

print(f'Part 2: {school.count_fish()}')
