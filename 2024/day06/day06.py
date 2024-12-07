from typing import Literal, Dict, TypedDict

type Coords = tuple[int, int]
type Direction = Literal['N', 'E', 'S', 'W']

with open("day06.input", "r") as f:
  lines = [line.strip() for line in f.readlines()]

class Guard:
  '''Controls direction and position of the guard'''
  direction: Direction
  position: Coords

  moves = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0)
  }
  turns = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N'
  }

  def __init__(self, position: Coords):
    self.position = position
    self.direction = 'N'

  def turn(self):
    self.direction = self.turns[self.direction]
    return self.direction

  def move(self):
    offset = self.moves[self.direction]
    self.position = tuple(map(sum, zip(self.position, offset)))
    return self.position

  # Need to be able to check the next position that the guard would
  # move to in order to know if we should turn
  @property
  def next_move(self):
    offset = self.moves[self.direction]
    return tuple(map(sum, zip(self.position, offset)))

class Map:
  '''Builds the map and determines whether guard is on map or looped (for part 2)'''
  patrol_map: list[str] = []
  guard: Guard
  max_x: int
  max_y: int
  # record the direction the guard was facing and the position. if guard returns to
  # the same position and is moving in the same direction, he is looped
  visited: Dict[tuple[Direction, Coords], int] = {}

  def __init__(self, lines: list[str]):
    self.patrol_map = list(lines)
    self.max_x = len(lines[0]) - 1
    self.max_y = len(lines) - 1
    self.visited = {}
    for y, row in enumerate(lines):
      x = row.find('^')
      if (x != -1):
        self.guard = Guard((x, y))
        self.record_visit()
  
  @property
  def guard_is_on_map(self):
    gx, gy = self.guard.position
    return 0 <= gx <= self.max_x and 0 <= gy <= self.max_y
  
  @property
  def guard_can_move(self):
    next_pos = self.get_pos(self.guard.next_move)
    if next_pos == '#' or next_pos == 'O':
      return False
    return True
  
  @property
  def guard_looped(self):
    return any(c > 2 for c in self.visited.values())

  def get_pos(self, position: Coords):
    x, y = position
    if 0 <= x <= self.max_x and 0 <= y <= self.max_y:
      return self.patrol_map[y][x]
    return None
  
  def move_guard(self):
    while not self.guard_can_move:
      self.guard.turn()
    self.guard.move()
    self.record_visit()

  def record_visit(self):
    gx, gy = self.guard.position
    if 0 <= gx <= self.max_x and 0 <= gy <= self.max_y:
      key = (self.guard.direction, self.guard.position)
      if key not in self.visited:
        self.visited[key] = 0
      self.visited[key] += 1
    
  def place_obstacle(self, position: Coords):
    ox, oy = position
    self.patrol_map[oy] = self.patrol_map[oy][:ox] + 'O' + self.patrol_map[oy][ox + 1:]

def part1(lines: list[str]):
  m = Map(lines)
  while m.guard_is_on_map:
    m.move_guard()
  locs_visited = set([v[1] for v in m.visited])
  return len(locs_visited)

def part2(lines: list[str]):
  # takes a while to run this, be patient
  loops = 0
  map_init = Map(lines)
  guard_start_pos = map_init.guard.position
  while map_init.guard_is_on_map:
    map_init.move_guard()
  locs_visited = set([v[1] for v in map_init.visited])
  locs_visited.remove(guard_start_pos)
  for loc in locs_visited:
    m = Map(lines)
    m.place_obstacle(loc)
    while m.guard_is_on_map and not m.guard_looped:
      m.move_guard()
    if m.guard_looped:
      loops += 1
  return loops


print('Part1: {}'.format(part1(lines)))
print('Part2: {}'.format(part2(lines)))