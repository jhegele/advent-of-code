# Day 08

https://adventofcode.com/2023/day/8

## Part 1

Pretty straightforward for part 1 today. We have a starting node (`AAA`) and we need to get to an end node (`ZZZ`) following a map that we've been provided. The twist is that we've also been provided a set of left/right directions that we have to follow in order to reach `ZZZ`. These left right directions are provided as a finite set but are treated as though they are repeated infinitely.

The approach here is just to use a dictionary where the key is the node you are at and the value is the two nodes that are connected. I chose to use a tuple for this so my dictionary ended up looking something like this:

```python
{
  "AAA": ("BBB", "CCC"),
  "BBB": ("DDD", "ZZZ")
}
```

This makes it easy for me to quickly pull the two nodes that my current node can reach and then I can just use the provided left/right directions to determine which one to pick. Once that's done, it's just a matter of looping over the directions, stepping to the next node, and counting the steps taken. Once you arrive at node `ZZZ`, just return the number of steps and there's your answer.

## Part 2

Part 2 generally uses the same logic as part 1 but the new twist is that you now have multiple different starting nodes and you need to move them simultaneously until all of them arrive at an end node (i.e. all of them arrive at an end node at the same time, so if one of them is at an end node and the others aren't, you keep moving all of the nodes). The provided sample is small enough that it's brute forceable so that's where I started but it became pretty obvious that the input surface area was way, way too large to brute force.

So, to make this problem doable, let's simplify things for a moment. Assume we have three starting nodes: AAA, BBB, and CCC. If we follow the logic we used in part 1 for node AAA, it arrives at an end node in 2 steps. If we do the same for nodes BBB and CCC, they arrive at end nodes in 3 steps and 4 steps, respectively. So we have start nodes that require 2, 3, and 4 steps if they are run independently.

For part 2, we need these three nodes to all arrive at their respective end nodes on the same step. If you think back to math classes, there's a concept that deals with this very problem! You probably first come across this concept when you're learning about adding fractions. Adding fractions with equivalent denominators is pretty easy: `1/4 + 1/4 = 2/4`. But what happened when you needed to add `1/2 + 1/3 + 1/4`? You had to find the lowest common denominator. That concept is also called least common multiple (LCM) in math (it's lowest common denominator for fractions, specifically but it's the same thing).

If we find the least common multiple for our nodes (2 steps, 3 steps, 4 steps) we would find that they would all simultaneously reach end nodes on step 12 and that would be our answer. Naturally, our puzzle answer is going to be much, much higher but that's the concept we need to use. For my input, the answer ended up being over 13 trillion which, in retrospect, is easy to see why I couldn't brute force it.

_ADDENDUM:_ To clarify, while LCM works here, it's not safe to assume that LCM will _always_ work for this type of problem. Within the context of Advent of Code, it's safe to assume and try it but for LCM to actually work we need to make some assumptions that are covered in a lot of detail in this thread: https://www.reddit.com/r/adventofcode/comments/18dfpub/2023_day_8_part_2_why_is_spoiler_correct/. All that said, I think the context of knowing that AoC is a solvable puzzle and that the inputs are purposely crafted for the problem makes it reasonable to try LCM without first validating all of the underlying assumptions.
