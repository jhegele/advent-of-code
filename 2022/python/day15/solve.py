def get_sensors_beacons(path):
    with open(path, 'r') as f:
        for line in f.readlines():
            sr, br = line.strip().split(': closest beacon is at ')
            sr = sr.replace('Sensor at ', '')
            sx, sy = sr.split(', ')
            bx, by = br.split(', ')
            yield ((int(sx[2:]), int(sy[2:]),), (int(bx[2:]), int(by[2:]),),)

def manhattan_distance(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

def get_row_coverage(row, sensor, beacon):
    md = manhattan_distance(sensor, beacon)
    sx, sy = sensor
    x_min, x_max = sx - md, sx + md
    y_min, y_max = sy - md, sy + md
    if not y_min <= row <= y_max:
        return None, None
    row_dist_from_sensor = abs(sy - row)
    return x_min + row_dist_from_sensor, x_max - row_dist_from_sensor

def line(pos_a, pos_b):
    print(pos_a, pos_b)
    x_a, y_a = pos_a
    x_b, y_b = pos_b
    d_x = 1 if x_b > x_a else -1
    d_y = 1 if y_b > y_a else -1
    line = set()
    pt = None
    while pt != pos_b:
        # print(pt)
        if pt is None:
            pt = pos_a
        else:
            px, py = pt
            if px > 100 or py > 100:
                break
            pt = px + d_x, py + d_y
        line.add(pt)
    return line

def bordering_positions(sensor, beacon):
    md = manhattan_distance(sensor, beacon)
    print(sensor, beacon)
    print(md)
    x, y = sensor
    min_y, max_y = y - md, y + md
    mid_y = (max_y - min_y - 1) // 2
    min_x, max_x = x - md, x + md
    mid_x = (max_x - min_x - 1) // 2
    print(min_x, mid_x, max_x)
    print(min_y, mid_y, max_y)
    # find corners of diamond: north, east, south, west
    c_n, c_e, c_s, c_w = (mid_x, min_y), (max_x, mid_y), (mid_x, max_y), (min_x, mid_y)
    print(c_n, c_e, c_s, c_w)
    border_positions = set()
    border_positions = border_positions.union(line(c_n, c_e))
    border_positions = border_positions.union(line(c_e, c_s))
    border_positions = border_positions.union(line(c_s, c_w))
    border_positions = border_positions.union(line(c_w, c_n))
    return border_positions

def p1():
    row = 2000000
    row_coverages = set()
    sensors_beacons_in_row = set()
    for sensor, beacon in get_sensors_beacons('input.txt'):
        if sensor[1] == row:
            sensors_beacons_in_row.add(sensor)
        if beacon[1] == row:
            sensors_beacons_in_row.add(beacon)
        min_x, max_x = get_row_coverage(row, sensor, beacon)
        if min_x is not None and max_x is not None:
            row_coverages.update(range(min_x, max_x + 1))
    return len(row_coverages) - len(sensors_beacons_in_row)

def p2():
    for sensor, beacon in get_sensors_beacons('test.txt'):
        # print(sensor, beacon)
        # break
        print(bordering_positions(sensor, beacon))

# print('Part 1: ', p1())
print('Part 2: ', p2())