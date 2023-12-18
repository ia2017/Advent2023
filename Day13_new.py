import math

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

for i in range(len(line_list)):
# for i in range(17,18):
    pattern = line_list[i]
    # for j in pattern:
    #     print(j)
    # print("\n")

    bool_row = False
    # print("------------")

    # ----- Check row case -----
    row_bool = False
    row_pivot = 0
    count_row = 0

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
                        break

            if row_bool:
                break


    # ----- Check column case ------
    columns = []

    columns.append("".join([pattern[x][0] for x in range(len(pattern))]))

    col_bool = False
    col_pivot = 0
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
                        break

            if col_bool:
                break

    if row_bool and row_pivot > 0:
        total += row_pivot * 100
    elif col_bool and col_pivot > 0:
        total += col_pivot
    else:
        print("HERE")

    print(f"i: {i}, row, col: {row_pivot}, {col_pivot}")



print(total)






