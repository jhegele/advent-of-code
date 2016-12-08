"""Advent of Code, Day 3
Problem: 2
http://adventofcode.com/2016/day/3
"""

class Triangle(object):
  """ Use the same triangle object to help maintain state
  """

  def __init__(self, line):
    self.values = line.split(' ')
    self.values = sorted([int(v.replace('\n','')) for v in self.values if v != ''], reverse=True)
    self.is_possible = (self.values[0] < self.values[1] + self.values[2])

with open('input.txt', 'r') as input_file:
  line_count = 1
  triangles = []
  lines = []
  for line in input_file:
    # Since columns make up potential triangles, we need to bring in 3 rows at
    # a time and use those 3 rows to construct 3 potential triangles
    if line_count % 3 != 0:
      # If we don't have 3 rows yet, keep adding new rows
      lines.append([int(v.replace('\n','')) for v in line.split(' ') if v != ''])
    else:
      # Add the 3rd row
      lines.append([int(v.replace('\n','')) for v in line.split(' ') if v != ''])
      # Build triangles using values in the COLUMNS of our multidimensional array
      triangles.append(Triangle('{0} {1} {2}'.format(lines[0][0], lines[1][0], lines[2][0])))
      triangles.append(Triangle('{0} {1} {2}'.format(lines[0][1], lines[1][1], lines[2][1])))
      triangles.append(Triangle('{0} {1} {2}'.format(lines[0][2], lines[1][2], lines[2][2])))
      lines = []
    line_count += 1

print(len([t for t in triangles if t.is_possible]))
