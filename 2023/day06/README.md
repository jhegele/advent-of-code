# Day 06

https://adventofcode.com/2023/day/6

# Notes

I'm assuming that Advent of Code decided to switch up the way difficulty is handled this year because, so far, the odd number days (1, 3, and 5) have been far more brutal than the even numbered days. Today was no exception. After feeling like I smashed my head against my desk for way too long yesterday I gave up on Part 2 (though I'm hoping to come back to it). Today I got both parts in about 15 minutes.

# Part 1

I spent a little time thinking about how I might optimize my approach here as I expected Part 2 to throw a wrench into my plans and increase the surface area of the problem exponentially (which it did). Ultimately I decided to just brute force it and optimize for Part 2 if I needed to.

In terms of how I considered optimizing, I think there's a way to calculate the lower bound that would create a winning run if you divide `distance + 1 / time`. I struggled to come up with something similar for calculating the upper bound but, intuitively, I feel like there's a way to do something similar to get an upper bound. Once you have the bounds, then you know how many ways you can win: `upper bound - lower bound + 1` (I think you'd need the plus one as the range should be inclusive of the boundaries). Anyways, I decided not to tinker with this approach and just dive in.

As expected, Part 1 was pretty easy with the brute force approach.

# Part 2

Well, that wrench that I was expecting was certainly thrown but, mercifully, it wasn't a huge wrench and brute force still worked. Took maybe 5-7 seconds to get the answer but I'll take it.

It's an interesting math optimization problem so maybe I'll come back to revist this one in the future.
