"""Advent of Code, Day 2
Problem: 1
http://adventofcode.com/2016/day/2
"""

# Initialize the keypad layout
keypad = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

with open('input.txt', 'r') as input_file:
  for line in input_file:
    # Each line gets initialized at 5 (keypad[1][1])
    vert = 1
    horiz = 1
    # Iterate over the characters and update the vert and horiz values based
    # on the specified moves
    for char in line:
      if char == 'U':
        # Vertical moves are bounded by 0 and 2 (cannot loop around the pad)
        vert = max([vert - 1, 0])
      if char == 'D':
        vert = min([vert + 1, 2])
      if char == 'L':
        # Horizontal moves are bounded by 0 and 2 (cannot loop around the pad)
        horiz = max([horiz - 1, 0])
      if char == 'R' :
        horiz = min([horiz + 1, 2])
    # Show the key we end on
    print(keypad[vert][horiz])
