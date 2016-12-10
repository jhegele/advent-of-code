"""Advent of Code, Day 9
Problem: 1
http://adventofcode.com/2016/day/9
"""

import re

def decompress(compressed):
  """Recursive function to decompress based on challenge rules
  """
  # Find a compression marker if one exists
  marker = re.search(r'\((\d+)x(\d+)\)', compressed)
  if not marker:
    # If there's no marker, just return the length of the passed text
    return len(compressed)
  length = int(marker.group(1))
  iterations = int(marker.group(2))
  pos_marker = marker.start()
  idx = pos_marker + len(marker.group())
  # For this challenge, we need to decompress all markers so this is similar to problem 1 but we also decompress
  # all of the text within repeated segments
  return len(compressed[:pos_marker]) + decompress(compressed[idx:idx+length]) * iterations + decompress(compressed[idx+length:])

with open('input.txt', 'r') as input_file:
  message = input_file.read().strip()

print('Decompressed length: {0}'.format(decompress(message)))
