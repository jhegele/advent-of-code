from collections import deque

def get_file(path):
    with open(path, 'r') as f:
        return list(map(int, f.readlines()))

def p2():
    key = 811589153
    file_orig = enumerate(map(lambda x: x * key, get_file('input.txt')))
    file = deque([*file_orig])
    for _ in range(10):
        for idx in range(len(file)):
            while file[0][0] != idx:
                file.rotate()
            orig_idx, mv = file.popleft()
            file.rotate(-mv)
            file.appendleft((orig_idx, mv))
    while file[0][1] != 0:
        file.rotate()
    coords = 0
    file.rotate(-1000)
    coords += file[0][1]
    file.rotate(-1000)
    coords += file[0][1]
    file.rotate(-1000)
    coords += file[0][1]
    return coords


def p1():
    file = deque(enumerate(get_file('input.txt')))
    for idx in range(len(file)):
        while file[0][0] != idx:
            file.rotate()
        orig_idx, mv = file.popleft()
        file.rotate(-mv)
        file.appendleft((orig_idx, mv))
    while file[0][1] != 0:
        file.rotate()
    coords = 0
    file.rotate(-1000)
    coords += file[0][1]
    file.rotate(-1000)
    coords += file[0][1]
    file.rotate(-1000)
    coords += file[0][1]
    return coords

# print('Part 1: ', p1())
print('Part 2: ', p2())