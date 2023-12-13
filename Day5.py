with open("inputs/Day5_test", newline="\n") as f:
    lines = [line.rstrip() for line in f]

seed_dict = {}
seed_title = ""
seeds = []
seed_title_no = 0

# Destination, Source, Range

for i, line in enumerate(lines):
    if i == 0:
        seed_line = line.split(":")[1].split(" ")
        seed_line.remove('')
        seeds = [int(x) for x in seed_line]
    else:
        if ":" in line:
            seed_title = line.split(" ")[0]
            seed_title_no += 1
            seed_dict[seed_title_no] = []
            seed_map = []
        elif line != "":
            seed_line = line.split(" ")
            seed_line = [int(x) for x in seed_line]
            seed_dict[seed_title_no].append(seed_line)

print(seed_dict)

# Process mapping

# For each mapping

def seed_mapping(seed, i):

    mapping = None

    for j in range(len(seed_dict[i])):

        rng = seed_dict[i][j][2]

        dest_low = seed_dict[i][j][0]
        source_low = seed_dict[i][j][1]
        source_high = seed_dict[i][j][1] + rng

        if seed >= source_low and seed < source_high:
            mapping = seed + dest_low - source_low
            break
        else:
            mapping = seed

    return mapping

def seed_mapping_2(seed_2_ranges, new, s, e, i):

    for j in range(len(seed_dict[i])):

        rng = seed_dict[i][j][2]

        dest_low = seed_dict[i][j][0]
        source_low = seed_dict[i][j][1]
        source_high = seed_dict[i][j][1] + rng

        os = max(s, source_low)
        oe = min(e, source_high)

        if os < oe:
            new.append((os - source_low + dest_low, oe - source_low + dest_low))

            if os > s:
                seed_2_ranges.append((s, os))
            if oe < e:
                seed_2_ranges.append((oe, e))

            break
    else:
        new.append((s, e))

    return seed_2_ranges, new

seeds_2 = seeds.copy() # Copy for part 2

# Part 1
for i in range(1, len(seed_dict) + 1, 1):
    for s in range(len(seeds)):
        seed = seed_mapping(seeds[s], i)

        seeds[s] = seed

min_seed = 1e8
seeds_2_ranges = []

# Part 2
for ns in range(0, len(seeds_2), 2):
    seeds_2_ranges.append((seeds_2[ns], seeds_2[ns] + seeds_2[ns + 1]))

new = []
while len(seeds_2_ranges) > 0:

    s, e = seeds_2_ranges.pop()

    for i in range(1, len(seed_dict) + 1, 1):
        seed_2_ranges, new = seed_mapping_2(seeds_2_ranges, new, s, e, i)
    seed_2_ranges = new

print(sorted(seed_2_ranges))

print("--------Out-----")
print(min(seeds))
print(min_seed)







