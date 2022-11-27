#!/usr/bin/env python

import helpers


class Board(list):

    def __init__(self, board):
        self._vals = {}
        for r, row in enumerate(board):
            self.append(row)
            for c, val in enumerate(row):
                self._vals[val] = (r, c)

    def mark(self, val):
        if val in self._vals:
            r, c = self._vals[val]
            self[r][c] = 'x'

    def done(self):
        for row in self:
            if all(v == 'x' for v in row):
                return True
        for c in range(len(self)):
            if all(self[r][c] == 'x' for r in range(len(self))):
                return True
        return False

    def sum_unmarked(self):
        return sum(int(v) for row in self for v in row if v != 'x')

    def __str__(self):
        str_ = ""
        for row in self:
            str_ += '\n'
            str_ += ' '.join(row)
        return str_

    def __repr__(self):
        return self.__str__()


class Game:

    def __init__(self, nums):
        self.nums = nums
        self.boards = []

    def play(self, to_win):
        for n in self.nums:
            for b in self.boards:
                b.mark(n)

            for i, b in enumerate(self.boards):
                if b.done():
                    if to_win:
                        return int(n) * b.sum_unmarked()
                    else:
                        if len(self.boards) == 1:
                            return int(n) * b.sum_unmarked()
                        else:
                            del self.boards[i]


data = helpers.get_input('2021_04')

game = Game(data[0].split(','))

for r in range(2, len(data), 6):
    board = Board([row.split() for row in data[r:r + 5]])
    game.boards.append(board)

print(f'Part 1: {game.play(to_win = True)}')
print(f'Part 2: {game.play(to_win = False)}')
