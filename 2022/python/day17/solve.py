def get_moves(path):
    with open(path, 'r') as f:
        return f.read().strip()

def p1():
    moves = get_moves('test.txt')
    print(moves)

p1()