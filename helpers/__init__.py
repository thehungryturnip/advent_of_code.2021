def get_input(day):
    with open(f'inputs/{day}.txt', 'r') as f:
        output = []
        for line in f.read().splitlines():
            if line[0] == '#':
                return output
            output.append(line)
        return output
