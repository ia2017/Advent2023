import math

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

current_nodes = []

# Get start nodes
for key, value in nodes.items():
    if key[2] == "A":
        current_nodes.append(key)

print(current_nodes)
lowest_count = []

for i, node in enumerate(current_nodes):
    count = 0
    current_node = node
    node_bool = False

    while not node_bool:
        for inst in instructions:


            if inst == "L":
                current_node = nodes[current_node][0]
            elif inst == "R":
                current_node = nodes[current_node][1]

            count += 1

            if current_node[2] == "Z":
                lowest_count.append(count)
                node_bool = True
                break

lowest_count.sort()
z = lowest_count[-1]

print(f"LCM: {math.lcm(lowest_count[0], lowest_count[1], lowest_count[2], lowest_count[3], lowest_count[4], lowest_count[5])}")


# Finding LCM

def gcd(a, b):
    if min(a, b) == 0:
        return max(a, b)
    a_1 = max(a, b) % min(a,b)
    return gcd(a_1, min(a,b))

def lcm(a, b):
    return (a * b) // gcd(a, b)

current_lcm = lowest_count[0]
for i in range(len(lowest_count) - 1):
    current_lcm = lcm(current_lcm, lowest_count[i + 1])
print(current_lcm)



