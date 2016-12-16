import re

# Flag to enable part 2
part2 = False

# Build our array of lights
lights = [[0 for i in range(0, 1000)] for i in range(0, 1000)]

def inst(cmd, f, t):
  """Handle instructions"""
  # Get coords
  f = [int(i) for i in f.split(',')]
  t = [int(i) for i in t.split(',')]
  for idx in range(f[1], t[1] + 1):
    for jdx in range(f[0], t[0] + 1):
      if cmd == 'turn on':
        v = 1 if not part2 else lights[idx][jdx] + 1
      if cmd == 'turn off':
        v = 0 if not part2 else max(lights[idx][jdx] - 1, 0)
      if cmd == 'toggle':
        v = abs(lights[idx][jdx] - 1) if not part2 else lights[idx][jdx] + 2
      lights[idx][jdx] = v

with open('input.txt', 'r') as input_file:
  # Loop through instructions in file
  for line in input_file:
    # Parse the instructions line
    m = re.search(r'(turn off|turn on|toggle) (\d+,\d+) through (\d+,\d+)', line)
    inst(m.group(1), m.group(2), m.group(3))

# Print the answer
if not part2:
  print('There are {0} lights on.'.format(sum([sum(i) for i in lights])))
else:
  print('Total brightness is {0}.'.format(sum([sum(i) for i in lights])))
