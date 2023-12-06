with open("inputs/Day3", newline="\n") as f:
    lines = [line.rstrip() for line in f]

print(lines)

part_sum = 0
symbol_bool = 0
total_sum = 0
char = ""

for i in range(len(lines)):
    line = lines[i]
    current_number = ""
    number_index = 0

    for j in range(len(line)):
        char = line[j]

        if char.isdigit():
            current_number += char
            number_index += 1

        elif (not char.isdigit() and current_number != ""):
            current_number = int(current_number)
            # LEFT
            if line[j - 1 - number_index] != "." and not line[j - 1 - number_index].isdigit():
                symbol_bool += 1
                # symbols.append(line[j - 1 - number_index])

            # RIGHT
            if char != "." and not char.isdigit():
                symbol_bool += 1
                # symbols.append(char)

            # TOP & BOTTOM
            for k in range(j - 1 - number_index, j + 1, 1):
                # Top
                if i > 0:
                    if lines[i - 1][k] != "." and not lines[i - 1][k].isdigit():
                        symbol_bool += 1
                        # symbols.append(lines[i - 1][k])

                # Bottom
                if i < len(lines) - 1:
                    if lines[i + 1][k] != "." and not lines[i + 1][k].isdigit():
                        symbol_bool += 1
                        # symbols.append(lines[i + 1][k])

            print(f"current_number : {current_number}, bool : {symbol_bool}, "
                  # f"symbols: {symbols}"
                  )
            # print(number_index)

            if symbol_bool > 0:
                part_sum += current_number
            total_sum += current_number

            symbol_bool = 0
            number_index = 0
            current_number = ""
            symbols = []


        else:
            pass

    # Last digit on line
    if char.isdigit():
        current_number = int(current_number)
        # LEFT
        if line[j - number_index] != "." and not line[j - number_index].isdigit():
            symbol_bool += 1
            # symbols.append(line[j - 1 - number_index])


        # TOP & BOTTOM
        for k in range(j - number_index, j + 1, 1):
            # Top
            if i > 0:
                if lines[i - 1][k] != "." and not lines[i - 1][k].isdigit():
                    symbol_bool += 1
                    # symbols.append(lines[i - 1][k])

            # Bottom
            if i < len(lines) - 1:
                if lines[i + 1][k] != "." and not lines[i + 1][k].isdigit():
                    symbol_bool += 1
                    # symbols.append(lines[i + 1][k])

        print(f"current_number : {current_number}, bool : {symbol_bool}, "
              # f"symbols: {symbols}"
              )
        # print(number_index)

        if symbol_bool > 0:
            part_sum += current_number
        total_sum += current_number

        symbol_bool = 0
        number_index = 0
        current_number = ""
        symbols = []



        # if not char.isdigit() and char != ".":
        #     print(f"i, j : {i}, {j}")
        #
        #     # ONLY MIDDLE
        #     if j != 0 or j != len(line) - 1:
        #         # Checks if top
        #         if lines[i][j - 1].isdigit() or lines[i][j].isdigit() or lines[i][j + 1].isdigit():
        #             # Get left
        #             number_left = ""
        #             for k in range(j - 1, 0, -1):
        #                 if lines[i][k] == ".":
        #                     break
        #                 number_left = str(lines[i][k]) + number_left
        #
        #             # Get right
        #             number_right = ""
        #             for k in range(j + 1, len(lines[i]) - 1, 1):
        #                 if lines[i][k] == ".":
        #                     break
        #                 number_right += str(lines[i][k])
        #
        #             # Get middle
        #             if lines[i][j] == ".":
        #                 number_middle = " "
        #             else:
        #                 number_middle = lines[i][j]
        #
        #             number_top = number_left + number_middle + number_right
        #
        #             number_top = number_top.split(" ")
        #
        #             for num in number_top:
        #                 if num.isdigit():
        #                     part_sum += int(num)
        #
        #         # Checks if bottom
        #         if lines[i + 2][j - 1].isdigit() or lines[i + 2][j].isdigit() or lines[i + 2][j + 1].isdigit():
        #             # Get left
        #             number_left = ""
        #             for k in range(j - 1, 0, -1):
        #                 if lines[i + 2][k] == ".":
        #                     break
        #                 number_left = str(lines[i + 2][k]) + number_left
        #
        #             # Get right
        #             number_right = ""
        #             for k in range(j + 1, len(lines[i + 2]) - 1, 1):
        #                 if lines[i + 2][k] == ".":
        #                     break
        #                 number_right += str(lines[i + 2][k])
        #
        #             # Get middle
        #             if lines[i + 2][j] == ".":
        #                 number_middle = " "
        #             else:
        #                 number_middle = lines[i + 2][j]
        #
        #             number_top = number_left + number_middle + number_right
        #
        #             number_top = number_top.split(" ")
        #
        #             for num in number_top:
        #                 if num.isdigit():
        #                     part_sum += int(num)
        #
        #         # LEFT
        #         if line[j - 1].isdigit():
        #             number = ""
        #             for k in range(j - 1, 0, -1):
        #                 if line[k] == ".":
        #                     break
        #                 number = str(line[k]) + number
        #
        #             number = int(number)
        #             part_sum += number
        #
        #         # RIGHT
        #         if line[j + 1].isdigit():
        #             number = ""
        #             for k in range(j + 1, len(line) - 1, 1):
        #                 if line[k] == ".":
        #                     break
        #                 number += line[k]
        #
        #             number = int(number)
        #             part_sum += number
        #
        #
        #         # if lines[i + 2][j - 1].isdigit():
        #         #     print("bottom left")
        #         # if lines[i + 2][j].isdigit():
        #         #     print("bottom")
        #         # if lines[i + 2][j + 1].isdigit():
        #         #     print("bottom right")
        #
        # # Checking if number

print(part_sum)
print(total_sum)