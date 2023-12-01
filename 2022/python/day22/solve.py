import re

class Trace:

    def __init__(self, start_pos, start_heading, board) -> None:
        self.pos = start_pos
        self.board = board
        self.heading = start_heading

    def _row_xs(self, row_idx):
        r = [x for x, y in self.board if y == row_idx]
        return sorted(r)

    def _col_ys(self, col_idx):
        c = [y for x, y in self.board if x == col_idx]
        return sorted(c)

    def get_row_col(self):
        c, r = self.pos
        return {
            'row': r + 1,
            'col': c + 1
        }

    def turn(self, direction):
        turns = {
            'E': ('S', 'N'),
            'S': ('W', 'E'),
            'W': ('N', 'S'),
            'N': ('E', 'W')
        }
        self.heading = turns[self.heading][0 if direction == 'R' else 1]

    def move(self, num):
        ct = 0
        moves = {
            'E': lambda x, y: (x + 1, y,),
            'S': lambda x, y: (x, y + 1,),
            'W': lambda x, y: (x - 1, y,),
            'N': lambda x, y: (x, y - 1,)
        }
        while ct < num:
            check_x, check_y = moves[self.heading](*self.pos)
            if self.heading in ['E', 'W']:
                valid_xs = self._row_xs(self.pos[1])
                if check_x > max(valid_xs):
                    check_x = min(valid_xs)
                if check_x < min(valid_xs):
                    check_x = max(valid_xs)
            if self.heading in ['N', 'S']:
                valid_ys = self._col_ys(self.pos[0])
                if check_y > max(valid_ys):
                    check_y = min(valid_ys)
                if check_y < min(valid_ys):
                    check_y = max(valid_ys)
            if self.board[(check_x, check_y,)] == '#':
                break
            self.pos = (check_x, check_y,)
            ct += 1

def get_map_and_path(path_to_file):
    with open(path_to_file, 'r') as f:
        map_raw, path_raw = f.read().split('\n\n')
        board_map = {}
        for y, line in enumerate(map_raw.split('\n')):
            for x, char in enumerate(line):
                if char == ' ':
                    continue
                board_map[(x, y)] = char
        path = []
        for match in re.findall(r'\d+[R|L]', path_raw):
            turn = match[-1]
            steps = int(match[:-1])
            path.append((steps, turn,))
        return board_map, path

def draw_board(board_map, visited = {}):
    path_chars = {
        'E': '>',
        'S': 'v',
        'W': '<',
        'N': '^'
    }
    max_x = max([x for x, _ in board_map])
    max_y = max([y for _, y in board_map])
    lines = ''
    for y in range(max_y + 1):
        row = ''
        for x in range(max_x + 1):
            if ((x, y,) not in board_map):
                row += ' '
            elif ((x, y,) in visited):
                row += path_chars[visited[(x, y,)]]
            else:
                row += board_map[(x, y,)]
        lines += '{}\n'.format(row)
    print(lines)
        
def p1():
    m, p = get_map_and_path('input.txt')
    # get starting position
    xs = set([x for x, _ in m])
    ys = set([y for _, y in m])
    pos = None
    for y in range(max(ys) + 1):
        for x in range(max(xs) + 1):
            if (x, y,) in m and m[(x, y,)] == '.':
                pos = (x, y,)
                break
        if pos is not None:
            break
    heading = 'E'
    trace = Trace(pos, heading, m)
    for num, turn in p:
        trace.move(num)
        trace.turn(turn)
    rc = trace.get_row_col()
    return 1000 * rc['row'] + 4 * rc['col'] + 'ESWN'.index(trace.heading)


print('Part 1: ', p1())