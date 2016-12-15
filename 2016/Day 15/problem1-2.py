"""
Problem input:
Disc #1 has 7 positions; at time=0, it is at position 0.
Disc #2 has 13 positions; at time=0, it is at position 0.
Disc #3 has 3 positions; at time=0, it is at position 2.
Disc #4 has 5 positions; at time=0, it is at position 2.
Disc #5 has 17 positions; at time=0, it is at position 0.
Disc #6 has 19 positions; at time=0, it is at position 7.
"""

# Flag to enable part 2
part2 = False

class Disc(object):
  """Object to represent a disc with a given order, total number of positions,
  and the value of the current position.
  """

  def __init__(self, order, total_pos, curr_pos):
    self.order = order
    self.total_pos = total_pos
    self.curr_pos = curr_pos

  def check(self, t):
    """Pass in the time that the capsule is released and check if thie
    disc is in position 0 at the time the capsule reaches it."""
    return (t + self.order + self.curr_pos) % self.total_pos == 0

# Our array of discs
discs = [
  Disc(1, 7, 0),
  Disc(2, 13, 0),
  Disc(3, 3, 2),
  Disc(4, 5, 2),
  Disc(5, 17, 0),
  Disc(6, 19, 7)
]

# Add a 7th disc for part 2
if part2:
  discs.append(Disc(7, 11, 0))

# Since we our largest disc must always be in the right position, we can
# just incremement by the largest size
ls = max([d.total_pos for d in discs])
# This optimization also means we need to move time forward enough to
# get the largest disc back to position 0 when the capsule hits
t = [d.total_pos - d.curr_pos - d.order for d in discs if d.total_pos == ls][0]
# Brute force is and iterate over time until everything is aligned
while not all([d.check(t) for d in discs]):
  t += ls

print('Press the button at t={0}.'.format(t))
