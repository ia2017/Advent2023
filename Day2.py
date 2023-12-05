with open("inputs/Day2", newline="\n") as f:
    lines = [line.rstrip() for line in f]

sum = 0
power = 0
for line in lines:
    valid = 0
    games = line.split(":")[1]
    game_number = int(line.split(":")[0].split(" ")[1])
    sets = games.split(";")

    # Part 2
    red_max = -1e8
    blue_max = -1e8
    green_max = -1e8

    for set in sets:
        cubes = set.split(",")
        for cube in cubes:
            cube = cube.split(" ")
            del cube[0]
            print(cube)
            if cube[1] == "red":
                if int(cube[0]) > 12:
                    valid += 1
                if int(cube[0]) > red_max:
                    red_max = int(cube[0])

            elif cube[1] == "blue":
                if int(cube[0]) > 14:
                    valid += 1
                if int(cube[0]) > blue_max:
                    blue_max = int(cube[0])

            elif cube[1] == "green":
                if int(cube[0]) > 13:
                    valid += 1
                if int(cube[0]) > green_max:
                    green_max = int(cube[0])

            else:
                print("None")

    print(f"red: {red_max}, green: {green_max}, blue: {blue_max}")
    if valid == 0:
        print("VALID")
        sum += game_number
    power += red_max * blue_max * green_max

print(power)







