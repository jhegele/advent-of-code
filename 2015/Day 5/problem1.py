def nice(s):
  # Initialize bad combos and vowels
  bad = ['ab', 'cd', 'pq', 'xy']
  vowels = ['a', 'e', 'i', 'o', 'u']
  if sum([1 if b in s else 0 for b in bad]) > 0:
    # If there is 1 or more bad combos, it's a naughty string
    return False
  if sum([s.count(v) for v in vowels]) < 3:
    # If there are fewer than 3 vowels, it's a naughty string
    return False
  idx = 0
  while idx < len(s) - 1:
    # If the string contains one double letter, it's nice
    if s[idx] == s[idx + 1]:
      return True
    idx += 1
  return False

if __name__ == '__main__':
  results = []
  with open('input.txt', 'r') as input_file:
    for line in input_file:
      # Check each input line to see if it's nice
      if nice(line):
        results.append(line)
  # Print the total number of nice lines
  print('There are {0} nice strings.'.format(len(results)))
