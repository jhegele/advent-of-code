# Day 02

https://adventofcode.com/2023/day/2

## Part 1

Right away, it's easy to see that the key to solving Part 1 (and likely Part 2) is going to be our ability to parse this data structure into a usable format. From past experience with Advent of Code, the specific format is likely irrelevant but because we know that getting the answer to part 1 will require adding the IDs, we'd benefit from a format that makes math operations somewhat simple.

I elected to break each line into a tuple that looks something like this:

`(id, [(r1, g1, b1), (r2, g2, b2), ..., (rN, gN, bN)])`

In this structure, `r1` refers to the number of red cubes in the first handful, `g1` is the number of green cubes in the first handful, `b1` is the number of blue cubes in the first handful, `r2` is red cubes in the second handful, and so on until you get to N number of handfuls. There are probably a lot more performant ways to parse each line into this structure but I went for the naive / simple approach of using string splitting. It requires several distinct split operations: original line is split into ID and all reveals, all reveals is split into turns, turns is split into red, green, and blue cubes.

Using this structure, it's relatively easy to grab the game ID and the max number of red cubes, green cubes, and blue cubes shows for a given game. That's all we really need to calculate the answer. From there, we just accumulate the valid IDs.

## Part 2

In the past, the data structure I've chosen for part 1 sometimes comes back to bite me when I get to part 2. Thankfully that wasn't an issue today. In fact, the structure and approach that I chose for part 1 allowed me to copy my code to run part 1, make a couple of changes and answer part 2 almost immediately.

For part 2, we're looking for the same data, we're just doing a different calc to get to our answer. Rather than accumulating valid IDs, we take the max red cubes, max green cubes, and max blue cubes and multiply those values. Then we accumulate that result and we have our answer.
