from collections import deque
from string import ascii_lowercase

alpha = ascii_lowercase

def get_map(path):
    with open(path, 'r') as f:
        return [l.strip() for l in f.readlines()]

def bfs(height_map, start):
    # u, d, l, r
    moves = [(0, -1,), (0, 1,), (-1, 0,), (1, 0,)]
    max_y = len(height_map) - 1
    max_x = len(height_map[0]) - 1
    queue = deque()
    queue.append((start, None,))
    searched = {}
    while queue:
        loc, prev = queue.popleft()
        x, y = loc
        if loc not in searched:
            searched[loc] = prev
            if height_map[y][x] == "E":
                path = []
                while loc is not None:
                    path.append(loc)
                    loc = searched[loc]
                return path
            else:
                neighbors = []
                for m_x, m_y in moves:
                    if not 0 <= m_x <= max_x:
                        continue
                    if not 0 <= m_y <= max_y:
                        continue
                    ch = alpha.index(height_map[y][x])
                    mh = alpha.index(height_map[m_y][m_x])
                    if abs(mh - ch) <= 1:
                        neighbors.append(((m_x, m_y,), loc))
                queue += neighbors

def p1():
    m = get_map("test.txt")
    start = None
    for idx, row in enumerate(m):
        if 'S' in row:
            start = (row.index('S'), idx)
            break
    path = bfs(m, start)
    print(len(path))

p1()