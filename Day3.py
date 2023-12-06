with open("inputs/Day3", newline="\n") as f:
    lines = [line.rstrip() for line in f]

part_sum = 0
symbol_bool = 0
total_sum = 0
char = ""
gear_index = {}
gear_ratio = 0
pairs = []

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

                if line[j - 1 - number_index] == "*" and f"{i}, {j - 1 - number_index}" not in gear_index.keys():
                    gear_index[f"{i}, {j - 1 - number_index}"] = current_number
                elif f"{i}, {j - 1 - number_index}" in gear_index.keys():
                    gear_ratio += current_number * gear_index[f"{i}, {j - 1 - number_index}"]
                    pairs.append([gear_index[f"{i}, {j - 1 - number_index}"], current_number])
                    del gear_index[f"{i}, {j - 1 - number_index}"]

                # symbols.append(line[j - 1 - number_index])

            # RIGHT
            if char != "." and not char.isdigit():
                symbol_bool += 1
                # symbols.append(char)
                if char == "*" and f"{i}, {j}" not in gear_index.keys():
                    gear_index[f"{i}, {j}"] = current_number
                elif f"{i}, {j}" in gear_index.keys():
                    gear_ratio += current_number * gear_index[f"{i}, {j}"]
                    pairs.append([current_number, gear_index[f"{i}, {j}"]])
                    del gear_index[f"{i}, {j}"]

            # TOP & BOTTOM
            for k in range(j - 1 - number_index, j + 1, 1):
                # Top
                if i > 0:
                    if lines[i - 1][k] != "." and not lines[i - 1][k].isdigit():
                        symbol_bool += 1
                        # symbols.append(lines[i - 1][k])
                        if lines[i - 1][k] == "*" and f"{i - 1}, {k}" not in gear_index.keys():
                            gear_index[f"{i - 1}, {k}"] = current_number
                        elif f"{i - 1}, {k}" in gear_index.keys():
                            gear_ratio += current_number * gear_index[f"{i - 1}, {k}"]
                            pairs.append([gear_index[f"{i - 1}, {k}"], current_number])

                            del gear_index[f"{i - 1}, {k}"]

                # Bottom
                if i < len(lines) - 1:
                    if lines[i + 1][k] != "." and not lines[i + 1][k].isdigit():
                        symbol_bool += 1
                        # symbols.append(lines[i + 1][k])
                        if lines[i + 1][k] == "*" and f"{i + 1}, {k}" not in gear_index.keys():
                            gear_index[f"{i + 1}, {k}"] = current_number
                        elif f"{i + 1}, {k}" in gear_index.keys():
                            gear_ratio += current_number * gear_index[f"{i + 1}, {k}"]
                            pairs.append([gear_index[f"{i + 1}, {k}"], current_number])

                            del gear_index[f"{i + 1}, {k}"]

            # print(f"current_number : {current_number}, bool : {symbol_bool}, "
            #       # f"symbols: {symbols}"
            #       )
            # print(number_index)

            # print(gear_index)

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
            if line[j - number_index] == "*" and f"{i}, {j - number_index}" not in gear_index.keys():
                gear_index[f"{i}, {j - number_index}"] = current_number
            elif f"{i}, {j - number_index}" in gear_index.keys():
                gear_ratio += current_number * gear_index[f"{i}, {j - number_index}"]
                pairs.append([gear_index[f"{i}, {j - number_index}"], current_number])
                del gear_index[f"{i}, {j - number_index}"]

        # TOP & BOTTOM
        for k in range(j - number_index, j + 1, 1):
            # Top
            if i > 0:
                if lines[i - 1][k] != "." and not lines[i - 1][k].isdigit():
                    symbol_bool += 1
                    # symbols.append(lines[i - 1][k])
                    if lines[i - 1][k] == "*" and f"{i - 1}, {k}" not in gear_index.keys():
                        gear_index[f"{i - 1}, {k}"] = current_number
                    elif f"{i - 1}, {k}" in gear_index.keys():
                        gear_ratio += current_number * gear_index[f"{i - 1}, {k}"]
                        pairs.append([gear_index[f"{i - 1}, {k}"], current_number])

                        del gear_index[f"{i - 1}, {k}"]

            # Bottom
            if i < len(lines) - 1:
                if lines[i + 1][k] != "." and not lines[i + 1][k].isdigit():
                    symbol_bool += 1
                    # symbols.append(lines[i + 1][k])

                    if lines[i + 1][k] == "*" and f"{i + 1}, {k}" not in gear_index.keys():
                        gear_index[f"{i + 1}, {k}"] = current_number
                    elif f"{i + 1}, {k}" in gear_index.keys():
                        gear_ratio += current_number * gear_index[f"{i + 1}, {k}"]
                        pairs.append([gear_index[f"{i + 1}, {k}"], current_number])

                        del gear_index[f"{i + 1}, {k}"]

        # print(f"current_number : {current_number}, bool : {symbol_bool}, "
        #       # f"symbols: {symbols}"
        #       )
        # print(number_index)

        if symbol_bool > 0:
            part_sum += current_number
        total_sum += current_number

        symbol_bool = 0
        number_index = 0
        current_number = ""
        symbols = []

print(pairs)
print(part_sum)
print(gear_ratio)