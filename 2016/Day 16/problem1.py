def dc(l, i):
  """Dragon curve function to fill the disk."""
  while len(i) < l:
    # As long as our input is shorter than the desired length, invert it, flip
    # the bits and add it to i with a zero in between
    i = '{0}0{1}'.format(i, ''.join('0' if c=='1' else '1' for c in reversed(i)))
  return i[:l]

def cs(i):
  """Generate the checksum of the disk contents."""
  c = []
  for ce, co in zip(i[::2], i[1::2]):
    # Append a 1 if the character pair matches, otherwise 0
    c.append('1' if ce == co else '0')
  if len(c) % 2 == 0:
    # Recursively generate as long as len is odd
    return cs(''.join(c))
  else:
    return ''.join(c)

# Part 1
print(cs(dc(35651584, '00111101111101000')))
# Part 2
print(cs(dc(35651584, '00111101111101000')))
