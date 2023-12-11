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
            current_node = pred[current_node]
            length += 1
        lengths.append(length)

    return lengths

lengths = bfs(graph, start_node)

print(lengths[-1])