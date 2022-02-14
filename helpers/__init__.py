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
