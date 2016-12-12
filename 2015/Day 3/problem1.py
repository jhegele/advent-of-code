with open('input.txt', 'r') as input_file:
  directions = input_file.read()

coords = [0, 0]
visits = []
visits.append('{0}, {1}'.format(coords[0], coords[1]))

for d in directions:
  if d == '^':
    coords = [coords[0], coords[1] + 1]
  elif d == 'v':
    coords = [coords[0], coords[1] - 1]
  elif d == '>':
    coords = [coords[0] + 1, coords[1]]
  elif d == '<':
    coords = [coords[0] - 1, coords[1]]
  visits.append('{0}, {1}'.format(coords[0], coords[1]))

print(len(set(visits)))
