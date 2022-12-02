values = {
  'rock': 1,
  'paper': 2,
  'scissors': 3,
  'lose': 0,
  'draw': 3,
  'win': 6
}

def get_data(path):
  with open(path, 'r') as f:
    lines = [l.strip().split() for l in f.readlines()]
  return lines

def p1():
  def score(round):
    opp, me = round
    if me == 'X':
      played = 'rock'
      if opp == 'A':
        result = 'draw'
      if opp == 'B':
        result = 'lose'
      if opp == 'C':
        result = 'win'
    if me == 'Y':
      played = 'paper'
      if opp == 'A':
        result = 'win'
      if opp == 'B':
        result = 'draw'
      if opp == 'C':
        result = 'lose'
    if me == 'Z':
      played = 'scissors'
      if opp == 'A':
        result = 'lose'
      if opp == 'B':
        result = 'win'
      if opp == 'C':
        result = 'draw'
    return values[played] + values[result]

  rounds = get_data("input.txt")
  total = sum([score(r) for r in rounds])
  return total

def p2():
  def score(round):
    opp, res = round
    if opp == 'A':
      if res == 'X':
        played = 'scissors'
        result = 'lose'
      if res == 'Y':
        played = 'rock'
        result = 'draw'
      if res == 'Z':
        played = 'paper'
        result = 'win'
    if opp == 'B':
      if res == 'X':
        played = 'rock'
        result = 'lose'
      if res == 'Y':
        played = 'paper'
        result = 'draw'
      if res == 'Z':
        played = 'scissors'
        result = 'win'
    if opp == 'C':
      if res == 'X':
        played = 'paper'
        result = 'lose'
      if res == 'Y':
        played = 'scissors'
        result = 'draw'
      if res == 'Z':
        played = 'rock'
        result = 'win'
    return values[played] + values[result]
  rounds = get_data('input.txt')
  total = sum([score(r) for r in rounds])
  return total

print('Part 1: {}'.format(p1()))
print('Part 2: {}'.format(p2()))