import functools

with open("inputs/Day12_test", newline="\n") as f:
    lines = [line.rstrip() for line in f]

@functools.lru_cache(maxsize=None)
def count(record, groups):

    # Did we run out of groups? We might still be valid
    if not groups:

        # Make sure there aren't any more damaged springs, if so, we're valid
        if "#" not in record:
            # This will return true even if record is empty, which is valid
            return 1
        else:
            # More damaged springs that aren't in the groups
            return 0

    # There are more groups, but no more record
    if not record:
        # We can't fit, exit
        return 0

    next_character = record[0]
    next_group = groups[0]

    # Logic that treats the first character as pound-sign "#"
    def pound():

        this_group = record[:next_group]
        this_group = this_group.replace("?", "#")

        if this_group != next_group * "#":
            return 0

        # If the rest of the record is just the last group, then we're
        # done and there's only one possibility
        if len(record) == next_group:
            # Make sure this is the last group
            if len(groups) == 1:
                # We are valid
                return 1
            else:
                # There's more groups, we can't make it work
                return 0

        # Make sure the character that follows this group can be a seperator
        if record[next_group] in "?.":
            # It can be seperator, so skip it and reduce to the next group
            return count(record[next_group + 1:], groups[1:])

        return 0

    # Logic that treats the first character as dot "."
    def dot():
        ## ADD LOGIC HERE ... need to process this character and call
        #  calc() on a substring
        return count(record[1:], groups)

    if next_character == '#':
        # Test pound logic
        out = pound()

    elif next_character == '.':
        # Test dot logic
        out = dot()

    elif next_character == '?':
        # This character could be either character, so we'll explore both
        # possibilities
        out = dot() + pound()

    else:
        raise RuntimeError

    # Help with debugging
    print(record, groups, "->", out)

    return out

sum_count = 0

i = 0
for line in lines:
    # print(f"{i} --------------")
    springs = line.split(" ")[0]
    broken = tuple(map(int, line.split(" ")[1].split(",")))
    sum_count += count(springs, broken)
    print(10 * "-")
    i += 1

print(sum_count)
