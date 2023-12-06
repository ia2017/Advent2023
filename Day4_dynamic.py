with open("inputs/Day4", newline="\n") as f:
    lines = [line.rstrip() for line in f]

print(lines)
card_count_total = 0

def process_card(winning_no, current_no):

    count = 0
    point = 0

    winning_no_new = []
    for winning in winning_no:
        if winning != "":
            winning_no_new.append(winning)

    for current in current_no:
        if current in winning_no_new:
            count += 1

    if count > 0:
        point += 1 * pow(2, count - 1)

    return point, count


def dynamicSolution(n, lines):
    points = 0
    p1 = 0
    card_dict = []

    N = {}

    # Process cards
    for i, line in enumerate(lines):
        if i not in N.keys():
            N[i] = 1
        else:
            N[i] += 1
        # Process
        # card_no = int(lines[i].split(":")[0].split(" ")[-1])
        winning_no = lines[i].split(":")[1].split("|")[0].split(" ")
        current_no = lines[i].split(":")[1].split("|")[1].split(" ")

        point, count = process_card(winning_no, current_no)
        card_dict.append(count)
        # for j in range()

        for j in range(count):
            if i + 1 + j not in N.keys():
                N[i + 1 + j] = N[i]
            else:
                N[i+1+j] += N[i]

        points += point

    print(sum(N.values()))

    return points

points = dynamicSolution(len(lines), lines)
print(points)
print(f"Card total: {card_count_total}")
print("Actual answer: 5659035")

