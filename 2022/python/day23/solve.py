def get_elves(path):
    elves = []
    with open(path, 'r') as f:
        for y, line in enumerate(f.readlines()):
            for x, char in enumerate(line):
                if char == '#':
                    elves.append((x, y,))
    return elves

checks = {
    'N': lambda x, y: ((x-1, y-1,), (x, y-1,), (x+1, y-1,)),
    'S': lambda x, y: ((x-1, y+1,), (x, y+1,), (x+1, y+1,)),
    'W': lambda x, y: ((x-1, y-1,), (x-1, y,), (x-1, y+1,)),
    'E': lambda x, y: ((x+1, y-1,), (x+1, y,), (x+1, y+1,))
}

def p1():
    elves = get_elves('test.txt')
    directions = 'NSWE'
    round = 0
    while round < 10:
        proposals = []
        for elf in elves:
            
