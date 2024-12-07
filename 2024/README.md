# Advent of Code 2024

## [Day 01](https://adventofcode.com/2024/day/1)
Day 1 was a pretty straightforward puzzle to start with. You're given two lists and you need to compare/utilize the values in each list in different ways between the two parts.

Parsing the input was probably the most difficult part of day 1. The fact that there are three spaces between the values tripped me up initially and I was concerned I'd have to break out regex. But the three spaces are consistent so we can just split on three spaces instead of one.

### Part 1
For part 1, you first need to sort the lists. Then you compare the elements in each position to find the distance between them (subtract and take the absolute value). Sum the distances and you have your answer.

There are a lot of ways to do this, I just naively looped through one of the lists since I knew that both lists would contain the same number of values. A more elegant solution might have used `zip()` but the simplest approach, for me, was to just loop through one list and use the index to access the correpsonding element from the other list.

### Part 2
For part 2, you iterate through each element in the left list and count the occurrences in the right list. You mulitply the element value from the left list by the number times it occurs in the right list and sum up those values.

Like part 1, there are more elegant ways to solve this but naively iterating through the left list works fine so that's what I went with.

## [Day 02](https://adventofcode.com/2024/day/2)
Day 2 gave us nested lists where each nested list is a report and the sequence of values determines if the report is safe or unsafe. The most notable part of Day 2 is that it introduced me to the handy dandy `pairwise()` function from itertools. `pairwise()` accepts a list and creates a list of adjacent pairs. So, if you have `my_list = [1, 2, 3, 4]`, `pairwise(my_list)` would return `[(1, 2), (2, 3), (3, 4)]`.

### Part 1
There are two criteria that determine whether a single report is safe: the elements continually increase (i.e. 1, 2, 3) or continually decrease (i.e. 3, 2, 1) **and** the absolute delta between two elements is between 1 and 3. I opted to create pretty simple functions that return boolean results for each of these two tests. Once that was done, it was just a matter of iterating throught the reports and counting how many were safe.

### Part 2
Part 2 introduces a twist that allows you to remove any single element from the list and, if removing that element makes the list safe then it can be marked as safe (even if it was unsafe with all of the elements present). My initial thought here was to build a set of heuristics that would make this more efficient. But the input is only 1,000 rows and each row, based on a cursory scan, has fewer than 10 elements. So it's entirely plausible to just brute force this which is what I ended up doing.

I used the same basic approach from Part 1 but, if a list was unsafe in Part 1 I would iterate through the elements in the list, remove the element and then run the tests again. If it came back safe, then the entire list is marked as safe and we move on. This is neither the most time or computationally efficient approach but, it's Day 2 and I haven't written Python at all this year so...yeah.

## [Day 03](https://adventofcode.com/2024/day/3)
Day 3, it's regex time! Looking at the input, I was terrified that I'd have to parse nested instructions but thankfully that wasn't the case. Honestly not too bad if you're familiar with regex.

### Part 1
Fairly straightforward, just need to parse out the multiply instructions from the input string. Plenty of ways to do this but I leaned into regex and used capturing groups to match valid `mul()` instructions *and* capture the two values. Made it a bit easier when it came time to actually multiply them.

### Part 2
This is where I figured I would have to parse nested instructions but mercifully that didn't happen. Really just needed to add a flag to indicate whether multiplication was enabled or not. If you hit a `do()` instruction enabled is flipped on, while hitting a `don't()` instruction flips it off.

## [Day 04](https://adventofcode.com/2024/day/4)
This one was a little more brutal than I anticipated for Day 4. I went through multiple approaches for Part 1 before finally settling on what was my first approach. I'm still not convinced that this was even the best approach, though. I was terrified that the approach I used for Part 1 would end up creating massive headaches for Part 2 but that didn't end up being the case and Part 2 ended up being much quicker which was a bit of a reprieve.

### Part 1
I spent a while thinking about how to approach this problem when I read through it the first time. Finding XMAS in the horizontal and vertical rows was fairly straightforward but accounting for the diagonals was where things would get tricky. I finally settled on an approach where I would just naively create all possible lines (horizontal, vertical, and both diagonal directions -- top left to bottom right, top right to bottom left). Once I had those lines I could just count the instances of "XMAS" or "SAMX".

Creating the diagonal lines ended up being a two-step process which I didn't originally anticipate. But this makes sense if we think about vertical lines from top left to bottom right, as an example. Our starting point, expressed as `(x, y)` coords, for the first diagonal in this direction will be at `(3, 0)` and, from there, we will grab characters at: `(2, 1)`, `(1, 2)`, and `(0, 3)`. Our next starting point will be `(4, 0)` and so on. But at some point our starting point is the point at the top right of the grid and the diagonal we create runs across the middle of the grid. From that point on, our starting point moves to the right side of the grid and we're at `(<max_x>, 1)`. So, creating all of these lines means you need to iterate over starting points at the top of the grid first and then iterate over starting points along the right side.

### Part 2
Using the approach of creating all possible lines for Part 1 made me worried that I would create a massive issue for myself in Part 2 but those worries were unfounded. Part 2 ended up being pretty quick and the key is to realize that any valid "X-MAS" will have A as its center. So just iterate through all of the "A" characters and then find the points to the upper left, upper right, bottom right, and bottom left and see if they are the correct combo of characters to make it valid.

## Day 05

Haven't had a chance o really work on Day 05 yet

## Day 06
Was excited when I saw Part 1 because I love these map-style puzzles where you have to navigate. Part 2 was rough, though. Fairly quickly realized how to optimize the algo but the implementation was a challenge.

### Part 1
The rules here are pretty straightforward. Created a class for the guard and a class for the map, then it's just navigating the guard through the map based on the rules provided.

### Part 2
Part 2 stumped me for a bit. Shortly after I started, I realized that you only need to place obstacles along the path that the guard walked in part 1. That helped to minimize the surface area that I would need to check. But it took me a long time to figure out how to determine if the guard was in a loop. I started out recording the coordinates visited by the guard and counting visits. I set various thresholds (from 3 up to 10000) to determine if a loop existed. This approach worked well for the sample but something about my implementation made it fail on the input.

The breakthrough was realizing that I needed to record not **only** the coordinates visited but also the direction the guard was facing. If the guard passes a single point twice and is facing in the same direction, then he must be in a loop.