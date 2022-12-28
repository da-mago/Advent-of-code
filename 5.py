import copy
import sys

# Read input
filename = sys.argv[0].split('.')[0] + '.in'
lines = [x for x in open(filename)]

# Parse input
crates = ''
orders = []
row_stacks = []
for line in lines:
    if "move" not in line:
        if '1' not in line and len(line)>0:
            row_stacks.append( line[1::4])
    else:
        dat = line.replace('from', '').replace('to', '').replace('move', '')
        orders.append( dat.split() )

# Build stacks
stacks_len = len(row_stacks[0]) # How many stacks
stacks = [[] for _ in range(stacks_len)]
for stack in row_stacks:
    for i,crate in enumerate(stack):
        if crate != ' ':
            stacks[i].insert(0,crate)

stacks2 = copy.deepcopy(stacks)

# Part 1
for order in orders:
    _qty, _from, _to = [int(x) for x in order]
    stacks[_to - 1].extend(stacks[_from - 1][0-_qty:])
    for i in range(_qty):
        stacks[_from - 1].pop()

crates = ''.join([last_crate[-1] for last_crate in stacks])
print("Part1", crates)

# Part 2
stacks = stacks2
for order in orders:
    _qty, _from, _to = [int(x) for x in order]
    for i in range(_qty):
        stacks[_to - 1].append( stacks[_from - 1].pop() )

crates = ''.join([last_crate[-1] for last_crate in stacks])
print("Part2", crates)

