class Present(object):

  def __init__(self, dims):
    self.l = int(dims.split('x')[0])
    self.w = int(dims.split('x')[1])
    self.h = int(dims.split('x')[2])

  def sq_ft(self):
    return (2 * self.l * self.w) + (2 * self.w * self.h) + (2 * self.h * self.l) + min([self.l * self.w, self.w * self.h, self.h * self.l])

presents = []
with open('input.txt', 'r') as input_file:
  for line in input_file:
    presents.append(Present(line))

print('Square feet: {0}'.format(sum([p.sq_ft() for p in presents])))
