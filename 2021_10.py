#!/usr/bin/env python

from collections import deque
from helpers import get_input


class NavSys(list):
    brackets = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }

    close = {")", "]", "}", ">"}

    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    def __init__(self, data):
        super().__init__(data)

    def __repr__(self):
        return '\n'.join(self)

    def sum_syntax_error_score(self):
        return sum([NavSys._calc_syntax_error_score(e) for e in self])

    @classmethod
    def _calc_syntax_error_score(cls, entry):
        tracker = deque([])

        for c in entry:
            if c in cls.brackets:
                tracker.append(cls.brackets[c])
            elif c in cls.close:
                if not c == tracker.pop():
                    return cls.points[c]

        return 0


data = get_input('2021_10', False)
sys = NavSys(data)

print(
    f'Pant 1: The total syntax error score is {sys.sum_syntax_error_score()}')
