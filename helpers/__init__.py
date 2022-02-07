def get_input(day):
    with open(f'inputs/{day}.txt', 'r') as f:
        output = []
        for line in f.read().splitlines():
            if len(line) > 1 and line[0] == '#':
                return output
            output.append(line)
        return output
