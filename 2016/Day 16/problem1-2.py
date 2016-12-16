def fill_disk(length, input):
  """Dragon curve function to fill the disk."""
  while len(input) < length:
    # As long as our input is shorter than the desired length, invert it, flip
    # the bits and add it to i with a zero in between
    input = '{0}0{1}'.format(input, ''.join('0' if c=='1' else '1' for c in reversed(input)))
  return input[:length]

def checksum(input):
  """Generate the checksum of the disk contents."""
  # If character pairs are equal, append 1, else append 0
  chk = ''.join(['1' if a == b else '0' for a, b in zip(input[::2], input[1::2])])
  # chk.append('1' if a == b else '0' for a, b in zip(input[::2], input[1::2]))
  if len(chk) % 2 == 0:
    # Recursively generate as long as len is odd
    return checksum(chk)
  else:
    return chk

# Part 1
print(checksum(fill_disk(272, '00111101111101000')))
# Part 2
print(checksum(fill_disk(35651584, '00111101111101000')))
