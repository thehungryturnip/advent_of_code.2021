from collections import namedtuple


def get_input(file, ex=False):
    if ex:
        file = f'{file}_ex'
    filepath = f'inputs/{file}.txt'

    with open(filepath, 'r') as f:
        output = []
        for line in f.read().splitlines():
            if len(line) > 1 and line[0] == '#':
                return output
            output.append(line)
        return output


Point = namedtuple("Point", "r c")


class RectMap(dict):

    def __init__(self, data):
        self.height = len(data)
        self.width = len(data[0])
        for r, row in enumerate(data):
            for c, v in enumerate(row):
                self[Point(r, c)] = int(v)

    def __repr__(self):
        return "\n".join([
            "".join([str(self[Point(r, c)]) for c in range(self.width)])
            for r
            in range(self.height)
        ])

    def get_neighbors(self, p):
        neighbors = [
            Point(p.r - 1, p.c),
            Point(p.r + 1, p.c),
            Point(p.r, p.c - 1),
            Point(p.r, p.c + 1),
        ]

        return list(filter(lambda p: not self.out_of_bounds(p), neighbors))

    def out_of_bounds(self, p):
        if p.r < 0 or p.c < 0:
            return True
        if p.r >= self.height:
            return True
        if p.c >= self.width:
            return True
        return False
