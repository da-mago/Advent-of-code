# Read input
lines = [x.strip() for x in open("1.in").readlines()]

calories = 0
elves = []
for line in lines:
    if len(line) > 0:
        calories += int(line)
    else:
        # This elf is done
        elves.append(calories)
        calories = 0

# Order from high to low
elves.sort(reverse=True)
print("Part 1: {}".format(elves[0]))
print("Part 2: {}".format(sum(elves[0:3])))
    


