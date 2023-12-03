# Day 03

https://adventofcode.com/2023/day/3

## Notes

Feels like AoC is ramping up the complexity and difficulty quickly this year! It's only day 3 and I easily spent 5 mins just thinking about how to approach this problem.

## Part 1

I spent a while thinking about how to effectively parse the input for this problem. I considered stripping out all periods and replacing them with spaces and then grabbing the values. I considered going character by character and just grabbing non period characters. I'm sure there were a few other approaches that I mulled over before ultimately falling back on just using regex.

At first, I thought I had devised a brilliant approach to use a multiline regex and parse the entire input in one go since I can use `re.finditer()` to get matches and positions in the string. But I didn't consider that doing this means I need some non-intuitive (or less intuitive) means of tracking my `y` (i.e. vertical) position. I'd have to count the number of line breaks or something and that seemed messier than just going line by line where I could use the line index as my `y` coordinate.

My initial parsing strategy broke the coordinates out into a single `y` coordinate (since any one value appears only on a single line) and a list of `x` values covered by the value. For symbols, `x` would (probably?) always be a list of length 1 but numeric values could have any length. This approach ultimately made it more of a pain when I needed to do things like find overlapping coordinates. So I ultimately settled on using a list of `x`, `y` pairs for each value.

I did have the foresight to include an `is_numeric` flag when I was parsing the data. That made things like filtering to numeric values only much easier.

Once the parsing step was done, the approach was faily straightforward in that I needed to check every numeric value to see if it had at least one adjacent symbol. My implementation is pretty brute force and horribly optimized. It took a few seconds to run on the full input but, hey, it worked.

## Part 2

Because of the data structure that I landed on, part 2 was easier and faster than part 1. The set of gears (`*` symbols) is likely much smaller than the set of numeric values. So iterating over those and finding the ones with exactly two adjacent numeric values was pretty quick and easy.
