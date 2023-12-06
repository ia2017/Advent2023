with open("inputs/Day5", newline="\n") as f:
    lines = [line.rstrip() for line in f]

seed_dict = {}
seed_title = 

print(lines)

for i, line in enumerate(lines):
    if i == 0:
        seed_line = line.split(":")[1].split(" ")
        seed_line.remove('')
        seeds = [int(x) for x in seed_line]
    else:
        if ":" in line:
            seed_title = line
            seed_dict[seed_title] = []
        else:


print(seeds)
