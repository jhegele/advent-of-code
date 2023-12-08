# Day 07

https://adventofcode.com/2023/day/7

**NOT YET COMPLETE**

## Notes

I need to come back to this and finish up part 2. I'm pretty sure I have a good approach laid out, just need to implement it.

## Part 1

As someone who enjoys poker, this was pretty fun to think through. It's simpler than poker (mercifully) but a fun thought experiment nonetheless. The key moment, for me, was realizing that I could represent a hand as a combination of it's overall hand value (5-of-a-kind, 4-of-a-kind, full house, etc) and the individual cards in the hand as a series of characters and then use Pythons native sort functionality to properly order the hands by their strength.

If we consider Python's string sorting, numeric characters (i.e. `"0", "1", "2", ...`) are sorted before alpha characters (i.e. `"A", "B", "C", ...`). So, we can represent the various hand values as:

- 5-of-a-kind: `"0"`
- 4-of-a-kind: `"1"`
- full house: `"2"`
- 3-of-a-kind: `"3"`
- 2 pairs: `"4"`
- 1 pair: `"5"`
- high card: `"6"`

We can use the same logic for card values where:

- Ace: `"0"`
- King: `"1"`
- ...
- 2: `"C"`

Note that, because we have 13 cards, we go through the numeric characters `0-9` then we use alpha characters `A-C`.

A specific hand can then be represented as a single 6 character string where the first character is the hand value and the subsequent characters are card values. So, a hand like `"KKKKQ"` would turn into `"111112` because it is four of a kind (the first `"1"`), there are four kings `"1111"` followed by one queen `"2"`. Once we have our string representations for every hand, we just use string sorting and we're all set!

## Part 2

Part 2 repurposes jacks (`"J"`) as jokers. A joker can take the value of any card in order to make the hand as strong as possible. I haven't completed this part yet but the approach I'm going to take is to leverage the same logic as above but, for hands with jokers, I'll just create all of the possible hands, take the strongest and use that in place of the original hand.
