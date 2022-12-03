import string

# build a list of lowercase and uppercase letters so we can use the
# indices for prioritization lookups
priorities = [*string.ascii_lowercase, *string.ascii_uppercase]

def get_rucksacks(path):
    with open(path, 'r') as f:
        rucksacks = []
        for line in f.readlines():
            # divide each rucksack into a tuple of compartments
            midpoint = len(line) // 2
            compartments = (line[:midpoint].strip(), line[midpoint:].strip())
            rucksacks.append(compartments)
    return rucksacks

def p1():
    rucksacks = get_rucksacks("input.txt")
    all_priorities = []
    for comp1, comp2 in rucksacks:
        # use set intersections to find duplicates between compartments
        dups = list(set(comp1).intersection(set(comp2)))
        # map duplicates to their priorities
        dups_priorities = map(lambda d: priorities.index(d) + 1, dups)
        all_priorities.append(*dups_priorities)
    return sum(all_priorities)

def p2():
    rucksacks = get_rucksacks("input.txt")
    # turns out, we probably shouldn't have split the compartments in
    # the get_rucksacks function. we break rucksacks into groups of 3
    # and rejoin the compartments
    elf_groups = [[''.join(r) for r in rucksacks[i:i+3]] for i in range(0, len(rucksacks), 3)]
    all_priorities = []
    for elf1, elf2, elf3 in elf_groups:
        dups = list(set(elf1).intersection(set(elf2)).intersection(set(elf3)))
        dups_priorities = map(lambda d: priorities.index(d) + 1, dups)
        all_priorities.append(*dups_priorities)
    return sum(all_priorities)

print('Part 1: ', p1())
print('Part 2: ', p2())