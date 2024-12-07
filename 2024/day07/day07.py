from itertools import product

with open("day07.input", "r") as f:
  lines = []
  for l in f.readlines():
    test, inputs = l.split(": ")
    lines.append((int(test), list(map(int, inputs.split()))))

def get_result(operation: int, left: int, right: int):
  # add
  if operation == 1:
    return left + right
  # multiply
  if operation == 2:
    return left * right
  # concatenate
  if operation == 3:
    return int('{}{}'.format(left, right))

def create_test_value(test: int, inputs: list[int], operators: list[int]):
  # use cartesian product to generate all possible combinations of operations. we will
  # always need len(inputs) - 1 operations.
  ops = product(*[operators for _ in range(len(inputs) - 1)])
  for op in ops:
    # each line must have at least two inputs, so initialize the running total using
    # the first two values
    total = get_result(op[0], inputs[0], inputs[1])
    # loop through remaining values and update the total
    for input_idx in range(2, len(inputs)):
      total = get_result(op[input_idx - 1], total, inputs[input_idx])
    # if our total matches the test value, return the test value to make it easy to
    # keep a running sum of matched values
    if total == test:
      return test
  # if there's no match, return a 0 so that we can just naively add all returned
  # values
  return 0

def part1(lines: list[tuple[int, list[int]]]):
  # we only have two operators for part 1: 1 = addition, 2 = multiplication
  return sum([create_test_value(test, inputs, [1, 2]) for test, inputs in lines])

def part2(lines: list[tuple[int, list[int]]]):
  # part 2 introduces a third operator: 3 = concatenation
  return sum([create_test_value(test, inputs, [1, 2, 3]) for test, inputs in lines])

print('Part 1: {}'.format(part1(lines)))
print('Part 2: {}'.format(part2(lines)))