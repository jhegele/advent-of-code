class Segment:
    moves = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0),
        # tail can move diagonally
        'UR': (1, 1),
        'UL': (-1, 1),
        'DR': (1, -1),
        'DL': (-1, -1)
    }

    def __init__(self) -> None:
        self.loc_head = (0, 0,)
        self.loc_tail = (0, 0,)
        self.visited_head = [(0, 0,)]
        self.visited_tail = [(0, 0,)]

    def _coords_add(self, loc, move):
        """Add two tuples, ex: (1, 2,) + (3, 4,) == (4, 6,)"""
        return tuple(sum(x) for x in zip(loc, move))

    def move_head(self, dir):
        """Move knot at head of segment by one spot in the given direction"""
        adj = Segment.moves[dir]
        self.loc_head = self._coords_add(self.loc_head, adj)
        self.visited_head.append(self.loc_head)
        pass

    def move_tail(self, part = 1):
        """Move the knot at tail in response to the head movement. Note that,
        because of chaining effects, the tail of a child segment can move
        diagonally for part 2 so we account for that."""
        all_moves = [m for _, m in Segment.moves.items()]
        # calculate all positions adjacent to the head AND the current position of the head
        # since the tail could be underneath it
        head_adjacent = [self.loc_head] + list(map(
            lambda m: self._coords_add(self.loc_head, m), 
            all_moves
        ))
        # if the tail is already under or adjacent, we don't need to move it
        if self.loc_tail not in head_adjacent:
            # the tail can move to any adjacent position in response to the
            # movement of the head
            tail_moves = list(map(
                lambda m: self._coords_add(self.loc_tail, m),
                all_moves
            ))
            if part == 1:
                # for part 1, if we are moving the tail it will always land in a position that
                # is immediately adjacent (directly up, down, left, or right) of the head; it
                # will never end up diagonal from the head
                valid_pos_moves = [m for d, m in Segment.moves.items() if d in ['U', 'D', 'L', 'R']]
                valid_pos = list(map(
                    lambda m: self._coords_add(self.loc_head, m),
                    valid_pos_moves
                ))
                self.loc_tail = [p for p in valid_pos if p in tail_moves][0]
                self.visited_tail.append(self.loc_tail)
            else:
                # in part 2, we can have instances where a move is diagonal as a result of the
                # chaining effect. we should try to use the rules as above but, if they fail
                # we know that the knot had to have been pulled diagonally
                valid_pos_moves = [m for d, m in Segment.moves.items() if d in ['U', 'D', 'L', 'R']]
                valid_pos = list(map(
                    lambda m: self._coords_add(self.loc_head, m),
                    valid_pos_moves
                ))
                # catch moves are moves that are invalid per the rules but could occur when
                # segments are chained together
                catch_pos_moves = [m for d, m in Segment.moves.items() if d in ['UR', 'UL', 'DR', 'DL']]
                catch_pos = list(map(
                    lambda m: self._coords_add(self.loc_head, m),
                    catch_pos_moves
                ))
                # try our list of valid moves
                try:
                    self.loc_tail = [p for p in valid_pos if p in tail_moves][0]
                # if the valid moves fail, the movement must be diagonal
                except:
                    self.loc_tail = [p for p in catch_pos if p in tail_moves][0]
                self.visited_tail.append(self.loc_tail)

    def move(self, dir, amt):
        """Process a move from the list of instructions"""
        for _ in range(amt):
            self.move_head(dir)
            self.move_tail()

    def set_head_loc(self, loc):
        """For part 2, this allows us to keep the head of a child segment in sync with the
        tail of its parent segment"""
        self.loc_head = loc
        self.visited_head.append(loc)
        self.move_tail(2)


def get_moves(path):
    with open(path, 'r') as f:
        lines = [l.strip().split() for l in f.readlines()]
    return [(d, int(c)) for d, c in lines]

def p1():
    s = Segment()
    for dir, amt in get_moves("input.txt"):
        s.move(dir, amt)
    return len(set(s.visited_tail))

def p2():
    # for part 2, realize that a single rope with 10 knots is the same thing as 9 rope
    # segments where the head of each child segment is equal to the tail of its parent
    # segment
    segments = [Segment() for _ in range(9)]
    for dir, amt in get_moves("input.txt"):
        for _ in range(amt):
            segments[0].move_head(dir)
            segments[0].move_tail(2)
            for idx in range(1, len(segments)):
                segments[idx].set_head_loc(segments[idx -1].loc_tail)  
    return len(set(segments[-1].visited_tail))


print('Part 1: ', p1())
print('Part 2: ', p2())