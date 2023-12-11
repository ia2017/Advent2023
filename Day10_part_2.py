with open("inputs/Day10", newline="\n") as f:
    lines = [line.rstrip() for line in f]

print(lines)

graph = {}
start_node = ""

# Store it in weighted graph
for i in range(len(lines)):
    for j in  range(len(lines[i])):

        current_node = lines[i][j]
        node = f"{i},{j}"
        node_above = f"{i - 1},{j}"
        node_below = f"{i + 1},{j}"
        node_left = f"{i},{j - 1}"
        node_right = f"{i},{j + 1}"

        if current_node == "S":
            graph[node] = []
            start_node = node

            node_above_value = lines[i - 1][j]
            node_below_value = lines[i + 1][j]
            node_left_value = lines[i][j - 1]
            node_right_value = lines[i][j + 1]

            # print(f"{node_above_value} {node_below_value} {node_left_value} {node_right_value}")

            if node_above_value == "|" or node_above_value == "F" or node_above_value == "7":
                graph[node].append(node_above)

            if node_below_value == "|" or node_below_value == "J" or node_below_value == "L":
                graph[node].append(node_below)

            if node_left_value == "L" or node_left_value == "-" or node_left_value == "F":
                graph[node].append(node_left)

            if node_right_value == "J" or node_right_value == "-" or node_right_value == "7":
                graph[node].append(node_right)

        if current_node == "|":
            graph[node] = []
            graph[node].append(node_above)
            graph[node].append(node_below)

        if current_node == "J":
            graph[node] = []
            graph[node].append(node_above)
            graph[node].append(node_left)

        if current_node == "L":
            graph[node] = []
            graph[node].append(node_above)
            graph[node].append(node_right)

        if current_node == "-":
            graph[node] = []
            graph[node].append(node_left)
            graph[node].append(node_right)

        if current_node == "7":
            graph[node] = []
            graph[node].append(node_below)
            graph[node].append(node_left)

        if current_node == "F":
            graph[node] = []
            graph[node].append(node_below)
            graph[node].append(node_right)

# print(graph)


def bfs(graph, src):
    visited = [src]
    pred = {src : ""}
    lengths = []

    queue = [src]

    while queue:
        m = queue.pop(0)
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                pred[neighbour] = m

    for i in range(len(visited)):
        length = 0
        current_node = visited[i]

        while current_node != src:
            pred_node = pred[current_node]
            # print(f"{i} current_node: {current_node}, src: {src}")
            # print(i)
            # if pred_node not in loop_list:
            #     loop_list.append(pred_node)
            length += 1
            current_node = pred_node

        lengths.append(length)



    print("HERE")
    # Ray casting

    within_loop = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            current_node = f"{i},{j}"
            if current_node not in visited:
                count_upleft = 0
                count_upright = 0
                count_downleft = 0
                count_downright = 0

                # Look upright
                if j < len(lines[i]) - 1 and i > 0:
                    i_plus = i
                    j_plus = j
                    while True:
                        i_plus -= 1
                        j_plus += 1
                        if i_plus < 0 - 1 or j_plus > len(lines[i]) - 1:
                            break

                        if f"{i_plus},{j_plus}" in visited:
                            count_upright += 1

                # Look upleft
                if j > 0 and i > 0:
                    i_plus = i
                    j_plus = j
                    while True:
                        i_plus -= 1
                        j_plus -= 1
                        if i_plus < 0 - 1 or j_plus < 0:
                            break

                        if f"{i_plus},{j_plus}" in visited:
                            count_upleft += 1

                # Look downright
                if i < len(lines) - 1 and j < len(lines[i]) - 1:
                    i_plus = i
                    j_plus = j
                    while True:
                        i_plus += 1
                        j_plus += 1
                        if i_plus > len(lines) - 1 or j_plus > len(lines[i]) - 1:
                            break

                        if f"{i_plus},{j_plus}" in visited:
                            count_downright += 1

                # Look downleft
                if j > 0 and i < len(lines) - 1:
                    i_plus = i
                    j_plus = j
                    while True:
                        i_plus += 1
                        j_plus -= 1
                        if i_plus > len(lines) - 1 or j_plus < 0:
                            break

                        if f"{i_plus},{j_plus}" in visited:
                            count_downleft += 1

                # print(f"{i},{j}")
                # print(count_left)
                # print(count_right)
                # print(count_up)
                # print(count_down)
                # print("----------------")

                if count_upright % 2 != 0 and count_upleft % 2 != 0 and count_downright % 2 != 0 and count_downleft % 2 != 0:
                    print(current_node)
                    within_loop += 1

    return lengths, within_loop

lengths, within_loop = bfs(graph, start_node)

print(lengths[-1])
print(within_loop)