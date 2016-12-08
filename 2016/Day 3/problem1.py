"""Advent of Code, Day 3
Problem: 1
http://adventofcode.com/2016/day/3
"""

class Triangle(object):
  """Triangle object to help preserve state for each potential triangle
  """

  def __init__(self, line):
    # Split and clean up the line that's passed in to get side lengths
    self.values = line.split(' ')
    # Sort the list so that we always have the largest at index 0
    self.values = sorted([int(v.replace('\n','')) for v in self.values if v != ''], reverse=True)
    # Per the problem, the sum of the two smaller values (indices 1 and 2)
    # must be greater than the largest value (index 0)
    self.is_possible = (self.values[0] < self.values[1] + self.values[2])

with open('input.txt', 'r') as input_file:
  triangles = []
  # Build all of the potential triangles
  for line in input_file:
    triangles.append(Triangle(line))

# Count the number of possible triangles
print(len([t for t in triangles if t.is_possible]))
