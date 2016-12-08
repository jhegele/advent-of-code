"""Advent of Code, Day 4
Problem: 1
http://adventofcode.com/2016/day/4
"""

import re
from collections import Counter

class Room(object):
  """Room object built from the encrypted code in the input file
  """

  def __init__(self, code):
    # Regex patterns to pull data from the codes
    re_checksum = r'\[([a-z]+)\]'
    re_sector_id = r'-(\d{3})\['
    re_name = r'([a-z-]+)-[1-9]'
    self.checksum = re.findall(re_checksum, code)[0]
    try:
      self.sector_id = int(re.findall(re_sector_id, code)[0])
    except:
      raise Exception(code)
    self.name = re.findall(re_name, code)[0].replace('-','')
    self.top_five = []
    frequencies = {}
    # Build a dictionary where the keys are frequencies and the values are
    # lists of letters with that frequency
    for freq in Counter(list(self.name)).most_common():
      letter = freq[0]
      occurrences = freq[1]
      if occurrences in frequencies:
        frequencies[occurrences].append(letter)
      else:
        frequencies[occurrences] = [letter]
    occurrences = sorted([k for k, v in frequencies.items()], reverse=True)
    # Add letters to our list of top 5 until we have 5 or more
    while len(self.top_five) < 5:
      for occ in occurrences:
        self.top_five = self.top_five + sorted(frequencies[occ])
    # Truncate the top 5 list to just 5 entries
    self.top_five = self.top_five[:5]

  def is_real(self):
    """ A room is real if the top five letters, in order of frequency, is
    equivalent to the checksum
    """
    return ''.join(self.top_five) == self.checksum

with open('input.txt', 'r') as input_file:
  rooms = []
  # Build all the possible rooms
  for room_code in input_file:
    rooms.append(Room(room_code))

# Print the count of rooms that are real
print(sum([r.sector_id for r in rooms if r.is_real()]))
