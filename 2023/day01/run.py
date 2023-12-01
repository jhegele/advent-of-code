import re

alpha = 'abcdefghijklmnopqrstuvwxyz'

with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

def part1(lines: list[str]):
    cumulative = 0
    num_lines = [[c for c in l.lower() if c not in alpha] for l in lines]
    for nl in num_lines:
        cumulative += int('{}{}'.format(nl[0], nl[-1]))
    return cumulative

def part2(lines: list[str]):
    cumulative = 0
    for line in lines:
        digits = []
        digit_matches = re.finditer(r'\d', line)
        for m in digit_matches:
            digits.append({
                'idx': m.start(),
                'val': line[m.start()]
            })
        terms = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        for term in terms:
            term_matches = re.finditer(term, line)
            for m in term_matches:
                digits.append({
                    'idx': m.start(),
                    'val': terms.index(term) + 1
                })
        digits.sort(key=lambda x: x['idx'])
        cumulative += int('{}{}'.format(digits[0]['val'], digits[-1]['val']))
    return cumulative
    

print('p1: {}'.format(part1(lines)))
print('p2: {}'.format(part2(lines)))