#!/usr/bin/env python

import helpers

class Crabs(list):
    def add(self, position):
        self.append(position)

    def get_linear_min(self):
        self.sort()
        middle = len(self) // 2
        return sum(abs(p - self[middle]) for p in self)

    def get_geometric_min(self):
        self.sort()
        best = self._fuel_at(min(self))
        for p in range(min(self) + 1 , max(self) + 1):
            fuel = self._fuel_at(p)
            if fuel < best:
                best = fuel
        return best

    def _fuel_at(self, target):
        return sum(self._fuel_between(p, target) for p in self)

    @staticmethod
    def _fuel_between(x, y):
        return sum(i + 1 for i in range(abs(x - y)))

data = helpers.get_input('2021_07')

crabs = Crabs()
for d in data[0].split(','):
    crabs.add(int(d))

print(f'Part 1: {crabs.get_linear_min()}')
print(f'Part 2: {crabs.get_geometric_min()}')
