from collections import deque

def get_map(path):
    with open(path, 'r') as f:
        return [l.strip() for l in  f.readlines()]

def blizzard_pos_at_min(minute, char, start_pos, mod_x, mod_y):
    x, y = start_pos
    if char == '<':
        x = x - minute % mod_x
    if char == '>':
        x = x + minute % mod_x
    if char == '^':
        y = y - minute % mod_y
    if char == 'v':
        y = y + minute % mod_y
    return x, y


def p1():
    m = get_map('test.txt')
    mod_y = len(m) - 2
    mod_x = len(m[0]) - 2
    pos_start = m[1].index('.') - 1, 0
    pos_end = m[-1].index('.'), len(m) - 1
    blizzards = []
    for y, row in enumerate(m):
        if y == 0 or y == len(m) - 1:
            continue
        for x, char in enumerate(row):
            if x == 0 or x == len(row) - 1:
                continue
            if char != '.':
                blizzards.append((char, (x - 1, y - 1,)))
    print(blizzards)
    blizz_pos = map(lambda b: blizzard_pos_at_min(13, b[0], b[1], mod_x, mod_y), [*blizzards])
    print(list(blizz_pos))
    queue = deque([(0, pos_start)])
    minute, curr_x, curr_y = None, None, None
    while queue:
        minute, curr_pos = queue.popleft()
        curr_x, curr_y = curr_pos
        if (curr_x + 1, curr_y + 1) == pos_end:
            break
        if not (0 <= curr_x <= mod_x):
            continue
        if not (0 <= curr_y <= mod_y):
            continue
        blizz_pos = map(lambda b: blizzard_pos_at_min(minute + 1, b[0], b[1], mod_x, mod_y), [*blizzards])
        moves = [
            (curr_x + 1, curr_y),
            (curr_x - 1, curr_y),
            (curr_x, curr_y + 1),
            (curr_x, curr_y - 1)
        ]
        queue.extend([(minute + 1, p) for p in moves if p not in blizz_pos])
    print(minute, curr_x, curr_y)

p1()