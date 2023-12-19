with open("inputs/Day15_test", newline="\n") as f:
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
        if line[i] == "-" or line[i] == "=":
            box = current_value
            sign = line[i]
            bool_number = True
        char_value = ord(line[i])
        current_value += char_value
        current_value *= 17
        current_value %= 256

    return current_value, box, sign, focal

total = 0
boxes = [[] for i in range(256)]
for i in range(len(lines)):
    current_value, box, sign, focal = ascii_convert(lines[i])
    boxes[box].insert(0, focal)
    print(box)
    total += current_value

print(total)

