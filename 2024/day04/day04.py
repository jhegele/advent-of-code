from typing import TypedDict, Optional

with open("day04.input", "r") as f:
  lines = [l.strip() for l in f.readlines()]
  bounds = (len(lines[0]) - 1, len(lines) - 1)

def pos_is_valid(pos: tuple[int, int]):
  x, y = pos
  max_x, max_y = bounds
  if x < 0:
    return False
  if x > max_x:
    return False
  if y < 0: 
    return False
  if y > max_y:
    return False
  return True

''' For part 1, we create all possible lines that are at least 4 characters long: horizontal, 
vertical, and diagonal. Diagonals are created in two directions, top right to bottom left and 
top left to bottom right. Creating these requires two steps since the starting point moves
from one edge of the grid to another after you create the diagonal that runs directly across
the middle of the grid.
'''
def get_all_lines(wordsearch: list[str]):
  max_x = len(wordsearch[0]) - 1
  max_y = len(wordsearch) - 1
  # top to bottom (init)
  all_lines = [*wordsearch]
  # left to right
  for x in range(max_x + 1):
    line_chars = [wordsearch[y][x] for y in range(len(wordsearch))]
    all_lines.append(''.join(line_chars))
  # top left to middle
  for x in range(3, max_x + 1):
    pos = (x, 0)
    line = ''
    while pos_is_valid(pos):
      line += wordsearch[pos[1]][pos[0]]
      pos = (pos[0] - 1, pos[1] + 1)
    if len(line) >= 4:
      all_lines.append(line)
  # middle to bottom right
  for y in range(1, max_y - 2):
    pos = (max_x, y)
    line = ''
    while pos_is_valid(pos):
      line += wordsearch[pos[1]][pos[0]]
      pos = (pos[0] - 1, pos[1] + 1)
    if len(line) >= 4:
      all_lines.append(line)
  # top right to middle
  for x in range(max_x - 3, -1, -1):
    pos = (x, 0)
    line = ''
    while pos_is_valid(pos):
      line += wordsearch[pos[1]][pos[0]]
      pos = (pos[0] + 1, pos[1] + 1)
    if len(line) >= 4:
      all_lines.append(line)
  # middle to bottom left
  for y in range(1, max_y - 2):
    pos = (0, y)
    line = ''
    while pos_is_valid(pos):
      line += wordsearch[pos[1]][pos[0]]
      pos = (pos[0] + 1, pos[1] + 1)
    if len(line) >= 4:
      all_lines.append(line)
  return all_lines

def is_x_mas(pos_a: tuple[int, int], wordsearch: list[str]):
  max_x = len(wordsearch[0]) - 1
  max_y = len(wordsearch) - 1
  x_a, y_a = pos_a
  # we can only have a valid x-mas if the position of the A
  # is at least one column in from the sides and one row in
  # from the top/bottom
  if x_a < 1 or x_a > max_x - 1:
    return False
  if y_a < 1 or y_a > max_y - 1:
    return False
  # grab letters that appear to the upper left, upper right
  # bottom right, and bottom left of the A
  ul = wordsearch[y_a - 1][x_a - 1]
  ur = wordsearch[y_a - 1][x_a + 1]
  br = wordsearch[y_a + 1][x_a + 1]
  bl = wordsearch[y_a + 1][x_a - 1]
  ul_to_br = False
  ur_to_bl = False
  # moving from upper left to bottom right, this is only a
  # valid diagonal if one character is an "M" and one is
  # an "S"
  if ul == "M":
    if br == "S":
      ul_to_br = True
  if ul == "S":
    if br == "M":
      ul_to_br = True
  # moving from upper right to bottom left, this is only a
  # valid diagonal if one character is an "M" and one is
  # an "S"
  if ur == "M":
    if bl == "S":
      ur_to_bl = True
  if ur == "S":
    if bl == "M":
      ur_to_bl = True
  # only a valid x-mas if both directions are true
  return ul_to_br and ur_to_bl

def part2(wordsearch: list[str]):
  total = 0
  for y, line in enumerate(wordsearch):
    for x, char in enumerate(line):
      if char == 'A':
        if (is_x_mas((x, y), wordsearch)):
          total += 1
  return total

def part1(wordsearch: list[str]):
  all_lines = get_all_lines(wordsearch)
  total = 0
  for line in all_lines:
    total += line.count('XMAS') + line.count('SAMX')
  return total

print('Part 1: {}'.format(part1(lines)))
print('Part 2: {}'.format(part2(lines)))