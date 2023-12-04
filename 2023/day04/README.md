# Day 04

https://adventofcode.com/2023/day/4

## Notes

The toughest part of this puzzle, for me, was the instructions. It's a somewhat convoluted instruction set for both parts (though for different reasons for each part). For part 2, it's also easy to get trapped in an approach that will make your code execution painfully slow. On top of all that, something weird happened with my logic for part 2 and I was getting the right answer for the sample and wrong answer for the real data. I made a slight change to how I was performing a check in my code and all of a sudden, it worked. It shouldn't have made a difference but it did. Just one of those things I guess.

## Part 1

We have a pile of scratchcards, each one with a set of card numbers and a set of winning numbers. Each card has a point value that is determined by the number of matches that exist between the card numbers and winning numbers. The only nuance here is that the first match is worth 1 point and every subsequent match doubles the point value. At first I thought this meant that every subsequent match was worth 2 points but that's not correct. Here are the point values for 0 through 5 matches:

0. 0
1. 1
2. 2
3. 4
4. 8
5. 16

Once you have that figured out (it's basically `2^n` where `n` is the number of matches) it's fairly straightforward. I used Python sets to find the intersection of the card numbers and the winning numbers. This approach **could** have been disastrous if there were any repeated numbers in either the card numbers or winning numbers, but that's (thankfully) not the case here.

## Part 2

For part 2, we ignore points completely and the instructions get far more complicated. The basic premise is that we still have our pile of cards. For a given card, we calculate the number of matches (N) that exist between card numbers and winning numbers. You then duplicate the N cards that follow the card you're looking at. For example, if we're looking at the 5th card and it has four matching numbers, we duplicate the 6th, 7th, 8th, and 9th cards.

Continuing with our example, when we get to the 6th card we now have two cards because we just duplicated it when we processed the 5th card. So we have to look at the 6th card twice. Each time we look at it, the same duplication rules apply. So if the 6th card has 2 matches, we end up duplicating the 7th and 8th cards twice. This goes on and on until you reach the end of the pile.

There are at least two approaches to solving this. The first approach is to use recursion since we're recursively duplicating cards. While this works, it will take forever to run the code on the full input because your final answer is going to be 8 to 9 million cards and you're stepping through each one of them. But, there's a better way!

The key to getting this to run performantly is to realize that there is no need to step through each card at a given position. If you're at the 100th card, you may have 100,000 cards (1 original and 99,999 duplicates). Because they are all the same card, you only have to find how many matches exist for one of them. That tells you that you need to duplicate the following N cards. Because you know that you have 100,000 instances of the 100th card, you know that you're going to duplicate the following N cards 100,000 times each. So, you can set up a list that represents the number of cards in each position and initialize it with a value of 1 at each spot. As you step through each card, just increment the positions that follow in your list by however many cards are at your current position. When you get to the end, just sum up the list and there's your answer.
