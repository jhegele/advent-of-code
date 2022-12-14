import json
from copy import deepcopy
from functools import cmp_to_key

def get_packet_pairs(path):
    with open(path, 'r') as f:
        for idx, raw_pair in enumerate(f.read().split('\n\n')):
            p1, p2 = raw_pair.strip().split('\n')
            yield (idx + 1, json.loads(p1), json.loads(p2),)

def right_order(a, b):
    # if a and b match, there's no answer here
    if (a == b):
        return None
    # if both are integers, compare them
    if type(a) == int and type(b) == int:
        if a < b:
            return True
        if a > b:
            return False
        # if equivalent, there's no answer
        return None
    # if both are lists
    elif type(a) == list and type(b) == list:
        ans = None
        # merge the lists and compare each set of elements
        for c_a, c_b in zip(a, b):
            ans = right_order(deepcopy(c_a), deepcopy(c_b))
            # if we find an answer, we can stop
            if ans is not None:
                break
        # if no answer was found, we can compare list lengths
        if ans is None:
            # if list a is shorter, then it would have run out of values
            # first so the condition is True
            if len(a) < len(b):
                ans = True
            if len(a) > len(b):
                ans = False
        return ans
    # if both are NOT int and both are NOT list, then we have one of
    # each type
    # if the first is an int and second is a list
    elif type(a) == int:
        # if the list contains only one integer, we can just compare
        if len(b) == 1 and type(b[0]) == int:
            if a < b[0]:
                return True
            if a > b[0]:
                return False
            return None
        # if the list contains multiple items, convert the int to a
        # list and run it through the function again
        else:
            return right_order([a], deepcopy(b))
    # if we've reached this point, the only possible option is that
    # the first is a list and the second is an int
    # treat this the same as above, just reversed
    else:
        if len(a) == 1 and type(a[0]) == int:
            if a[0] < b:
                return True
            if a[0] > b:
                return False
            return None
        else:
            return right_order(deepcopy(a), [b])
        

def p1():
    pairs = get_packet_pairs('input.txt')
    return sum([i for i, a, b in pairs if right_order(a, b)])

def p2():
    # for part 2, we ignore packet pairs and add in these two divider packets
    divider_packets = [
        [[2]],
        [[6]]
    ]
    all_pairs = [*divider_packets]
    for _, p1, p2 in get_packet_pairs('input.txt'):
        all_pairs += [p1, p2]
    # use the function we built to sort everything
    all_pairs.sort(key=cmp_to_key(lambda a, b: -1 if right_order(a, b) else 1))
    return (all_pairs.index(divider_packets[0]) + 1) * (all_pairs.index(divider_packets[1]) + 1)

print('Part 1: ', p1())
print('Part 2: ', p2())