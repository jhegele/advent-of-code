import re


def get_positions(lines: list[str]):
    """
    Parse raw lines from input file into a usable data structure.

    We need the value from the line, a flag indicating whether the value is numeric or not,
    and the list of coordinates covered by the value (numeric values can be greater than
    one character in length). The flag just makes it easy for us to quickly filter out
    symbols."""
    # Use two regexes, one for numeric data (re_digits) and one for symbol data
    # (re_symbols)
    re_digits = re.compile(r"([\d]+)")
    re_symbols = re.compile(r"([^\d|\.|\v]+)")
    positions = []
    # y coord is the index of the line from the input file
    for idx, line in enumerate(lines):
        for match in re_digits.finditer(line.strip()):
            val = int(line[match.start() : match.end()])
            positions.append(
                {
                    "val": val,
                    "is_numeric": True,
                    # coords will always be a list of x, y pairs that are covered by
                    # the value
                    "coords": [(x, idx) for x in range(match.start(), match.end())],
                }
            )
        for match in re_symbols.finditer(line.strip()):
            val = line[match.start() : match.end()]
            positions.append(
                {
                    "val": val,
                    "is_numeric": False,
                    "coords": [(x, idx) for x in range(match.start(), match.end())],
                }
            )
    return positions


def intersection(list1, list2):
    """
    Helper function to determine if two lists share any members"""
    return len(list(set(list1) & set(list2))) > 0


def get_surrounding(coords, positions):
    """
    Given a set of coordinates and all parsed positions, return all positions that are
    adjacent to the provided coordinates."""
    y = coords[0][1]
    x = [c[0] for c in coords]
    points_to_check = []
    for cy in range(y - 1, y + 2):
        if cy < 0:
            pass
        for cx in set(range(x[0] - 1, x[-1] + 2)):
            if (cx, cy) not in coords:
                points_to_check.append((cx, cy))
    return [pos for pos in positions if intersection(pos["coords"], points_to_check)]


def symbol_adjacent(coords, positions):
    """
    Helper function to determine if a symbol is adjacent to a set of coordinates"""
    surrounding = get_surrounding(coords, positions)
    return sum([1 for s in surrounding if not s["is_numeric"]]) > 0


def gear_ratio(coords, positions):
    """
    For part 2, we need to calculate gear ratios for any "*" symbol that has
    _exactly_ two numeric values adjacent to it."""
    # Get any surrounding positions that are numeric since we don't care
    # about symbols here
    surrounding = [s for s in get_surrounding(coords, positions) if s["is_numeric"]]
    # If there aren't exactly two numeric values, we don't need to
    # calculate the ratio and can just return 0
    if len(surrounding) != 2:
        return 0
    return surrounding[0]["val"] * surrounding[1]["val"]


def part1(lines: list[str]):
    """
    For part 1, we need to get the sum of all numeric values that have an adjacent symbol.

    Note: this is very, very poorly optimized and takes a couple of seconds to run, but it works.
    """
    positions = get_positions(lines)
    # To calculate the sum, we grab all values that are numeric and have at least one adjacent symbol
    total_numeric = sum(
        [
            p["val"]
            for p in positions
            if p["is_numeric"] and symbol_adjacent(p["coords"], positions)
        ]
    )
    return total_numeric


def part2(lines: list[str]):
    """
    For part 2, we're really only concerned with gears which are denoted by "*". Any gear with exactly two numeric values adjacent has a gear ratio.
    """
    positions = get_positions(lines)
    gears = [p for p in positions if p["val"] == "*"]
    ratios = [gear_ratio(g["coords"], positions) for g in gears]
    return sum(ratios)


with open("input.txt", "r") as f:
    lines = f.readlines()

print("P1: {}".format(part1(lines)))
print("P2: {}".format(part2(lines)))
