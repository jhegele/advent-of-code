from collections import deque, namedtuple
import sys
import time

# Named tuple to track position in the maze
Position = namedtuple('Position', ['x', 'y', 's', 'h'])

def maze(input, max_x, max_y):
  """Build the maze based on the challenge rules"""
  m = []
  for y in range(0, max_y + 1):
    m.append([])
    for x in range(0, max_x + 1):
      b = format((x * x) + (3 * x) + (2 * x * y) + y + (y * y) + input, 'b')
      m[y].append(' ' if b.count('1') % 2 == 0 else '#')
  return m

def valid(maze, pos_x, pos_y):
  """Determine whether a given position in the maze is valid"""
  if pos_x < 0 or pos_y < 0:
    return False
  if pos_x >= len(maze[0]) or pos_y >= len(maze):
    return False
  return maze[pos_y][pos_x] != '#'

def draw(maze, pos, end_x, end_y):
  parents = []
  while pos:
    parents.append(pos)
    pos = pos.h
  parents.reverse()
  maze[end_y][end_x] = '\033[31mX\033[32m'
  for p in parents:
    maze[p.y][p.x] = '0'
  sys.stdout.flush()
  for row in maze:
    print(''.join(row))
  print('\n')
  time.sleep(0.03)

def bfs(maze, start_x, start_y, end_x, end_y):
  """Breadth-first search algo to move us through the maze."""
  # Initialize our queue to store all potential moves
  queue = deque()
  queue.append(Position(start_x, start_y, 0, None))
  # Initialize a set to store previous positions so we don't backtrack
  prior = set()
  while queue:
    # As long as there are moves in the queue, evaluate them from the left
    pos = queue.popleft()
    if not valid(maze, pos.x, pos.y) or '{0},{1}'.format(pos.x, pos.y) in prior:
      # If this isn't a valid move, skip it
      continue
    if pos.x == end_x and pos.y == end_y:
      # We solved the maze!
      print('Solved in {0} steps!'.format(pos.s))
      return
    # Add this position to our previously visited positions
    prior.add('{0},{1}'.format(pos.x, pos.y))
    draw(maze, pos, end_x, end_y)
    # Add up, down, left, right moves from the current position to the queue
    queue.append(Position(pos.x + 1, pos.y, pos.s + 1, pos))
    queue.append(Position(pos.x, pos.y + 1, pos.s + 1, pos))
    queue.append(Position(pos.x - 1, pos.y, pos.s + 1, pos))
    queue.append(Position(pos.x, pos.y - 1, pos.s + 1, pos))
  else:
    # Something happened and we couldn't solve the maze
    print('I couldn\'t solve it!')

if __name__ == '__main__':
  m = maze(1364, 50, 50)
  bfs(m, 1, 1, 31, 39)
