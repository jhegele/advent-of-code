def get_games(line: str):
    raw_id, all_revealed = line.split(': ')
    id = int(raw_id.replace('Game ', ''))
    turns = all_revealed.split(';')
    results = []
    for turn in turns:
        r, g, b = (0, 0, 0) # (R, G , B)
        for grab in turn.strip().split(','):
            qty, color = grab.strip().split(' ')
            if color.strip() == 'red':
                r += int(qty)
            if color.strip() == 'green':
                g += int(qty)
            if color.strip() == 'blue':
                b += int(qty)
        results.append((r, g, b))
    return id, results 

def part1(lines: list[str]):
    games = list(map(get_games, lines))
    sum_ids = 0
    for id, revealed in games:
        max_red = max([r[0] for r in revealed])
        max_green = max([r[1] for r in revealed])
        max_blue = max([r[2] for r in revealed])
        if max_red <= 12 and max_green <= 13 and max_blue <= 14:
            sum_ids += id
    return sum_ids

def part2(lines: list[str]):
    games = list(map(get_games, lines))
    power = 0
    for _, revealed in games:
        max_red = max([r[0] for r in revealed])
        max_green = max([r[1] for r in revealed])
        max_blue = max([r[2] for r in revealed])
        power += max_red * max_green * max_blue
    return power

with open('input.txt', 'r') as f:
    lines = f.readlines()

print('p1: {}'.format(part1(lines)))
print('p2: {}'.format(part2(lines)))