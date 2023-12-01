# Day 01

https://adventofcode.com/2023/day/1

## Notes

These days I write a lot more Typescript than I do Python so trying to knock some of the rust off was an adventure itself. Might revisit this in a few days to optimize some things as I think my rustiness shows a bit here.

## Part 1

My first instinct here was to use regex to pull out all the numeric values from each line. I felt like that was overkill (which ultimately came back to bite me when I did part 2) so I, instead, stripped out all of the alpha characters from the string so that only the digits remained.

From there, it's pretty straightforward to just pull the first and last digit, smash them together, parse the value as an integer and add it to the cumulative total.

## Part 2

...and then the wheels fell off. At first glance, I thought I could pretty easily brute force this one by replacing all string values with their equivalent number values. But that falls apart completely in the sample data. I was doing replacements in order (so `'one'` became `'1'`, then `'two'` became `'2'`, etc). If you use that logic on line 2 of the example: `eightwothree` the progression looks like this:

1. `eightwothree`
2. `eigh2three`
3. `eigh23`

The eight never gets replaced because it shares its last letter `t` with the first letter of `two`. So, clearly the brute force approach doesn't work here and we need to keep the original string intact as we search for each individual numeric word. Additionally, we also need to make sure we're keeping all of the characters that are already digits.

I took a two step approach to do this. For each line, here is the process I used:

1. Use regex to find all numeric characters **and** their indices in the string and append them to a list
2. Find all numeric words (i.e. `one` or `two`) and their indices in the string and append the numeric equivalent (`one` becomes `1`, e.g.) along with the starting position of the original numeric word to the same list
3. Sort the list by index values so that the order matches the original string
4. Pull the first and last value from the list
5. Smash the values together
6. Parse as an integer
7. Add to cumulative total
