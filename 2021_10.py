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

    syntax_error_points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    autocomplete_points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    def __init__(self, data):
        super().__init__(data)

    def __repr__(self):
        return '\n'.join(self)

    def sum_syntax_error_score(self):
        return sum([NavSys._calc_syntax_error_score(e) for e in self])

    def calc_middle_autocomplete_score(self):
        all_scores = [NavSys._calc_autocomplete_score(e) for e in self]
        autocomplete_scores = sorted([s for s in all_scores if not s == 0])
        return autocomplete_scores[len(autocomplete_scores) // 2]

    @classmethod
    def _calc_syntax_error_score(cls, entry):
        tracker = deque([])

        for c in entry:
            if c in cls.brackets:
                tracker.append(cls.brackets[c])
            elif c in cls.close:
                if not c == tracker.pop():
                    return cls.syntax_error_points[c]

        return 0

    @classmethod
    def _calc_autocomplete_score(cls, entry):
        tracker = deque([])

        for c in entry:
            if c in cls.brackets:
                tracker.append(cls.brackets[c])
            elif c in cls.close:
                if not c == tracker[-1]:
                    return 0
                else:
                    tracker.pop()

        score = 0
        while tracker:
            score = score * 5
            c = tracker.pop()
            score = score + cls.autocomplete_points[c]

        return score


data = get_input('2021_10')
sys = NavSys(data)

print(
    f'Part 1: The total syntax error score is {sys.sum_syntax_error_score()}')
print(
    f'Part 2: The middle autocomplete score is {sys.calc_middle_autocomplete_score()}')
