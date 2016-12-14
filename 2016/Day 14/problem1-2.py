import hashlib
import re
from functools import lru_cache

# Flag to enable part 2
part2 = True

class Key(object):
  """Creates a key and tracks its state"""

  def __init__(self, idx, seq):
    self.idx = idx
    self.seq = seq
    self.valid = False
    self.check = True

  def check_seq(self, idx, seq):
    """Check a potentially matching sequence against this key"""
    if idx > self.idx + 1000:
      self.check = False
    else:
      if ''.join([self.seq[0] for i in range(0, 5)]) == seq:
        self.valid = True
        self.check = False

# Since hashing can be expensive, we memoize this function which allows
# caching and speeds up performance
@lru_cache(maxsize=None)
def get_hash(salt, idx):
  """Build our hash from the provided salt and index value"""
  h = hashlib.md5('{0}{1}'.format(salt, idx).encode()).hexdigest()
  # For part 2, we need to stretch the key by rehashing an additional 2016
  # times
  if part2:
    for i in range(0, 2016):
      h = hashlib.md5('{0}'.format(h).encode()).hexdigest()
  return h

if __name__ == '__main__':
  # Initialize a list to store all potential keys and our salt
  keys = []
  salt = 'ngcjuoqr'
  idx = 0
  # Generate 64 valid keys
  while len([k for k in keys if k.valid == True]) <= 64:
    # Get the hast to test against
    h = get_hash(salt, idx)
    # Match triplets and quintuplets of any character in the hash
    m3 = re.search(r'(.)\1\1', h)
    m5 = re.search(r'(.)\1\1\1\1', h)
    # We have to check for quintuplets first, otherwise we get false positives
    # if we have a hash that contains both a triplet and a quintuplet
    if m5 is not None:
      for k in keys:
        if k.check and k.seq == m3.group(0):
          k.check_seq(idx, m5.group(0))
    # If we have a triplet, add it as a potential key
    if m3 is not None:
      keys.append(Key(idx, m3.group(0)))
    idx += 1
  # Pull our 64 valid keys and show the index where the last key was found
  keys = [k for k in keys if k.valid][:64]
  print('Last key found at {0}.'.format(keys[-1].idx))
