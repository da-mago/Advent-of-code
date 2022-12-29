# Read input
lines = open("10.in").readlines()

# Common
opcode_table = {'noop': [0, 1], 'addx': [0, 2]}
cycle = 0
X = 1
# Part 1
target = [20, 60, 100, 140, 180, 220]
strength = 0
part1_done = False
# Part 2
x_len, y_len = 40, 6
screen = [['.' for _ in range(x_len)] for _ in range(y_len)]
for line in lines:
    instr = line.split()

    # Get cycle/value
    value = int(instr[1]) if instr[0] != 'noop' else 0
    _, num_cycles = opcode_table[instr[0]]

    for _ in range(num_cycles):
        # Part 2
        x,y = cycle % x_len, cycle // x_len
        if (x >= (X - 1)) and (x <= (X + 1)):
            screen[y][x] = '#'
        cycle += 1 

        # Part 1
        if not part1_done:
            if cycle == target[0]:
                target.pop(0)
                strength += cycle * X
                if len(target) == 0:
                    part1_done = True

    # Update X
    X += value

print('Part 1', strength)
# Show screen
print('Part 2')
for line in screen:
    print(''.join(line))
