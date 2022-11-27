#!/usr/bin/env python

from collections import deque
from functools import reduce
from helpers import get_input, Point, RectMap


class DepthMap(RectMap):

    def __init__(self, data):
        super().__init__(data)

    def __repr__(self):
        return super().__repr__()

    def sum_low_points(self):
        low_points = list(filter(lambda p: self._is_low_point(p), self))
        return sum([self[p] + 1 for p in low_points])

    def multiply_basin_sizes(self):
        low_points = list(filter(lambda p: self._is_low_point(p), self))
        basin_sizes = sorted(map(lambda p: self._basin_size(p), low_points))
        biggest_3 = basin_sizes[-3:]
        return reduce(lambda x, y: x * y, biggest_3)

    def _is_low_point(self, point):
        neighbors = self.get_neighbors(point)
        higher = [self[neighbor] > self[point] for neighbor in neighbors]
        return all(higher)

    def _basin_size(self, point):
        basin_points = {point}
        to_check = deque([point])

        while (to_check):
            p = to_check.pop()
            neighbors = self.get_neighbors(p)

            for n in neighbors:
                if (self[n] == 9):
                    continue
                if (n not in basin_points):
                    to_check.append(n)
                    basin_points.add(n)

        return len(basin_points)


data = get_input('2021_09')
map_ = DepthMap(data)

print(f'Pant 1: Risk level is {map_.sum_low_points()}')
print(f'Part 2: Multiplied basin size is {map_.multiply_basin_sizes()}')
