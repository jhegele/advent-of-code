"""Advent of Code, Day 7
Problem: 2
http://adventofcode.com/2016/day/7
"""

import re

re_bracketed = r'\[([a-z]+)\]'

def inside_outside_match(inside_seq, outside_seq):
  """Test whether a 3 character sequence from inside brackets pairs with a 3
  character sequence from outside of brackets
  """
  return ((inside_seq[0] == outside_seq[1]) and (inside_seq[1] == outside_seq[2]))

def is_mirror(seq):
  """Does this 3 character sequence follow the form "ABA" or not?"""
  return ((seq[0] == seq[2]) and (seq[0] != seq[1]))

def get_matches(sequences):
  """Given a set of sequences, pull out any 3 character sets that follow the
  form "ABA"
  """
  matches = []
  for sequence in sequences:
    if len(sequence) >= 3:
      last_char = 3
      while last_char <= len(sequence):
        s = sequence[last_char-3:last_char]
        if is_mirror(s):
          matches.append(s)
        last_char += 1
  return matches

def ip_is_ssl(ip):
  """Does a given IP support SSL?"""
  outside = ip
  inside = re.findall(re_bracketed, ip)
  if len(inside) > 0:
    for seq in inside:
      outside = outside.replace(seq, ' ')
  # Get all 3 char sequences that follow the form "ABA" from characters inside
  # and outside brackets
  inside_sequences = get_matches(inside)
  outside_sequences = get_matches([outside])
  # Test all permutations of pairs from inside and outside brackets
  for i_seq in inside_sequences:
    for o_seq in outside_sequences:
      if inside_outside_match(i_seq, o_seq):
        # If we find one match, we can break the loop
        return True
  return False

with open('input.txt', 'r') as input_file:
  total_ssl = 0
  for ip in input_file:
    if ip_is_ssl(ip):
      total_ssl += 1
  print('There are {0} SSL addresses.'.format(total_ssl))
