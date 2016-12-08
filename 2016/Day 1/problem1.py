"""Advent of Code, Day 1
Problem: 1
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

with open('input.txt', 'r') as input_file:
  # Build a list of each step from the input file
  steps = input_file.read().split(', ')
  for step in steps:
    # Before moving, we need to update the direction we're facing using our
    # graph
    facing = direction[facing][step[0]]
    blocks = int(step[1:])
    # Recalculate new coords based on where we've moved to
    if facing == 'N':
      vert += blocks
    if facing == 'S':
      vert -= blocks
    if facing == 'E':
      horiz += blocks
    if facing == 'W':
      horiz -= blocks

total_blocks = abs(vert) + abs(horiz)
print('Blocks away: {0}'.format(total_blocks))
