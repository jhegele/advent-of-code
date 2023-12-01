import re

def get_blueprints(path):
    blueprints = {}
    with open(path, 'r') as f:
        for line in f.readlines():
            matches = re.findall(r"\d+", line)
            blueprints[int(matches[0])] = {
                'ore': {
                    'ore': int(matches[1])
                },
                'clay': {
                    'ore': int(matches[2])
                },
                'obsidian': {
                    'ore': int(matches[3]),
                    'clay': int(matches[4])
                },
                'geode': {
                    'ore': int(matches[5]),
                    'obsidian': int(matches[6])
                }
            }
    return blueprints

def p1():
    print(get_blueprints('test.txt'))

p1()