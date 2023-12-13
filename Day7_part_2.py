with open("inputs/Day7_test", newline="\n") as f:
    lines = [line.rstrip() for line in f]

hands = []

bets = {}

hand_points = {
    "A" : 13,
    "K" : 12,
    "Q" : 11,
    "T" : 10,
    "9" : 9,
    "8" : 8,
    "7" : 7,
    "6" : 6,
    "5" : 5,
    "4" : 4,
    "3" : 3,
    "2" : 2,
    "J" : 1,

}

def compare_hand(hand_1, hand_2):
    # Savings first char
    chars_1 = {hand_1[0]: 1}
    chars_2 = {hand_2[0]: 1}

    # Assembling characters
    for j in range(1, len(hand_1), 1):
        if hand_1[j] not in chars_1:
            chars_1[hand_1[j]] = 1
        else:
            chars_1[hand_1[j]] += 1

        if hand_2[j] not in chars_2:
            chars_2[hand_2[j]] = 1
        else:
            chars_2[hand_2[j]] += 1

    # Fix J as Joker
    if "J" in chars_1:
        j_count = chars_1["J"]
        chars_1.pop("J", None)
        max_char = ""

        for key, value in chars_1.items():
            if value == max(chars_1.values()):
                max_char = key
                break

        # Check if empty
        if len(chars_1) != 0:
            chars_1[max_char] += j_count
        else:
            chars_1["J"] = j_count


    if "J" in chars_2:
        j_count = chars_2["J"]
        chars_2.pop("J", None)
        max_char = ""

        for key, value in chars_2.items():
            if value == max(chars_2.values()):
                max_char = key
                break

        # Check if empty
        if len(chars_2) != 0:
            chars_2[max_char] += j_count
        else:
            chars_2["J"] = j_count

    if max(chars_1.values()) > max(chars_2.values()):
        return hand_1, hand_2
    elif max(chars_1.values()) < max(chars_2.values()):
        return hand_2, hand_1
    else:
        pair_count_1 = sum(value == 2 for value in chars_1.values())
        pair_count_2 = sum(value == 2 for value in chars_2.values())

        # Checking for full house
        if 3 in chars_1.values() and 2 in chars_1.values() and 3 in chars_2.values() and 2 not in chars_2.values():
            return hand_1, hand_2
        elif 3 in chars_2.values() and 2 in chars_2.values() and 3 in chars_1.values() and 2 not in chars_1.values():
            return hand_2, hand_1
        elif pair_count_1 > pair_count_2:
            return hand_1, hand_2
        elif pair_count_1 < pair_count_2:
            return hand_2, hand_1
        else:

            for i in range(len(hand_1)):

                # points_1.append(hand_points[hand_1[i]])
                # points_2.append(hand_points[hand_2[i]])
                if hand_points[hand_1[i]] > hand_points[hand_2[i]]:
                    return hand_1, hand_2
                elif hand_points[hand_1[i]] < hand_points[hand_2[i]]:
                    return hand_2, hand_1


    print("Conditions not met")

    return hand_1, hand_2


for i in range(len(lines)):
    hand = lines[i].split(" ")[0]
    bet = int(lines[i].split(" ")[1])

    # Saving bets
    if hand not in bets.keys():
        bets[hand] = bet
    else:
        print("REPEATED HAND")

    hands.append(hand)

    if i > 0:
        for j in range(len(hands) - 1, 0, -1):
            hand_1, hand_2 = compare_hand(hands[j - 1], hands[j])
            hands[j - 1] = hand_1
            hands[j] = hand_2

total_points = 0
rank = len(hands)

# Adding up points
for i in range(len(hands)):
    total_points += rank * bets[hands[i]]
    rank -= 1

print(total_points)
