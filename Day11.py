with open("inputs/Day11", newline="\n") as f:
    lines = [line.rstrip() for line in f]

print(lines)

increment = 1000000

graph = {}
pos_i = []
pos_j = []
node = 0
row_bool = [True for x in range(len(lines[0]))]
column_bool = [True for y in range(len(lines))]


i_plus = 0
j_plus = 0
# Store it in weighted graph
for i in range(len(lines)):
    for j in range(len(lines[i])):
        current_node = lines[i][j]

        if current_node == "#":
            graph[node] = {}
            pos_i.append(i + i_plus)
            pos_j.append(j)
            node += 1
            row_bool[i] = False
            column_bool[j] = False

    if row_bool[i] == True:
        i_plus += 1*(increment - 1)


j_bool = [False for x in range(len(pos_j))]
for j in range(len(column_bool)):
    if column_bool[j] == True:
        j_plus += 1*(increment - 1)
    for k in range(len(pos_j)):
        if pos_j[k] <= j and not j_bool[k]:
            pos_j[k] += j_plus
            j_bool[k] = True

print(pos_j)
print("Expanded")
visited_pairs = {}
sum_dist = 0
for i in range(len(pos_i)):
    for j in range(len(pos_j)):
        if i != j:
            if f"{i},{j}" not in visited_pairs and f"{j},{i}" not in visited_pairs:
                visited_pairs[f"{i},{j}"] = 0
                dist = abs(pos_i[i] - pos_i[j]) + abs(pos_j[i] - pos_j[j])
                # graph[i][j] = dist
                sum_dist += dist
    # print(i)

# def Dijkstra(graph, src):
#     visited = []

# print(graph)
print(sum_dist)
