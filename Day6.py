with open("inputs/Day6", newline="\n") as f:
    lines = [line.rstrip() for line in f]

time = []
time_2 = ""
record = []
record_2 = ""
time_in = lines[0].split(" ")[1:]

for i in range(len(time_in)):
    if time_in[i].isdigit():
        time.append(int(time_in[i]))
        time_2 += time_in[i]

record_in = lines[1].split(" ")[1:]

for i in range(len(record_in)):
    if record_in[i].isdigit():
        record.append(int(record_in[i]))
        record_2 += record_in[i]

time_2 = int(time_2)
time.append(time_2)
record_2 = int(record_2)
record.append(record_2)

wins = []
for i in range(len(time)):
    win = 0
    for j in range(0, time[i]):
        time_left = time[i] - j
        dist = j * time_left

        if dist > record[i]:
            win += 1

    wins.append(win)

total = 1
for w in wins[:-1]:
    total *= w
print(total)
print(wins[-1])

