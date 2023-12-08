from functools import reduce


def get_times_distances_from_lines(lines: list[str], part2: bool = False):
    """
    Parse times and distances (for part 1) and single time and distance (for
    part 2) from the input lines.
    """
    if part2:
        time = int(lines[0].replace("Time: ", "").replace(" ", ""))
        distance = int(lines[1].replace("Distance: ", "").replace(" ", ""))
        return time, distance
    times = map(int, lines[0].replace("Time: ", "").strip().split())
    distances = map(int, lines[1].replace("Distance: ", "").strip().split())
    return list(times), list(distances)


def get_press_distances(time: int, distance: int):
    """
    Calculate distances for press times spanning 1ms to Nms where N is the time
    value passed. Return all distances that are greater than the passed
    distance value.
    """
    # press length gives you mm/ms but you travel 0mm while pressing. so you can
    # multiply press length by the total time - press length to get the total
    # distance. just do that for the entire range, starting at 1, and you end up
    # with all possible distances.
    all_distances = [press * (time - press) for press in range(1, time + 1)]
    # we only need to return the winning distances
    return [d for d in all_distances if d > distance]


def part1(lines: list[str]):
    times, distances = get_times_distances_from_lines(lines)
    wins = [get_press_distances(t, d) for t, d in zip(times, distances)]
    return reduce(lambda acc, val: acc * len(val), wins, 1)


def part2(lines: list[str]):
    time, distance = get_times_distances_from_lines(lines, True)
    wins = get_press_distances(time, distance)
    return len(wins)


with open("./input.txt", "r") as f:
    lines = f.readlines()

print("P1: {}".format(part1(lines)))
print("P2: {}".format(part2(lines)))
