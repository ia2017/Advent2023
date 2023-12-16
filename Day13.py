import math

with open("inputs/Day13_test", newline="\n") as f:
    lines = [line.rstrip() for line in f]

print(lines)

line_list = []
current_pattern = []
for line in lines:
    if line == "":
        line_list.append(current_pattern)
        current_pattern = []
    else:
        current_pattern.append(line)

line_list.append(current_pattern)

mid = 0

for i in range(len(line_list)):
    pattern = line_list[i]

    bool_row = False
    # Check row case
    if pattern[0] == pattern[len(pattern) - 1]:
        mid += math.floor((0 + len(pattern) + 1) / 2) * 100
        bool_row = True

    if pattern[0] == pattern[len(pattern) - 2]:
        mid += math.floor((0 + len(pattern) - 1 + 1) / 2) * 100
        bool_row = True

    if pattern[1] == pattern[len(pattern) - 1]:
        mid += math.floor((1 + len(pattern) + 1) / 2) * 100
        bool_row = True

    # Check column case
    if not bool_row:
        column_left = "".join([pattern[x][0] for x in range(len(pattern))])
        column_right = "".join([pattern[x][-1] for x in range(len(pattern))])
        column_left_plus = "".join([pattern[x][1] for x in range(len(pattern))])
        column_right_plus = "".join([pattern[x][-2] for x in range(len(pattern))])

        if column_left == column_right:
            mid += math.floor((0 + len(column_right) + 1) / 2)

        if column_left == column_right_plus:
            mid += math.floor((0 + len(column_right) - 1 + 1) / 2)

        if column_left_plus == column_right:
            mid += math.floor((1 + len(column_right) + 1) / 2)

print(mid)






