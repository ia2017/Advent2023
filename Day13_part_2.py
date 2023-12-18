with open("inputs/Day13_test", newline="\n") as f:
    lines = [line.rstrip() for line in f]

# print(lines)

line_list = []
current_pattern = []
for line in lines:
    if line == "":
        line_list.append(current_pattern)
        current_pattern = []
    else:
        current_pattern.append(line)

line_list.append(current_pattern)

total = 0
total_2 = 0

for i in range(len(line_list)):
# for i in range(1,2):
    pattern = line_list[i]
    pattern_2 = line_list[i].copy()
    # for j in pattern:
    #     print(j)
    # print("\n")

    bool_row = False
    # print("------------")

    # ----- Check row case -----
    row_bool = False
    row_pivot = 0
    count_row = 0
    row_pivot_2 = 0

    for j in range(0, len(pattern), 1):

        if j > 0:
            if pattern[j] == pattern[j - 1] and not row_bool:
                k = 0
                # Look back
                while True:
                    k += 1

                    # Reaches the end
                    if j + k > len(pattern) - 1 or j - 1 - k < 0:
                        row_pivot = j
                        row_bool = True
                        break

                    front = pattern[j + k]
                    back = pattern[j - 1 - k]

                    if front != back:
                        row_pivot_2 = j
                        break

            if row_bool:
                break

    # ----- Check column case ------
    columns = []

    columns.append("".join([pattern[x][0] for x in range(len(pattern))]))

    col_bool = False
    col_pivot = 0
    col_pivot_2 = 0
    count_col = 0

    for j in range(1, len(pattern[0]), 1):
        columns.append("".join([pattern[x][j] for x in range(len(pattern))]))

    for j in range(1, len(columns), 1):
        if j > 0:

            if columns[j] == columns[j - 1] and not col_bool:
                k = 0
                # Look back
                while True:
                    k += 1

                    # Reaches the end
                    if j + k > len(columns) - 1 or j - 1 - k < 0:
                        col_pivot = j
                        col_bool = True
                        break

                    front = columns[j + k]
                    back = columns[j - 1 - k]

                    if front != back:
                        col_pivot_2 = j
                        break

            if col_bool:
                break

    row_bool_2 = False
    row_pivot_2 = 0
    col_bool_2 = False
    col_pivot_2 = 0

    # ---- Part 2 -----------
    for n in range(len(pattern_2)):
        orig = pattern_2[n]
        for m in range(len(pattern_2[n])):
            temp = list(orig)
            if temp[m] == "#":
                temp[m] = "."
                temp_string = "".join(temp)
                pattern_2[n] = temp_string
            elif temp[m] == ".":
                temp[m] = "#"
                temp_string = "".join(temp)
                pattern_2[n] = temp_string

            # if n == len(pattern_2) - 1 and m == 4:
            #     for pat in pattern_2:
            #         print(pat)
            #     print("")

            # ----- Check row case -----
            row_bool_2 = False
            row_pivot_2 = 0
            col_bool_2 = False
            col_pivot_2 = 0

            for j in range(0, len(pattern_2), 1):

                if j > 0:

                    if pattern_2[j] == pattern_2[j - 1] and not row_bool_2:
                        k = 0

                        # Look back
                        while True:
                            k += 1

                            # Reaches the end
                            if j + k > len(pattern_2) - 1 or j - 1 - k < 0:
                                row_pivot_2 = j
                                row_bool_2 = True

                                break

                            front = pattern_2[j + k]
                            back = pattern_2[j - 1 - k]

                            if front != back:
                                break

                    if row_bool_2 and row_pivot_2 != row_pivot:
                        break
                    else:
                        row_bool_2 = False

            # ----- Check column case ------
            columns_2 = []

            columns_2.append("".join([pattern_2[x][0] for x in range(len(pattern_2))]))


            for j in range(1, len(pattern_2[0]), 1):
                columns_2.append("".join([pattern_2[x][j] for x in range(len(pattern_2))]))

            for j in range(1, len(columns_2), 1):
                if j > 0:

                    if columns_2[j] == columns_2[j - 1] and not col_bool_2:

                        k = 0
                        # Look back
                        while True:
                            k += 1

                            # Reaches the end
                            if j + k > len(columns_2) - 1 or j - 1 - k < 0:
                                col_pivot_2 = j
                                col_bool_2 = True
                                break

                            front = columns_2[j + k]
                            back = columns_2[j - 1 - k]

                            if front != back:
                                break

                    if col_bool_2 and col_pivot_2 != col_pivot:
                        break
                    else:
                        col_bool_2 = False

            if (row_pivot_2 != row_pivot and row_bool_2) or (col_pivot_2 != col_pivot and col_bool_2):
                break
        if (row_pivot_2 != row_pivot and row_bool_2) or (col_pivot_2 != col_pivot and col_bool_2):
            break
        pattern_2[n] = orig
    print(f"{20*'-'}")
    print(f"{i} part 1: {row_pivot}, {col_pivot}")
    print(f"{i} part 2: {row_pivot_2}, {col_pivot_2}")

    if row_bool and row_pivot > 0:
        total += row_pivot * 100
    elif col_bool and col_pivot > 0:
        total += col_pivot
    else:
        print("HERE")

    # Find smudged version:
    if row_bool_2 and row_pivot_2 > 0 and row_pivot_2 != row_pivot:
        total_2 += row_pivot_2 * 100
    elif col_bool_2 and col_pivot_2 > 0 and col_pivot_2 != col_pivot:
        total_2 += col_pivot_2
    else:
        print("HERE")



print(total)
print(total_2)







