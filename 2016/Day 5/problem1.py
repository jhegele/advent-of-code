"""Advent of Code, Day 5
Problem: 1
http://adventofcode.com/2016/day/5
"""

import hashlib

# Initialize
door_id = 'ugkcyxxp'
password_length = 8

# Empty list where we'll collect our password characters
pw = []

idx = 0
# Start at 0 and increment the index, generating a hash each time
while len(pw) < password_length:
  # Build a byte version of the concatenated door ID and index
  id_bytes = '{0}{1}'.format(door_id, idx).encode()
  # Build the encrypted MD5 hash
  hex_hash = hashlib.md5(id_bytes).hexdigest()
  # We only care about hashes that start with five zeroes
  if hex_hash[:5] == '00000':
    pw.append(hex_hash[5])
    print('Character {0}: {1} | Index: {2}'.format(len(pw), pw[-1:], idx))
  idx += 1

print(''.join(pw))
