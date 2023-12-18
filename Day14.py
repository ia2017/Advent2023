with open("inputs/Day14_test", newline="\n") as f:
    lines = [line.rstrip() for line in f]

# print(lines)
cycles = 1

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
for n in range(cycles):
    # North - get positions


    # West

    # South

    # East

    pass

print(total_load)

