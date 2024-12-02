from itertools import pairwise

with open("day02.input", "r") as f: 
  lines = [list(map(int, l.split())) for l in f.readlines()]

'''
Check that all vals share the same sign (positive or negative)
'''
def same_sign(line_diffs: list[int]):
  count_neg = sum([1 for v in line_diffs if v < 0])
  return count_neg == len(line_diffs) or count_neg == 0

'''
Check that all vals increase or decrease by safe amounts (between 1 and 3)
'''
def safe_change(line_diffs: list[int]):
  safe_changes = len([1 for v in line_diffs if abs(v) >= 1 and abs(v) <= 3])
  return safe_changes == len(line_diffs)

def part1(lines: list[list[int]]):
  safe = 0
  for line in lines:
    diffs = [a - b for (a, b) in pairwise(line)]
    if same_sign(diffs) and safe_change(diffs):
      safe += 1
  return safe

def part2(lines: list[list[int]]):
  safe = 0
  for line in lines:
    diffs = [a - b for (a, b) in pairwise(line)]
    if same_sign(diffs) and safe_change(diffs):
      safe += 1
    else:
      for i in range(len(line)):
        new_line = [v for idx, v in enumerate(line) if idx != i]
        new_diffs = [a - b for (a, b) in pairwise(new_line)]
        if same_sign(new_diffs) and safe_change(new_diffs):
          safe += 1
          break
  return safe
        
print('Part 1: {}'.format(part1(lines)))
print('Part 2: {}'.format(part2(lines)))