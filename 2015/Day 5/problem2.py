def nice(s):
  # Initialize lists to hold the bigrams and trigrams from our string
  bigram = []
  trigram = []
  has_b = False
  has_t = False
  idx = 0
  # Build bigram/trigrams from the string
  while idx < len(s) - 1:
    bigram.append(s[idx:idx + 2])
    idx += 1
  idx = 0
  while idx < len(s) - 2:
    trigram.append(s[idx:idx + 3])
    idx += 1
  for b in bigram:
    # If any bigram appears at least twice, we can move on
    if s.count(b) >= 2:
      has_b = True
      break
  for t in trigram:
    # If any trigram has the same start and end letter, we can move on
    if t[0] == t[2]:
      has_t = True
      break
  # True only if we pass the bigram and trigram rules
  return has_b and has_t

if __name__ == '__main__':
  results = []
  with open('input.txt', 'r') as input_file:
    for line in input_file:
      # Check each input line to see if it's nice
      if nice(line):
        results.append(line)
  # Print the total number of nice lines
  print('There are {0} nice strings.'.format(len(results)))
