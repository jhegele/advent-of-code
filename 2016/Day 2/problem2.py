"""Advent of Code, Day 2
Problem: 2
http://adventofcode.com/2016/day/2
"""

# This is kind of hacky, but because we have a small key pad, the easiest
# way to do this is to create a graph of all possible moves given a starting
# position.
keypad = {
  '1' : {
    'D' : '3'
  },
  '2' : {
    'R' : '3',
    'D' : '6'
  },
  '3' : {
    'U' : '1',
    'L' : '2',
    'D' : '7',
    'R' : '4'
  },
  '4' : {
    'L' : '3',
    'D' : '8'
  },
  '5' : {
    'R' : '6'
  },
  '6' : {
    'U' : '2',
    'L' : '5',
    'D' : 'A',
    'R' : '7'
  },
  '7' : {
    'U' : '3',
    'L' : '6',
    'D' : 'B',
    'R' : '8'
  },
  '8' : {
    'U' : '4',
    'L' : '7',
    'D' : 'C',
    'R' : '9'
  },
  '9' : {
    'L' : '8'
  },
  'A' : {
    'U' : '6',
    'R' : 'B'
  },
  'B' : {
    'U' : '7',
    'L' : 'A',
    'D' : 'D',
    'R' : 'C'
  },
  'C' : {
    'U' : '8',
    'L' : 'B'
  },
  'D' : {
    'U' : 'B'
  }
}

with open('input.txt', 'r') as input_file:
  for line in input_file:
    # Start at 5 for each line of instructions
    entry = '5'
    # Try to move based on each character in the line, if it fails, just
    # move on
    for char in line:
      try:
        entry = keypad[entry][char]
      except:
        pass
    print(entry)
