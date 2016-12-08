"""Advent of Code, Day 4
Problem: 2
http://adventofcode.com/2016/day/4
"""

import re
from collections import Counter

class Room(object):
  """Room object built from the encrypted code in the input file
  """

  def __init__(self, code):
    # This is all the same as problem 1
    re_checksum = r'\[([a-z]+)\]'
    re_sector_id = r'-(\d{3})\['
    re_name = r'([a-z-]+)-[1-9]'
    self.checksum = re.findall(re_checksum, code)[0]
    try:
      self.sector_id = int(re.findall(re_sector_id, code)[0])
    except:
      raise Exception(code)
    self.name = re.findall(re_name, code)[0].replace('-',' ')
    self.top_five = []
    frequencies = {}
    for freq in Counter(list(self.name)).most_common():
      letter = freq[0]
      occurrences = freq[1]
      if occurrences in frequencies:
        frequencies[occurrences].append(letter)
      else:
        frequencies[occurrences] = [letter]
    occurrences = sorted([k for k, v in frequencies.items()], reverse=True)
    while len(self.top_five) < 5:
      for occ in occurrences:
        self.top_five = self.top_five + sorted(frequencies[occ])
    self.top_five = self.top_five[:5]

  def decrypted_name(self):
    """To decrypt the room names, we have to shift letters through the alphabet
    """
    decrypted = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Find the number of extra shifts we need based on the sector ID (i.e. if
    # we shift a letter 26 times, it just comes back to the same letter)
    offset = self.sector_id % 26
    for letter in self.name:
      if letter != ' ':
        letter_idx = alphabet.index(letter)
        # Do we need to loop around (i.e. do we pass through "z")
        if letter_idx + offset > 25:
          decrypt_idx = (letter_idx + offset) - 26
        else:
          decrypt_idx = (letter_idx + offset)
        decrypted.append(alphabet[decrypt_idx])
      else:
        decrypted.append(' ')
    return ''.join(decrypted)

  def is_real(self):
    return ''.join(self.top_five) == self.checksum

with open('input.txt', 'r') as input_file:
  rooms = []
  for room_code in input_file:
    rooms.append(Room(room_code))

for room in rooms:
  # We need to find a room with 'north' in the name
  if 'north' in room.decrypted_name():
    print('{0}: {1}'.format(room.sector_id, room.decrypted_name()))
