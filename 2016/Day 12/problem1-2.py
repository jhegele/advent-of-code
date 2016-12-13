class Register(object):
  """Register object to store value and state"""

  def __init__(self):
    self.value = 0

  def copy(self, to_copy):
    self.value = int(to_copy)

  def inc(self):
    self.value += 1

  def dec(self):
    self.value -= 1

# Part 1
# instructions = []
# Part 2 -- Initialize C to 1 at the start
instructions = ['cpy 1 c']
with open('input.txt','r') as input_file:
  # Load all the instructions
  for line in input_file:
    instructions.append(line.strip())

idx = 0
registers = {
  'a' : Register(),
  'b' : Register(),
  'c' : Register(),
  'd' : Register()
}
# Loop through instructions
while idx < len(instructions):
  i = instructions[idx].split(' ')
  if i[0] == 'cpy':
    registers[i[2]].value = registers[i[1]].value if i[1] in [k for k, v in registers.items()] else int(i[1])
  if i[0] == 'inc':
    registers[i[1]].inc()
  if i[0] == 'dec':
    registers[i[1]].dec()
  if i[0] == 'jnz':
    if i[1] in [k for k, v in registers.items()]:
      j = registers[i[1]].value
    else:
      j = int(i[1])
    idx += int(i[2]) - 1 if j != 0 else 0
  idx += 1

# Print value from register A
print('Register A Value: {0}'.format(registers['a'].value))
