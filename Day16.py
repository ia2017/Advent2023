with open("inputs/Day16", newline="\n") as f:
    lines = [line.rstrip() for line in f]

def plot(o_list):
    plot = []
    for i in range(len(lines)):
        inner_plot = []
        for j in range(len(lines[i])):
            inner_plot.append(".")
        plot.append(inner_plot)

    for key, value in o_list.items():
        i = int(key.split(",")[0])
        j = int(key.split(",")[1])

        plot[i][j] = "#"

    output = []
    for i in range(len(plot)):
        inner_string = "".join(plot[i])
        output.append(inner_string)
        print(inner_string)

    return output

i = 0
j = 0

bools = [False, False, True, False] # 0: Left , 1: Up, 2: Right, 3: Down

ray_queue = [[i, j]]
next_dir = []
energised = {}
first = True

# Get direction
dir = bools.index(True)

n = 0
while ray_queue:
    current_cell = f"{i},{j}"
    print(dir)
    if current_cell not in energised:
        energised[current_cell] = 0

    if lines[i][j] == "\\":
        if dir == 0: dir = 1
        elif dir == 1: dir = 0
        elif dir == 2: dir = 3
        elif dir == 3: dir = 2

        bools = [False for i in range(4)]
        bools[dir] = True

    elif lines[i][j] == "/":
        if dir == 0: dir = 3
        elif dir == 3: dir = 0
        elif dir == 1: dir = 2
        elif dir == 2: dir = 1

        bools = [False for i in range(4)]
        bools[dir] = True

    elif lines[i][j] == "|":
        # Left
        if dir == 0:
            if not first:
                # Queueing
                ray_queue.append([i, j])
                # Next up
                next_dir.append(2)

            # Goes down
            bools = [False for i in range(4)]
            dir = 3
            bools[dir] = True

        # Right
        elif dir == 2:
            if not first:
                # Queueing
                ray_queue.append([i, j])
                # Next down
                next_dir.append(0)

            # Goes up
            bools = [False for i in range(4)]
            dir = 1
            bools[dir] = True

    elif lines[i][j] == "-":
        # Up
        if dir == 1:
            if not first:
                # Queueing
                ray_queue.append([i, j])
                # Next left
                next_dir.append(3)

            # Goes right
            bools = [False for i in range(4)]
            dir = 2
            bools[dir] = True

        # Down
        elif dir == 3:
            if not first:
                # Queueing
                ray_queue.append([i, j])
                # Next right
                next_dir.append(1)

            # Goes left
            bools = [False for i in range(4)]
            dir = 0
            bools[dir] = True

    first = False
    if bools[0]:
        j -= 1
    elif bools[1]:
        i -= 1
    elif bools[2]:
        j += 1
    elif bools[3]:
        i += 1

    ray_queue[0] = [i, j]
    print(f"{n} : {len(energised)}")
    n += 1
    if n > 100000000:
        break
    if i > len(lines) - 1 or i < 0 or j > len(lines[0]) - 1 or j < 0:
        ray_queue.pop(0)
        if not ray_queue:
            break
        dir = next_dir[0]
        next_dir.pop(0)
        i = ray_queue[0][0]
        j = ray_queue[0][1]
        first = True

# Part 1
print(len(energised))
# plot(energised)

# Part 2
