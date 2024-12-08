from typing import NamedTuple
from itertools import combinations

class Antenna(NamedTuple):
  freq: str
  x: int
  y: int

with open("day08.input", "r") as f:
  lines = [l.strip() for l in f.readlines()]

def get_antennas(puzzle_input: list[str]) -> list[Antenna]:
  antennas: list[Antenna] = []
  for y, line in enumerate(puzzle_input):
    for x, char in enumerate(line):
      if char != ".":
        antennas.append(Antenna(char, x, y))
  return antennas

def get_antinodes(ant_a: Antenna, ant_b: Antenna, puzzle_input: list[str], part: int):
  puzzle_max_x = len(puzzle_input[0]) - 1
  puzzle_max_y = len(puzzle_input) - 1
  dist_x = ant_b.x - ant_a.x
  dist_y = ant_b.y - ant_a.y
  # logic is constrainted to a single pair of antinodes for part 1
  if part == 1:
    # node_ab represents directionally a -> b
    node_ab_x, node_ab_y = ant_b.x + dist_x, ant_b.y + dist_y
    # node ba represents directionally b -> a
    node_ba_x, node_ba_y = ant_a.x - dist_x, ant_a.y - dist_y
    # initialize as None since we may end up off the map
    node_ab = None
    # if we're within map bounds, define the node
    if 0 <= node_ab_x <= puzzle_max_x and 0 <= node_ab_y <= puzzle_max_y:
      node_ab = (node_ab_x, node_ab_y)
    node_ba = None
    if 0 <= node_ba_x <= puzzle_max_x and 0 <= node_ba_y <= puzzle_max_y:
      node_ba = (node_ba_x, node_ba_y)
    # return the pair of created nodes (or None if either are off the map)
    return (node_ab, node_ba)
  # for part 2, we create a series of antinodes in line with the anntennas
  else:
    # nodes_ab represents the series of nodes, beginning at b that moves
    # in the a -> direction
    nodes_ab = []
    node_ab = (ant_b.x + dist_x, ant_b.y + dist_y)
    while 0 <= node_ab[0] <= puzzle_max_x and 0 <= node_ab[1] <= puzzle_max_y:
      nodes_ab.append(node_ab)
      node_ab = (node_ab[0] + dist_x, node_ab[1] + dist_y)
    # nodes_ba represents the series of nodes, beginning at a that moves
    # in the b -> a direction
    nodes_ba = []
    node_ba = (ant_a.x - dist_x, ant_a.y - dist_y)
    while 0 <= node_ba[0] <= puzzle_max_x and 0 <= node_ba[1] <= puzzle_max_y:
      nodes_ba.append(node_ba)
      node_ba = (node_ba[0] - dist_x, node_ba[1] - dist_y)
    return nodes_ab + nodes_ba
      

def part1(puzzle_input: list[str]):
  antennas = get_antennas(puzzle_input)
  antinodes = set()
  # iterate over distinct frequencies
  for freq in set([a.freq for a in antennas]):
    antennas_at_freq = [a for a in antennas if a.freq == freq]
    # use combinatorials to compute all possible antenna pairs
    for ant_a, ant_b in combinations(antennas_at_freq, 2):
      # add all antinodes that appear on the map to our set
      antinodes.update([a for a in get_antinodes(ant_a, ant_b, puzzle_input, 1) if a is not None])
  return len(antinodes)

def part2(puzzle_input: list[str]):
  # part2 is a near duplicate of part 1
  antennas = get_antennas(puzzle_input)
  antinodes = set()
  for freq in set([a.freq for a in antennas]):
    antennas_at_freq = [a for a in antennas if a.freq == freq]
    for ant_a, ant_b in combinations(antennas_at_freq, 2):
      # our part 2 logic prevents antinodes being off the map, so no
      # need to filter them out
      antinodes.update(get_antinodes(ant_a, ant_b, puzzle_input, 2))
  # by definition, each antenna will be an antinode so add their
  # locations to our set
  antinodes.update([(a.x, a.y) for a in antennas])
  return len(antinodes)


print('Part 1: {}'.format(part1(lines)))
print('Part 2: {}'.format(part2(lines)))