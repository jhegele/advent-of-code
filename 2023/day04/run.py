def get_points(line: tuple[list[int], list[int]]):
    """
    For part 1, we need to calculate points based on how many matches there are
    between the list of cards and the list of winning numbers. The only real
    complexity here is that the first match is worth 1 point, then subsequent
    matches double the point value. The net result is, if there is 1 or 0
    matches, you just return the number of matches. Anything above 1 match is
    2^n where n is the number of matches.
    """
    card, win = line
    common = list(set(card).intersection(set(win)))
    if len(common) <= 1:
        return len(common)
    return 2 ** (len(common) - 1)


def get_winning_numbers(line: tuple[list[int], list[int]]):
    """
    For part 2, we don't care about points, we just need to know how many matches
    exist between the cards and the winning numbers.
    """
    card, win = line
    return list(set(card).intersection(set(win)))


def get_cards(lines: list[str]):
    """
    Take a raw line from the input and parse it into a tuple containing a list of
    cards and a list of winning numbers
    """
    cards = []
    for line in lines:
        _, values = line.split(": ")
        card, win = values.split("|")
        card_nums = [int(n) for n in card.strip().split()]
        win_nums = [int(n) for n in win.strip().split()]
        cards.append(
            (
                card_nums,
                win_nums,
            )
        )
    return cards


def part1(lines: list[str]):
    """
    For part 1, we just calculate the total number of points across all
    cards.
    """
    cards = get_cards(lines)
    points = [get_points(c) for c in cards]
    return sum(points)


def part2(lines: list[str]):
    """
    For part two, we consider each card independently. For a given card, we
    calculate that there are N matches. That means that we replicate the N
    cards that follow exactly once. You do this for all of the cards in a
    given position (i.e. when you get to the 5th card, you may have 1
    original card and it may have been replicated 3 times so you'd do this
    a total of 4 times).

    The key to optimizing this process is realizing that you don't need to
    recursively iterate through the cards. If you have 4 instances (1
    original, 3 copies) of the 5th card and the 5th card has N matches, you
    know that you'll replicate the following N cards exactly 4 times.
    """
    cards = get_cards(lines)
    # This list is where we'll track the quantity of cards at each position.
    # We initialize each position with 1 because we know we have at least
    # one card (the original) at each position.
    copies = [1 for _ in range(len(cards))]
    for idx, card in enumerate(cards):
        # We need to grab the number of cards at our current position as this
        # tells us how much we need to increment subsequent cards if there
        # are any matches.
        num_cards = copies[idx]
        # Get the list of winning numbers for our card
        win = get_winning_numbers(card)
        # If we need to duplicate cards, the duplication will begin at
        # idx + 1 and will end at idx + 1 + len(win). So, if there are two
        # matches, we start at idx + 1 and end at idx + 3. If there are zero
        # matches, we start and end at idx + 1 (i.e. no duplication occurs)
        inc_start = idx + 1
        inc_end = idx + 1 + len(win)
        for i in range(inc_start, inc_end):
            # We don't need to duplicate anything beyond the end of our list
            # so this check is to prevent going past the end
            if i < len(copies):
                # We increment each position by the number of cards at our
                # current position. If we have 100 cards at our current
                # position and there are matches, the same matches will
                # exist across all 100 cards. So rather than iterate through
                # each card, just increment by the count of cards.
                copies[i] += num_cards
    return sum(copies)


with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

print("P1: {}".format(part1(lines)))
print("P2: {}".format(part2(lines)))
