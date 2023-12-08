from typing import TypeAlias

MapData: TypeAlias = list[tuple[tuple[int, int], tuple[int, int]]]


def get_map_ranges(raw_map: str):
    raw_ranges = [tuple(map(int, line.split())) for line in raw_map.split("\n")[1:]]
    ranges = []
    for rr in raw_ranges:
        destination, source, length = rr
        ranges.append(
            ((source, source + length - 1), (destination, destination + length - 1))
        )
    return ranges


def get_seeds_and_maps(input: str):
    (
        part_seeds,
        part_seed_to_soil,
        part_soil_to_fertilizer,
        part_fertilizer_to_water,
        part_water_to_light,
        part_light_to_temp,
        part_temp_to_humidity,
        part_humidity_to_loc,
    ) = input.split("\n\n")
    return (
        list(map(int, part_seeds.replace("seeds: ", "").split())),
        get_map_ranges(part_seed_to_soil),
        get_map_ranges(part_soil_to_fertilizer),
        get_map_ranges(part_fertilizer_to_water),
        get_map_ranges(part_water_to_light),
        get_map_ranges(part_light_to_temp),
        get_map_ranges(part_temp_to_humidity),
        get_map_ranges(part_humidity_to_loc),
    )


def get_destination(source: int, map_data: MapData):
    destination_match = list(
        filter(lambda md: md[0][0] <= source and md[0][1] >= source, map_data)
    )
    if len(destination_match) > 1:
        raise Exception("More than one destination match found for source!")
    elif len(destination_match) == 1:
        dm = destination_match[0]
        return dm[1][0] + (source - dm[0][0])
    else:
        return source


def get_overlap(range1: tuple[int, int], range2: tuple[int, int]):
    r1s, r1e = range1
    r2s, r2e = range2
    # range 1 fully contained by range 2
    if r2s <= r1s <= r1e <= r2e:
        return range1
    # range 2 fully contained by range 1
    if r1s <= r2s <= r2e <= r1e:
        return range2
    # range 2 overlaps end of range 1
    if r1s <= r2s <= r1e:
        return (r2s, r1e)
    # range 1 overlap end of range 2
    if r2s <= r1s <= r2e:
        return (r1s, r2e)
    # no overlap
    return None


def part1(input: str):
    (
        seeds,
        map_seed_to_soil,
        map_soil_to_fertilizer,
        map_fertilizer_to_water,
        map_water_to_light,
        map_light_to_temp,
        map_temp_to_humidity,
        map_humidity_to_loc,
    ) = get_seeds_and_maps(input)
    locs = []
    for seed in seeds:
        loc = get_destination(
            get_destination(
                get_destination(
                    get_destination(
                        get_destination(
                            get_destination(
                                get_destination(seed, map_seed_to_soil),
                                map_soil_to_fertilizer,
                            ),
                            map_fertilizer_to_water,
                        ),
                        map_water_to_light,
                    ),
                    map_light_to_temp,
                ),
                map_temp_to_humidity,
            ),
            map_humidity_to_loc,
        )
        locs.append(loc)
    return min(locs)


# not completed
def part2(input: str):
    (
        seeds_raw,
        map_seed_to_soil,
        map_soil_to_fertilizer,
        map_fertilizer_to_water,
        map_water_to_light,
        map_light_to_temp,
        map_temp_to_humidity,
        map_humidity_to_loc,
    ) = get_seeds_and_maps(input)
    print(map_seed_to_soil)


with open("sample.txt", "r") as f:
    input = f.read()

# print("P1: {}".format(part1(input)))
print("P2: {}".format(part2(input)))
