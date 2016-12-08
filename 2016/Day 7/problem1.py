"""Advent of Code, Day 7
Problem: 1
http://adventofcode.com/2016/day/7
"""

import re

# Pattern to match any information inside brackets "[]"
re_bracketed = r'\[([a-z]+)\]'

def sequence_mirror(sequence):
  """Test whether a sequence of 4 characters is a palindrom ("abba", e.g.)"""
  if (sequence[:1] == sequence[3:]) and (sequence[1:2] == sequence[2:3]):
    if sequence[:1] != sequence[1:2]:
      return True
  return False

def sequence_contains_mirror(sequence_list):
  """Given a long sequence, does it contain ANY 4 character palindromes? """
  for sequence in sequence_list:
    if len(sequence) >= 4:
      last_char = 4
      # Iterate over the sequence 4 characters at a time
      while last_char <= len(sequence):
        sample = sequence[last_char-4:last_char]
        if sequence_mirror(sample):
          # We only need to find a single 4 character palindrome
          return True
        last_char += 1
  return False

def ip_is_tls(ip):
  """Does a given IP sequence support TLS?"""
  # Initialize content that is outside/inside brackets
  outside = ip
  inside = re.findall(re_bracketed, ip)
  if len(inside) > 0:
    # If we have characters inside brackets, strip those out of the original
    # string
    for sequence in inside:
      outside = outside.replace('[{0}]'.format(sequence),' ')
    if sequence_contains_mirror(inside):
      return False
  if not sequence_contains_mirror([outside]):
    return False
  return True

with open('input.txt', 'r') as input_file:
  total_tls = 0
  for ip in input_file:
    if ip_is_tls(ip):
      total_tls += 1
  print('There are {0} TLS addresses.'.format(total_tls))
