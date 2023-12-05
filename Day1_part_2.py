lines = []

number_dict = {

    "zero" : 0,
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,

}

with open("inputs/Day1") as f:
    for line in f:
        lines.append(line.split("\n")[0])

sum = 0

test = []
a_list = []

print(lines[201])

for line in lines:
    a = []
    b = ""
    for char in line:
        if char.isdigit():
            a.append(char)
        else:
            b += char

        for key in number_dict.keys():
            if key in b:
                a.append(str(number_dict[key]))
                b = b[-1]

    assembled_number = int(a[0] + a[-1])
    a_list.append(a)
    test.append(assembled_number)
    sum += assembled_number

print(a_list[201])
print(test[201])


print(sum)


