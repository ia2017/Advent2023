with open("inputs/Day12_test", newline="\n") as f:
    lines = [line.rstrip() for line in f]

def count(springs, broken):
    if springs == "":
        return 1 if broken == () else 0
    if broken == ():
        return 0 if "#" in springs else 1

    result = 0

    if springs[0] in ".?":
        print(f"springs 1: {springs}")
        result += count(springs[1:], broken)
    print(f"springs 1.5: {springs}, {result}")

    if springs[0] in "#?":
        if broken[0] <= len(springs) and "." not in springs[:broken[0]] and (broken[0] == len(springs) or springs[broken[0]] != "#"):
            print(f"springs 2: {springs}, {result}")
            result += count(springs[broken[0] + 1:], broken[1:])

    return result

sum_count = 0

i = 0
for line in lines:
    print(f"{i} --------------")
    springs = line.split(" ")[0]
    broken = tuple(map(int, line.split(" ")[1].split(",")))
    sum_count += count(springs, broken)
    i += 1

print(sum_count)
