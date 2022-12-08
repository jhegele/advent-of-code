def get_trees(path):
    trees = {}
    with open(path, 'r') as f:
        for y, row in enumerate(f.readlines()):
            for x, val in enumerate(row.strip()):
                trees[(x, y)] = int(val)
    return trees

def get_visible_idxs_from_left(tree_row):
    """Every line of trees will be fed as a single list that we'll check from
    left-to-right. So, when we want to look from the right side or the bottom
    the list needs to be reversed before being passed in."""
    max_height = 0
    for i in range(0, len(tree_row)):
        if i == 0:
            max_height = tree_row[0]
            yield i
        else:
            height_diff = tree_row[i] - max_height
            if height_diff > 0:
                max_height = tree_row[i]
                yield i

def get_scenic_score(loc, trees):
    """Brute forced this which is pretty ugly and not very performant. Pass in a
    single tree location with the entire dict of trees. From the location passed
    we walk north, south, west, and east one step at a time until we hit a tree
    that is at least as large as the one we're on (loc)."""
    # Get values for eastern and southern edges
    max_x = max([loc[0] for loc in trees])
    max_y = max([loc[1] for loc in trees])
    # Initialize each direction as 1 to acknowledge that we can see the trees
    # immediately surrounding our position
    # [n, s, w, e]
    score = [1, 1, 1, 1]
    x, y = loc
    height = trees[loc]
    n_y, s_y = y - 1, y + 1
    w_x, e_x = x - 1, x + 1
    # Move north (up) until we hit a tree as large as our current loc or we
    # hit the edge (0)
    while n_y >= 0:
        score[0] = y - n_y
        if trees[(x, n_y)] >= height:
            break
        n_y -= 1
    # Move south (down) until we hit a tree as large as our current loc or we
    # hit the edge (max_y)
    while s_y <= max_y:
        score[1] = s_y - y
        if trees[(x, s_y)] >= height:
            break
        s_y += 1
    # Same as north but we're moving left (west)
    while w_x >= 0:
        score[2] = x - w_x
        if trees[(w_x, y)] >= height:
            break
        w_x -= 1
    # Same as south but we're moving right (east)
    while e_x <= max_x:
        score[3] = e_x - x
        if trees[(e_x, y)] >= height:
            break
        e_x += 1
    return score[0] * score[1] * score[2] * score[3]
    

def p1():
    trees = get_trees('input.txt')
    visible = []
    xs = list(set([loc[0] for loc in trees]))
    ys = list(set([loc[1] for loc in trees]))
    # col by col
    for y in ys:
        line = [trees[(y, loc_x)] for loc_x in range(min(xs), max(xs) + 1)]
        visible += [(x, y) for x in get_visible_idxs_from_left(line)]
        visible += [(max(xs) - x, y) for x in get_visible_idxs_from_left(line[::-1])]
    # row by row
    for x in xs:
        line = [trees[(loc_y, x)] for loc_y in range(min(ys), max(ys) + 1)]
        visible += [(x, y) for y in get_visible_idxs_from_left(line)]
        visible += [(x, max(ys) - y) for y in get_visible_idxs_from_left(line[::-1])]
    return len(set(visible))

def p2():
    trees = get_trees('input.txt')
    # Calculate positions for eastern and southern edges
    max_x = max([loc[0] for loc in trees])
    max_y = max([loc[1] for loc in trees])
    # Any tree that is on an edge will have a scenic score of 0 since, on
    # one side there are no trees at all. Get all tree locations that are
    # NOT on an edge.
    tree_locs = [l for l in trees if l[0] > 0 and l[0] < max_x and l[1] > 0 and l[1] < max_y]
    # Calculate a scenic score for each location and get the max
    scenic_scores = list(map(lambda loc: get_scenic_score(loc, trees), tree_locs))
    return max(scenic_scores)

# print('Part 1: ', p1())
print('Part 2: ', p2())