lines = []

with open("inputs/Day1") as f:
    for line in f:
        lines.append(line.split("\n")[0])

sum = 0

print(lines)
for line in lines:
    a = []
    for char in line:
        if char.isdigit():
            a.append(char)

    assembled_number = int(a[0] + a[-1])

    sum += assembled_number

print(sum)


