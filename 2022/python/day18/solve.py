def get_droplets(path):
    with open(path, 'r') as f:
        return set(tuple(map(int, d.strip().split(','))) for d in f.readlines())

def is_external(loc, droplets):
    x, y, z = loc
    cx_a = sum([1 for dx, dy, dz in droplets if x < dx < x + 1000 and y == y and z == z])
    cx_b = sum([1 for dx, dy, dz in droplets if x > dx > x - 1000 and y == y and z == z])
    if (cx_a >= 1 and cx_b == 0):
        return True
    if (cx_b >= 1 and cx_a == 0):
        return True
    cy_a = sum([1 for dx, dy, dz in droplets if x == x and y < dy < y + 1000 and z == z])
    cy_b = sum([1 for dx, dy, dz in droplets if x == x and y > dy > y - 1000 and z == z])
    if (cy_a >= 1 and cy_b == 0):
        return True
    if (cy_b >= 1 and cy_a == 0):
        return True
    cz_a = sum([1 for dx, dy, dz in droplets if x == x and y == y and z < dz < z + 1000])
    cz_b = sum([1 for dx, dy, dz in droplets if x == x and y == y and z > dz > z - 1000])
    if (cz_a >= 1 and cz_b == 0):
        return True
    if (cz_b >= 1 and cz_a == 0):
        return True
    return False

def is_air_pocket(loc, droplets):
    x, y, z = loc
    if loc in droplets:
        return False
    possible_connected = set([
        (x-1, y, z),
        (x+1, y, z),
        (x, y-1, z),
        (x, y+1, z),
        (x, y, z-1),
        (x, y, z+1)
    ])
    connected = sum([1 for d in droplets if d in possible_connected])
    return connected == 6

def p1():
    droplets = get_droplets('input.txt')
    exposed_sides = 0
    for x, y, z in droplets:
        possible_connected = set([
            (x-1, y, z),
            (x+1, y, z),
            (x, y-1, z),
            (x, y+1, z),
            (x, y, z-1),
            (x, y, z+1)
        ])
        connected = sum([1 for d in droplets if d in possible_connected])
        exposed_sides += 6 - connected
    return exposed_sides

def p2():
    droplets = get_droplets('input.txt')
    exposed_sides = 0
    # air_pockets = 0
    # air_pockets_checked = set()
    for x, y, z in droplets:
        if is_external((x, y, z,), droplets):
            possible_connected = set([
                (x-1, y, z),
                (x+1, y, z),
                (x, y-1, z),
                (x, y+1, z),
                (x, y, z-1),
                (x, y, z+1)
            ])
            connected = sum([1 for d in droplets if d in possible_connected])
            exposed_sides += 6 - connected
        # air_pockets += sum([1 for p in possible_connected if p not in air_pockets_checked and is_air_pocket(p, droplets)])
        # air_pockets_checked.update(possible_connected)
    # return exposed_sides - (6 * air_pockets)
    return exposed_sides



# print('Part 1: ', p1())
print('Part 2: ', p2())