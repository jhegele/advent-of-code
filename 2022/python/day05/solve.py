import re

def get_stacks_and_procedure(path):
    with open(path, 'r') as f:
        stacks_raw, proc_raw = f.read().split('\n\n')
    # build list of lists to represent stacks
    stacks_lines = stacks_raw.split('\n')
    stacks_pos = []
    stacks = []
    # invert the list so we start at the last line (which
    # is the line with stack numbers). ultimately, we want
    # to transpose the stacks so that we end up with a list
    # of lists where each child list is a stack
    for line in stacks_lines[::-1]:
        if (len(stacks_pos) == 0):
            # build a list of positions where stack numbers appear -- all
            # crates will be in one of these positions
            stacks_pos = [match.span()[0] for match in re.finditer(r"[1-9]", line)]
            # initialize the right number of stacks
            stacks = [[] for _ in stacks_pos]
        else:
            for idx, pos in enumerate(stacks_pos):
                if (line[pos] != ' '):
                    stacks[idx].append(line[pos])
    # build list of procedures where each procedure is a
    # tuple: (move, from, to)
    proc = []
    for line in proc_raw.split('\n'):
        mv, fr, to = map(int, re.findall(r"[0-9]+", line))
        proc.append((mv, fr, to,))
    return stacks, proc


def p1():
    stacks, proc = get_stacks_and_procedure('input.txt')
    for num_crates, from_stack, to_stack in proc:
        # grab the crates to be moved from the origin stack
        crates_to_move = stacks[from_stack - 1][-num_crates:]
        # remove crates from origin stack
        stacks[from_stack - 1] = stacks[from_stack - 1][:-num_crates]
        # invert the list of crates to move because they are
        # moved one at a time, and drop them on the
        # destination stack
        stacks[to_stack - 1] = stacks[to_stack - 1] + crates_to_move[::-1]
    return ''.join([s[-1] for s in stacks])

def p2():
    stacks, proc = get_stacks_and_procedure('input.txt')
    for num_crates, from_stack, to_stack in proc:
        crates_to_move = stacks[from_stack - 1][-num_crates:]
        stacks[from_stack - 1] = stacks[from_stack - 1][:-num_crates]
        # in part 2, crates are moved all together, so we don't
        # need to invert
        stacks[to_stack - 1] = stacks[to_stack - 1] + crates_to_move
    return ''.join([s[-1] for s in stacks])

print('Part 1: ', p1())
print('Part 2: ', p2())
            