with open('input.txt', 'r') as input_file:
  instructions = input_file.read()

floor = 0
idx = 0
while floor >= 0:
  floor += 1 if instructions[idx] == '(' else -1
  idx += 1

print('Position {0}'.format(idx))
