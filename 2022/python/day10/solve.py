def get_program(path):
    with open(path, 'r') as f:
        return [l.strip() for l in f.readlines()]

def p1():
    """Build a list that tracks the history of the register value where the index of
    an element is the register value DURING the cycle and index + 1 is the register
    value AFTER the cycle. Note that this approach results in one extra element in
    the list when we finish."""
    check_cycles = [20, 60, 100, 140, 180, 220]
    register_history = [1]
    for line in get_program('input.txt'):
        if line == 'noop':
            register_history.append(register_history[-1])
        else:
            update = int(line.split()[1])
            register_history += [register_history[-1], register_history[-1] + update]
    return sum(map(lambda c: c * register_history[c - 1], check_cycles))

def p2():
    """Use the same approach as above to build our list with register history. The
    fact that we have an extra element in our history doesn't really matter here as
    we end up accounting for that when we split the history into CRT rows. The 
    'tricky' piece here is that each row of the CRT has to be evaluated individually
    using indices 0 through 39 so you have to chop up the history into appropriate
    rows, then do the evaluation of each pixel in each row."""
    register_history = [1]
    for line in get_program('input.txt'):
        if line == 'noop':
            register_history.append(register_history[-1])
        else:
            update = int(line.split()[1])
            register_history += [register_history[-1], register_history[-1] + update]
    # split our history into rows of 40 (CRT is 40 pixels wide)
    rows = [register_history[(r-1)*40: r*40] for r in range(1, 7)]
    # for each row, if the pixel is lit the value is X if the pixel is dark, the value
    # is ' ' (space). The problem uses . for empty spaces but it's easier to read the
    # output with spaces instead.
    crt_rows = [['X' if r-1<=i<=r+1 else ' ' for i, r in enumerate(row)] for row in rows]
    # merge the values in each row, then merge each row onto a new line to generate our
    # output
    crt = '\n'.join([''.join(row) for row in crt_rows])
    return crt

print('Part 1: ', p1())
print('Part 2: ')
print(p2())