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