import hashlib

def find_checksum(puzzle_input, leading_zeroes):
  answer = None
  i = 1
  while answer == None:
    h = hashlib.md5('{0}{1}'.format(puzzle_input, i).encode()).hexdigest()
    answer = i if h[:leading_zeroes] == ''.join(['0' for i in range(0, leading_zeroes)]) else None
    i += 1
  print('Answer: {0}'.format(answer))

if __name__ == '__main__':
  puzzle_input = 'ckczppom'
  # Problem 1
  find_checksum(puzzle_input, 5)
  # Problem 2
  find_checksum(puzzle_input, 6)
