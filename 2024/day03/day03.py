import re

with open("day03.input", "r") as f:
  memory = f.read()

def part2(mem: str):
  re_valid = r"mul\((\d{1,3}),(\d{1,3})\)|don\'t\(\)|do\(\)"
  enabled = True
  total = 0
  for match in re.finditer(re_valid, mem):
    val = match.group(0)
    if val == "do()":
      enabled = True
    elif val == "don't()":
      enabled = False
    else:
      if enabled:
        a, b = int(match.group(1)), int(match.group(2))
        total += (a * b)
  return total

def part1(mem: str):
  re_valid = r"mul\((\d{1,3}),(\d{1,3})\)"
  total = 0
  for match in re.finditer(re_valid, mem):
    a, b = int(match.group(1)), int(match.group(2))
    total += (a * b)
  return total

print('Part 1: {}'.format(part1(memory)))
print('Part 2: {}'.format(part2(memory)))