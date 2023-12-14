with open("inputs/Day10", newline="\n") as f:
    lines = [line.rstrip() for line in f]

print(lines)

graph = {}
start_node = ""
connections_left = {
    "L" : ["-", "J", "7"],
    "F" : ["-", "J", "7"],
    "-" : ["-", "J", "7"],
}

connections_down = {
    "|" : ["|", "J", "L"],
    "F" : ["|", "J", "L"],
    "7" : ["|", "J", "L"],
}

start_node_line = ["|", "-", "L", "J", "7", "F"]
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
                if "-" in start_node_line: start_node_line.remove("-")
                if "F" in start_node_line: start_node_line.remove("F")
                if "7" in start_node_line: start_node_line.remove("7")

            if node_below_value == "|" or node_below_value == "J" or node_below_value == "L":
                graph[node].append(node_below)
                if "-" in start_node_line: start_node_line.remove("-")
                if "J" in start_node_line: start_node_line.remove("J")
                if "L" in start_node_line: start_node_line.remove("L")

            if node_left_value == "L" or node_left_value == "-" or node_left_value == "F":
                graph[node].append(node_left)
                if "|" in start_node_line: start_node_line.remove("|")
                if "L" in start_node_line: start_node_line.remove("L")
                if "F" in start_node_line: start_node_line.remove("F")

            if node_right_value == "J" or node_right_value == "-" or node_right_value == "7":
                graph[node].append(node_right)
                if "|" in start_node_line: start_node_line.remove("|")
                if "J" in start_node_line: start_node_line.remove("J")
                if "7" in start_node_line: start_node_line.remove("7")

            lines[i] = lines[i].replace("S", start_node_line[0])

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
print(lines)
print(start_node_line)

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

    print("----- VISITED -----")
    # Ray casting

    within_loop = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            current_node = f"{i},{j}"

            if current_node not in visited:
                count_right = 0
                count_left = 0
                count_up = 0
                count_down = 0

                # Look right
                if j < len(lines[i]) - 1:
                    start_intersect = ""
                    start_bool = False
                    for k in range(j + 1, len(lines[i]), 1):
                        if f"{i},{k}" in visited:
                            # print(f"all: {lines[i][k]}")
                            if not start_bool:
                                start_intersect = lines[i][k]
                                if lines[i][k] == "|":
                                    start_bool = False
                                else:
                                    start_bool = True
                                count_right += 1
                            elif start_bool and start_intersect == "L" and lines[i][k] == "7":
                                start_bool = False
                            elif start_bool and start_intersect == "F" and lines[i][k] == "J":
                                start_bool = False
                            elif start_bool and start_intersect == "L" and lines[i][k] == "-":
                                pass
                            elif start_bool and start_intersect == "F" and lines[i][k] == "-":
                                pass
                            else:
                                count_right += 1
                                start_bool = False

                # Look left
                if j > 0:
                    start_intersect = ""
                    start_bool = False
                    for k in range(0, j, 1):
                        if f"{i},{k}" in visited:
                            if not start_bool:
                                start_intersect = lines[i][k]
                                if lines[i][k] == "|":
                                    start_bool = False
                                else:
                                    start_bool = True
                                count_left += 1
                            elif start_bool and start_intersect == "L" and lines[i][k] == "7":
                                start_bool = False
                            elif start_bool and start_intersect == "F" and lines[i][k] == "J":
                                start_bool = False
                            elif start_bool and start_intersect == "L" and lines[i][k] == "-":
                                pass
                            elif start_bool and start_intersect == "F" and lines[i][k] == "-":
                                pass
                            else:
                                count_left += 1
                                start_bool = False

                # Look down
                if i < len(lines) - 1:
                    start_intersect = ""
                    start_bool = False
                    for k in range(i + 1, len(lines), 1):
                        if f"{k},{j}" in visited:
                            # if f"{i},{j}" == "4,8":
                            #     print(f"all: {lines[k][j]}")
                            if not start_bool:
                                # if f"{i},{j}" == "4,8":
                                #     print(f"not bool: {lines[k][j]}")
                                start_intersect = lines[k][j]
                                if lines[k][j] == "-":
                                    start_bool = False
                                else:
                                    start_bool = True
                                count_down += 1
                            elif start_bool and start_intersect == "F" and lines[k][j] == "J":
                                start_bool = False
                            elif start_bool and start_intersect == "7" and lines[k][j] == "L":
                                start_bool = False
                            elif start_bool and start_intersect == "F" and lines[k][j] == "|":
                                pass
                            elif start_bool and start_intersect == "7" and lines[k][j] == "|":
                                pass
                            else:
                                # if f"{i},{j}" == "4,8":
                                #     print(f"else: {lines[k][j]}")
                                count_down += 1
                                start_bool = False
                # Look up
                if i > 0:
                    start_intersect = ""
                    start_bool = False
                    for k in range(0, i, 1):
                        if f"{k},{j}" in visited:
                            if not start_bool:
                                start_intersect = lines[k][j]
                                if lines[k][j] == "-":
                                    start_bool = False
                                else:
                                    start_bool = True
                                count_up += 1
                            elif start_bool and start_intersect == "F" and lines[k][j] == "J":
                                start_bool = False
                            elif start_bool and start_intersect == "7" and lines[k][j] == "L":
                                start_bool = False
                            elif start_bool and start_intersect == "F" and lines[k][j] == "|":
                                pass
                            elif start_bool and start_intersect == "7" and lines[k][j] == "|":
                                pass
                            else:
                                count_up += 1
                                start_bool = False

                # if f"{i},{j}" == "5,8":
                #     print("----------------")
                #     print(f"{i},{j}")
                #     print(count_left)
                #     print(count_right)
                #     print(count_up)
                #     print(count_down)
                #     print("----------------")

                if count_up % 2 != 0 and count_down % 2 != 0 and count_right % 2 != 0 and count_left % 2 != 0:
                    # print(current_node)
                    within_loop += 1

    return lengths, within_loop

lengths, within_loop = bfs(graph, start_node)

print(lengths[-1])
print(within_loop)