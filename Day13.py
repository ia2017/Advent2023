import math

with open("inputs/Day13", newline="\n") as f:
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

total = 0

for i in range(len(line_list)):
# for i in range(17,18):
    pattern = line_list[i]
    for j in pattern:
        print(j)
    print("\n")

    bool_row = False
    # print("------------")

    # ----- Check row case -----
    row_bool = False
    row_pivot = 0
    row_inc = 0
    count_row = 0
    row_count_cache = []
    row_pivot_cache = []
    for j in range(1, len(pattern), 1):
        if row_bool:
            # print(f"pivots j: {j} : {row_pivot + row_inc}, {row_pivot - 1 - row_inc}")
            if pattern[row_pivot + row_inc] == pattern[row_pivot - 1 - row_inc]:
                count_row += 1
                row_inc += 1
            else:
                row_count_cache.append(count_row)
                row_pivot_cache.append(row_pivot)

                row_bool = False

            if row_pivot - 1 - row_inc < 0:
                row_count_cache.append(count_row)
                row_pivot_cache.append(row_pivot)

                row_bool = False

            if row_pivot + row_inc > len(pattern) - 1:
                break


        if pattern[j] == pattern[j - 1] and not row_bool:
            count_row = 0
            row_inc = 0
            row_pivot = j
            row_inc += 1
            count_row += 1
            row_bool = True
    if row_pivot < len(pattern) - 1:
        row_count_cache.append(count_row)
        row_pivot_cache.append(row_pivot)

    # ----- Check column case ------
    columns = []

    columns.append("".join([pattern[x][0] for x in range(len(pattern))]))

    col_bool = False
    col_pivot = 0
    col_inc = 0
    count_col = 0
    col_count_cache = []
    col_pivot_cache = []

    for j in range(1, len(pattern[0]), 1):
        columns.append("".join([pattern[x][j] for x in range(len(pattern))]))

    for j in range(1, len(columns), 1):
        if col_bool:
            if columns[col_pivot + col_inc] == columns[col_pivot - 1 - col_inc]:
                count_col += 1
                col_inc += 1
            else:
                col_count_cache.append(count_col)
                col_pivot_cache.append(col_pivot)

                col_bool = False

            if col_pivot - 1 - col_inc < 0:
                col_count_cache.append(count_col)
                col_pivot_cache.append(col_pivot)

                col_bool = False

            if col_pivot + col_inc > len(columns) - 1:
                break


        if columns[j] == columns[j - 1] and not col_bool:
            count_col = 0
            col_inc = 0
            col_pivot = j
            col_inc += 1
            count_col += 1
            col_bool = True

    if col_pivot < len(columns) - 1:
        col_count_cache.append(count_col)
        col_pivot_cache.append(col_pivot)

    if not row_count_cache:
        row_count_cache = [0]
    if not col_count_cache:
        col_count_cache = [0]

    print(f"{i} : {max(row_count_cache)}, {max(col_count_cache)}")

    if max(row_count_cache) > max(col_count_cache):
        index = row_count_cache.index(max(row_count_cache))
        total += row_pivot_cache[index] * 100
    elif max(row_count_cache) < max(col_count_cache):
        index = col_count_cache.index(max(col_count_cache))
        total += col_pivot_cache[index]
    else:
        if len(pattern) - 2 * max(row_count_cache) < len(columns) - 2 * max(col_count_cache) and max(row_count_cache) > 0:
            index = row_count_cache.index(max(row_count_cache))
            total += row_pivot_cache[index] * 100
        elif len(pattern) - 2 * max(row_count_cache) > len(columns) - 2 * max(col_count_cache) and max(col_count_cache) > 0:
            index = col_count_cache.index(max(col_count_cache))
            total += col_pivot_cache[index]

        else:
            print("None")

print(total)






