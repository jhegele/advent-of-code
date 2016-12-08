"""Advent of Code, Day 8
Problem: 1 & 2
http://adventofcode.com/2016/day/8
"""

import re

class Screen(object):
  """Object to represent our "screen"
  """

  def __init__(self, wide, tall):
    """Set the "pixel" width and height and initialize all pixels to the
    off (0) position
    """
    self.wide = wide
    self.tall = tall
    self.pixels = []
    for i in range(0, tall):
      self.pixels.append([0 for j in range(0, wide)])

  def display(self):
    """Convert the multidimensional "screen" array to a prettier print format
    that follows the style in the problem
    """
    for row in self.pixels:
      display_row = ''.join([str(pixel) for pixel in row]).replace('1', '#').replace('0', '.')
      print(display_row)

  def count_pixels_on(self):
    """Sum the rows in our "screen" array to get the count of lit pixels
    """
    pixels_on = 0
    for row in self.pixels:
      pixels_on += sum(row)
    return pixels_on

  def rect(self, wide, tall):
    """Light pixels with given dimensions in the top left corner of our "screen"
    """
    for i in range(0, tall):
      for j in range(0, wide):
        self.pixels[i][j] = 1

  def rotate_column(self, col_idx):
    """Shift the contents of a column in the multidimensional array down by one
    and allow contents to loop around the screen
    """
    new_pixels = []
    for i in range(0, self.tall):
      # Add a row to our new array for each row in the existing array
      new_pixels.append([])
      for j in range(0, self.wide):
        # If this array element is in the shift column, copy the element from the prior row
        if j == col_idx:
          value = self.pixels[i - 1][j]
        else:
          value = self.pixels[i][j]
        new_pixels[i].append(value)
    self.pixels = new_pixels

  def rotate_row(self, row_idx):
    """Shift the contents of a row in the multidimensional array to the right
    by one and allow contents to loop around the screen
    """
    new_row = []
    for i in range(0, self.wide):
      new_row.append(self.pixels[row_idx][i - 1])
    self.pixels[row_idx] = new_row

# Regex's to pull pertinent info from the input file
re_rect = r'(\d+)x(\d+)'
re_row = r'y=(\d+) by (\d+)'
re_col = r'x=(\d+) by (\d+)'

# Initialize an empty screen with 50 x 6 dimensions
screen = Screen(50, 6)
# Execute the instructions from the input file
with open('input.txt', 'r') as input_file:
  for instruction in input_file:
    if 'rect' in instruction:
      match = re.findall(re_rect, instruction)
      wide, tall = int(match[0][0]), int(match[0][1])
      screen.rect(wide, tall)
    if 'rotate row' in instruction:
      match = re.findall(re_row, instruction)
      row_idx, iterations = int(match[0][0]), int(match[0][1])
      for i in range(0, iterations):
        screen.rotate_row(row_idx)
    if 'rotate column' in instruction:
      match = re.findall(re_col, instruction)
      col_idx, iterations = int(match[0][0]), int(match[0][1])
      for i in range(0, iterations):
        screen.rotate_column(col_idx)
screen.display()
print('Illuminated pixel count: {0}'.format(screen.count_pixels_on()))
