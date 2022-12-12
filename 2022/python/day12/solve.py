from collections import deque
from string import ascii_lowercase

alpha = ascii_lowercase

def get_map(path):
    with open(path, 'r') as f:
        return [l.strip() for l in f.readlines()]

def get_height_num(height_char):
    """Per the problem, the starting point (S) is at height a and
    the ending point (E) is at height z. We use the list of all
    lowercase letters and their respective indices to calculate
    height values."""
    if height_char == 'S':
        return alpha.index('a')
    if height_char == 'E':
        return alpha.index('z')
    return alpha.index(height_char)

def bfs(height_map, start, part=1):
    """Breadth-first search. For this implementation, we start at
    node S and add each surrounding node to the queue, then we
    explore each surrounding node until we find node E. We use a
    dictionary (searched) where the value of a key is the node
    that led to that key. So, when we find node E, we just work
    backward through our searched dict to find the path length."""
    # u, d, l, r
    moves = [(0, -1,), (0, 1,), (-1, 0,), (1, 0,)]
    max_y = len(height_map) - 1
    max_x = len(height_map[0]) - 1
    queue = deque()
    # Each item in the queue has the form (location, previous_location)
    queue.append((start, None,))
    searched = {}
    while queue:
        # Grab the first item in our queue
        loc, prev = queue.popleft()
        x, y = loc
        # If we've already searched this location, ignore it
        if loc not in searched:
            # Add the location to our searched dictionary
            searched[loc] = prev
            # If this is the end node (E), we're done, just build the
            # path and return it
            if height_map[y][x] == "E":
                path = []
                while loc is not None:
                    path.append(loc)
                    loc = searched[loc]
                return path
            # If this is not the end node, we need to add any new nodes
            # that are neighbors to our queue
            else:
                neighbors = []
                for m_x, m_y in moves:
                    new_x, new_y = x + m_x, y + m_y
                    # Make sure that we only add valid nodes that are 
                    # not the previous node
                    if not 0 <= new_x <= max_x:
                        continue
                    if not 0 <= new_y <= max_y:
                        continue
                    if (new_x, new_y) == prev:
                        continue
                    # For part 2, if we've arrived at another potential starting
                    # point, we know this isn't the shortest path
                    if part == 2:
                        if height_map[new_y][new_x] in ['S', 'a']:
                            continue
                    ch = get_height_num(height_map[y][x]) 
                    mh = get_height_num(height_map[new_y][new_x])
                    # We can only climb up by one but we can go down any amount
                    if mh - ch <= 1:
                        neighbors.append(((new_x, new_y,), loc))
                queue += neighbors

def p1():
    m = get_map("input.txt")
    start = None
    # Find the starting node (S)
    for idx, row in enumerate(m):
        if 'S' in row:
            start = (row.index('S'), idx)
            break
    path = bfs(m, start)
    # We deduct one because our path contains the starting node and ending node
    # so the steps from start to end would be the number of nodes minus one.
    return len(path) - 1

def p2():
    m = get_map("input.txt")
    starts = []
    max_y = len(m) - 1
    max_x = len(m[0]) - 1
    # For part 2, we need to find all potential starting points (any 
    # node that is an 'a' and the original 'S')
    for y, row in enumerate(m):
        for x, height in enumerate(row):
            if height in ['a', 'S']:
                moves = [(0, -1,), (0, 1,), (-1, 0,), (1, 0,)]
                for m_x, m_y in moves:
                    new_x, new_y = x + m_x, y + m_y
                    if not 0 <= new_x <= max_x:
                        continue
                    if not 0 <= new_y <= max_y:
                        continue
                    # A valid starting node also needs at least one adjacent
                    # node that can be reached -- since we are starting at
                    # height a, at least one adjacent node must be an a, b,
                    # or S.
                    if m[new_y][new_x] in ['b', 'a', 'S']:
                        starts.append((x, y,))
                        break
    path_lengths = []
    for start in starts:
        path = bfs(m, start, 2)
        if path is not None:
            path_lengths.append(len(path) - 1)
    return min(path_lengths)

print('Part 1: ', p1())
print('Part 2: ', p2())