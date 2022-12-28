# Read input
lines = [x.strip() for x in open("4.in")]

num_assignments1 = 0
num_assignments2 = 0
for assignments in lines:
    elves = assignments.split(',')
    e_ranges = [[int(x) for x in elf.split('-')] for elf in elves]

    # Part 1
    if ((e_ranges[0][0] >= e_ranges[1][0]) and (e_ranges[0][1] <= e_ranges[1][1])) or \
       ((e_ranges[1][0] >= e_ranges[0][0]) and (e_ranges[1][1] <= e_ranges[0][1])):
           num_assignments1 += 1

    # Part 2
    if (((e_ranges[0][0] >= e_ranges[1][0]) and (e_ranges[0][0] <= e_ranges[1][1]))  or \
        ((e_ranges[0][1] >= e_ranges[1][0]) and (e_ranges[0][1] <= e_ranges[1][1]))) or \
       (((e_ranges[1][0] >= e_ranges[0][0]) and (e_ranges[1][0] <= e_ranges[0][1]))  or \
        ((e_ranges[1][1] >= e_ranges[0][0]) and (e_ranges[1][1] <= e_ranges[0][1]))):
           num_assignments2 += 1

print("Part 1", num_assignments1)
print("Part 2", num_assignments2)

