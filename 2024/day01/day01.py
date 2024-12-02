with open("day01.input", "r") as f:
  lines = [l.strip() for l in f.readlines()]

# part 1
def part1(left: list[int], right: list[int]):
  left.sort()
  right.sort()
  distance = 0
  for idx, lval in enumerate(left):
    distance += abs(lval - right[idx])
  return distance

# part 2
def part2(left: list[int], right: list[int]):
  similarities = []
  for val in left:
    occ = len([v for v in right if v == val])
    similarities.append(val * occ)
  return sum(similarities)

left = []
right = []
for line in lines:
  l, r = line.split('   ')
  left.append(int(l))
  right.append(int(r))

print('Part 1: {}'.format(part1(left, right)))
print('Part 2: {}'.format(part2(left, right)))