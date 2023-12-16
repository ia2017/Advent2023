from itertools import permutations, combinations, product
import math

with open("inputs/Day12", newline="\n") as f:
    lines = [line.rstrip() for line in f]

# print(lines)

line_dict = {"#" : 0, "?" : 1}

total_count = 0

# for i in range(len(lines)):
for i in range(0, len(lines), 1):
    line = lines[i]
    springs = line.split(" ")[0]
    springs_list = list(springs)
    broken = list(map(int, line.split(" ")[1].split(",")))
    line_count = []
    line_bool = []
    unknown_index = []
    unknown_count = 0
    count = 0
    prev_char = ""
    for j in range(len(springs)):
        if springs[j] == "?":
            unknown_index.append(j)
            unknown_count += 1

        if j > 0:
            if springs[j] != prev_char and prev_char != ".":
                line_count.append(count)
                line_bool.append(line_dict[prev_char])
                count = 0
            elif springs[j] != prev_char and prev_char == ".":
                count = 0

        prev_char = springs[j]
        count += 1

    # After loop finishes
    if prev_char != ".":
        line_count.append(count)
        line_bool.append(line_dict[prev_char])

    broke = 0
    spring = unknown_count

    for j in range(unknown_count + 1):

        combi = ["#" for b in range(broke)]
        combi += ["." for s in range(spring)]

        perms = list(set(permutations(combi)))
        print(len(perms))
        tested_combinations = {}

        for k in range(len(perms)):

            for n in range(len(unknown_index)):
                springs_list[unknown_index[n]] = perms[k][n]

            broken_compare = []
            broken_count = 0
            prev_broken_char = ""
            for n in range(len(springs_list)):
                if prev_broken_char != springs_list[n] and springs_list[n] == ".":
                    if broken_count > 0:
                        broken_compare.append(broken_count)
                    broken_count = 0
                if prev_broken_char != springs_list[n] and springs_list[n] == "#":
                    broken_count = 0
                prev_broken_char = springs_list[n]
                broken_count += 1

            if prev_broken_char == "#":
                broken_compare.append(broken_count)
                broken_count = 0

            compare_bool = 0
            if len(broken_compare) == len(broken):
                for n in range(len(broken_compare)):
                    if broken_compare[n] != broken[n]:
                        compare_bool += 1
            else:
                compare_bool += 1

            if compare_bool == 0:
                total_count += 1
                print(f"i: {i}, {total_count}")

        # print(perms)
        broke += 1
        spring -= 1

        # perm_val = int(math.factorial(len(combi)) / (math.factorial(spring) * math.factorial(broke)))
        #
        # tested_combis = {}
        # current_combi = combi
        # for k in range(perm_val):
        #     if current_combi not in tested_combis:
        #         tested_combis[current_combi] = 0
        #
        #         # changing combi
        #
        #
        #         combi =
        # print(f"Perm val: {perm_val}")
        # print(broke)


print(total_count)


