def get_pairs(path):
    ''' We want to parse the data into a list where each list element contains
    two tuples. Each tuple represents the min and max of the range of sections
    for a single elf. So, if we had the line "2-4, 3-9" it would parse to:
    ((2,4),(3,9)).
    '''
    pairs = []
    with open(path, 'r') as f:
        for line in f.readlines():
            elf1_sec, elf2_sec = line.split(',')
            elf1 = tuple(int(s) for s in elf1_sec.split('-'))
            elf2 = tuple(int(s) for s in elf2_sec.split('-'))
            pairs.append((elf1, elf2))
    return pairs

def full_overlap(sec1, sec2):
    ''' In order to have complete overlap, the start and end of one set of
    sections will be fully contained by the other section.
    '''
    if sec1[0] >= sec2[0] and sec1[1] <= sec2[1]:
        return True
    if sec2[0] >= sec1[0] and sec2[1] <= sec1[1]:
        return True
    return False

def partial_overlap(sec1, sec2):
    ''' To check for partial overlap, we build the full list of section
    numbers for both elves in a pair. Then we create a set which contains
    only the unique section numbers from the full list. If there is any
    overlap, the unique set will be shorter than the full set.
    '''
    all_sec = [*range(sec1[0], sec1[1] + 1), *range(sec2[0], sec2[1] + 1)]
    unique_sec = set(all_sec)
    return len(all_sec) != len(unique_sec)

def p1():
    pairs = get_pairs("input.txt")
    count = [1 for e1, e2 in pairs if full_overlap(e1, e2)]
    return sum(count)

def p2():
    pairs = get_pairs("input.txt")
    count = [1 for e1, e2 in pairs if partial_overlap(e1, e2)]
    return sum(count)

print('Part 1: ', p1())
print('Part 2: ', p2())