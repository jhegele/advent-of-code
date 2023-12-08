from math import lcm


def get_nodes(lines: list[str]):
    """
    Transform input lines to node mappings
    """
    nodes = {}
    for line in lines:
        key, connects_to = line.split(" = ")
        val = (connects_to[1:4], connects_to[6:9])
        nodes[key] = val
    return nodes


def part2(lines: list[str]):
    """
    The "trick" for part 2 is that you can't brute force it. For my input, it
    required over 13 trillion iterations to have every start node arrive at
    an end node simultaneously. The only practical way to calculate that is
    to determine the steps required for each individual node to arrive at its
    respective end node then calculate the least common multiple for all of
    the individual step counts.
    """
    instructions = lines[0].strip()
    node_map = get_nodes(lines[2:])
    step = 0
    # For this part, we need to track not only the node we're at but also how
    # many steps it has taken to get there
    location_nodes = [(k, step) for k in node_map if k[-1] == "A"]
    total_nodes = len(location_nodes)
    while True:
        direction = instructions[step % len(instructions)]
        # Inside the loop, we only want to work with nodes that are not
        # currently at an end node. We need to enumerate so that we can
        # update the correct nodes in location_nodes
        unfinished_location_nodes = [
            n for n in enumerate(location_nodes) if n[1][0][-1] != "Z"
        ]
        for idx, (node, steps_taken) in unfinished_location_nodes:
            location_nodes[idx] = (
                node_map[node][0 if direction == "L" else 1],
                steps_taken + 1,
            )
        # If all nodes are at end nodes, we're done
        if sum([1 for l in location_nodes if l[0][-1] == "Z"]) == total_nodes:
            break
        step += 1
    # Calculate the least common multiple for the step counts across all of
    # our completed nodes.
    return lcm(*[l[1] for l in location_nodes])


def part1(lines: list[str]):
    """
    Pretty straightforward today. Just trace a path through the map from node
    AAA to node ZZZ and count how many steps. The only (minor) complexity is
    that each node maps to two other nodes and you have to trace your route
    based on the left (L) and right (R) directions that are provided.
    """
    instructions = lines[0].strip()
    node_map = get_nodes(lines[2:])
    step = 0
    # We start at node AAA
    location = "AAA"
    while True:
        # Find the direction for this step
        direction = instructions[step % len(instructions)]
        # Node map is a key value pair in the form:
        # AAA = (BBB, CCC)
        # If the direction is left, we choose BBB, if it's right
        # we choose CCC.
        location = node_map[location][0 if direction == "L" else 1]
        step += 1
        # If we're at node ZZZ, break the loop and return the step count
        if location == "ZZZ":
            break
    return step


with open("input.txt", "r") as f:
    lines = f.readlines()

print("P1: {}".format(part1(lines)))
print("P2: {}".format(part2(lines)))
