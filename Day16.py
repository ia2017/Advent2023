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


edge_lengths = 2 * len(lines) + 2 * len(lines[0])

i_start = 0
j_start = 0
start_direction = 3
edge_bool = [True, False, False, False]  # Top edge first

max_energised = -1e8

for edge in range(edge_lengths):

    ray_queue = [[i_start, j_start]]
    next_dir = []
    energised = {}
    first = True
    beam_history = {}
    beam_bool = False

    # Get direction
    direction = start_direction
    bools = [False for i in range(4)]   # 0: Left, 1: Up, 2: Right, 3: Down
    bools[direction] = True

    i = ray_queue[0][0]
    j = ray_queue[0][1]

    n = 0

    while ray_queue:
        current_cell = f"{i},{j}"

        prev_dir = direction

        if current_cell not in energised:
            energised[current_cell] = 0

        if lines[i][j] == "\\":
            if direction == 0: direction = 1
            elif direction == 1: direction = 0
            elif direction == 2: direction = 3
            elif direction == 3: direction = 2

            bools = [False for i in range(4)]
            bools[direction] = True

        elif lines[i][j] == "/":
            if direction == 0: direction = 3
            elif direction == 3: direction = 0
            elif direction == 1: direction = 2
            elif direction == 2: direction = 1

            bools = [False for i in range(4)]
            bools[direction] = True

        elif lines[i][j] == "|":
            # Left
            if direction == 0:
                if not first:
                    # Queueing
                    ray_queue.append([i, j])
                    # Next up
                    next_dir.append(2)

                # Goes down
                bools = [False for i in range(4)]
                direction = 3
                bools[direction] = True

            # Right
            elif direction == 2:
                if not first:
                    # Queueing
                    ray_queue.append([i, j])
                    # Next down
                    next_dir.append(0)

                # Goes up
                bools = [False for i in range(4)]
                direction = 1
                bools[direction] = True

        elif lines[i][j] == "-":
            # Up
            if direction == 1:
                if not first:
                    # Queueing
                    ray_queue.append([i, j])
                    # Next left
                    next_dir.append(3)

                # Goes right
                bools = [False for i in range(4)]
                direction = 2
                bools[direction] = True

            # Down
            elif direction == 3:
                if not first:
                    # Queueing
                    ray_queue.append([i, j])
                    # Next right
                    next_dir.append(1)

                # Goes left
                bools = [False for i in range(4)]
                direction = 0
                bools[direction] = True

        current_beam = current_cell + f",{prev_dir}"
        if current_beam not in beam_history:
            beam_history[current_beam] = 0
        else:
            beam_bool = True

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
        # print(f"{n} : {len(energised)}")
        n += 1


        if i > len(lines) - 1 or i < 0 or j > len(lines[0]) - 1 or j < 0 or beam_bool:
            ray_queue.pop(0)
            if not ray_queue:
                break
            direction = next_dir[0]
            next_dir.pop(0)
            i = ray_queue[0][0]
            j = ray_queue[0][1]
            first = True
            beam_bool = False


    if i_start == 0 and j_start == len(lines[0]) - 1 and not edge_bool[1]:
        start_direction = 0
        edge_bool = [False for i in range(4)]
        edge_bool[1] = True
    elif i_start == len(lines) - 1 and j_start == len(lines[0]) - 1 and not edge_bool[2]:
        start_direction = 1
        edge_bool = [False for i in range(4)]
        edge_bool[2] = True

    elif i_start == len(lines) - 1 and j_start == 0 and not edge_bool[3]:
        start_direction = 2
        edge_bool = [False for i in range(4)]
        edge_bool[3] = True

    elif i_start == 0 and j_start == 0 and not edge_bool[0] and n > 0:
        start_direction = 3
        edge_bool = [False for i in range(4)]
        edge_bool[0] = True

    else:
        if edge_bool[0]:
            j_start += 1
        elif edge_bool[1]:
            i_start += 1
        elif edge_bool[2]:
            j_start -= 1
        elif edge_bool[3]:
            i_start -= 1

    energised_length = len(energised)

    if energised_length > max_energised:
        max_energised = energised_length


# Part 1
print(max_energised)
# plot(energised)

# Part 2
