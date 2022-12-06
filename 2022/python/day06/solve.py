def get_stream(path):
    with open(path, 'r') as f:
        return f.read()

def p1():
    stream = get_stream('input.txt')
    for i in range(4, len(stream)):
        s, e = i - 4, i
        if len(set(stream[s:e])) == 4:
            return e

def p2():
    stream = get_stream('input.txt')
    for i in range(14, len(stream)):
        s, e = i - 14, i
        if len(set(stream[s:e])) == 14:
            return e


print('Part 1: ', p1())
print('Part 2: ', p2())