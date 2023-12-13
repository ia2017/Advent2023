with open("inputs/Day9", newline="\n") as f:
    lines = [line.rstrip() for line in f]

sum_ex = 0
sum_back = 0

for line in lines:
    line = list(map(int, line.split(" ")))

    current_line = line
    diffs = [current_line]

    # Getting diffs
    while True:
        new_line = []
        for i in range(len(current_line) - 1):
            new_line.append(current_line[i + 1] - current_line[i])
        diffs.append(new_line)

        current_line = new_line
        if sum(new_line) == 0:
            break

    diffs[-1].append(0)
    diffs[-1].insert(0, 0)
    for i in range(len(diffs) - 1, 0, -1):
        diffs[i - 1].append(diffs[i - 1][-1] + diffs[i][-1])
        diffs[i - 1].insert(0, diffs[i - 1][0] - diffs[i][0])

    sum_back += diffs[0][0]
    sum_ex += diffs[0][-1]

print(sum_ex)
print(sum_back)