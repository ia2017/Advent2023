with open("inputs/Day4", newline="\n") as f:
    lines = [line.rstrip() for line in f]

print(lines)

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


def process_copy(start, stop, lines):

    points = 0
    card_count_total = 0

    for i in range(start, stop, 1):

        # Process
        card_no = int(lines[i].split(":")[0].split(" ")[-1])
        winning_no = lines[i].split(":")[1].split("|")[0].split(" ")
        current_no = lines[i].split(":")[1].split("|")[1].split(" ")

        # Process current card
        point, count = process_card(winning_no, current_no)
        print(f"card_no: {card_no}, count: {count}, i: {i}")

        # if count > 0:
        point_rec, card_count = process_copy(i + 1, i + count + 1, lines)

        points += point
        card_count_total += card_count + 1

    return points, card_count_total


points, card_count_total = process_copy(0, len(lines), lines)

print(points)
print(card_count_total)


