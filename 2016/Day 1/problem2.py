"""Advent of Code, Day 1
Problem: 2
http://adventofcode.com/2016/day/1
"""

# Initialize our coordinates to 0, 0
vert = 0
horiz = 0

# Build a graph of all possible directional changes. Ex: if facing north, if
# the turn is to the right, you are now facing east.
direction = {
  'N' : {
    'R' : 'E',
    'L' : 'W'
  },
  'E' : {
    'R' : 'S',
    'L' : 'N'
  },
  'W' : {
    'R' : 'N',
    'L' : 'S'
  },
  'S' : {
    'R' : 'W',
    'L' : 'E'
  }
}

# Initialize the direction we are facing
facing = 'N'
# Initialize a list to track every point we visit
visited = [[horiz, vert]]
loc = None

with open('input.txt', 'r') as input_file:
  steps = input_file.read().split(', ')
  for step in steps:
    # Update which direction we're facing before we move
    facing = direction[facing][step[0]]
    blocks = int(step[1:])
    # Instead of moving in one huge jump, we need to track each specific
    # coordinate that we pass through and check to see if we've been there
    # before.
    if facing == 'N':
      # Record a move for each block we step through
      for i in range(0, blocks):
        vert += 1
        # If we've visited this block, we can stop everything
        if [horiz, vert] in visited:
          loc = [horiz, vert]
          break
        # If not, add the block to our list of visited locations
        visited.append([horiz, vert])
    # The S, E, and W conditions act the same as N (so probably could have
    # been functionalized, but oh well, it's a hack)
    if facing == 'S':
      for i in range(0, blocks):
        vert -= 1
        if [horiz, vert] in visited:
          loc = [horiz, vert]
          break
        visited.append([horiz, vert])
    if facing == 'E':
      for i in range(0, blocks):
        horiz += 1
        if [horiz, vert] in visited:
          loc = [horiz, vert]
          break
        visited.append([horiz, vert])
    if facing == 'W':
      for i in range(0, blocks):
        horiz -= 1
        if [horiz, vert] in visited:
          loc = [horiz, vert]
          break
        visited.append([horiz, vert])
    if loc is not None:
      break

# The total number of blocks away is simply the sum of the absolute values
# of our horizontal and vertical coordinates
total_blocks = abs(loc[0]) + abs(loc[1])
print('Blocks away: {0}'.format(total_blocks))

