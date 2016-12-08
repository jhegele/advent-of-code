"""Advent of Code, Day 6
Problem: 1
http://adventofcode.com/2016/day/6
"""

from collections import Counter

class Pos(object):
  """ Position object represents a specific position in a row of characters
  """

  def __init__(self):
    self.values = []

  def most_common(self):
    """ Find the single most common letter among all the letters that
    appear in this position
    """
    if len(self.values) > 0:
      return Counter(self.values).most_common(1)[0][0]
    else:
      return ''

  def add_value(self, value):
    """Add non-whitespace values"""
    if value not in ['\n', ' ']:
      self.values.append(value)

positions = []

# Go through input lines and log letters at each position
with open('input.txt', 'r') as input_file:
  line_count = 1
  for line in input_file:
    for i in range(0, len(line)):
      if line_count == 1:
        positions.append(Pos())
      positions[i].add_value(line[i])
    line_count += 1

# Print out the most common letters in each position
print(''.join([p.most_common() for p in positions]))
