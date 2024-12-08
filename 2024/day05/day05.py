from functools import cmp_to_key

with open("day05.input", "r") as f:
  text = f.read()
  rules_raw, pages_raw = text.split('\n\n')
  rules = [tuple(r.split('|')) for r in rules_raw.split('\n')]
  pages_list = [p.split(',') for p in pages_raw.split('\n')]

def compare(a: str, b: str):
  return -1 if (a, b) in rules else 1 if (b, a) in rules else 0

def part1():
  total = 0
  for pages in pages_list:
    sorted_pages = sorted(pages, key=cmp_to_key(compare))
    if (pages == sorted_pages):
      middle_idx = len(pages)//2
      total += int(pages[middle_idx])
  return total

def part2():
  total = 0
  for pages in pages_list:
    sorted_pages = sorted(pages, key=cmp_to_key(compare))
    if (pages != sorted_pages):
      middle_idx = len(sorted_pages)//2
      total += int(sorted_pages[middle_idx])
  return total


print('Part 1: {}'.format(part1()))
print('Part 2: {}'.format(part2()))
