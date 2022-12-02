from functools import reduce

def get_data(path_to_data):
  with open(path_to_data, 'r') as f:
    groups = f.read().split('\n\n')
    elves = [list(map(int, g.split('\n'))) for g in groups]
  return elves

def p1():
  elves = get_data("input.txt")
  total_cals = [reduce(lambda a, b: a + b, e) for e in elves]
  total_cals.sort(reverse=True)
  print('Part 1: {}'.format(total_cals[0]))

def p2():
  elves = get_data("input.txt")
  total_cals = [reduce(lambda a, b: a + b, e) for e in elves]
  total_cals.sort(reverse=True)
  print('Part 2: {}'.format(total_cals[0] + total_cals[1] + total_cals[2]))

p1()
p2()