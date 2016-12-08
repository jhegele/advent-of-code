"""Advent of Code, Day 5
Problem: 2
http://adventofcode.com/2016/day/5
"""

import hashlib

# Initialize
door_id = 'ugkcyxxp'
password_length = 8

# Use a dict to track the PW positions that are filled
pw = {
  '0' : None,
  '1' : None,
  '2' : None,
  '3' : None,
  '4' : None,
  '5' : None,
  '6' : None,
  '7' : None
}

idx = 0
# Keep looping as long as there are None values in the password dict
while len([v for k, v in pw.items() if v is not None]) < password_length:
  id_bytes = '{0}{1}'.format(door_id, idx).encode()
  hex_hash = hashlib.md5(id_bytes).hexdigest()
  if hex_hash[:5] == '00000':
    # We only care about hashes where index 5 is less than 8
    if hex_hash[5] in ['0', '1', '2', '3', '4', '5', '6', '7']:
      # Only use the first match for a given password position
      if pw[hex_hash[5]] is None:
        pw[hex_hash[5]] = hex_hash[6]
        print('Found character {0} at index {1}: {2}'.format(hex_hash[5], idx, hex_hash[6]))
  idx += 1

print(''.join([v for k, v in pw.items()]))
