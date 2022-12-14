class Sand:

    def __init__(self, x, y, in_motion) -> None:
        self.x = x
        self.y = y
        self.in_motion = in_motion

    def move(self, new_loc):
        self.x, self.y = new_loc

    def get_potential_moves(self):
        return (self.x, self.y + 1,), (self.x - 1, self.y + 1,), (self.x + 1, self.y - 1)

    def stop(self):
        self.in_motion = False

class Mapp:

    def __init__(self) -> None:
        self.sand_origin = (500, 0)
        self.rocks = []
        self.bounds = {
            'x': (None, None),
            'y': (None, None)
        }
        self.sand = []

    def add_rocks(self, path):
        segments_raw = path.strip().split(' -> ')
        segments = []
        for segment in segments_raw:
            x, y = segment.split(',')
            segments.append((int(x), int(y),))
        for i in range(1, len(segments)):
            a_x, a_y = segments[i - 1]
            b_x, b_y = segments[i]
            for x in range(min(a_x, b_x), max(a_x, b_x) + 1):
                for y in range(min(a_y, b_y), max(a_y, b_y) + 1):
                    self.rocks.append((x, y,))
        self._update_bounds()

    def add_floor(self):
        max_y = self.bounds['y'][1]
        self.rocks.append((None, max_y + 2))
        self._update_bounds()

    def _update_bounds(self):
        all_locs = [*self.rocks, *self.sand, self.sand_origin]
        xs = [x for x, _ in all_locs]
        ys = [y for _, y in all_locs]
        self.bounds['x'] = (min(xs), max(xs))
        self.bounds['y'] = (min(ys), max(ys))

    def tick(self):
        sand_in_motion = [s for s in self.sand if s.in_motion]
        if len(sand_in_motion) == 0:
            print('new')
            origin_x, origin_y = self.sand_origin
            self.sand.append(Sand(origin_x, origin_y, True))
        else:
            print('old')
            grain = sand_in_motion[0]
            occupied_locs = [*self.rocks] + [(s.x, s.y,) for s in self.sand if not s.in_motion]
            valid_moves = [l for l in grain.get_potential_moves() if l not in occupied_locs]
            if len(valid_moves) > 0:
                grain.move(valid_moves[0])
            else:
                grain.stop()

    def is_overflowing(self):
        overflow_sand = [1 for s in self.sand if s.y >= self.bounds['y'][1]]
        return sum(overflow_sand) > 0
                
    def draw(self):
        if (self.bounds['x'] == (None, None,) or self.bounds['y'] == (None, None,)):
            print("Cannot draw map")
            return
        min_y, max_y = self.bounds['y']
        min_x, max_x = self.bounds['x']
        for y in range(min_y - 1, max_y + 2):
            row = ''
            for x in range(min_x - 1, max_x + 2):
                loc = (x, y,)
                if loc in [(s.x, s.y,) for s in self.sand]:
                    row += 'o'
                    continue
                if loc == self.sand_origin:
                    row += '+'
                    continue
                if loc in self.rocks:
                    row += '#'
                    continue
                row += '.'
            print(row)

        

symbols = {
    'rock': '#',
    'sand_origin': '+',
    'air': '.',
    'sand': 'o'
}

# class Map:

#     def __init__(self) -> None:
#         self.locs = {
#             (500, -1): {'type': 'sand_origin', 'in_motion': False}
#         }
#         self.bounds_x = (None, None)
#         self.bounds_y = (None, None)
#         self.floor_y = None

#     def add_rock(self, rock_path, part = 1):
#         path_segments_raw = rock_path.strip().split(' -> ')
#         path_segments = []
#         for segment in path_segments_raw:
#             x, y = segment.split(',')
#             path_segments.append((int(x), int(y),))
#         for idx in range(1, len(path_segments)):
#             a_x, a_y = path_segments[idx - 1]
#             b_x, b_y = path_segments[idx]
#             new_locs = []
#             if b_x > a_x:
#                 for x in range(a_x, b_x + 1):
#                     if b_y > a_y:
#                         for y in range(a_y, b_y + 1):
#                             new_locs.append((x, y,))
#                     else:
#                         for y in range(b_y, a_y + 1):
#                             new_locs.append((x, y,))
#             else:
#                 for x in range(b_x, a_x + 1):
#                     if b_y > a_y:
#                         for y in range(a_y, b_y + 1):
#                             new_locs.append((x, y,))
#                     else:
#                         for y in range(b_y, a_y + 1):
#                             new_locs.append((x, y,))
#             for loc in new_locs:
#                 self.locs[loc] = {
#                     'type': 'rock',
#                     'in_motion': False
#                 }
#         self._update_bounds(part)

#     def _update_bounds(self, part = 1):
#         xs = [x for x, _ in self.locs]
#         ys = [y for _, y in self.locs]
#         adj = 1 if part == 1 else 3
#         self.bounds_x = (min(xs) - adj, max(xs) + adj)
#         self.bounds_y = (min(ys) - adj, max(ys) + adj)
#         if part == 2:
#             self.floor_y = self.bounds_y[1] - 1

#     def _move_sand(self, loc, part = 1):
#         x, y = loc
#         if part == 2:
#             # for part 2, the floor is 2 plus the max y value in the scan
#             # print(self.floor_y, y + 1)
#             if y + 1 == self.floor_y:
#                 return None
#         d, dl, dr = (x, y + 1), (x - 1, y + 1), (x + 1, y + 1)
#         stationary_locs = [loc for loc, state in self.locs.items() if not state['in_motion']]
#         if d not in stationary_locs:
#             return d
#         if dl not in stationary_locs:
#             return dl
#         if dr not in stationary_locs:
#             return dr
#         return None


#     def cycle_sand(self, part = 1):
#         sand_in_motion = [loc for loc, state in self.locs.items() if state['type'] == 'sand' and state['in_motion']]
#         if len(sand_in_motion) == 0:
#             sand_origins = [loc for loc, state in self.locs.items() if state['type'] == 'sand_origin']
#             for so_x, so_y in sand_origins:
#                 self.locs[(so_x, so_y + 1,)] = {
#                     'type': 'sand',
#                     'in_motion': True
#                 }
#         for grain_loc in sand_in_motion:
#             new_loc = self._move_sand(grain_loc, part)
#             if new_loc is not None:
#                 self.locs[new_loc] = self.locs.pop(grain_loc)
#             else:
#                 self.locs[grain_loc]['in_motion'] = False
            

#     def sand_overflowing(self):
#         sand_locs = [loc for loc, state in self.locs.items() if state['type'] == 'sand']
#         sand_overflows = [y for _, y in sand_locs if y >= self.bounds_y[1]]
#         return len(sand_overflows) > 0

#     def sand_source_blocked(self):
#         return len([loc for loc, state in self.locs.items() if state['type'] == 'sand' and not state['in_motion'] and loc == (500, 0,)]) == 3

#     def get_resting_sand_count(self):
#         return sum([1 for _, state in self.locs.items() if state['type'] == 'sand' and not state['in_motion']])

#     def draw(self):
#         start_x, end_x = self.bounds_x
#         start_y, end_y = self.bounds_y
#         if not all([start_x is not None, end_x is not None, start_y is not None, end_y is not None]):
#             print('Not enough data to draw map')
#             return
#         for y in range(start_y, end_y + 1):
#             if y == (end_y - 1):
#                 row = ['#' for _ in range(start_x, end_x + 1)]
#             else:
#                 row = [symbols['air'] if (x, y,) not in self.locs else symbols[self.locs[(x, y,)]['type']] for x in range(start_x, end_x + 1)]
#             print(''.join(row))
            


def get_map(path):
    with open(path, 'r') as f:
        return f.readlines()

def p1():
    m = get_map('test.txt')
    map = Mapp()
    for p in m:
        map.add_rocks(p)
    c = 1
    while not map.is_overflowing():
        map.tick()
        map.draw()
        if c > 2:
            break
        # c += 1
    map.draw()
    # return map.get_resting_sand_count()

def p2():
    m = get_map('test.txt')
    map = Mapp()
    for p in m:
        map.add_rocks(p)
    map.draw()
    # m = get_map('test.txt')
    # map = Map()
    # for p in m:
    #     map.add_rock(p, 2)
    # # map.draw()
    # c = 1
    # while not map.sand_source_blocked():
    #     map.cycle_sand(2)
    #     locs = [l for l in map.locs]
    #     print(max([y for _, y in locs]))
    #     map.draw()
    #     # if c >= 307:
    #     #     break
    #     # c += 1
    # return map.get_resting_sand_count()

print('Part 1: ', p1())
# print('Part 2: ', p2())