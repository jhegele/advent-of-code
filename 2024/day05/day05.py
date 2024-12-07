from typing import NamedTuple, Set

class Rule(NamedTuple):
  before: Set[int]
  after: Set[int]

with open("sample.input", "r") as f:
  text = f.read()
  rules_raw, instructions_raw = text.split("\n\n")
  rules = [tuple(map(int, line.split("|"))) for line in rules_raw.split("\n")]
  instructions = [list(map(int, line.split(","))) for line in instructions_raw.split("\n")]

def parse_rules(rules: list[tuple[int, int]]):
  parsed: dict[int, Rule] = {}
  for rule in rules:
    a, b = rule
    if a not in parsed:
      parsed[a] = Rule(before=set(), after=set())
    if b not in parsed:
      parsed[b] = Rule(before=set(), after=set())
    parsed[a].before.add(b)
    parsed[b].after.add(a)
  return parsed

def is_valid(idx: int, instructions: list[int], rules: list[tuple[int, int]]):
  val = instructions[idx]
  before = instructions[:idx]
  for i in before:
    print(i)
    if val in rules[i].before:
      return False
  return True

def part1(rules: list[tuple[int, int]], instructions: list[list[int]]):
  parsed = parse_rules(rules)
  for instruction in instructions:
    valid = [is_valid(idx, instruction, parsed) for idx, i in enumerate(instruction)]
    print(valid)

  
print(rules)
print(part1(rules, instructions))