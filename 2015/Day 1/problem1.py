with open('input.txt', 'r') as input_file:
  instructions = input_file.read()

floor = sum([1 for i in instructions if i == '(']) + sum([-1 for i in instructions if i == ')'])
print('Floor {0}'.format(floor))
