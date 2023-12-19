with open("inputs/Day14_test", newline="\n") as f:
    lines = [line.rstrip() for line in f]

# print(lines)
cycles = 2

def calculate_load(lines):
    length = len(lines)
    total_load = 0
    for col in range(len(lines[0])):
    # for col in range(0,1):
        prev_hash = -1
        count = 0
        # counts = []
        for i in range(len(lines)):
            # print(lines[i][col])
            if lines[i][col] == "O":
                count += 1
            elif lines[i][col] == "#":
                # counts.append(count)

                current_load = length - prev_hash - 1
                for j in range(count):
                    total_load += current_load
                    current_load -= 1

                prev_hash = i
                count = 0

        # counts.append(count)

        current_load = length - prev_hash - 1
        for j in range(count):
            total_load += current_load
            current_load -= 1

    return total_load

# Part 1
total_load = calculate_load(lines)

# Part 2
o_list = []
hash_list = {}

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "O":
            o_list.append([i, j])
        elif lines[i][j] == "#":
            o_list.append([i, j])
            hash_list[f"{i},{j}"] = 0

def north(o_list):
    col_hashes = [-1 for i in range(len(lines[0]))]
    o_list.sort(reverse=False)


    for i, o in enumerate(o_list):
        current_col = o[1]
        o_hash = f"{o_list[i][0]},{o_list[i][1]}"
        if o_hash in hash_list:
            col_hashes[current_col] = o_list[i][0]
        else:
            # Pushing north
            o_list[i][0] = col_hashes[current_col] + 1
            col_hashes[current_col] = o_list[i][0]

    result = o_list

    return result

def west(o_list):
    row_hashes = [-1 for i in range(len(lines))]
    o_list.sort(reverse=False)

    for i, o in enumerate(o_list):
        current_row = o[0]
        o_hash = f"{o_list[i][0]},{o_list[i][1]}"
        if o_hash in hash_list:
            row_hashes[current_row] = o_list[i][1]
        else:
            # Pushing north
            o_list[i][1] = row_hashes[current_row] + 1
            row_hashes[current_row] = o_list[i][1]

    result = o_list

    return result

def east(o_list):
    row_hashes = [len(lines) for i in range(len(lines))]
    o_list.sort(reverse=True)

    for i, o in enumerate(o_list):
        current_row = o[0]
        o_hash = f"{o_list[i][0]},{o_list[i][1]}"
        if o_hash in hash_list:
            row_hashes[current_row] = o_list[i][1]
        else:
            # Pushing north
            o_list[i][1] = row_hashes[current_row] - 1
            row_hashes[current_row] = o_list[i][1]

    result = o_list

    return result

def south(o_list):
    col_hashes = [len(lines[0]) for i in range(len(lines[0]))]
    o_list.sort(reverse=True)

    for i, o in enumerate(o_list):
        current_col = o[1]
        o_hash = f"{o_list[i][0]},{o_list[i][1]}"
        if o_hash in hash_list:
            col_hashes[current_col] = o_list[i][0]
        else:
            # Pushing north
            o_list[i][0] = col_hashes[current_col] - 1
            col_hashes[current_col] = o_list[i][0]

    result = o_list

    return result

def plot(o_list):
    plot = []
    for i in range(len(lines)):
        inner_plot = []
        for j in range(len(lines[i])):
            inner_plot.append(".")
        plot.append(inner_plot)

    for i in range(len(o_list)):
        if f"{o_list[i][0]},{o_list[i][1]}" in hash_list:
            plot[o_list[i][0]][o_list[i][1]] = "#"
        else:
            if o_list[i][0] > len(lines) - 1:
                pass
            else:
                plot[o_list[i][0]][o_list[i][1]] = "O"

    output = []
    for i in range(len(plot)):
        inner_string = "".join(plot[i])
        output.append(inner_string)
        # print(inner_string)

    return output

print(o_list)
for n in range(cycles):
    # North - get positions
    o_list = north(o_list)

    # West
    o_list = west(o_list)

    # South
    o_list = south(o_list)

    # East
    o_list = east(o_list)

    pass

new_lines = plot(o_list)
total_load_2 = calculate_load(new_lines)

print(total_load_2)

print(total_load)

