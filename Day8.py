with open("inputs/Day8", newline="\n") as f:
    lines = [line.rstrip() for line in f]

nodes = {}
instructions = ""

for i, line in enumerate(lines):
    if i == 0:
        instructions = line
    else:
        if "=" in line:
            node = line.split(" = ")[0]
            network = line.split(" = ")[1].replace("(", "").replace(")", "").split(", ")
            network_nodes = (network[0], network[1])
            nodes[node] = network_nodes

current_node = "AAA"
count = 0

while current_node != "ZZZ":
    for inst in instructions:
        if inst == "L":
            current_node = nodes[current_node][0]
        elif inst == "R":
            current_node = nodes[current_node][1]
        count += 1

print(count)