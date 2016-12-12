class Present(object):

  def __init__(self, dims):
    self.l = int(dims.split('x')[0])
    self.w = int(dims.split('x')[1])
    self.h = int(dims.split('x')[2])

  def sq_ft(self):
    sides = [self.l, self.w, self.h]
    return (sorted(sides)[0] * 2) + (sorted(sides)[1] * 2) + (self.l * self.w * self.h)

presents = []
with open('input.txt', 'r') as input_file:
  for line in input_file:
    presents.append(Present(line))

print('Square feet: {0}'.format(sum([p.sq_ft() for p in presents])))
