from collections import deque, namedtuple

"""
Problem input:
The first floor contains a promethium generator and a promethium-compatible microchip.
The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
The fourth floor contains nothing relevant."""

start_pt1 = [1, 1, 2, 3, 2, 3, 2, 3, 2, 3]
start_pt2 = [1, 1, 1, 1, 1, 1, 2, 3, 2, 3, 2, 3, 2, 3]

State = namedtuple('State', ['f', 'e', 's'])

def valid(state):
  """Check that this floor setup is valid per the puzzle rules"""

  # elevator isn't on a valid floor
  if not 1 <= state.e <= 4:
    return False
  # chip / generator not on a valid floor
  if any(not 1 <= i <= 4 for i in state.f):
    return False
  # iterate over each chip (odd numbered indices)
  for idx, c in enumerate(state.f[1::2]):
    # find the releveant generator index
    g_idx = idx * 2
    # if the chip and gen aren't on the same floor and there are
    # other generators on this floor, the chip fries
    if c != state.f[g_idx] and any(c == i for i in state.f[::2]):
      return False
  return True

def generalize(state):
  """We need a quick way to check whether we've seen a given state before in
  order to filter options out of our queue efficiently"""

  # build ordered list that summarizes how many generators are on each floor
  gen = [sum(1 for g in state.f[::2] if g == fn) for fn in range(1, 5)]
  # do the same for chips
  chip = [sum(1 for c in state.f[1::2] if c == fn) for fn in range(1, 5)]
  # build a string out of the above lists and the elevator position
  return ''.join(map(str, gen + chip)) + str(state.e)

def solved(state):
  # check that everything is on floor 4
  return all(i == 4 for i in state.f)

def bfs(floor_config):
  """Breadth-first search algo."""

  # initialize our queue and add the starting state
  queue = deque()
  queue.append(State(floor_config, 1, 0))
  # track previous states
  prior = set()

  while queue:
    state = queue.popleft()
    # if we've seen this state before or it's not valid, skip it
    if generalize(state) in prior or not valid(state):
      continue
    prior.add(generalize(state))

    # we solved the puzzle!
    if solved(state):
      print('Solved in {0} steps.'.format(state.s))
      return

    # loop through the floor list and move items (just move a single item first)
    for idx in range(len(state.f)):
      # if the chip/gen isn't on the elevator floor, it can't be moved
      if state.e != state.f[idx]:
        continue
      # move down one floor
      state.f[idx] -= 1
      queue.append(State(list(state.f), state.e - 1, state.s + 1))
      # move up one floor
      state.f[idx] += 2
      queue.append(State(list(state.f), state.e + 1, state.s + 1))
      # reset the index to the current floor
      state.f[idx] -= 1

      # loop through items with a higher index and move them as well (this moves
      # a second item in addition to the first)
      for jdx in range(idx + 1, len(state.f)):
        # if the chip/gen isn't on the elevator floor, it can't be moved
        if state.e != state.f[jdx]:
          continue
        state.f[jdx] -= 1
        state.f[idx] -= 1
        queue.append(State(list(state.f), state.e - 1, state.s + 1))
        state.f[jdx] += 2
        state.f[idx] += 2
        queue.append(State(list(state.f), state.e + 1, state.s + 1))
        state.f[jdx] -= 1
        state.f[idx] -= 1
  else:
    print('Can\'t solve!')

bfs(start_pt2)
