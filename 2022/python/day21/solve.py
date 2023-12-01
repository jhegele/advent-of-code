def get_monkeys(path):
    monkeys = {}
    with open(path, 'r') as f:
        for line in f.readlines():
            nm, fn = line.strip().split(': ')
            if fn[0] in '1234567890':
                fn = int(fn)
            monkeys[nm] = fn
    return monkeys

def yell(m, monkeys):
    if type(monkeys[m]) == int:
        return monkeys[m]
    m1, op, m2 = monkeys[m].split()
    if (op == '='):
        return yell(m1, monkeys) == yell(m2, monkeys)
    if (op == '+'):
        return yell(m1, monkeys) + yell(m2, monkeys)
    if (op == '-'):
        return yell(m1, monkeys) - yell(m2, monkeys)
    if (op == '*'):
        return yell(m1, monkeys) * yell(m2, monkeys)
    return yell(m1, monkeys) // yell(m2, monkeys)

def build_ast(n, nodes):
    if n == 'humn':
        return 0
    if type(nodes[n]) == int:
        return nodes[n]
    n1, op, n2 = nodes[n].split()
    return [op, build_ast(n1, nodes), build_ast(n2, nodes)]

def reverse_ast(op, n1, n2):
    o = None
    if op == '+':
        o = lambda a, b: a - b
    if op == '-':
        o = lambda a, b: a + b
    if op == '*':
        o = lambda a, b: a / b
    if op == '/':
        o = lambda a, b: a * b
    if type(n1) == int and type(n2) == int:
        return o(n1, n2)
    if type(n1) == int:
        return o(n1, reverse_ast(n2[0], n2[1], n2[2]))
    if type(n2) == int:
        return o(reverse_ast(n1[0], n1[1], n1[2]), n2)
    return o(reverse_ast(n1[0], n1[1], n1[2]), reverse_ast(n2[0], n2[1], n2[2]))

def p1():
    monkeys = get_monkeys('test.txt')
    return yell('root', monkeys)

def p2():
    monkeys = get_monkeys('input.txt')
    rc1, _, rc2 = monkeys['root'].split()
    # find which root node is NOT monotonic
    monkeys['humn'] = 0
    rc1_a, rc2_a = yell(rc1, monkeys), yell(rc2, monkeys)
    monkeys['humn'] = 1000
    rc1_b = yell(rc1, monkeys)
    changing_node = None
    match_value = None
    if rc1_a != rc1_b:
        changing_node = rc1
        match_value = rc2_a
    else:
        changing_node = rc2
        match_value = rc1_a
    monkeys['humn'] = 'humn'
    print(changing_node, match_value)
    print(build_ast(changing_node, monkeys))
    # op, n1, n2 = build_ast('root', monkeys)
    # print(reverse_ast(op, n1, n2))



    # monkeys['humn'] = 0
    # # root: hppd + czdp
    # start = 3243000000000
    # monkeys['humn'] = start
    # while not yell('root', monkeys):
    #     # print(monkeys['humn'])
    #     # print(yell('hppd', monkeys), yell('czdp', monkeys))
    #     # print(yell('hppd', monkeys))
    #     # print(yell('rswb', monkeys))
    #     # print(yell('dsvv', monkeys))
    #     # print(yell('qzhw', monkeys))
    #     monkeys['humn'] += 1
    #     if monkeys['humn'] > start + 1:
    #         break
    # return monkeys['humn']

# print('Part 1: ', p1())
print('Part 2: ', p2())