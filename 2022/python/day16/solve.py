def get_valves(path):
    valves = {}
    with open(path, 'r') as f:
        for line in f.readlines():
            a, b = line.strip().split('; ')
            name = a[6:8]
            flow = int(a.split("=")[1])
            children = b[23:].split(',')
            valves[name] = {
                'flow': flow,
                'children': children
            }
    return valves

def p1():
    print(get_valves('test.txt'))

p1()