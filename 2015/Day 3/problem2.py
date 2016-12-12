class Santa(object):

  def __init__(self):
    self.x = 0
    self.y = 0
    self.visits = ['{0}, {1}'.format(self.x, self.y)]

  def move(self, direction):
    if direction == '^':
      self.y += 1
    elif direction == 'v':
      self.y += -1
    elif direction == '>':
      self.x += 1
    else:
      self.x += -1
    self.visits.append('{0}, {1}'.format(self.x, self.y))

with open('input.txt', 'r') as input_file:
  directions = input_file.read()

count = 1
santa = Santa()
robo_santa = Santa()
for d in directions:
  if count % 2 == 0:
    robo_santa.move(d)
  else:
    santa.move(d)
  count += 1

print(len(set(santa.visits + robo_santa.visits)))
