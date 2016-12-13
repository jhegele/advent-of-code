from collections import deque, namedtuple

# Named tuple to track position in the maze
Position = namedtuple('Position', ['x', 'y', 's'])

def maze(input, max_x, max_y):
  """Build the maze based on the challenge rules"""
  m = []
  for y in range(0, max_y + 1):
    m.append([])
    for x in range(0, max_x + 1):
      b = format((x * x) + (3 * x) + (2 * x * y) + y + (y * y) + input, 'b')
      m[y].append('.' if b.count('1') % 2 == 0 else '#')
  return m

def valid(maze, pos_x, pos_y):
  """Determine whether a given position in the maze is valid"""
  if pos_x < 0 or pos_y < 0:
    return False
  if pos_x >= len(maze[0]) or pos_y >= len(maze):
    return False
  return maze[pos_y][pos_x] != '#'

def bfs(maze, start_x, start_y, max_steps):
  """Breadth-first search algo to move us through the maze."""
  # Initialize our queue to store all potential moves
  queue = deque()
  queue.append(Position(start_x, start_y, 0))
  # Initialize a set to store previous positions so we don't backtrack
  prior = set()
  while queue:
    # As long as there are moves in the queue, evaluate them from the left
    pos = queue.popleft()
    if not valid(maze, pos.x, pos.y) or '{0},{1}'.format(pos.x, pos.y) in prior:
      # If this isn't a valid move, skip it
      continue
    # Add this position to our previously visited positions
    prior.add('{0},{1}'.format(pos.x, pos.y))
    # If we haven't reached the max number of steps, add new potential moves
    if pos.s < max_steps:
      queue.append(Position(pos.x + 1, pos.y, pos.s + 1))
      queue.append(Position(pos.x, pos.y + 1, pos.s + 1))
      queue.append(Position(pos.x - 1, pos.y, pos.s + 1))
      queue.append(Position(pos.x, pos.y - 1, pos.s + 1))
  # The list of prior locations represents all the distinct positions we can
  # travel to within the given number of steps
  print('Visited {0} locations within {1} steps.'.format(len(prior), max_steps))

if __name__ == '__main__':
  m = maze(1364, 100, 100)
  bfs(m, 1, 1, 50)
