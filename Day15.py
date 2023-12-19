with open("inputs/Day15", newline="\n") as f:
    lines = [line.rstrip() for line in f]

lines = lines[0].split(",")
# print(lines)

def ascii_convert(line):

    current_value = 0
    box = 0
    sign = ""
    focal = 0
    bool_number = False
    label = ""
    for i in range(len(line)):
        if bool_number:
            focal = int(line[i:])
        if (line[i] == "-" or line[i] == "=") and not bool_number:
            box = current_value
            sign = line[i]
            bool_number = True
        if not bool_number:
            label += line[i]
        char_value = ord(line[i])
        current_value += char_value
        current_value *= 17
        current_value %= 256

    return current_value, box, label, sign, focal

total = 0
boxes = [{} for i in range(256)]

for i in range(len(lines)):
    current_value, box, label, sign, focal = ascii_convert(lines[i])
    if sign == "=":
        if label in boxes[box]:
            boxes[box][label] = focal
        else:
            boxes[box][label] = focal
    elif sign == "-":
        if label in boxes[box]:
            del boxes[box][label]

    total += current_value

# Post process boxes

total_2 = 0
for i in range(len(boxes)):
    if len(boxes[i]) > 0:
        j = 1
        for key, index in boxes[i].items():
            total_2 += (i + 1) * j * boxes[i][key]
            j += 1

# Part 1
print(total)

# Part 2
print(total_2)
